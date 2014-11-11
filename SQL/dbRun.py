import sqlite3

conn = sqlite3.connect("polyglot.db")
conn.row_factory = sqlite3.Row # return dct not tuple
cursor = conn.cursor()

result = cursor.execute("SELECT id, language FROM languages WHERE answered = 1")#result не е дикшънъри в паметта а е няккакъв итеруем указател
#za da ne se prepulni pametta pri golama zaqvka

for row in result:
    print("{} - {}".format(row['id'], row['language']))
