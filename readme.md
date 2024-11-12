# 📂 Simple SQLite Database (Python Module)

**Author:** Ashish Ajin Thomas

---

## 🚀 Overview

**Simple SQLite Database** is a beginner-friendly Python module for SQLite, designed to make database interactions effortless. It provides a clean, modular interface for connecting, managing, and querying SQLite databases – no need to manually create connections or cursors! With this library, you can dive right into using SQL in Python. Perfect for handling multiple databases with ease. 

---

## 📥 Installation

Get started by installing the module with pip:

```bash
pip install simpleSQLiteDB==1.0.0
```

Then, add it to your Python project:

```python
from simpleDB import Database
```

---

## 🛠️ Usage

### 1️⃣ Creating & Connecting to a Database

To create or connect to an existing database, initialize the `Database` class with a filename:

```python
# Import the module
from simpleDB import Database

# Connect to (or create) a database file called 'Database.db'
db = Database('Database.db')
```

### 2️⃣ Executing SQL Commands

Use the `execute` method to run SQL commands. It returns a tuple containing the command’s result and status.

#### 🏗️ Creating a Table

Define your table structure with `CREATE TABLE`. Here’s an example:

```python
# Create a table called 'foo' with columns 'bar' (INTEGER) and 'baz' (TEXT)
result, status = db.execute("CREATE TABLE foo (bar INTEGER, baz TEXT);")
print(result, status)
```

⚠️ **Tip**: Run `CREATE TABLE` only once per table, as running it multiple times will raise an error.

#### 📥 Inserting Data

Add a row to your table with the `INSERT INTO` command:

```python
# Insert a row with values (1, "First Row") for 'bar' and 'baz'
result, status = db.execute("INSERT INTO foo (bar, baz) VALUES (?, ?);", (1, "First Row"))
print(result, status)
```

#### 🔍 Retrieving Data

Get all rows from a table with a `SELECT` statement:

```python
# Select all rows from 'foo'
rows, status = db.execute("SELECT * FROM foo;")
print(rows, status)  # 'rows' will contain a list of dictionaries (one for each row)
```

Here, each row is a dictionary, where column names are keys, and values are the data.

---

## 📜 Class & Method Reference

### 🔹 Database Class

- **Constructor**: `Database(filename)`
  - **filename**: Specifies the database file name to connect or create in the current directory.

### 🔹 `Database.execute` Method

- **Syntax**: `execute(command, [*args])`
  - **command**: The SQL command you want to run.
  - **args** (optional): Parameters for the command. If you have only one argument in a tuple, write it as `(variable,)`.

The `execute` method performs any SQL command on the connected database. For `SELECT` statements, it returns the results as a list of dictionaries.

#### 🔧 Special Commands

- **`.schema;`**: Returns a list of all tables and their SQL schema definitions in the database.

---

## 🔄 Running `simpleDB.py` Directly

You can also interact with the database directly by running `simpleDB.py` from the command line and executing SQLite commands without using Python.

---

## ❤️ Acknowledgements & Thank You

Thank you for choosing Simple SQLite Database! Happy coding! 🎉
