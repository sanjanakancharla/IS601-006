<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Burgers</td></tr>
<tr><td> <em>Student: </em> Sanjana Kancharla (sk3298)</td></tr>
<tr><td> <em>Generated: </em> 3/28/2023 2:18:44 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-2-burgers/grade/sk3298" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb">https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder BurgerMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/225415257-68fcbbe7-1e05-49e8-abc6-bd7809ed39c2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot displays the function that is calculating the cost of the burger<br>by iterating through the in_progress burger array and then returning the cost.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/225416105-959888ca-88a3-4767-9fa7-12aa94df9232.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The following screenshots shows the value in currency format along with the $<br>sign.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/225416868-0dc169aa-5906-4a56-9310-8e339dc9a842.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The $ sign has been appended to total cost so as to get<br>proper currency format.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>To implement the <b>calculate_cost()</b> function in the BurgerMachine class, we need to,<div>&nbsp;<br>&nbsp; &nbsp;* Define a variable cost and initialize it with 0.</div><div>&nbsp; &nbsp; &nbsp;<em><br>Iterate over the inprogress_burger array and add the cost of each item to<br>the cost variable.&nbsp;</div><div>&nbsp; &nbsp; &nbsp;</em> Return the cost variable at the end of<br>the function.<br></div><div><br></div><div>2. In Order to handle the currency format the proper currency format<br>has been achieved by putting the $ sign in&nbsp;<span style="background-color: rgb(30, 30, 30);<br>font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre; color: rgb(156, 220, 254);">total</span><span style="background-color: rgb(30,<br>30, 30); color: rgb(212, 212, 212); font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre;"><br>= </span><span style="background-color: rgb(30, 30, 30); font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre;<br>color: rgb(220, 220, 170);">input</span><span style="background-color: rgb(30, 30, 30); color: rgb(212, 212, 212); font-family:<br>Consolas, &quot;Courier New&quot;, monospace; white-space: pre;">(</span><span style="background-color: rgb(30, 30, 30); font-family: Consolas, &quot;Courier<br>New&quot;, monospace; white-space: pre; color: rgb(86, 156, 214);">f</span><span style="background-color: rgb(30, 30, 30); font-family:<br>Consolas, &quot;Courier New&quot;, monospace; white-space: pre; color: rgb(206, 145, 120);">&quot;Your total is $</span>&lt;span<br>style=&quot;background-color: rgb(30, 30, 30); font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre; color: rgb(86,<br>156, 214);&quot;&gt;{</span><span style="background-color: rgb(30, 30, 30); font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre;<br>color: rgb(156, 220, 254);">expected</span><span style="background-color: rgb(30, 30, 30); font-family: Consolas, &quot;Courier New&quot;, monospace;<br>white-space: pre; color: rgb(86, 156, 214);">}</span><span style="background-color: rgb(30, 30, 30); font-family: Consolas, &quot;Courier<br>New&quot;, monospace; white-space: pre; color: rgb(206, 145, 120);">, please enter the exact value.</span>&lt;span<br>style=&quot;background-color: rgb(30, 30, 30); font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre; color: rgb(215,<br>186, 125);&quot;&gt;\n</span><span style="background-color: rgb(30, 30, 30); font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre;<br>color: rgb(206, 145, 120);">&quot;</span><span style="background-color: rgb(30, 30, 30); color: rgb(212, 212, 212); font-family:<br>Consolas, &quot;Courier New&quot;, monospace; white-space: pre;">)</span></div><div style="color: rgb(212, 212, 212); background-color: rgb(30, 30,<br>30); font-family: Consolas, &quot;Courier New&quot;, monospace; line-height: 19px; white-space: pre;"><div></div></div><div><br></div><div><br></div><div><br></div><br></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228121998-9edb3795-f544-413d-a4f9-06a5dbee8cf6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code snippet for outofstockexception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228122241-3e972404-4cf2-47cf-9180-34ebb517a757.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code snippet for NeedsCleaningException <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228122481-57e34376-07b4-4acf-af32-1897cee849e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code snippet for InvalidChoiceException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228122798-56fe207b-5477-4045-a90a-b15c42bda22b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code snippet for ExceededRemainingChoicesExceptions <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228123012-2d5a09f1-b0fb-449d-acf1-904dbf3b297f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code snippet for InvalidPaymentException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228136879-6d60067f-5012-44b4-96ad-dbf4fea7ba01.jpeg"/></td></tr>
<tr><td> <em>Caption:</em> <p> The OutOfStockException is handled with proper user feedback and continued program flow.<br>Shows the stage/category that the choice was out of stock in.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228137326-8891bc04-f70c-46ae-9eec-2776091ef7b0.jpeg"/></td></tr>
<tr><td> <em>Caption:</em> <p>The NeedsCleaningException is handled where it prompts the user to type the word<br>&#39;clean&#39; to clean the machine; other words are ignored. Displays a message whether<br>or not the machine was cleaned.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228137637-be9eb1b7-9a8c-4fad-9329-f3a458879357.jpeg"/></td></tr>
<tr><td> <em>Caption:</em> <p>The various InvalidChoiceExceptions are handled with proper user feedback and continued program flow.<br>Show the stage/category that the choice was invalid in.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228137883-9eb2d9c3-db66-4da0-ba75-d3d151a16a0b.jpeg"/></td></tr>
<tr><td> <em>Caption:</em> <p> The various ExceededRemainingChoicesExceptions are handled with proper user feedback and continued program<br>flow. Shows the stage/category where the choice limit was exceeded. Moves the user<br>to the next stage/category.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228138128-4d0473fb-4e98-4972-84f6-9494297cce52.jpeg"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows how the InvalidPaymentException is handled with proper user feedback and continued program<br>flow.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <p>The code defines custom exceptions for specific scenarios that may occur while a<br>user interacts with a Burger making program. These custom exceptions are defined in<br>a separate file named BurgerMachineExceptions.py. The exceptions include: ExceededRemainingChoicesException: raised when the user<br>attempts to select more patties or toppings than the limit allows InvalidChoiceException: raised<br>when the user selects an invalid option InvalidStageException: raised when the user tries<br>to select an item out of order NeedsCleaningException: raised when the BurgerMachine requires<br>cleaning before it can be used again OutOfStockException: raised when an item is<br>out of stock and cannot be used InvalidPaymentException: raised when the user tries<br>to pay an amount that does not match the total cost of the<br>burger.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228107856-e2371473-b0bb-448d-b453-99f5e0497961.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228108195-db6ca089-4d32-4782-a3b8-a2dd1e1ca442.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228109266-5fe96977-9190-4714-aee7-b4d02ef4ae7e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228109413-b0c8600f-5861-4b22-9976-7c3a27af3f4b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228109759-657a368a-9f36-4a60-8432-785b5b30bc6b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228109941-5a179c76-e3f8-49ca-8d66-852cd357b5a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test6<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228110124-6da7dda0-6628-4c7c-aa68-8d1bf2cc7feb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test7<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228110415-d15e055f-1335-4501-ba73-c7fe697ecec0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228119308-d6f7012a-11eb-4afb-97b8-0392699ffdfe.jpeg"/></td></tr>
<tr><td> <em>Caption:</em> <p>this screenshot shows that all 1-8 testcases are passing in the terminal.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <div><font color="#111827" face="Söhne Mono, Monaco, Andale Mono, Ubuntu Mono, monospace"><b>1. test_first_selection: </b>This test<br>case checks if the current selection stage is correctly set to the STAGE.Bun.</font></div><div><font<br>color="#111827" face="Söhne Mono, Monaco, Andale Mono, Ubuntu Mono, monospace"><b><br></b></font></div><div><font color="#111827" face="Söhne Mono, Monaco,<br>Andale Mono, Ubuntu Mono, monospace"><b>2.test_patties_in_stock: </b>This test case checks if the program correctly<br>detects whether there is a sufficient quantity of patties in stock or not.</font></div><div><font<br>color="#111827" face="Söhne Mono, Monaco, Andale Mono, Ubuntu Mono, monospace"><b><br></b></font></div><div><font color="#111827" face="Söhne Mono, Monaco,<br>Andale Mono, Ubuntu Mono, monospace"><b>3.test_toppings_in_stock: </b>This test case checks if the program correctly<br>detects whether there is a sufficient quantity of toppings in stock or not.</font></div><div><font<br>color="#111827" face="Söhne Mono, Monaco, Andale Mono, Ubuntu Mono, monospace"><b><br></b></font></div><div><font color="#111827" face="Söhne Mono, Monaco,<br>Andale Mono, Ubuntu Mono, monospace"><b>4.test_max_patties: </b>This test case checks if the program correctly<br>detects when the maximum number of patties has been reached.</font></div><div><font color="#111827" face="Söhne Mono,<br>Monaco, Andale Mono, Ubuntu Mono, monospace"><b><br></b></font></div><div><font color="#111827" face="Söhne Mono, Monaco, Andale Mono, Ubuntu<br>Mono, monospace"><b>5.test_max_toppings: </b>This test case checks if the program correctly detects when the<br>maximum number of toppings has been reached.</font></div><div><font color="#111827" face="Söhne Mono, Monaco, Andale Mono,<br>Ubuntu Mono, monospace"><b><br></b></font></div><div><font color="#111827" face="Söhne Mono, Monaco, Andale Mono, Ubuntu Mono, monospace"><b>6.test_total_cost: </b>This<br>test case checks if the program correctly calculates the total cost of a<br>burger.</font></div><div><font color="#111827" face="Söhne Mono, Monaco, Andale Mono, Ubuntu Mono, monospace"><b><br></b></font></div><div><font color="#111827" face="Söhne Mono,<br>Monaco, Andale Mono, Ubuntu Mono, monospace"><b>7.test_total_sales:</b> This test case checks if the program<br>correctly calculates the total sales.</font></div><div><font color="#111827" face="Söhne Mono, Monaco, Andale Mono, Ubuntu Mono,<br>monospace"><b><br></b></font></div><div><font color="#111827" face="Söhne Mono, Monaco, Andale Mono, Ubuntu Mono, monospace"><b>8.test_total_burgers: </b>This test case<br>is commented out, but it is intended to check if the program correctly<br>calculates the total number of burgers sold.</font></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sanjanakancharla/IS601-006/pull/15">https://github.com/sanjanakancharla/IS601-006/pull/15</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>I learnt a lot during this assignment, I got a good understanding on<br>the different types of exceptions in python. and how to handle these exceptions.<br>I was able to write custom exceptions. I am more familiar with python<br>now. I faced difficulty while handling the exceptions in the program. for example<br>, to prompt user to clean machine().<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228127480-80356ee7-8ceb-4654-b0d6-ba93d31fd368.jpeg"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this screenshot, the program execution is successfull, the type of burger bun,<br>1 patty type, 2 different toppings are selected and the total cost is<br>computed successfully , i.e 2.75. we get thank you message at the end<br>and the program executes again. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/228127691-e7ae40d2-e8bb-427e-8900-4e47a6d9cfb1.jpeg"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this screenshot, the program execution is successfull, the type of burger bun,<br>patty is not selected, 1 topping is selected and the total cost is<br>computed successfully , i.e 1.75. we get thank you message at the end<br>and the program executes again. <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-2-burgers/grade/sk3298" target="_blank">Grading</a></td></tr></table>
