import psycopg2

conn = psycopg2.connect(database="kazami", user="kazami", password="dj4xji4", host="127.0.0.1", port="5432")

cur = conn.cursor()
cur.execute("SELECT * from users")

rows = cur.fetchall()
print("\nShow me the databases:\n")
for row in rows:
	print(" ", row[0], " ", row[1])
print("opened")
