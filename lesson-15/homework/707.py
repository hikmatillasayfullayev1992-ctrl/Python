import sqlite3

conn = sqlite3.connect("StarfleetDB.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

cursor.executemany("""
INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
""", [
    ("Abror Saidov", "Human", 45),
    ("Bobir Jurayev", "Trill", 35),
    ("Malika Nosirova", "Bajoran", 30)
])

cursor.execute("""
UPDATE Roster
SET Name = 'Eshqobil Boltayev'
WHERE Name = 'Bobir Jurayev'
""")

cursor.execute("""
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran'
""")

results = cursor.fetchall()

for row in results:
    print(row)

conn.commit()
conn.close()
