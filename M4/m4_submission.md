<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Sanjana Kancharla (sk3298)</td></tr>
<tr><td> <em>Generated: </em> 2/27/2023 8:30:01 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/sk3298" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sum-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/221299355-303ef431-bac7-4a77-8fde-03c9b276cefc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In the screenshot, I am showing add function, I have cropped it out<br>from my vs code, it performs the addition by taking inputs of 2<br>numbers<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/221299638-d574cb3f-0e88-4f7b-954e-091e6ab282c9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In the screenshot, I am showing subtractfunction, I have cropped it out from<br>my vs code, it performs the subtraction by taking inputs of 2 numbers.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/221300076-c2e63201-1979-4efb-b9c8-b2585bf7ee4e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In the screenshot, I am showing multiplication function, I have cropped it out<br>from my vs code, it performs the multiplying by taking inputs of 2<br>numbers.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/221300925-7e358c4a-75a5-4460-81a8-cf616c365219.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In the screenshot, I am showing division function, I have cropped it out<br>from my vs code, it performs the division by taking inputs of 2<br>numbers.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/221695144-1210811b-1efc-4ea2-b199-bef35ed0ca1f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot shows if the test case checks whether the add function correctly<br>adds two numbers and returns the expected result. and also processes series of<br>data.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/221304941-90979996-ec0e-4fda-b003-0c0103dec4c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>I opened the test tab and configured pytest, and ran the mentioned testcase,<br>it can be tracked at he left hand side and also the green<br>tick symbol next to the fucntion def shows the testcase passed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/221696236-d3607dd5-2551-403b-854a-34b02bf4a870.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot shows if the test case checks whether the add function correctly<br>adds two numbers where one among them is a variable &quot;ans&quot; which has<br>a value assigned, returns the expected result. and also processes series of data.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/221696567-eeef62bc-0c28-4b6d-8a04-f625d4a60f02.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>I opened the test tab and configured pytest, and ran the mentioned testcase,<br>it can be tracked at he left hand side and also the green<br>tick symbol next to the fucntion def shows the testcase passed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/221697102-036d06ff-d9a1-4264-ba6d-3b01f2fcbb59.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot shows if the test case checks whether the sub function correctly<br>subtracts two numbers , returns the expected result. and also processes series of<br>data.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/221697346-01915d1c-cb85-47d8-9fc4-9ccc91d4cc81.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>I opened the test tab and configured pytest, and ran the mentioned testcase,<br>it can be tracked at he left hand side and also the green<br>tick symbol next to the function def shows the testcase passed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/221698401-5ca51c3b-cb78-484b-bb82-7ed46fa70d09.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot shows if the test case checks whether the sub function correctly<br>subtracts two numbers with &quot;ans&quot; variable that has a value assigned, returns the<br>expected result. and also processes series of data.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/221698801-69283a44-454a-4fe4-8b8e-49f7aaec8f00.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>I opened the test tab and configured pytest, and ran the mentioned testcase,<br>it can be tracked at he left hand side and also the green<br>tick symbol next to the function def shows the testcase passed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/221722463-9dbf4599-b0df-4ed5-9555-84d002ec7fc0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows if the test case checks whether the test_number_mult_number function correctly<br>multiplies two numbers , returns the expected result. and also processes series of<br>data.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/221723002-6bb8e2cd-9af2-48ea-b1da-13d746821c2a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>I opened the test tab and configured pytest, and ran the mentioned testcase,<br>it can be tracked at he left hand side and also the green<br>tick symbol next to the function def shows the testcase passed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/221723672-b91f24e3-3866-446b-9808-03d1fb3debd5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot shows if the test case checks whether the ans-multi-number function correctly<br>multiplies two numbers with &quot;ans&quot; variable that has a value assigned, returns the<br>expected result. and also processes series of data.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/221724350-337b2991-4859-4604-8873-aab0b59efb47.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>I opened the test tab and configured pytest, and ran the mentioned testcase,<br>it can be tracked at he left hand side and also the green<br>tick symbol next to the function def shows the testcase passed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/221725608-3b73672a-91b2-4d93-9245-edb1a7921ae5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows if the test case checks whether the test_number_div_number function correctly<br>divides two numbers , returns the expected result. and also processes series of<br>data.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/221725884-f4823bfa-ace1-4a8c-8674-014b9d1c38e3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>I opened the test tab and configured pytest, and ran the mentioned testcase,<br>it can be tracked at he left hand side and also the green<br>tick symbol next to the function def shows the testcase passed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/221725992-76953e28-3965-4e94-9c94-d73f04d22115.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot shows if the test case checks whether the test_ans_div_number function correctly<br>divides two numbers with &quot;ans&quot; variable that has a value assigned, returns the<br>expected result. and also processes series of data.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/221726187-6ec7467f-6f3d-4738-b5d5-f44f1066b553.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>I opened the test tab and configured pytest, and ran the mentioned testcase,<br>it can be tracked at he left hand side and also the green<br>tick symbol next to the function def shows the testcase passed.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>I have learnt certain new things from implementing the calculator class. The<i> <b>if<br><strong>name</strong> == &#39;<strong>main</strong>&#39;:</b></i><b> block</b> provides a way to run the code as a<br>script and interact with the calculator using the CLI. another thing is I<br>have learnt how <b>error handling </b>can be done for invalid inputs and division<br>by zero. and I have learnt how to write<b> unit tests</b> in python<br>and about the unittest and unittest.mock libraries that are used to carry out<br>the tests.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <div><span style="background-color: rgb(247, 247, 248);"><font color="#374151" face="Söhne, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto,<br>Ubuntu, Cantarell, Noto Sans, sans-serif, Helvetica Neue, Arial, Apple Color Emoji, Segoe UI<br>Emoji, Segoe UI Symbol, Noto Color Emoji"><span style="font-size: 16px; white-space: pre-wrap;">The test case<br>consists of two variables, a and b, which are input values to the<br>add/sub/multiply functions, and a third variable, <b>expected_output</b>, which is the expected output of<br>the add function with those input values. The assert statement is then used<br>to compare the actual output of the add function with the expected output.<br>If the actual output matches the expected output, then the test case passes.<br>Otherwise, the <b>assert </b>statement raises an <b>AssertionError</b>, indicating that the test case has<br>failed. </span></font></span></div><div><span style="background-color: rgb(247, 247, 248);"><font color="#374151" face="Söhne, ui-sans-serif, system-ui, -apple-system, Segoe UI,<br>Roboto, Ubuntu, Cantarell, Noto Sans, sans-serif, Helvetica Neue, Arial, Apple Color Emoji, Segoe<br>UI Emoji, Segoe UI Symbol, Noto Color Emoji"><span style="font-size: 16px; white-space: pre-wrap;"><br></span></font></span></div><div><span style="background-color:<br>rgb(247, 247, 248);"><font color="#374151" face="Söhne, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell,<br>Noto Sans, sans-serif, Helvetica Neue, Arial, Apple Color Emoji, Segoe UI Emoji, Segoe<br>UI Symbol, Noto Color Emoji"><span style="font-size: 16px; white-space: pre-wrap;">From the above code, I<br>can see that test cases are an essential aspect of software development as<br>they ensure that the program functions as expected and helps in finding any<br>bugs or errors. The use of <b>assert </b>statements is a standard practice in<br>writing test cases as they provide an easy and efficient way to check<br>that the actual output of the program matches the expected output.</span></font><br></span></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/sk3298" target="_blank">Grading</a></td></tr></table>