from funcForDB import *
import cgi
print("Content-type: text/html\n")

form = cgi.FieldStorage()
book = form.getvalue("books")
author = form.getvalue("authors")
date = form.getvalue("releaseDate")

addAuthorsBook(book, author , date)

print('<meta http-equiv="refresh" content="5;url=../cgi-bin/booksAuthors.py">')
print("<p>Author added successfully! You will be redirected in 5 seconds.</p>")