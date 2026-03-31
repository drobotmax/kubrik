#!/usr/bin/env bash
# Fetch all configured RSS blog feeds
# Usage: bash scripts/fetch_blogs.sh [--period 7] [--platform google]
# Output: combined TSV to stdout (date, platform, title, url, summary)

set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
. "$SCRIPT_DIR/common.sh"

load_config
ensure_dirs
parse_common_params "$@"

COMBINED="$CACHE_DIR/blogs_combined.tsv"
: > "$COMBINED"

# Parse NEWS_RSS_FEEDS (pipe-separated: name|url|platform)
echo "$NEWS_RSS_FEEDS" | while IFS= read -r line; do
    # Skip empty lines
    line=$(echo "$line" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
    [ -z "$line" ] && continue

    _name=$(echo "$line" | cut -d'|' -f1 | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
    _url=$(echo "$line" | cut -d'|' -f2 | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
    _platform=$(echo "$line" | cut -d'|' -f3 | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')

    [ -z "$_url" ] && continue

    # Filter by platform if specified
    if [ -n "$PLATFORM" ] && [ "$_platform" != "$PLATFORM" ]; then
        continue
    fi

    echo "Fetching: $_name ($_platform)..." >&2

    bash "$SCRIPT_DIR/fetch_rss.sh" \
        --url "$_url" \
        --platform "$_platform" \
        --name "$_name" \
        --period "$PERIOD" >> "$COMBINED" 2>/dev/null || {
        echo "Warning: failed to fetch $_name" >&2
    }
done

# Sort by date descending
if [ -s "$COMBINED" ]; then
    sort -t$'\t' -k1,1r "$COMBINED"
    _count=$(wc -l < "$COMBINED" | tr -d ' ')
    echo "Total blog articles: $_count" >&2
else
    echo "No blog articles found for period=$PERIOD days" >&2
fi
