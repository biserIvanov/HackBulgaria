from flask import Flask
from flask import request, render_template
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

app = Flask(__name__)

def dbSearch(key_word):
    try:
        engine = create_engine("sqlite:///info.db")
        connection = engine.connect()
        key_word = "%" + key_word + "%"
        result = connection.execute("SELECT URL FROM Website WHERE HTML_version LIKE ?", (key_word,))
        result_list = []
        for url in result:
            result_list.append(url)
            print(url)
        connection.close()
        return result_list
    except Exception as e:
        return e


@app.route('/')
def hello_world():
    return render_template("index.html", links=[])


@app.route('/search')
def get():
    key_word = request.args.get('key_word', '')
    result_list = []
    result_list = dbSearch(key_word)

    resultData = ''

    for row in result_list:
        resultData += '<li><a href="' + row[0] + '">' + row[0] + '</a></li>'

    return resultData

    result = []
    for tup in result_list:
        result.append(tup[0])
    #ads, SSL, points, multy_language, pages_count, HTML_version
    return render_template('index.html', links=result)
    #return str(result)




if __name__ == '__main__':
    app.run(debug=True)
