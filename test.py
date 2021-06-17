import sqlite3
from random import randint
global db, sql
db = sqlite3.connect('orders.db')
sql = db.cursor()
sql.execute(("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash BIGINT) 
 """))
db.commit()


def reg():
    user_login = input('Login: ')
    user_password = input('Password: ')

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, 0))
        db.commit()

        print('Зарегестрированно!')
    else:
        print('Такая запись уже имеется!')

        for value in sql.execute("SELECT * FROM users"):
            print(value)


def casino():
    user_login = input('Log in: ')
    number = randint(1, 2)

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        print('Такого логина не существует')
        reg()
    else:
        if number == 1:
            sql.execute(f"UPDATE users SET cash = {1000} WHERE login = '{user_login}'")
            db.commit()
        else:
            print('Вы проиграли')


def enter():
    for i in sql.execute('SELECT login, cash FROM users'):
        print(i)


def main():
    casino()
    enter()


main()
