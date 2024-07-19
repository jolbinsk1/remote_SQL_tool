# first, if mysql.connector isn't installed, use pip install

pip install mysql-connector-python

# next, run the script

import mysql

import mysql.connector

def run_query(remote_host, username, password, query):
    try:
        connection = mysql.connector.connect(host=remote_host, user=username, password=password)
        
        if connection.is_connected():
            print(f'You are now connected to MySQL server at {remote_host}')
            
            nav = connection.cursor()
            nav.execute(query)
            results = nav.fetchall()

            for row in results:
                print(row)
            
            nav.close()
            connection.close()
            
            print("You have been disconnected from MySQL server")

    except mysql.connector.Error as error:
        print(f'Error: {error}')
