from flask import Blueprint, render_template, request, flash,redirect,url_for
from sql.db import DB
employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN 
    #ht272
    query = "SELECT employees.id as id, first_name, last_name, email, companies.id as company_id, COALESCE(companies.name, 'N/A' ) as company_name FROM IS601_MP3_Employees employees LEFT JOIN IS601_MP3_Companies companies ON employees.company_id=companies.id"
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = [("first_name", "First Name"), ("last_name", "Last Name"), ("email", "Email"), ("company_name", "Company Name")] #ht272
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    first_name = request.args.get('fn', '' ) #ht272
    last_name = request.args.get('ln', '' )
    email = request.args.get('email', '' )
    company_id = request.args.get('company', '' )
    column = request.args.get('column', '' )
    order = request.args.get('order', '' )
    limit = request.args.get('limit', '' )
    if first_name != '' or last_name != '' or email != '' or company_id != '':
        query += " WHERE "
    # TODO search-3 append like filter for first_name if provided
    if first_name != '': #ht272
        first_name = f"%{first_name}%"
        query += " first_name LIKE %s"
        args.append(first_name)
    # TODO search-4 append like filter for last_name if provided
    if last_name != '': #ht272
        if list(query.split(" "))[-2] != 'WHERE':
            query += "AND"
        last_name = f"%{last_name}%"
        query += " last_name LIKE %s"
        args.append(last_name)
    # TODO search-5 append like filter for email if provided
    if email != '': #ht272
        if list(query.split(" "))[-2] != 'WHERE':
            query += "AND"
        email = f"%{email}%"
        query += " email LIKE %s"
        args.append(email)
    # TODO search-6 append equality filter for company_id if provided
    if company_id != '': #ht272
        if list(query.split(" "))[-2] != 'WHERE':
            query += "AND"
        query += " company_id LIKE %s"
        args.append(company_id)
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    if column != '': #ht272
        query += f" ORDER BY {column} {order}"
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    if limit != '': #ht272
        limit = limit
    else:
        limit = 10
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    try:
        limit = int(limit)
    except:
        flash('Limit should be an integer', "danger")
    if limit < 1 or limit > 100:
        flash('Limit should be greater than 1 and less than or equal to 100', "danger")

    if column == '':
        query += f" ORDER BY id asc"

    query += f" LIMIT %s"
    args.append(limit)
    
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-10 make message user friendly
        flash("Something went wrong while getting an employee records", "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_columns)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        first_name = request.form['first_name'] #ht272
        last_name = request.form['last_name']
        email = request.form['email']
        
        if 'company' in request.form:
            company = request.form['company']
        else:
            company = ""

        form_error = False
        # TODO add-2 first_name is required (flash proper error message)
        if first_name == "": #ht272
            flash('First name is required', "danger")
            form_error = True
        # TODO add-3 last_name is required (flash proper error message)
        if last_name == "": #ht272
            flash('Last name is required', "danger")
            form_error = True
        # TODO add-4 company (may be None)
        if company == "": #ht272
            company = None
        # TODO add-5 email is required (flash proper error message)
        if email == "": #ht272
            flash('Email is required', "danger")
            form_error = True
        
        if form_error == True:
            return redirect(request.url)
        
        try:
            result = DB.insertOne("""
            INSERT INTO IS601_MP3_Employees (first_name, last_name, email, company_id)
            VALUES (%s, %s, %s, %s)
            """, first_name, last_name, email, company
            ) # <-- TODO add-6 add query and add arguments
            if result.status:
                flash("Created Employee Record", "success")
        except Exception as e:
            # TODO add-7 make message user friendly #ht272
            flash("There was an error creating the employee record", "danger")
    return render_template("add_employee.html")

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    if request.args.get('id', '' ) == '':
        flash('id is required', "danger")

    row = {}

    id = request.args.get('id', '' ) #ht272
    if id != '': # TODO update this for TODO edit-1
        if request.method == "POST":
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            #ht272
            result = DB.selectOne("SELECT employees.id as id, first_name, last_name, email, companies.id as company_id, IF(name is not null, name,'N/A') as company_name FROM IS601_MP3_Employees employees LEFT JOIN IS601_MP3_Companies companies ON employees.company_id=companies.id WHERE employees.id=%s", id)
            if result.status:
                row = result.row

            if 'first_name' in request.form:
                first_name = request.form['first_name']
            else:
                first_name = row['first_name']

            if 'last_name' in request.form:
                last_name = request.form['last_name']
            else:
                last_name = row['last_name']

            if 'email' in request.form:
                email = request.form['email']
            else:
                email = row['email']

            if 'company' in request.form:
                company_id = request.form['company']
            else:
                company_id = row['company_id']
        
            form_error = False
            # TODO edit-2 first_name is required (flash proper error message)
            if first_name == "": #ht272
                flash('First name is required', "danger")
                form_error = True
            # TODO edit-3 last_name is required (flash proper error message)
            if last_name == "": #ht272
                flash('Last name is required', "danger")
                form_error = True
            # TODO edit-4 company may be None
            if company_id == "": #ht272
                company_id = None
            # TODO edit-5 email is required (flash proper error message)
            if email == "": #ht272
                flash('Email is required', "danger")
                form_error = True
            
            data = [first_name, last_name, company_id, email]
            data.append(id)
            try:
                # TODO edit-6 fill in proper update query
                #ht272
                result = DB.update("""
                UPDATE IS601_MP3_Employees SET first_name=%s, last_name=%s, company_id=%s, email=%s WHERE id=%s
                """, *data)
                if result.status:
                    flash("Updated record", "success")
                    return redirect(url_for('employee.search', first_name="", last_name="", email="", company="", order="asc", column="", limit=10))
            except Exception as e:
                # TODO edit-7 make this user-friendly
                flash("Something went wrong while updating the employee record", "danger")
        try: #ht272
            # TODO edit-8 fetch the updated data (including company_name)
            # company_name should be 'N/A' if the employee isn't assigned to a copany
            #ht272
            result = DB.selectOne("SELECT employees.id as id, first_name, last_name, email, companies.id as company_id, IF(name is not null, name,'N/A') as company_name FROM IS601_MP3_Employees employees LEFT JOIN IS601_MP3_Companies companies ON employees.company_id=companies.id WHERE employees.id=%s", id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash("Something went wrong while retrieving the employee record", "danger")
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html",  employee=row)

@employee.route("/delete", methods=["GET"])
def delete(): #ht272
    if request.args.get('id', '' ) == '':
        flash('id is required', "danger")

    id = request.args.get('id', '' )
    # TODO delete-1 delete employee by id
    try: #ht272
        result = DB.delete("DELETE FROM IS601_MP3_Employees WHERE id=%s", id)
        if result.status:
            flash("Employee record successfully deleted", "success")
    except Exception as e:
        flash("There was an error deleting employee record", "danger")
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    return redirect(url_for('employee.search', first_name="", last_name="", email="", company="", order="asc", column="", limit=10))