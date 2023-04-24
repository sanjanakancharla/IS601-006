<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Sanjana Kancharla (sk3298)</td></tr>
<tr><td> <em>Generated: </em> 4/24/2023 2:28:58 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/sk3298" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/233724725-057f7c3f-b85d-405a-ab39-a6855bd211a3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin create page with a valid data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/234083332-9ee3e22d-ad68-4e41-a62c-588f94f4c1d6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows populated product table with name , descriptions ,category, stock and other<br>important attributes<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <div>The values are sent to the item function in shop.py after being entered<br>on the add page. To determine if the action is to edit or</div><div>add,<br>it looks to see if an id has been passed. This is a<br>create action since no id is supplied; hence, an INSERT statement is</div><div>executed passing<br>the values to the Products table, and if successful, a flash is shown.</div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sanjanakancharla/IS601-006/pull/24">https://github.com/sanjanakancharla/IS601-006/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3298-prod.herokuapp.com/admin/item">https://is601-sk3298-prod.herokuapp.com/admin/item</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/233734090-97eec865-ec50-4628-b2dc-a59e9f7026ff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page showing items without filters/sorting applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/233734314-8f39e3a3-ea1f-4a87-9493-3df7f44af3ca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page showing items without filters/sorting applied - continuation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/233763102-9e145666-61cc-4c98-8609-24ee70854479.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page showing both filter with Electronics and sorted from<br>low to high price<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/233763366-d8cb9591-e047-4a5e-b6de-e6a7731ceb12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page showing both filter with food and sorted from<br>high to low<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/233550295-95f1a40d-c749-4bd4-80cf-f55a42d7f41d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows code to sort as per the FilterBy and sortBY parameters provided<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <p>First data is taken as a parameter for sort and filter By value<br>as this is indicated in the code above. then once the data is<br>fetched from database we have used inbuilt python array.sort which takes key as<br>a parameter so as to filter out the values based on parameters provided<br>by the user.<br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sanjanakancharla/IS601-006/pull/24">https://github.com/sanjanakancharla/IS601-006/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3298-prod.herokuapp.com/shop?name=&category=Food&price=ASC">https://is601-sk3298-prod.herokuapp.com/shop?name=&category=Food&price=ASC</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/233763681-42a3351e-5116-4fcf-ab54-615223520880.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Admin List page/results<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <div>Without applying any filters, we choose every field from the Products database and<br>feed it to the HTML page. Since no conditions are stated anywhere, every<br>product will be shown regardless of visibility status.</div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sanjanakancharla/IS601-006/pull/24">https://github.com/sanjanakancharla/IS601-006/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3298-prod.herokuapp.com/admin/items">https://is601-sk3298-prod.herokuapp.com/admin/items</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/233763831-39f152c8-bcd2-435d-9aff-57ed59f824c9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the edit button visible to the Admin on the Shop<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/233764062-3e55a66d-9479-45cd-a9a6-a1a8bf3bfb25.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the edit button visible to the Admin on the Product Details<br>Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/233764180-e34de0b2-bddf-4d2b-a735-83d56319c3a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add a screenshot showing the edit button visible to the Admin on the<br>Admin Product List Page (The admin page)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/233764414-c2ff7120-8cc2-4b18-a1a1-c54bb9c12f19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the edit page with present details of the product DEERC Drone<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/233764637-61e6f63e-56db-4ae6-a9c4-1764d1bdf8ce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the list of products before editing the product DEERC Drone<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/233764758-45571ce3-88a3-4c5a-bcc6-ae819d26dddd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the list of products after editing the product DEERC Drone<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <div><font color="#1f2328" face="-apple-system, BlinkMacSystemFont, Segoe UI, Noto Sans, Helvetica, Arial, sans-serif, Apple Color<br>Emoji, Segoe UI Emoji"><span style="font-size: 16px;">Every product in shop.html has a check to<br>see whether the user is&nbsp;</span></font><span style="font-size: 16px; color: rgb(31, 35, 40); font-family: -apple-system,<br>BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI<br>Emoji&quot;;">logged in and if they are an admin. If both are true, we&nbsp;</span><span<br>style="font-size: 16px; color: rgb(31, 35, 40); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;,<br>Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;">display an edit button that<br>takes the user to the item page with&nbsp;</span><span style="font-size: 16px; color: rgb(31, 35,<br>40); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color<br>Emoji&quot;, &quot;Segoe UI Emoji&quot;;">the product details.</span></div><div><font color="#1f2328" face="-apple-system, BlinkMacSystemFont, Segoe UI, Noto Sans,<br>Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji"><span style="font-size: 16px;">The edit button<br>is displayed on the item details page if&nbsp;</span></font><span style="font-size: 16px; color: rgb(31, 35,<br>40); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color<br>Emoji&quot;, &quot;Segoe UI Emoji&quot;;">the user is an admin.</span></div><div><font color="#1f2328" face="-apple-system, BlinkMacSystemFont, Segoe UI,<br>Noto Sans, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji"><span style="font-size: 16px;">Since<br>only administrators can access the page, the edit&nbsp;</span></font><span style="font-size: 16px; color: rgb(31, 35,<br>40); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color<br>Emoji&quot;, &quot;Segoe UI Emoji&quot;;">button is the default on the admin items page.</span></div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sanjanakancharla/IS601-006/pull/24">https://github.com/sanjanakancharla/IS601-006/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3298-prod.herokuapp.com/itemdetails?id=1">https://is601-sk3298-prod.herokuapp.com/itemdetails?id=1</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/234075618-39bf2a85-909d-4569-801a-be20f45ced85.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the button (clickable item) that directs the user to the Product<br>Details Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/234075844-2497a3b3-552a-42fd-8ee2-0c0b667cddb5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the result of the Product TV Sony<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <div>For this, I made the itemdetails.html and item details functions.</div><div>The product name has<br>been made clickable; when clicked, it will send the product id to the<br>item details function, which will retrieve all the information from the Products database<br>using the id and display it on the item details page.</div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sanjanakancharla/IS601-006/pull/24">https://github.com/sanjanakancharla/IS601-006/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3298-prod.herokuapp.com/itemdetails?id=5">https://is601-sk3298-prod.herokuapp.com/itemdetails?id=5</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/234076464-1ae82cdf-1c75-4255-8856-2d3575fb738d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the success message of adding TV item to the cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/234076789-f2342e68-d6e0-4f2c-8f87-834b484ce941.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the error message of adding to cart when not logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/234077270-77f1443d-d227-4f19-8da0-c8b8eca37969.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB showing some records of carts<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <div><font color="#1f2328" face="-apple-system, BlinkMacSystemFont, Segoe UI, Noto Sans, Helvetica, Arial, sans-serif, Apple Color<br>Emoji, Segoe UI Emoji"><span style="font-size: 16px;">Product id and user id serve as the<br>composite unique key for one&nbsp;</span></font><span style="font-size: 16px; color: rgb(31, 35, 40); font-family: -apple-system,<br>BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI<br>Emoji&quot;;">cart per user.</span></div><div><font color="#1f2328" face="-apple-system, BlinkMacSystemFont, Segoe UI, Noto Sans, Helvetica, Arial, sans-serif,<br>Apple Color Emoji, Segoe UI Emoji"><span style="font-size: 16px;"><br></span></font></div><div><font color="#1f2328" face="-apple-system, BlinkMacSystemFont, Segoe UI,<br>Noto Sans, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji"><span style="font-size: 16px;">And<br>receives the products from the shop whenever a user is&nbsp;</span></font><span style="font-size: 16px; color:<br>rgb(31, 35, 40); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif,<br>&quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;">added to the cart a insert query will<br>perform that inserts the data</span></div><div><font color="#1f2328" face="-apple-system, BlinkMacSystemFont, Segoe UI, Noto Sans, Helvetica,<br>Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji"><span style="font-size: 16px;">into the cart. and<br>also perform an update and delete queries when a&nbsp;</span></font><span style="font-size: 16px; color: rgb(31,<br>35, 40); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple<br>Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;">user wants to update quantity or delete a product.</span></div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <div>When the amount field is provided to the cart function in shop.py by<br>clicking the ADD button, the product id is passed as a hidden field<br>and as long as the quantity is larger than 0,&nbsp;</div><div>we insert the product<br>id, user id, desired quantity, and unit price (fetching it from products table)</div><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sanjanakancharla/IS601-006/pull/24">https://github.com/sanjanakancharla/IS601-006/pull/24</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/234079081-bb5d7bde-db9c-4022-b226-b7ef982972e2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart View with subtotal of each line and adding up,<br>cart total, link to product details page for each product<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <div><font color="#1f2328" face="-apple-system, BlinkMacSystemFont, Segoe UI, Noto Sans, Helvetica, Arial, sans-serif, Apple Color<br>Emoji, Segoe UI Emoji"><span style="font-size: 16px;">When we click the cart, the function checks<br>to see if a product&nbsp;</span></font><span style="font-size: 16px; color: rgb(31, 35, 40); font-family: -apple-system,<br>BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI<br>Emoji&quot;;">id is being passed and, if it isn't, it recognizes that this isn't</span></div><div><font<br>color="#1f2328" face="-apple-system, BlinkMacSystemFont, Segoe UI, Noto Sans, Helvetica, Arial, sans-serif, Apple Color Emoji,<br>Segoe UI Emoji"><span style="font-size: 16px;">an add or update function. It then moves to<br>the SELECT block to&nbsp;</span></font><span style="font-size: 16px; color: rgb(31, 35, 40); font-family: -apple-system, BlinkMacSystemFont,<br>&quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;">get<br>the user id, id, product id, name, and desired quantity, calculates the</span></div><div><font color="#1f2328"<br>face="-apple-system, BlinkMacSystemFont, Segoe UI, Noto Sans, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe<br>UI Emoji"><span style="font-size: 16px;">subtotal by multiplying the desired quantity by the unit price,<br>and passes these&nbsp;</span></font><span style="font-size: 16px; color: rgb(31, 35, 40); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe<br>UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;">values to<br>cart.html.</span></div><div><font color="#1f2328" face="-apple-system, BlinkMacSystemFont, Segoe UI, Noto Sans, Helvetica, Arial, sans-serif, Apple Color<br>Emoji, Segoe UI Emoji"><span style="font-size: 16px;">For the purpose of calculating the total, we<br>render each item&nbsp;</span></font><span style="font-size: 16px; color: rgb(31, 35, 40); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe<br>UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;">as a<br>row in a table in the HTML output, add the subtotal&nbsp;</span><span style="font-size: 16px;<br>color: rgb(31, 35, 40); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial,<br>sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;">value for each row to a variable<br>called ns.total, and then display the&nbsp;</span><span style="font-size: 16px; color: rgb(31, 35, 40); font-family:<br>-apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe<br>UI Emoji&quot;;">total at the bottom.</span></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sanjanakancharla/IS601-006/pull/24">https://github.com/sanjanakancharla/IS601-006/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3298-prod.herokuapp.com/cart">https://is601-sk3298-prod.herokuapp.com/cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/234079081-bb5d7bde-db9c-4022-b226-b7ef982972e2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before updating cart qty<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/234079806-a817bcf3-c158-435b-a731-abfcb2a5fd2d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing after updating the quantity of item bagel<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/234080425-2692ac8e-3dc0-4752-baae-f2e0e4f4e106.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing of cart before setting the quantity to 0 for product kellogs<br>cornflakes<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/234080650-3b5980ef-4213-4bc0-ac9d-6f639e550db4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing of cart after setting the quantity to 0 for product kellogs<br>cornflakes<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/234081206-dc687b1e-aac4-4cdf-9366-e6afd2059755.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing how a negative quantity is handled when tried to set -1 to<br>the item bagel<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <div>- When we press the update button next to the amount field and<br>update button in the cart, a concealed product id is sent to the<br>cart function.</div><div>- In the code, if the quantity is greater than 0, we<br>first retrieve the name and price from the products table before updating the<br>quantity and price in the cart table while supplying the product id and<br>user id.</div><div>- As the number is less than 0, when we enter 0<br>in the quantity field, the code moves to the DELETE block, where we<br>delete the product from the cart database while passing the product id and<br>user id.</div><div>- We set the minimum value for the input field in HTML<br>to 0 to handle negative values in the amount field.</div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sanjanakancharla/IS601-006/pull/24">https://github.com/sanjanakancharla/IS601-006/pull/24</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/234081796-04f20884-a26a-4d22-a823-3908f0cc866a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the cart before deleting the item carpet<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/234082127-0bdc933c-800b-4187-8074-54ba388e47c0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the cart after deleting the item carpet<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/234082336-033247a8-7531-463a-b557-43a51dce1c4a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing before clearing a cart completely<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/38933770/234082469-578d8c0d-6ddf-4ad3-9fc8-14c9f276748c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing after the clearing the cart completely<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <div>When deleting a single item from a cart, a hidden field amount of<br>-1 will be supplied next to the delete button, and the cart function</div><div>will<br>process the delete query while sending the product id if the number is<br>less than zero.</div><div>When clearing the entire cart, we pass the variable delete all<br>with a value of 1, and if the delete all value is True<br>in the cart method, we delete the records in the Cart table while<br>passing the user id.</div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/sanjanakancharla/IS601-006/pull/24">https://github.com/sanjanakancharla/IS601-006/pull/24</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>One of the place where I got stuck was, while creating the tables,<br>the cart table is depend on product table and the query for creating</div><div>for<br>cart table is before the creation of product table so there my product<br>table was created but the items were not able to get into</div><div>cart and<br>later i noticed that there was no cart table created and then i<br>realize so i run inti_db.py again and the cart table was created.</div><div><br></div><div>And rest<br>was all normal and got a chance to learn to build the webpages<br>in a real-life project.</div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3298-prod.herokuapp.com/login">https://is601-sk3298-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/sk3298" target="_blank">Grading</a></td></tr></table>