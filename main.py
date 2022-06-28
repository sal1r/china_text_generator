import sqlite3 as sq

text = input()
cur = sq.connect('db.db').cursor()
keys = cur.execute("SELECT * FROM keys").fetchall()

if text == "":
	print("Please try again and input any chars")
	exit()
for k in keys:
	text.replace(k[0], k[1])
print(text)