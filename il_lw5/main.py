# Создать БД в соответствии с предметной областью
# БД должна содержать не менее трех связанных таблиц
# Заполнить таблицы БД информацией с помощью SQL-запросов
# Написать не менее трех статических запросов (SELECT)
# Создать CGI-сервер
# Создать форму(формы) для заполнения полей таблицы
# Осуществить вывод содержимого таблиц
# Экспорт\импорт таблицы в xml, использую заданную библиотеку
#
# Предметная область: литература
# библиотека lxml
# экспсорт любой таблицы в xml
# есть xml файл из него дополнить таблицу
from http.server import HTTPServer, CGIHTTPRequestHandler

from workingWithXML import *

serverAddress = ('localhost', 8000)
httpServer = HTTPServer(serverAddress, CGIHTTPRequestHandler)
print("Server started on http://localhost:8000/")
httpServer.serve_forever()

# getXML('Authors')
# insertXMLintoDB('Authors', 'input.xml')

# # Запрос 1: Получение списка всех книг с их названиями и жанрами
# request1 = con.execute('SELECT book_name, book_genre FROM Books').fetchall()
#
# # Запрос 2: Получение списка всех авторов и их дат рождения
# request2 = con.execute('SELECT author_firstName, author_lastName, author_birthDay FROM Authors').fetchall()
#
# # Запрос 3: Получение списка книг и соответствующих авторов с датами релиза
# result3 = con.execute('SELECT b.book_name, a.author_firstName, a.author_lastName, ba.release_date FROM BooksAuthors ba JOIN Books b ON ba.book_id = b.book_id JOIN Authors a ON ba.author_id = a.author_id').fetchall()
