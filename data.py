import psycopg2
import json

conn = psycopg2.connect(database="kazami", user="kazami", password="dj4xji4", host="127.0.0.1", port="5432")

cur = conn.cursor()
cur.execute("INSERT INTO users(name, love) VALUES (%s, %s)", ("kazami", json.JSONEncoder().encode({"FOOD":{"LUNCH":["X", "Y"], "C":"Y"}})))

cur.execute("SELECT * from users")

rows = cur.fetchall()
print("\nShow me the databases:\n")
for row in rows:
	print(" ", row[0], " ", row[1])
print("opened")
conn.commit()
cur.close()
