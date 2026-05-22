import os
import re
import chardet
import quopri
from datetime import datetime

# CHANGE path AS REQUIRED
path = "./"

messages_xml = []

xml_header = """<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
"""

for file in os.listdir(path):
    # Read original OPPO smss
    if file.lower().endswith(".vmsg"):

        fname = os.path.join(path, file)

        # Detect encoding
        with open(fname, "rb") as f:
            raw_content = f.read()
            encoding = chardet.detect(raw_content).get("encoding") or "utf-8"

        # Read file
        with open(fname, "r", encoding=encoding, errors="ignore") as f:
            content = f.read()

        # Split ALL VMSG blocks
        messages = re.findall(r"BEGIN:VMSG(.*?)END:VMSG", content, re.S)

        for msg in messages:

            # -------------------------
            # READ STATUS
            # -------------------------
            read = 1 if "X-READ:READ" in msg else 0

            # -------------------------
            # MESSAGE TYPE
            # -------------------------
            msgtype = 1  # inbox by default

            if "X-BOX:SENDBOX" in msg:
                msgtype = 2

            # -------------------------
            # CONTACT
            # -------------------------
            contact = "Unknown"

            match = re.search(r"TEL:(.+)", msg)

            if match:
                contact = match.group(1).strip()

            # -------------------------
            # DATE
            # -------------------------
            timestamp = 0
            readable_date = ""

            match = re.search(r"Date:(.+)", msg)

            if match:
                date_str = match.group(1).strip()

                try:
                    dt = datetime.strptime(date_str, "%Y/%m/%d %H:%M:%S")
                    # convert to UNIX timestamp (seconds)
                    timestamp = int(dt.timestamp())

                    # IMPORTANT FIX: convert to milliseconds for Android compatibility
                    timestamp_ms = timestamp * 1000
                    
                    readable_date = dt.strftime("%d %b %Y %H:%M:%S")

                except Exception:
                    readable_date = date_str
                    timestamp_ms = 0

            # -------------------------
            # MESSAGE BODY
            # -------------------------
            body = ""

            match = re.search(
                r"SubjectENCODING=QUOTED-PRINTABLE;CHARSET=UTF-8:(.*?)END:VBODY",
                msg,
                re.S,
            )

            if match:

                encoded_body = match.group(1).strip()

                try:
                    body = quopri.decodestring(encoded_body).decode(
                        "utf-8",
                        errors="ignore"
                    )

                except Exception:
                    body = encoded_body

            # -------------------------
            # XML ESCAPING
            # -------------------------
            body = (
                body.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
            )

            contact = (
                contact.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
            )

            # -------------------------
            # XML LINE
            # -------------------------
            line = (
                f'<sms protocol="0" '
                f'address="{contact}" '
                #f'date="{timestamp}" '
                f'date="{timestamp_ms}" '
                f'type="{msgtype}" '
                f'subject="null" '
                f'body="{body}" '
                f'toa="null" '
                f'sc_toa="null" '
                f'service_center="null" '
                f'read="{read}" '
                f'status="-1" '
                f'locked="0" '
                #f'date_sent="{timestamp}" '
                f'date_sent="{timestamp_ms}" '
                f'sub_id="-1" '
                f'readable_date="{readable_date}" '
                f'contact_name="{contact}" />\n'
            )

            messages_xml.append(line)

# -------------------------
# FINAL XML
# -------------------------
xml = (
    xml_header
    + f'<smses count="{len(messages_xml)}" '
    + 'backup_set="3ff83320-2c57-44c2-bdd5-7eae6758fcef" '
    + 'backup_date="1711616976109" '
    + 'type="full">\n'
)

xml += "".join(messages_xml)

xml += "</smses>"

# -------------------------
# WRITE FILE
# -------------------------
with open("smss_converted.xml", "w", encoding="utf-8") as f:
    f.write(xml)

print(f"Done! Exported {len(messages_xml)} SMS messages to sms_converted.xml")
