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
        """CREATE TABLE IF NOT EXISTS Restaurant(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(200) NOT NULL UNIQUE,
            city CHAR(14) NOT NULL,
            town VARCHAR(50) NOT NULL,
            district CHAR(20) NOT NULL,
            address VARCHAR(400) NOT NULL,
            phone_number CHAR(11) NOT NULL UNIQUE,
            owner_ssn INTEGER NOT NULL,
            owner_name VARCHAR(100) NOT NULL,
            owner_surname VARCHAR(100) NOT NULL,
            owner_phone_number CHAR(11) NOT NULL,
            email CHAR(320) NOT NULL UNIQUE,
            password CHAR(14) NOT NULL)""",
    ]

    for query in queries:
        cursor.execute(query)
    
    con.commit()
    con.close()

def validate_user_register(register_form):
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


def validate_owner_register(register_form):
    #VALIDATING RESTAURANT NAME
    if len(register_form["name"]) == 0:
        return {'validated':False, 'message':'Restoran Adını Kontrol Ediniz.'}
    #VALIDATING SSN
    if len(register_form["owner_ssn"]) != 11:
        return {'validated':False, 'message':"TCKN'yi Kontrol Ediniz."}
    if len(register_form["address"]) == 0:
        return {'validated':False, 'message':"Adresi Kontrol Ediniz."}
    #VALIDATING OWNER NAME
    if not register_form["owner_name"].replace(" ", "").isalpha():
        return {'validated': False, 'message': 'Adı Kontrol Ediniz.'}
    #VALIDATING OWNER SURNAME
    if not register_form['owner_surname'].replace(" ", "").isalpha():
        return {'validated': False, 'message': 'Soyadı Kontrol Ediniz.'}
    #VALIDATING OWNER PHONE NO
    if len(register_form["owner_phone_number"]) != 11 or not register_form["owner_phone_number"].startswith("0"):
        return {'validated': False, 'message': 'Telefon Numarası 0xxxxxxxxxxxx Olmalıdır.'}
    #VALIDATING RESTAURANT PHONE NO
    if len(register_form["phone_number"]) != 11 or not register_form["phone_number"].startswith("0") :
        return {'validated': False, 'message': 'Restoran Telefonu 0xxxxxxxxxx Olmalıdır.'}
    #VALIDATING E-MAIL
    if not email_is_valid(register_form["email"]):
        return {'validated': False, 'message': 'Hatalı E-Posta Girdiniz.'}
    #VALIDATING PASSWORD
    if len(register_form['password']) < 8:
        return {'validated': False, 'message': 'Şifre 8-14 Karakter Olmalıdır.'}
    #VALIDATING PASSWORD CONFIRMATION
    if register_form['password'] != register_form['password_confirmation']:
        return {'validated': False, 'message': 'Şifreler Uyuşmuyor.'}
    
    return {'validated': True, 'message': 'Başarıyla Kayıt Oldunuz!'}


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

def save_restaurant(register_form):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    form_tuple = (register_form['name'], register_form['city'], register_form['town'],
                  register_form['district'], register_form['address'], register_form['phone_number'],
                  register_form['owner_ssn'], register_form['owner_name'], register_form['owner_surname'],
                  register_form['owner_phone_number'], register_form['email'], register_form['password'])

    cursor.execute('''INSERT INTO Restaurant (name, city, town, district, address, phone_number, owner_ssn, owner_name, 
                      owner_surname, owner_phone_number, email, password) values (?,?,?,?,?,?,?,?,?,?,?,?)''', form_tuple)
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
