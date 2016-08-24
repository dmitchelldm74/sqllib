# Usage

## Importing
```
from sqllib import SQL
```
## Initializing
```
sql = SQL(databasename)
```
## Create Tables
```
sql.create(tablename, (columnname, type))
```
## Remove Tables
```
sql.remove(table_name)
```
## Inserting Into Tables
```
sql.insert(table_name, \[value])
```
### Substitution
```
sql.insert(table_name, \['?'], value)
```
## Selecting From Tables
```
for sel in sql.select(\[column_name], table_name, where_query):
    print sel
```
### For no where query
```
for sel in sql.select(\[column_name], table_name, None):
    print sel
```
### Substitution for where query
```
for sel in sql.select(\[column_name], table_name, 'something=?', that_something):
    print sel
```
## Deleting From Tables
```
sql.delete(\[column_name], table_name, where_query)
```
### For no where query
```
sql.delete(\[column_name], table_name, None)
```
### Substitution for where query
```
sql.delete(\[column_name], table_name, 'something=?', that_something)
```
## Check if Table exists
```
sql.exists(table_name)
```
# Installation
## Windows (Command Prompt)
```
python setup.py install
### or 
"setup.py" install
```
## Linux and Mac (Bash)
```
sudo python setup.py install
```
