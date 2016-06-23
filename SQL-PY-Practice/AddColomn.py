#take adb.db3 as database and add a new column
import sqlite3
db = r"abs.db3"
con =sqlite3.connect(db)

c=con.cursor()

c.execute("ALTER TABLE A ADD occupation varchar(10)")
c.execute("UPDATE A set occupation='teacher' WHERE ANAME='Jack'")
c.execute("UPDATE A set occupation='janitor' WHERE ANAME='Katie'")
c.execute("UPDATE A set occupation='lawyer' WHERE ANAME='Eric'")

c.execute("SELECT ANAME FROM A")
con.commit()
print(c.fetchall())
