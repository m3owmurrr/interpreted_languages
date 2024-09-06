import sqlite3
import xml.dom.minidom as minidom

def get_column_names(cur, table_name):
    cur.execute(f'PRAGMA table_info({table_name})')
    columns = cur.fetchall()
    return [column[1] for column in columns]

def get_xml(table_name):
    con = sqlite3.connect('insurance.db')
    cur = con.cursor()

    try:
        column_names = get_column_names(cur, table_name)

        root = minidom.Document()
        xml_root = root.createElement('root')
        root.appendChild(xml_root)

        cur.execute(f'SELECT * FROM {table_name}')
        data = cur.fetchall()

        for row in data:
            item_element = root.createElement('item')

            for i, column_name in enumerate(column_names):
                field_element = root.createElement(column_name)
                field_element.appendChild(root.createTextNode(str(row[i])))
                item_element.appendChild(field_element)

            xml_root.appendChild(item_element)

        with open('output.xml', 'w', encoding='utf-8') as xml_file:
            root.writexml(xml_file, indent='\t', addindent='\t', newl='\n', encoding='utf-8')

    finally:
        con.close()


def insert_xml_into_db(table_name, xml_name):
    con = sqlite3.connect('insurance.db')
    cur = con.cursor()

    try:
        column_names = get_column_names(cur, table_name)
        placeholders = ', '.join('?' for _ in column_names)

        tree = minidom.parse(xml_name)
        root = tree.documentElement

        for item in root.getElementsByTagName('item'):
            fields = []
            for column_name in column_names:
                field_value = item.getElementsByTagName(column_name)[0].firstChild.nodeValue
                fields.append(field_value)

            cur.execute(f'INSERT INTO {table_name} VALUES ({placeholders})', fields)

        con.commit()

    finally:
        con.close()

