# Agent Communication Protocol: File-Based

## Принцип

Агенты KUBRIK pipeline общаются **только через файлы**. Никакой контекст не передаётся "по воздуху" между агентами. Каждый агент читает строго определённые input-файлы и записывает строго определённые output-файлы.

## Зачем

1. **Audit trail** - каждое решение pipeline зафиксировано в файле, можно отследить кто что сгенерировал
2. **Клиентская прозрачность** - клиент видит промежуточные артефакты, а не только финальный пакет
3. **Изоляция агентов** - предотвращает context leak, anchoring bias, groupthink
4. **Воспроизводимость** - можно перезапустить любой агент с теми же input-файлами и получить тот же класс output
5. **Параллельная работа** - несколько клиентов не пересекаются по контексту

## Contract: Input/Output по агентам

Каждый агент получает ТОЛЬКО перечисленные файлы. Ничего больше.

| Агент | Input файлы | Output файл |
|-------|------------|-------------|
| Стратег | `brief.md` | `strategy.md` |
| Strategy Council | `brief.md`, `strategy.md` | `strategy-council.md` |
| Фактчекер | `brief.md`, `strategy.md` | `fact-check.md` |
| Контекстолог | `strategy.md`, `fact-check.md` | `context-plan.md` |
| Таргетолог | `strategy.md`, `fact-check.md` | `targeting-plan.md` |
| Media Buyer | `strategy.md`, `context-plan.md`, `targeting-plan.md` | `media-plan.md` |
| Копирайтер | `strategy.md`, `media-plan.md` | `creatives.md`, `content-plan.md` |
| char-guard (скрипт) | `creatives.md` | `creatives.char-guard.md`, `creatives.char-guard.report.md` |
| Валидатор | `brief.md`, `strategy.md`, `media-plan.md`, `creatives.char-guard.md` | `validation.md` |
| Sales QA | `brief.md`, transcript/chat | `sales-qa.md` |

## Правила

### 1. No context passthrough
Оркестратор (pipeline skill) НЕ передаёт reasoning или промежуточный контекст от одного агента другому. Только файлы из таблицы выше.

### 2. Sub-agent isolation
Агенты, критичные к bias (Strategy Council персоны, Валидатор), запускаются как **отдельные sub-agents** через Agent tool. Это гарантирует чистый context window.

### 3. Feedback через файлы
Если Валидатор возвращает REVISE:
1. `validation.md` записывается в клиентскую папку
2. Копирайтер читает `validation.md` как input
3. Копирайтер пишет обновлённый `creatives.md`
4. char-guard перезапускается
5. Валидатор получает ТОЛЬКО новый `creatives.char-guard.md` (без предыдущего `validation.md`)

### 4. Versioning при итерациях
При повторных раундах Generator-Evaluator loop:
- Текущая версия всегда в основном файле (`creatives.md`, `validation.md`)
- Предыдущие версии сохраняются как `creatives.v1.md`, `validation.v1.md`
- Improvement log ведётся в финальном `validation.md`

### 5. Операционная память отдельно
Файлы в `ops/` (client-memory.md, sessions/, learnings.md) - это долгоживущая память. Pipeline-артефакты в корне клиентской папки - это артефакты одного запуска.

## Диаграмма pipeline

```
brief.md
    |
    v
[Стратег] --> strategy.md
    |
    v
[Strategy Council] --> strategy-council.md
    |                   (PASS / REVISE / ESCALATE)
    v
[Фактчекер] --> fact-check.md
    |
    +-------+-------+
    v               v
[Контекстолог]  [Таргетолог]     <- параллельно
    |               |
    v               v
context-plan.md  targeting-plan.md
    |               |
    +-------+-------+
            |
            v
      [Media Buyer] --> media-plan.md
            |
            v
      [Копирайтер] --> creatives.md + content-plan.md
            |
            v
      [char-guard] --> creatives.char-guard.md
            |
            v
      [Валидатор] --> validation.md
            |
            +-- PASS --> готово
            +-- REVISE --> обратно к Копирайтеру (max 3 раунда)
            +-- BLOCKED --> эскалация на команду
```
