import sqlite3

con = sqlite3.connect('db01.db')
cursor = con.cursor()


print("Content-type: text/html\n")

print('<!DOCTYPE html>')
print('<html lang="en">')
print('<head>')
print('    <meta charset="UTF-8">')
print('    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('    <title>Add Author</title>')
print('</head>')
print('<body>')
print('    <h1>Add Author</h1>')

print('    <form action="/cgi-bin/authorsTabHandler.py" method="post">')
print('        <label for="firstName">First Name:</label>')
print('        <input type="text" id="firstName" name="firstName" required><br>')

print('        <label for="lastName">Last Name:</label>')
print('        <input type="text" id="lastName" name="lastName" required><br>')

print('        <label for="birthDay">Birth Day:</label>')
print('        <input type="date" id="birthDay" name="birthDay" required><br>')

print('        <input type="submit" value="Add Author">')
print('    </form>')

cursor.execute('SELECT * FROM Authors')
authors = cursor.fetchall()

print('    <h1>Author Table</h1>')

print('    <table border="1">')
print('        <tr>')
print('            <th>ID</th>')
print('            <th>First Name</th>')
print('            <th>Last Name</th>')
print('            <th>Birth Day</th>')
print('        </tr>')

for author in authors:
    print('        <tr>')
    print(f'            <td>{author[0]}</td>')
    print(f'            <td>{author[1]}</td>')
    print(f'            <td>{author[2]}</td>')
    print(f'            <td>{author[3]}</td>')
    print('        </tr>')

print('    </table>')
print('</body>')
print('</html>')
