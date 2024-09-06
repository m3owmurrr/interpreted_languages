import sqlite3

con = sqlite3.connect('db01.db')
cursor = con.cursor()

print("Content-type: text/html\n")
print('<!DOCTYPE html>')
print('<html lang="en">')
print('<head>')
print('    <meta charset="UTF-8">')
print('    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('    <title>Link Authors and Books</title>')
print('</head>')
print('<body>')
print('    <h1>Add Books to Authors</h1>')
print('')
print('    <form action="/cgi-bin/booksAuthorsTabHandler.py" method="GET">')
print('        <label for="books">Выберите книгу:</label>')
print('        <select id="books" name="books">')



cursor.execute('SELECT book_id, book_name FROM Books')
books = cursor.fetchall()

for book in books:
    book_id, title = book
    print(f'            <option value="{book_id}">{title}</option>')


print('        </select> <p>')
print('')




print('        <label for="authors">Выберите автора:</label>')
print('        <select id="authors" name="authors">')



cursor.execute('SELECT author_id, author_firstName, author_lastName FROM Authors')
authors = cursor.fetchall()

for author in authors:
    author_id, first_name, last_name = author
    print(f'            <option value="{author_id}">{first_name + last_name}</option>')


print('        </select> <p>')
print('')
print('        <label for="releaseDate">Release Date:</label>')
print('        <input type="date" id="releaseDate" name="releaseDate" required><br>')
print('')
print('        <input type="submit" value="Link Authors and Books">')
print('    </form>')
print('</body>')
print('</html>')


