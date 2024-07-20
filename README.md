# MySQL Query Tool

This script allows you to connect to a remote MySQL server and run an SQL query. The query results are then displayed.

## Requirements

### Install the mysql-connector-python package using pip:

```bash
pip install mysql-connector-python
``` 
## Usage

Run the script:

```bash
python remote_sql_tool.py
```
When prompted, enter the following information:

- **Remote host:** The address of the MySQL server you want to connect to.
- **Username:** Your MySQL username.
- **Password:** Your MySQL password.
- **SQL query:** The SQL query you want to execute.

The script will connect to the specified MySQL server, execute the query, and print the results.

### Example

```bash
python remote_sql_tool.py
```

```bash
Enter the remote host: 127.0.0.1
Enter username: your_username
Enter password: your_password
Enter your SQL query: SELECT * FROM table_1;
```

### Example output:

```bash
You are now connected to MySQL server at 127.0.0.1
(1, 'Mark Johnson', 'mjohnson@xyz.com')
(2, 'Anne James', 'ajames@xyz.com')
You have been disconnected from MySQL server
```

## Error Handling

If there is an error connecting to the MySQL server or executing the query, an error message will be displayed. 

### Example:

```bash
Error: 1045 (28000): Access denied for user 'xyz'@'localhost' (using password: XYZ)
```

## Notes

Ensure that the MySQL server is running and accessible from your machine.
Make sure you have the necessary permissions to access the database and execute the query.
