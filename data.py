import psycopg2

conn = psycopg2.connect(database="testdb", user="kazami", password="dj4xji4", host="127.0.0.1", port="5432")

print("opened")
