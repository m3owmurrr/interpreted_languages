from funcForDB import *
import cgi
print("Content-type: text/html\n")

form = cgi.FieldStorage()
policy_type = form.getvalue("policyType")
coverage_amount = form.getvalue("coverageAmount")
start_date = form.getvalue("startDate")
client_id = form.getvalue("clientId")

add_police(policy_type, coverage_amount, start_date, client_id)

print('<meta http-equiv="refresh" content="5;url=../cgi-bin/policies.py">')
print("<p>Author added successfully! You will be redirected in 5 seconds.</p>")