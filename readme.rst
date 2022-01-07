Simple SQLite Database (Module)
===============================

Author: Ashish Ajin Thomas
^^^^^^^^^^^^^^^^^^^^^^^^^^

What is this?
-------------

   It is a python module to simplify the usage of SQLite3 and more
   begginer friendly for those starting off with SQL in python It does
   the task of creating connections, cursors etc, to enable clean code
   It makes the whole process more modular to allow for ease of use for
   more than 1 database

Getting Started
---------------

   run ``pip install simpleSQLiteDB==1.0.0`` then add
   ``from simpleDB import Database`` to your python file Now you can
   instantiate from the Database class and create databases

Documentation
-------------

First Steps
~~~~~~~~~~~

Add this to file

::

   # import module
   from simpleDB import Database

   # connect/create the database called 'Database.db' at './'
   db = Database('Database.db')

   # Execute a command to Create a new Table called foo with 2 columns: bar and baz of type INTEGER and TEXT respectively
   a = db.execute("CREATE TABLE foo (bar INT, baz TEXT);")
   print(a)
   # a will be a tuple containing return value and status of the command

   # Execute a command to INSERT a Row into the table with values 1 and "First Row" as the values for bar and baz columns respectively
   b = db.execute("INSERT INTO foo (bar, baz) VALUES (?, ?);", (1, "First Row"))
   print(b)
   # b will be a tuple containing return value and status of the command

Run the CREATE TABLE command only once as running it multiple times will
bring about an error

now you can remove the a and b parts of the file as the commands have
already been executed

Your File should not look like this

::

   # import module
   from simpleDB import Database

   # connect/create the database called 'Database.db' at './'
   db = Database('Database.db')

To SELECT All the Values from the Table we can run

::

   rows, status = db.execute("SELECT * FROM foo;")
   print(rows, status)
   # rows will have all the rows

Using these you can run any SQLite3 Command with a single statement

Database
~~~~~~~~

The Database class can be instantiated using Database(filename) The
filename argument refers to the database file in the same directory

.. _databaseexecute:

Database.execute
~~~~~~~~~~~~~~~~

The Database.execute(command, [*args]) function takes in a command and
an optional \*args argument the \*args has to be a tuple if there is
only 1 argument inside the tuple make sure the tuple is like this

::

   (variable,)

and not like (variable)

The execute method will execute the command to the Database that the
file was connected to at the instantiation

SELECT statements
^^^^^^^^^^^^^^^^^

The SELECT statements will return the Values as a list of dictionaries
in which each dictionary has the column name as the key and the value as
the value for that row and column Note: the command will return a None
if no rows are found

.schema;
^^^^^^^^

.. code:: Database.execute(".schema;")~~~

   will return a list of all the Tables in the Database along with their SQL


   ## Running the simpleDB.py File

   Can directly Manipulate the Database by running SQLite commands without using python

   ## Thank You
