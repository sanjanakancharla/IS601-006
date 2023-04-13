<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Sanjana Kancharla (sk3298)</td></tr>
<tr><td> <em>Generated: </em> 4/12/2023 8:25:56 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/sk3298" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231346054-3e445cc7-8d5d-41e0-b3a1-f3094afc043e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this screenshot, DIAR-mt85 is updated to DIAR-ucid of mine sk3298(in nav.html)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231346641-c551c0fe-348f-469f-9638-b75cbffe97dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this screenshot, URL is visible and from heroku dev and &quot;Brought to<br>you by...&quot; message is updated to include student&#39;s firstname, ucid, and IS601 section.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231347526-e6f2186e-d0d9-419a-b136-0bb32cd18993.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Relevant url_for reference is added for company search and company add<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231347740-3e355bb3-6c76-46d6-a1f5-7ca453b5dbed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Relevant url_for reference is added for employee search and employee add<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231347961-14083590-de64-4faa-b6be-aeec0424a9dd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Relevant url_for reference is added for admin import<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231348919-5979a70b-f3af-4b61-af77-49654bcc27bf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this screenshot, IS601_MP3_Companies table is visible along with UCID and DB<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231349148-e509b8d5-6c69-45e1-8f5e-ecf22115979c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this screenshot, IS601_MP3_Employees table is visible along with UCID and DB<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231471247-2aaefe6a-ebc3-4f60-b057-7ba92d6ea502.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code checks if the file is a .csv file otherwise rejects with a<br>flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231471597-405af03c-79d7-40ef-bf5f-27ee471eb880.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>CSV file should be read from the provided stream as a dict<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231472047-19cce0ab-1618-4838-90d9-8ca50db3f8e0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Extracted company data is  appended as a dict to the company list<br>(only consider data if all fields are present for company)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231472580-2c7cf4ac-33fc-47c9-86a3-445611448868.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Extracted employee data is appended as a dict to the employee list (only<br>consider data if all fields are present for employee)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231473990-39aaa7cb-3992-4a2e-a661-0e4a72bbbe0e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After each query a flash message is  generated noting how many records<br>were processed and if  a particular lis t isempty a flash message<br>notes that the particular list wasn&#39;t loaded or was empty<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231474658-69e3bd2e-66a3-4f5c-bf6c-05974dd48cc8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Frontend screenshot showing flash msg for a file that is uploaded which is<br>not csv<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/205521919-c706839a-9a4f-432f-be53-c4626e0d3f5a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The above screenshots shows the flash message when data is successfully inserted it<br>also include no. of records imported.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231475265-6ef76b1d-4fe4-4662-8ad9-1bf8c26cdf7a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The above screenshot displays flash message when no file is selected.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231476245-c33565e9-dae2-4073-904c-7ee5cf692a55.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing some company data was uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231476536-d0f87385-045e-4674-b8a5-f46dbdf59cc0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing some employee data was uploaded<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231478975-5252ccfc-b209-4ff2-bf62-d26c8d22f1a7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code retrieves first_name, last_name, company (id), email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231479376-04e5ccf4-b58b-40d4-aca5-a4bf9baaba58.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for first_name is required (flash proper error message if missing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231479757-28f234ea-cdd2-4202-ab4b-438debe9034c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for last_name is required (flash proper error message if missing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231480001-b7709b8b-e9c7-4d3e-9701-3ad990c544d3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for company doesn&#39;t require a flash and may be empty/None<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231484419-05cd3d65-5c75-4135-895e-4df815c899c4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for email is required and Email format is verified (flash proper error<br>message if missing or invalid format)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231482539-da8785e7-e042-408e-871f-8a29e51305ee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for Proper INSERT query should be visible along with the data being<br>passed in<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231482973-8e8bdf51-b965-4897-9e8c-eb8c9e3a73cf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for Except block should have a user-friendly message flashed and a print()<br>of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231503361-1282ccb7-22ad-44ac-8dc1-0be002666313.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot displays filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231507156-a365de51-6585-4c26-8bea-c7453aa62514.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231505668-c36db5d3-47d0-45b3-bb1c-125b818ce776.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows first_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231506165-1143b8dd-8cfe-4f4e-a534-6113dbff6034.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows last_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231506515-2b30def4-c575-4471-addd-ebad156eca73.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows email error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231585743-f668f0d2-6029-4c7d-88e2-cc1122678907.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot includes the valid employee data shown previously and please check for<br>employee sanjana.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231586658-133da984-27c7-4e57-99f9-6bba378c5a9a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>select query to retrieve employee details<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231586841-9134c3e9-2d86-4b9a-948a-c8f790ac533a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>remaining part of the select query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231587116-0580db89-4d55-4b2c-8a76-9c3fd9610729.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Checks request args for fn, ln, email, company, column, order, limit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231587790-220cf232-aa96-412e-9d67-28edff39ea35.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows appending like filter for first_name, last_name, email and company_id<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231588787-6734245a-040c-4eb4-aa38-44ac91bdd097.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows appending of  sorting if column and order are provided,<br>append limit (default 10) or limit greater than or equal to 1 and<br>less than or equal to 100<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231589620-55d61814-e3e8-4a64-8576-49d2fe785ea1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>provides a proper error message if limit isn&#39;t a number or if it&#39;s<br>out of bounds<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231589864-15cea4c9-6d29-4ed0-a19a-141497b49568.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows that Except block has a user friendly message flashed and<br>a print() of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231591129-bade3a70-4ca0-48e2-860a-f71d4b8625bd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows results with first_name filter applied.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231591766-34ebca8f-65de-4d13-b153-06e157a35db5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows results with last_name filter applied.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231592299-000b9a5f-56a4-436e-9f55-a8fb19778664.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows results with email filter applied.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231593264-26d9f738-c521-4545-addd-fcf0bcf27739.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows results with company filter applied.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231594027-4bac66fb-1761-4df9-aee4-051aa4e1f4ca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows one asc filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231594894-3e6d7b60-7143-446e-8af0-17e2119bf4a5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows one desc filter applied<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231597195-b98e7963-99ee-441b-bd3a-ad8d4a3a0a56.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code retrieves id (from request args) first_name, last_name, company (id), email from form.<br>Missing id is handled with a flash message .<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231597465-15102740-73c9-429b-8a24-59041b4f7f9c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot displays code for flash messages for first_name , last_name ,email, company.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231597911-0fcd4aa3-6a71-4695-89d4-57537344296c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot displays code for UPDATE query, except blocks, employee data is passed<br>to render .<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231598458-af3b2d1f-b6f7-4733-851c-28cbf192a5c5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper SELECT query is visible in this screenshot.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231600153-f321bac0-ce2a-4558-aca7-a11bc3e1b9ad.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231600402-b168b389-dcc2-4960-9a1e-9394d4630296.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show data after an edit (should be different)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231601069-01805bfb-0bd2-4481-8f72-dc541f7e988c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>when data&#39;s gets updated.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231602102-dd9a3f15-2f09-45b8-9128-3da751ba7da6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ID 6595 with first name Joseph before updation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231602387-4b537862-9a5a-47f4-9cbb-dd0629bd01c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ID 6595 with first name Joseph after updation to name Joe<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231603252-19292b8c-0f16-47b7-a89c-31568ed0fc0b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code retrieves form data for name, address, city, state, country, zip, website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231603609-10a62fa3-515a-4f32-8c41-cbbb41aa7a0f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot displays that the following items are required, name, address, city, state,<br>country.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231604053-821b5e26-12ac-4817-b001-6fe0012379f4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot displays, website is not required, zipcode is required, INSERT query <br>is be visible along with the data being inserted, Except blocks with a<br>user friendly msg.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231605684-cff65d76-8ff1-4b42-8f62-50a7a1593049.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show filled in valid data prior to submisson<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231606140-3ae6da6f-71e6-4dc1-9c32-028cf9f6f642.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show filled in valid data prior to submissin- remaining part<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231606292-e4660ccf-686a-4fe4-bbb9-5c7c0485c905.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231606701-7409ecb1-8c40-4e39-be0e-408ad25149e3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>1)Show name,adress,city,state,company error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231607897-c2368e73-9ba4-41f1-959b-3fc34e6a69b1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Includes the valid company data shown previously.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231608239-d3b76b45-f671-42d7-b142-bad91a2b07da.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows SELECT query , checks request args, appends a LIKE filter<br>for name, country, state, sorting .<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231608535-e5931ca3-7267-4e6a-8f7d-20152def185f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot displays append limit, error msg if limit isnt a number or<br>out of bounds.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231608792-10d70e5a-b7e1-4a58-a8de-24698c4e9a86.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot displays user friendly msg and prints exception.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231609714-fbb959c9-ff5b-4464-a7d0-c9fa7acd5ed5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231609992-98249b0f-eef1-453d-80da-a61dddb0489a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with state filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231610580-81e57768-75c7-4d63-b50f-3f4869a97cfc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows name asc filter applied <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231610778-a56e815b-f034-4597-bd6c-edc86d869654.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows name desc filter applied <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231610899-e03368fc-46d4-4731-b480-2aa6c950615f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code is retrieved and flash msg for ID<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231611445-86716ec7-7110-49a8-be53-c81e59f33c84.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>flash msgs for name, address, city , state, country.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231611614-954e5d00-878a-4635-af45-cdf9ee7ed24b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>this screenshot shows, UPDATE query, except blocks, select query, render template.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231612101-824f8be0-f038-44dc-81a4-481adb38bb9a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show data before an edit, the first row company name is being edited<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231612330-7dc48874-2b9e-4117-b764-988189c8da0d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show data after an edit, the first row company data as it is<br>edited, it is differnet from above<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231612537-a1bf910e-7843-41ef-8e99-fe1486e653af.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>here ID no:1 company name is going to be changed.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231612638-a8baa41a-f0bf-4bb5-86af-520ff868e073.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>here ID no:1 company name is successfully changed.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231612987-d13a9de2-20d2-4aa4-a421-a5d372496b44.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>delete employee route, redirects, msg is displayed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231613188-7563e3e9-58bb-4d7a-ad78-5b1bb0d524df.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>deleted employee sanjana<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231613291-7bffa9bb-8460-44f1-ad9b-9a129a599760.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message displayed after deleteing employee sanjana<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231613051-2a71472a-6796-493f-bf79-ba5b2034f119.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>delete company route, redirects, msg is displayed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231613528-e8c6df6d-78e4-4b95-82d0-c7c7895e6409.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting company &quot;Morlong associates&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/231613633-26ace7c6-b09e-43f3-9f82-789a978a6694.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting company &quot;Morlong associates&quot;<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/205535899-8eb85ad1-9195-40db-9083-02b331cbcb9a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>running pytest command to run test cases<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/205536019-c23ff784-d3c2-4ae7-8611-bf88af858b91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screen shot shows all test cases passed !!<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <ol dir="auto" style="box-sizing: border-box; padding-left: 2em; margin-top: 0px; margin-bottom: 16px; color: rgb(31, 35,<br>40); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color<br>Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px; background-color: rgb(246, 248, 250);"><li style="box-sizing: border-box;">Learned about<br>flask framework and how to make full fledge full stack application<br style="box-sizing: border-box;">using<br>mysql,html,css and python.</li><li style="box-sizing: border-box; margin-top: 0.25em;">Learned about complex queries in sql and<br>how we can<br style="box-sizing: border-box;">join tables in SQL.</li><li style="box-sizing: border-box; margin-top: 0.25em;">Also learn<br>about application deployment using heroku.</li><li style="box-sizing: border-box; margin-top: 0.25em;">Learned about pytest library<br style="box-sizing:<br>border-box;">where we can make sure whether entire functionality running properly or not and<br<br>style="box-sizing: border-box;">also it helps in making app bugs free.</li></ol><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/sk3298" target="_blank">Grading</a></td></tr></table>
