if __name__ == "__main__":
    remote_host = input("Enter the remote host: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    query = input("Enter your SQL query: ")
    
    run_query(remote_host, username, password, query)
