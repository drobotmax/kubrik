#!/usr/bin/awk -f
# Parse RSS/Atom XML into TSV: date\tplatform\ttitle\turl\tsummary
# Usage: awk -v platform=google -v cutoff=2026-03-20 -f parse_rss.awk feed.xml
#
# Works with both BSD awk (macOS) and gawk

BEGIN {
    in_item = 0
    title = ""
    link = ""
    pubdate = ""
    desc = ""
    guid = ""
}

/<item[ >]/ || /<entry[ >]/ {
    in_item = 1
    title = ""
    link = ""
    pubdate = ""
    desc = ""
    guid = ""
    next
}

/<\/item>/ || /<\/entry>/ {
    if (in_item && title != "") {
        # Use link, fallback to guid
        url = (link != "") ? link : guid

        # Extract ISO date from pubdate
        iso_date = extract_date(pubdate)

        if (iso_date != "" && iso_date >= cutoff && url != "") {
            # Clean text
            gsub(/\t/, " ", title)
            gsub(/\t/, " ", desc)
            gsub(/\r/, "", title)
            gsub(/\r/, "", desc)

            # Truncate desc
            if (length(desc) > 200) desc = substr(desc, 1, 200) "..."

            printf "%s\t%s\t%s\t%s\t%s\n", iso_date, platform, title, url, desc
        }
    }
    in_item = 0
    next
}

in_item {
    # Title
    if (title == "" && $0 ~ /<title/) {
        title = extract_content($0, "title")
    }
    # Link (RSS style)
    if (link == "" && $0 ~ /<link>/) {
        link = extract_content($0, "link")
    }
    # Link (Atom style: <link href="..."/>)
    if (link == "" && $0 ~ /<link[^>]*href=/) {
        tmp = $0
        sub(/.*href="/, "", tmp)
        sub(/".*/, "", tmp)
        link = tmp
    }
    # Guid
    if (guid == "" && $0 ~ /<guid/) {
        guid = extract_content($0, "guid")
    }
    # PubDate
    if (pubdate == "" && $0 ~ /<pubDate/) {
        pubdate = extract_content($0, "pubDate")
    }
    if (pubdate == "" && $0 ~ /<published/) {
        pubdate = extract_content($0, "published")
    }
    if (pubdate == "" && $0 ~ /<updated/) {
        pubdate = extract_content($0, "updated")
    }
    # Description
    if (desc == "" && $0 ~ /<description/) {
        desc = extract_content($0, "description")
        gsub(/<[^>]*>/, "", desc)
        gsub(/&lt;[^&]*&gt;/, "", desc)
        gsub(/&amp;/, "\\&", desc)
    }
    if (desc == "" && $0 ~ /<summary/) {
        desc = extract_content($0, "summary")
        gsub(/<[^>]*>/, "", desc)
    }
}

function extract_content(line, tag,    tmp) {
    tmp = line
    # Remove opening tag
    sub(".*<" tag "[^>]*>", "", tmp)
    # Handle CDATA
    sub(/^<!\[CDATA\[/, "", tmp)
    sub(/\]\]>.*/, "", tmp)
    # Remove closing tag
    sub("</" tag ">.*", "", tmp)
    # Trim
    gsub(/^[[:space:]]+|[[:space:]]+$/, "", tmp)
    return tmp
}

function extract_date(datestr,    months, m, d, y, mn, idx) {
    # ISO format: 2026-03-26 or 2026-03-26T...
    if (datestr ~ /^[0-9]{4}-[0-9]{2}-[0-9]{2}/) {
        return substr(datestr, 1, 10)
    }
    # RFC 2822: "Thu, 26 Mar 2026 16:00:00 +0000"
    # or: "Fri, 27 Mar 2026 11:39:27 GMT"
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    # Extract day, month name, year
    if (split(datestr, parts, " ") >= 4) {
        for (i = 1; i <= length(parts); i++) {
            if (parts[i] ~ /^[0-9]{1,2}$/ && d == "") d = parts[i]
            else if (parts[i] ~ /^[A-Z][a-z]{2}$/) m = parts[i]
            else if (parts[i] ~ /^[0-9]{4}$/) y = parts[i]
        }
        if (m != "" && d != "" && y != "") {
            idx = index(months, m)
            if (idx > 0) {
                mn = int((idx - 1) / 3) + 1
                return sprintf("%s-%02d-%02d", y, mn, d + 0)
            }
        }
    }
    return ""
}
