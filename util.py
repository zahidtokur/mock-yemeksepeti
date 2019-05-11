import sqlite3
import re

def create_tables():
    con = sqlite3.connect("database.db")
    cursor = con.cursor()

    queries = [
        """CREATE TABLE IF NOT EXISTS Customer(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email CHAR(320) NOT NULL UNIQUE, 
            password CHAR(14) NOT NULL, 
            name VARCHAR(100) NOT NULL, 
            surname VARCHAR(100) NOT NULL,
            city CHAR(14) NOT NULL)""",
        """CREATE TABLE IF NOT EXISTS CustomerAddress(
            customer_id INTEGER NOT NULL,
            phone_number CHAR(13) NOT NULL,
            city CHAR(14) NOT NULL,
            district VARCHAR(255) NOT NULL,
            address TEXT NOT NULL,
            address_description TEXT NOT NULL,
            FOREIGN KEY(customer_id) REFERENCES Customer(id))""",
    ]

    for query in queries:
        cursor.execute(query)
    
    con.commit()
    con.close()

def validate_register_form(register_form):
    #VALIDATING E-MAIL
    if not email_is_valid(register_form['email']):
        return {'validated':False, 'message':'Hatalı E-Posta Girdiniz.'}
    #VALIDATING NAME
    if not register_form['name'].replace(" ","").isalpha():
        return {'validated':False, 'message':'Adı Kontrol Ediniz.'}
    #VALIDATING SURNAME
    if not register_form['surname'].replace(" ", "").isalpha():
        return {'validated':False, 'message':'Soyadı Kontrol Ediniz.'}
    #VALIDATING PASSWORD
    if len(register_form['password']) < 8:
        return {'validated':False, 'message':'Şifre 8-14 Karakter Olmalıdır.'}
    #VALIDATING PASSWORD CONFIRMATION
    if register_form['password'] != register_form['password_confirmation']:
        return {'validated':False, 'message':'Şifreler Uyuşmuyor.'}

    return {'validated':True, 'message':'Başarıyla Kayıt Oldunuz!'}

def validate_login():
    pass


def email_is_valid(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email) or ' ' in email:
        return False
    return True

def save_customer(register_form):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    form_tuple = (register_form['email'], register_form['password'], register_form['name'], register_form['surname'], register_form['city'])
    cursor.execute('INSERT INTO Customer (email,password,name,surname,city) values (?,?,?,?,?)', form_tuple)
    con.commit()
    con.close()

def authenticate_user(login_form):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute('SELECT id FROM Customer WHERE email=? AND password=?', (login_form['email'], login_form['password']))
    user = cursor.fetchone()
    if len(user) == 0:
        return -1
    
    return user[0]