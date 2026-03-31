# KUBRIK News Pipeline

Automated monitoring of ad platform updates (Google Ads, Meta, Yandex Direct).
Detects spec changes, policy updates, and new features - then updates the knowledge base and agent definitions.

## How it works

1. **Fetch** - RSS feeds + Telegram channels (weekly, Monday 08:23 MSK)
2. **Classify** - each article: spec_change, policy_update, new_feature, deprecation, notify_only, skip
3. **Deep read** - full article content for actionable items
4. **Update KB** - edit platform-specs.md, knowledge/ files, agent skill.md files
5. **Commit** - structured commit to main with `news-pipeline:` prefix
6. **Notify** - Telegram digest to team

## Sources

| Source | Type | URL |
|--------|------|-----|
| Google Ads Blog | RSS | blog.google/products/ads-commerce/rss/ |
| Yandex Ads News | RSS | yandex.ru/adv/news/rss |
| TG: @paborobot | Telegram | PPC media, context ads |
| TG: @directorologia | Telegram | Yandex Direct |
| TG: @targetolog | Telegram | Meta/VK targeting |
| TG: @caborobot | Telegram | Digital marketing |

## Files

- `changelog.md` - append-only log of all KB changes (audit trail)
- `config.md` - dependency map: what to update when platform changes detected
- `orchestration-prompt.md` - prompt for the scheduled trigger
- `snapshots/` - pre-edit file hashes per run

## Safety

- Max 10 file edits per run
- Confidence threshold 80% for spec changes
- Telegram posts = secondary source only (never update specs from TG alone)
- All commits prefixed with `news-pipeline:` for easy rollback via `git revert`

## Manual run

```bash
# Fetch fresh digest
bash ~/.claude/skills/kubrik-news/scripts/digest.sh --period 7 --no-dedup

# Or trigger the full pipeline
# /schedule run kubrik-news-pipeline
```
