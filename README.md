OPPO SMS& Call Log Recovery Tool

Convert old OPPO backup files (.vmsg and OPPO call log XML) into Android-compatible XML files and restore them using SMS Backup & Restore.

This repository contains Python scripts that convert proprietary OPPO backup exports into standard XML files compatible with Android restore tools.
The project was tested successfully on:
	•	Old OPPO model (e.g.: Oppo F9)
	•	New OPPO model (e.g.: Oppo A5)

The recovery process was validated with:
	•	46,000+ SMS messages
	•	1,500+ call logs

Features
SMS Recovery
	•	Converts OPPO .vmsg SMS exports into Android-compatible XML
	•	Supports multi-message .vmsg files
	•	Decodes quoted-printable UTF-8 SMS content
	•	Preserves timestamps correctly
	•	Compatible with SMS Backup & Restore
Call Log Recovery
	•	Converts OPPO proprietary <CALL_RECORDS> XML exports
	•	Preserves:
	◦	phone numbers
	◦	call duration
	◦	call type
	◦	timestamps
	◦	contact names

Why this tool exists
Many old OPPO phones export SMS and call logs using proprietary formats that are not directly compatible with Android restore apps or Google restore services.
Common issues include:
	•	Google Cloud restore failing
	•	Android migration incompatibilities
	•	unsupported OPPO backup formats
	•	timestamp conversion issues
	•	encoding problems in old SMS exports
This tool converts those exports into formats recognized by Android restore applications.

Requirements
	•	Python 3
	•	Required packages:

pip install chardet

SMS Recovery Instructions
1. Export SMS from the old OPPO device
Copy the .vmsg backup files from the old phone to your computer.

2. Run the SMS converter

python3 oppo_vmsg_to_xml.py

The script will:
	•	detect encoding automatically
	•	decode SMS contents
	•	merge all messages into a single XML file
Output:
sms.xml

3. Transfer the XML file to Android
Copy:

sms.xml

to your Android phone.
Recommended locations:
	•	Download
	•	Internal Storage root

4. Restore messages
Install: SMS Backup & Restore
Then:
	1	Open the app
	2	Select Restore
	3	Choose Local Backup Location
	4	Locate sms.xml
	5	Restore Messages

Call Log Recovery Instructions
1. Export OPPO call logs XML
Copy the original OPPO call log XML file to your computer.
Example OPPO structure:

<CallLog>
<CALL_RECORDS ... />
</CallLog>

2. Run the call log converter

python3 oppo_calls_to_xml.py

Output:

calls_converted.xml


3. Restore call logs
Using SMS Backup & Restore:
	1	Open Restore
	2	Select Call Logs
	3	Locate: calls_converted.xml
	4	Allow required Android permissions
	5	Restore call history

Notes
	•	Large restores may take several minutes
	•	Android may temporarily lag while indexing messages
	•	Timestamps are converted to milliseconds for Android compatibility
	•	The tool preserves UTF-8 characters and special symbols

Tested Recovery Scenario
Successful migration from:
	•	dead/broken OPPO motherboard
	•	failed Google Cloud restore
	•	inaccessible Android migration backups
Recovered successfully:
	•	46K+ SMS
	•	1500+ call logs

Disclaimer
This tool was created for personal backup recovery purposes.
Always create backups before restoring or modifying SMS/call log databases.

