![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Benjamin144,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use.

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

--------

Happy coding!

##  Python And MySQL Introduction
Running MySQL commands from Python code. Connecting to MySQL database with hostname, user and password is not required on this Gitpod platform. 
This tutorial is geared to people with their own hosting platform..Cloud9 in particular. Uses the pymysql library and it's inbuilt methods.

## Connecting to MySQL from Python
Running MySQL commands from Python code, Connects to MySQL database with hostname, user and password. Use the pymysql library and it's inbuilt methods

## Cursor
A data structure that allows us to access the rows of data in a database. Allows us to run SQL queries and access the results. Create a cursor from a database connection then use it to execute SQL 

## Create A Table
The SQL 'CREATE TABLE' command, Creates a DB Table, Executes the command, giving it the names and types of columns that the table should contain.

## INSERT
The SQL 'INSERT' command Inserts Data Into A Table, Specify the table and columns to insert into, and the values for each column

## EXECUTE MANY
A method of the cursor object, which allows multiple SQL Statements to be executed. We do this by passing a SQL statement and a list of tuples containing data values, and the statement will be executed for each tuple.