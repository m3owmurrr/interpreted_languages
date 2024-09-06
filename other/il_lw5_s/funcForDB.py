import sqlite3 as sql3

def create_tables():
    con = sql3.connect('insurance.db')
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Clients (
            client_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            birth_day DATE,
            address VARCHAR(255)
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Policies (
            policy_id INTEGER PRIMARY KEY AUTOINCREMENT,
            policy_type VARCHAR(255),
            coverage_amount DECIMAL(10, 2),
            start_date DATE,
            client_id INTEGER,
            FOREIGN KEY (client_id) REFERENCES Clients(client_id)
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS InsuranceClaims (
            claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            claim_date DATE,
            policy_id INTEGER,
            FOREIGN KEY (policy_id) REFERENCES Policies(policy_id)
        )
    ''')

    con.commit()
    con.close()

def add_client(firstName, lastName, birth_day, address):
    con = sql3.connect('insurance.db')
    cur = con.cursor()
    cur.execute('INSERT INTO Clients VALUES (NULL, ?, ?, ?, ?)', (firstName, lastName, birth_day, address))
    con.commit()
    con.close()

def add_police(policy_type, coverage_amount, start_date, client_id):
    con = sql3.connect('insurance.db')
    cur = con.cursor()
    cur.execute('INSERT INTO Policies VALUES (NULL, ?, ?, ?, ?)', (policy_type, coverage_amount, start_date, client_id))
    con.commit()
    con.close()

def add_insurance_claim(description, claim_date, policy_id):
    con = sql3.connect('insurance.db')
    cur = con.cursor()
    cur.execute('INSERT INTO InsuranceClaims VALUES (NULL, ?, ?, ?)', (description, claim_date, policy_id))
    con.commit()
    con.close()