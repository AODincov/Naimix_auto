from src.initalization.Db import Db
import psycopg2.extras

Db1 = Db()
cur = Db1.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

list1 = Db1.select_data(cur, "nm", "Users", "login")
for row in list1:
   print("LOGIN =", row)

#cur.execute('SELECT "login", "passwordHash", "role", "locked", "deleted", "clientId", "active", "expiredDateTime" FROM nm."Users" WHERE NOT "login" IS NULL')
#rows = cur.fetchall()
#for row in rows:
#   print("LOGIN =", row[0])
#   print("LOGIN =", f"{row['login']}")

print("Operation done successfully")
Db1.connection.close()
# test