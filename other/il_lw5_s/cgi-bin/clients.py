import sqlite3

con = sqlite3.connect('insurance.db')
cursor = con.cursor()

html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Client</title>
</head>
<body>
    <h1>Add Client</h1>

    <form action="/cgi-bin/clientsTabHandler.py" method="post">
        <label for="firstName">First Name:</label>
        <input type="text" id="firstName" name="firstName" required><br>

        <label for="lastName">Last Name:</label>
        <input type="text" id="lastName" name="lastName" required><br>

        <label for="birthDay">Birth Day:</label>
        <input type="date" id="birthDay" name="birthDay" required><br>

        <label for="address">Address:</label>
        <input type="text" id="Address" name="address" required><br>
        
        <input type="submit" value="Add Client">
    </form>

    <h1>Clients Table</h1>

    <table border="1">
        <tr>
            <th>ID</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Birth Day</th>
            <th>Address</th>
        </tr>
'''

cursor.execute('SELECT * FROM Clients')
clients = cursor.fetchall()

for client in clients:
    print(client)
    html_content += f'''
        <tr>
            <td>{client[0]}</td>
            <td>{client[1]}</td>
            <td>{client[2]}</td>
            <td>{client[3]}</td>
            <td>{client[4]}</td>
        </tr>
    '''

html_content += '''
    </table>
</body>
</html>
'''

print('Content-type: text/html\n')
print(html_content)

con.close()
