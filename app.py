
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

db_name = 'bar_data.db'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/Type_information')
def type_1():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("select * from barlist")
    rows = cur.fetchall()
    conn.close()
    return render_template('Type_information.html', rows=rows)
@app.route('/Size_information')
def Size():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("select * from barsize")
    rows = cur.fetchall()
    conn.close()
    return render_template('Size_information.html', rows=rows)


if __name__ == '__main__':
    app.run()