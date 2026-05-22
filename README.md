<h1>OPPO SMS& Call Log Recovery Tool</h1>

Convert old OPPO backup files (.vmsg and OPPO call log XML) into Android-compatible XML files and restore them using SMS Backup & Restore.

This repository contains Python scripts that convert proprietary OPPO backup exports into standard XML files compatible with Android restore tools.
The project was tested successfully on:
	<ul>
	<li>Old OPPO model (e.g.: Oppo F9)</li>
	<li>New OPPO model (e.g.: Oppo A5)</li>
	</ul>

The recovery process was validated with:
	<ul>
	<li>45,000+ SMS messages</li>
	<li>1,500+ call logs</li>
	</ul>

<h2>Features</h2>
<h3>SMS Recovery</h3>
	<ul>
	<li>Converts OPPO .vmsg SMS exports into Android-compatible XML</li>
	<li>Supports multi-message .vmsg files</li>
	<li>Decodes quoted-printable UTF-8 SMS content</li>
	<li>Preserves timestamps correctly</li>
	<li>Compatible with SMS Backup & Restore</li>
	</ul>

<h3>Call Log Recovery</h3>
	<ul>
	<li>Converts OPPO proprietary <CALL_RECORDS> XML exports</li>
	</ul>
	<ul>
	Preserves:
	<ul>
	<li>phone numbers</li>
	<li>call duration</li>
	<li>call type</li>
	<li>timestamps</li>
	<li>contact names</li>
	</ul>

<h3>Why this tool exists</h3>
Many old OPPO phones export SMS and call logs using proprietary formats that are not directly compatible with Android restore apps or Google restore services.
<p></p>
Common issues include:
	<ul>
	<li>Google Cloud restore failing</li>
	<li>Android migration incompatibilities</li>
	<li>unsupported OPPO backup formats</li>
	<li>timestamp conversion issues</li>
	<li>encoding problems in old SMS exports</li>
	</ul>
<p></p>
This tool converts those exports into formats recognized by Android restore applications.
<p></p>

<h2>Requirements</h2>
	<ul>
	<li>Python 3</li>
	<li>Required packages:</li>
	</ul>
	<p></p>	
	<pre>	pip install chardet</pre>
<p></p>	

<h3>** SMS Recovery Instructions **</h3>
<b>1. Export SMS from the old OPPO device:</b><br><br>
Copy the .vmsg backup files from the old phone to your computer.<br><br>

<b>2. Run the SMS converter</b>
   <pre>	python3 vmsg2xml.py</pre>

The script will:
	<ul>
	<li>detect encoding automatically</li>
	<li>decode SMS contents</li>
	<li>merge all messages into a single XML file</li>
	</ul>
<p></p>	
Output:
	<pre>	smss_converted.xml</pre>
		<p></p>
<b>3. Transfer the XML file to Android</b><br><br>
Copy:
	<pre>	smss_converted.xml</pre>
<p></p>
to your Android phone.
<p></p>
Recommended locations:
	<ul>
	<li>Download</li>
	<li>Internal Storage root</li>
	</ul>
<p></p>	
<b>4. Restore messages</b><br><br>
Install: <a href="https://play.google.com/store/apps/details?id=com.riteshsahu.SMSBackupRestore&hl=en&gl=US&pli=1">SMS Backup & Restore</a>
<p></p>
Then:
	<ul>
	<li>1-	Open the app</li>
	<li>2-	Select Restore</li>
	<li>3-	Choose Local Backup Location</li>
	<li>4-	Locate sms.xml</li>
	<li>5-	Restore Messages</li>
	</ul>


<h3>** Call Log Recovery Instructions **</h3>
<b>1. Export OPPO call logs XML</b><br><br>
Copy the original OPPO call log XML file to your computer.
<p></p>
Example OPPO structure:
<code>
	&lt;CallLog&gt;
		&lt;CALL_RECORDS ... /&gt;
		&lt;/CallLog&gt;
</code>
<p></p>
<b>2. Run the call log converter</b>
<p></p>
<pre>	python3 convert_calls.py</pre>
<p></p>
Output:
<p></p>
<pre>	calls_converted.xml</pre>
<p></p>
<b>3. Restore call logs</b><br></br>
Using SMS Backup & Restore:
	<ul>
	<li>1-	Open Restore</li>
	<li>2-	Select Call Logs</li>
	<li>3-	Locate:</li> 
		<pre>	calls_converted.xml</pre>
	<li>4-	Allow required Android permissions</li>
	<li>5-	Restore call history</li>
	</ul>
<p></p>
<h2>Notes:</h2>
	<ul>
	<li>Large restores may take several minutes</li>
	<li>Android may temporarily lag while indexing messages</li>
	<li>Timestamps are converted to milliseconds for Android compatibility</li>
	<li>The tool preserves UTF-8 characters and special symbols</li>
	</ul>
<p></p><br>
<b>*Tested Recovery Scenario*</b><br><br>
Successful migration from:
	<ul>
	<li>dead/broken OPPO motherboard</li>
	<li>failed Google Cloud restore</li>
	<li>inaccessible Android migration backups</li>
	</ul>
	<p></p>
Recovered successfully:
	<ul>
	<li>45K+ SMS</li>
	<li>1500+ call logs</li>
	</ul>
	<p></p><br>
<b>*Disclaimer*</b><br><br>
This tool was created for personal backup recovery purposes.<br>
Always create backups before restoring or modifying SMS/call log databases.

<h2>DEMO</h2>
demo folder -> Click file "vmsg&calls2xlm_DEMO.ipynb"

