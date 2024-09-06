from funcForDB import *
import cgi
print("Content-type: text/html\n")

form = cgi.FieldStorage()
first_name = form.getvalue("firstName")
last_name = form.getvalue("lastName")
birth_day = form.getvalue("birthDay")

addAuthor(first_name,  last_name, birth_day)

print('<meta http-equiv="refresh" content="5;url=../cgi-bin/authors.py">')
print("<p>Author added successfully! You will be redirected in 5 seconds.</p>")