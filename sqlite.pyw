import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")


def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")
    
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():

    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)

    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
          (unix, date, keyword, value))

    conn.commit()
    time.sleep(1)

def read_from_db():
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

    c.execute('SELECT * FROM stuffToPlot WHERE value = 3')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

    c.execute('SELECT * FROM stuffToPlot WHERE unix > 1452554972')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

    c.execute('SELECT value, datestamp FROM stuffToPlot WHERE unix > 1452554972')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row[0])
    
read_from_db()
c.close
conn.close()
"""def del_and_update():
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    [print(row) for row in data]


    c.execute('UPDATE stuffToPlot SET value = 99 WHERE value = 3')
    conn.commit()

    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    [print(row) for row in data]

    c.execute('DELETE FROM stuffToPlot WHERE value = 99')
    conn.commit()

    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    [print(row) for row in data]

    (1452562314.0, '2016-01-11 17:31:54', 'Python', 1.0)
(1452562315.0, '2016-01-11 17:31:55', 'Python', 4.0)
(1452562316.0, '2016-01-11 17:31:56', 'Python', 8.0)
(1452562318.0, '2016-01-11 17:31:58', 'Python', 9.0)
(1452562322.0, '2016-01-11 17:32:02', 'Python', 4.0)
(1452562323.0, '2016-01-11 17:32:03', 'Python', 2.0)"""


#        try except else finally 
