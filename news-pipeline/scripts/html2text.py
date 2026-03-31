#!/usr/bin/env python3
"""Extract readable text from HTML. Strips scripts, styles, nav, JSON-LD, etc.
Usage: echo "<html>..." | python3 html2text.py
"""
import sys
import re
import html

def html_to_text(raw):
    # Remove script, style, nav, footer, header, noscript blocks
    for tag in ['script', 'style', 'nav', 'footer', 'header', 'noscript', 'svg', 'iframe']:
        raw = re.sub(rf'<{tag}[^>]*>.*?</{tag}>', '', raw, flags=re.DOTALL | re.IGNORECASE)

    # Remove JSON-LD and other structured data
    raw = re.sub(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>.*?</script>', '', raw, flags=re.DOTALL)

    # Remove HTML comments
    raw = re.sub(r'<!--.*?-->', '', raw, flags=re.DOTALL)

    # Convert <br> and <p> to newlines
    raw = re.sub(r'<br\s*/?>', '\n', raw, flags=re.IGNORECASE)
    raw = re.sub(r'</p>', '\n\n', raw, flags=re.IGNORECASE)
    raw = re.sub(r'</div>', '\n', raw, flags=re.IGNORECASE)
    raw = re.sub(r'</li>', '\n', raw, flags=re.IGNORECASE)
    raw = re.sub(r'<li[^>]*>', '- ', raw, flags=re.IGNORECASE)

    # Convert headers to markdown
    for i in range(1, 7):
        prefix = '#' * i
        raw = re.sub(rf'<h{i}[^>]*>(.*?)</h{i}>', rf'\n\n{prefix} \1\n', raw, flags=re.DOTALL | re.IGNORECASE)

    # Strip all remaining tags
    raw = re.sub(r'<[^>]+>', '', raw)

    # Decode HTML entities
    raw = html.unescape(raw)

    # Clean up whitespace
    lines = []
    for line in raw.split('\n'):
        line = line.strip()
        if line:
            lines.append(line)

    # Collapse multiple blank lines
    text = '\n'.join(lines)
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Truncate to reasonable length (first ~500 lines)
    result_lines = text.split('\n')[:500]
    return '\n'.join(result_lines)

if __name__ == '__main__':
    raw = sys.stdin.read()
    print(html_to_text(raw))
