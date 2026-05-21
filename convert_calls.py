import re

# Read original OPPO call log
with open("callrecord_backup.xml", "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Find all CALL_RECORDS entries
records = re.findall(r'<CALL_RECORDS (.*?)\/>', content)

calls_xml = []

for r in records:

    def extract(attr):
        match = re.search(fr'{attr}="(.*?)"', r)
        return match.group(1) if match else ""

    number = extract("number")
    duration = extract("duration")
    calltype = extract("type")
    date = extract("date")
    name = extract("name")

    # XML escaping
    name = (
        name.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )

    line = (
        f'<call number="{number}" '
        f'date="{date}" '
        f'duration="{duration}" '
        f'type="{calltype}" '
        f'name="{name}" '
        f'readable_date="" '
        f'contact_name="{name}" />\n'
    )

    calls_xml.append(line)

# Final XML
xml = (
    "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>\n"
    + f'<calls count="{len(calls_xml)}">\n'
)

xml += "".join(calls_xml)

xml += "</calls>"

# Save
with open("calls_converted.xml", "w", encoding="utf-8") as f:
    f.write(xml)

print(f"Done! Exported {len(calls_xml)} call logs.")