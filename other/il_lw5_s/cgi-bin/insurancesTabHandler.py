from funcForDB import *
import cgi
print("Content-type: text/html\n")

form = cgi.FieldStorage()
description = form.getvalue('description')
claim_date = form.getvalue('claimDate')
policy_id = form.getvalue('policyId')

add_insurance_claim(description, claim_date, policy_id)

print('<meta http-equiv="refresh" content="5;url=../cgi-bin/insurances.py">')
print("<p>Author added successfully! You will be redirected in 5 seconds.</p>")