import sqlite3

con = sqlite3.connect('insurance.db')
cursor = con.cursor()

html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Police</title>
</head>
<body>
    <h1>Add Police</h1>

    <form action="/cgi-bin/policiesTabHandler.py" method="post">
        <label for="policyType">Policy type:</label>
        <input type="text" id="policyType" name="policyType" required><br>

        <label for="coverageAmount">Coverage amount:</label>
        <input type="number" id="coverageAmount" name="coverageAmount" step="1000" required><br>

        <label for="startDate">Start date:</label>
        <input type="date" id="startDate" name="startDate" required><br>

        <label for="clientId">Client ID:</label>
        <select id="clientId" name="clientId">
'''

cursor.execute('SELECT client_id, last_name, first_name FROM Clients')
clients = cursor.fetchall()

for client in clients:
    client_id, last_name, first_name = client
    html_content += f'''
        <option value="{client_id}">{last_name}, {first_name}</option>
    '''

html_content += f'''
       <br><input type="submit" value="Add Policy">
    </form>
    
    <h1>Clients Table</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Policy Type</th>
            <th>Coverage Amount</th>
            <th>Start Date</th>
            <th>Client ID</th>
        </tr>
'''

cursor.execute('SELECT * FROM Policies')
policies = cursor.fetchall()

for policy in policies:
    html_content += f'''
        <tr>
            <td>{policy[0]}</td>
            <td>{policy[1]}</td>
            <td>{policy[2]}</td>
            <td>{policy[3]}</td>
            <td>{policy[4]}</td>
        </tr>
    '''

# Завершаем формирование HTML-страницы
html_content += '''
    </table>
</body>
</html>
'''

# Закрываем соединение с базой данных
con.close()

# Выводим сформированную HTML-страницу
print('Content-type: text/html\n')
print(html_content)
