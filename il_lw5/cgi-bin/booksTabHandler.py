from funcForDB import *
import cgi
print("Content-type: text/html\n")

form = cgi.FieldStorage()
title = form.getvalue("title")
genre = form.getvalue("genre")
rate = form.getvalue("rate")

addBook(title,  genre, rate)

print('<meta http-equiv="refresh" content="5;url=../tables/books.html">')
print("<p>Author added successfully! You will be redirected in 5 seconds.</p>")