
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

db_name = 'bar_data.db'

# 定义处理HTTP 404错误的函数
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# 定义处理数据库错误的函数
@app.errorhandler(sqlite3.Error)
def handle_database_error(error):
    return render_template('error.html', message='Database error: {}'.format(str(error))), 500

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