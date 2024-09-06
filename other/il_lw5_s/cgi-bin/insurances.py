import sqlite3

con = sqlite3.connect('insurance.db')
cursor = con.cursor()

html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Insurance Claim</title>
</head>
<body>
    <h1>Add Insurance Claim</h1>

    <form action="/cgi-bin/insurancesTabHandler.py" method="post">
        <label for="description">Description:</label>
        <input type="text" id="description" name="description" required><br>

        <label for="claimDate">Claim Date:</label>
        <input type="date" id="claimDate" name="claimDate" required><br>

        <label for="policyId">Policy ID:</label>
        <select id="policyId" name="policyId">
'''

cursor.execute('SELECT policy_id, policy_type FROM Policies')
policies = cursor.fetchall()

for policy in policies:
    policy_id, policy_type = policy
    html_content += f'''
        <option value="{policy_id}">{policy_id}</option>
    '''

html_content += '''
        </select>
        <br><br>
        <input type="submit" value="Add Insurance Claim">
    </form>

    <h1>Insurance Claims Table</h1>
    <table border="1">
        <tr>
            <th>Claim ID</th>
            <th>Description</th>
            <th>Claim Date</th>
            <th>Policy ID</th>
        </tr>
'''

cursor.execute('SELECT * FROM InsuranceClaims')
claims = cursor.fetchall()

for claim in claims:
    html_content += f'''
        <tr>
            <td>{claim[0]}</td>
            <td>{claim[1]}</td>
            <td>{claim[2]}</td>
            <td>{claim[3]}</td>
        </tr>
    '''

html_content += '''
    </table>
</body>
</html>
'''

con.close()

print('Content-type: text/html\n')
print(html_content)