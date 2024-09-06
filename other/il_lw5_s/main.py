from http.server import HTTPServer, CGIHTTPRequestHandler
import funcForDB
from workingWithXML import *

funcForDB.create_tables()

# con = sqlite3.connect('insurance.db')
# # Запрос 1: Получение списка всех клиентов который родились после 2000ого года
# request1 = con.execute('SELECT first_name, last_name, birth_day FROM Clients WHERE birth_day > "2000-01-01"').fetchall()
# print(request1)
# # Запрос 2: Получение списка полисов и их владельцев
# request2 = con.execute('SELECT p.policy_id, p.policy_type, p.coverage_amount, p.start_date, c.first_name, c.last_name FROM Policies AS p INNER JOIN Clients AS c ON p.client_id = c.client_id').fetchall()
# print(request2)
# # Запрос 3: Получение списка всех страховых случаев
# request3 = con.execute('SELECT COUNT(*) FROM InsuranceClaims').fetchall()
# print(request3)



# get_xml('Policies')
# insert_xml_into_db('Policies', 'input.xml')




serverAddress = ('localhost', 8000)
httpServer = HTTPServer(serverAddress, CGIHTTPRequestHandler)
print("Server started on http://localhost:8000/")
httpServer.serve_forever()
