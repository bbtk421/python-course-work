import sqlite3


conn = sqlite3.connect(':memory:')
with conn:
      cur = conn.cursor()
      cur.execute("CREATE TABLE if not exists Roster( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            Name TEXT, \
            Species TEXT, \
            IQ INT \
            );")
      conn.commit()
      records = [('Jean-Baptiste Zorg', 'Human', '122'),
                 ('Korben Dallas', 'Meat Popsicle', '100'),
                 ('Ak\'not', 'Mangalore', '-5')]
      cur.executemany("INSERT INTO Roster (Name, Species, IQ) VALUES(?,?,?)", records);
      cur.execute("UPDATE Roster SET Species = Human WHERE Species = Meat Popsicle")
      cur.execute("SELECT Name, IQ FROM Roster WHERE Species = Human")
      print(fetchall())
conn.close()

