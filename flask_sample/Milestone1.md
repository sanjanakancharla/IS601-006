<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Himanshu Tomar (ht272)</td></tr>
<tr><td> <em>Generated: </em> 12/21/2022 10:55:30 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone1-deliverable/grade/ht272" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209038380-4ab7a64d-d06f-4a0e-a2ad-64814e0e879c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows email invalid whenever the email filled is in wrong format.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209038452-cd2a1005-41c8-46d3-b6ae-98c4c8e9d510.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows invalid password<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209039452-b1de2f9b-ae6f-4d6e-bd8a-563cefcd9b91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows password length should be at least 8 character or long...<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209040175-d8338977-2f20-40fb-8c07-75831bf252b1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>already registered flash message changes <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209040426-f794d61d-04c9-47d9-8c0c-a6fe7a7745b2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User already exists added<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209040583-a89d8405-f579-4258-aaff-d930e7feb838.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Form Filled before registering screenshot added<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209040768-c45d3ebd-669d-44c7-8655-6fed17d97c89.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The valid data gets stored in database. 3rd entry is the proof.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/himanshu98/IS601Fall2022/pull/10">https://github.com/himanshu98/IS601Fall2022/pull/10</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>Every existing route data from the form would be inserted into the<br>database. I am using the Insert statement.<br>2) Every invalid entry is checked before<br>inserting into the database if any unexpected error has occurred then it is<br>handled using try-catch statement.<div>3) Password is handled, firstly it is checked while registering<br>in the frontend only whether confirmed password and password are same or not<br>and also the password if first decrypted using bycrypt library then it is<br>stored in database so as to make it secure .<br>4) Now if data<br>already exists and it is loggedin it will land to dashboard page.</div><br></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209042726-0f524093-962e-47f8-b47c-cb83b9053a5c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>When password doesn&#39;t match it shows invalid password.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209042821-fb7c3eb1-a0fc-4c09-b6e9-723dbb671b48.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>When user doesn&#39;t exists in database it shows appropriate message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209043291-f4523214-c198-4e09-9ecd-cfe18d5fa30d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of successful login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/himanshu98/IS601Fall2022/pull/10">https://github.com/himanshu98/IS601Fall2022/pull/10</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>Every existing route data from the form would be inserted into the<br>database. I am using the Insert statement.<br>2) Every invalid entry is checked before<br>inserting into the database if any unexpected error has occurred then it is<br>handled using try-catch statement.<div>3) Password is handled, firstly it is checked while registering<br>in the frontend only whether confirmed password and password are same or not<br>and also the password if first decrypted using bycrypt library then it is<br>stored in database so as to make it secure .</div><div>5) Password gets encrypted<br>and then gets compared to password present in the database.<br>4) Now if data<br>already exists and it is loggedin it will land to dashboard page.</div><br></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209044045-d42bd9d2-fe5f-4819-b4f4-e2facfb473b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successfully Logged out Page.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209044045-d42bd9d2-fe5f-4819-b4f4-e2facfb473b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>When not being logged in login page will come first<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/himanshu98/IS601Fall2022/pull/10">https://github.com/himanshu98/IS601Fall2022/pull/10</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div><font color="#273239" face="urw-din, sans-serif"><span style="font-size: 17px; letter-spacing: 0.162px;">Data that is required will be<br>saved in a temporary directory on the server and it is stored in<br>the top of cookies and signed by the server&nbsp;<br>cryptographically and it also remembered<br>the logged-in user</span></font></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209044784-59b56a12-950f-4425-bd71-c1d7ecf2a8e2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows that we are trying to access a page directly from a<br>route so it shows unauthorized message as this is not allowed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209044784-59b56a12-950f-4425-bd71-c1d7ecf2a8e2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows that permission is not granted to access this page.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209045586-79840959-139d-43b0-b2c7-9a814d84ce15.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin record added so roles drop down appears on landing page.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209045709-e4effa4d-3848-4d29-a7d5-eb50f622e923.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows admin data added<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209045781-dfe0ea39-41ed-4658-9e71-1ca9f8fdb703.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username of himanshu is admin above attached screen shot for reference.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/himanshu98/IS601Fall2022/pull/10">https://github.com/himanshu98/IS601Fall2022/pull/10</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>@login_required is used to protect the route it checks whether the required route<br>is accessible or not&nbsp;<br>Session stores the login information if the person has not<br>logged out he/she will be able to access the landing page.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p><span style="color: rgb(39, 50, 57); font-family: urw-din, sans-serif; font-size: 17px; letter-spacing: 0.162px;">Data that<br>is required will be saved in a temporary directory on the server and<br>it is stored in the top of cookies and signed by the server&nbsp;</span>&lt;br<br>style=&quot;color: rgb(39, 50, 57); font-family: urw-din, sans-serif; font-size: 17px; letter-spacing: 0.162px;&quot;&gt;<span style="color: rgb(39,<br>50, 57); font-family: urw-din, sans-serif; font-size: 17px; letter-spacing: 0.162px;">cryptographically and it also remembered<br>the logged-in user</span><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209046385-55870cc2-e935-463a-a6dc-96bbce9ff467.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Bootstrap styling has been used for navigation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209046427-21a51f6b-4fa6-4fd7-92f4-cb0bde7f0a75.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Bootstrap styling has been used for forms ,UI and everything<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/himanshu98/IS601Fall2022/pull/10">https://github.com/himanshu98/IS601Fall2022/pull/10</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>Bootstrap has been used which contains separate classes for each styling it has<br>been used to so as to make the UI quickly and mobile responsive.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209047882-3579a67d-4dc1-4d7c-b8bb-885b0306bb07.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the code where flash messages has been added<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/himanshu98/IS601Fall2022/pull/10">https://github.com/himanshu98/IS601Fall2022/pull/10</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>First step is to debug and find from where and which route the<br>message is being generated and then convert the flash messages into appropriate user<br>friendly message.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209048543-dd708ea5-821e-47f3-90dd-f93b1a4264d3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Above screen shot shows prefill User Profie<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/himanshu98/IS601Fall2022/pull/10">https://github.com/himanshu98/IS601Fall2022/pull/10</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <div style="color: rgb(212, 212, 212); background-color: rgb(30, 30, 30); font-family: Consolas, &quot;Courier New&quot;,<br>monospace; line-height: 19px; white-space: pre;"><div>&nbsp; <span style="color: #9cdcfe;">result</span> = <span style="color: #4ec9b0;">DB</span>.<span style="color:<br>#dcdcaa;">selectOne</span>(<span style="color: #ce9178;">"SELECT password FROM IS601_Users where id = </span><span style="color: #569cd6;">%s</span><span style="color:<br>#ce9178;">"</span>, <span style="color: #9cdcfe;">user_id</span>)</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color:<br>#c586c0;">if</span> <span style="color: #9cdcfe;">result</span>.status <span style="color: #569cd6;">and</span> <span style="color: #9cdcfe;">result</span>.row:</div><div>&nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #6a9955;"># verify current password</span></div><div>&nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #c586c0;">if</span> <span style="color:<br>#9cdcfe;">bcrypt</span>.<span style="color: #dcdcaa;">check_password_hash</span>(<span style="color: #9cdcfe;">result</span>.row[<span style="color: #ce9178;">"password"</span>], <span style="color: #9cdcfe;">current_password</span>):</div><div>&nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #6a9955;"># update new<br>password</span></div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span<br>style="color: #9cdcfe;">hash</span> = <span style="color: #9cdcfe;">bcrypt</span>.<span style="color: #dcdcaa;">generate_password_hash</span>(<span style="color: #9cdcfe;">password</span>)</div><div>&nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #c586c0;">try</span>:</div><div>&nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color:<br>#9cdcfe;">result</span> = <span style="color: #4ec9b0;">DB</span>.<span style="color: #dcdcaa;">update</span>(<span style="color: #ce9178;">"UPDATE IS601_Users SET password =<br></span><span style="color: #569cd6;">%s</span><span style="color: #ce9178;"> WHERE id = </span><span style="color: #569cd6;">%s</span><span style="color: #ce9178;">"</span>,<br><span style="color: #9cdcfe;">hash</span>, <span style="color: #9cdcfe;">user_id</span>)</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #c586c0;">if</span> <span style="color: #9cdcfe;">result</span>.status:</div><div>&nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; <span style="color: #dcdcaa;">flash</span>(<span style="color: #ce9178;">"Updated password"</span>, <span style="color: #ce9178;">"success"</span>)</div><div>&nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #c586c0;">except</span> <span style="color:<br>#4ec9b0;">Exception</span> <span style="color: #c586c0;">as</span> <span style="color: #9cdcfe;">ue</span>:</div><div><br></div><div><br></div><div><br></div><div>As per the above code data is<br>fetched from USers tables using id and then its gets populated in the<br>profile html page.</div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209049961-a130bc5f-ef35-44a7-ab09-c09f33dd0609.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209050281-1c43e4a2-f324-48ff-8526-32f994a78650.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email Validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209050377-e3c30770-8450-40e5-8082-c3ed2f9b8019.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password confirmation validation <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209050790-b630b4ba-4a08-4370-a735-226966ebaba9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before changing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209050867-5d09b470-2fef-484b-9159-14d4fcf89c7d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data Updated<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209051013-98073853-575a-47f8-93e2-9134826293fa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Updation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/20930496/209051074-bc5d4d64-7010-4f8e-b300-4242b414f3ce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Updation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/himanshu98/IS601Fall2022/pull/10">https://github.com/himanshu98/IS601Fall2022/pull/10</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>Edit logic is triggering the Update Statement so as to update user table.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>The only issues I faced while making changes debugging and adding roles were<br>a bit tricky using printout helped me to figure it out.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ht272-prod.herokuapp.com/">https://is601-ht272-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone1-deliverable/grade/ht272" target="_blank">Grading</a></td></tr></table>
