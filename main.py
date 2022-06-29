import sqlite3 as sq

text = input("Enter any text")
cur = sq.connect('db.db').cursor()
keys = cur.execute("SELECT * FROM keys").fetchall()

if text == "":
	print("\nPlease try again and enter any text")
	exit()
for k in keys:
	text.replace(k[0], k[1])
print(text)