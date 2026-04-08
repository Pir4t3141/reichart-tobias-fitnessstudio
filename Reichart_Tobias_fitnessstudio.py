import sqlite3

conn = sqlite3.connect('Reichart_Tobias_fitnessstudio.db')
cursor = conn.cursor()

cursor.executescript('''
CREATE TABLE IF NOT EXISTS trainer (
    trainer_id INTEGER PRIMARY KEY,
    vorname TEXT,
    nachname TEXT,
    spezialgebiet TEXT
);

CREATE TABLE IF NOT EXISTS kurs (
    kurs_id INTEGER PRIMARY KEY,
    trainer_id INTEGER,
    bezeichnung TEXT,
    wochentag TEXT,
    uhrzeit TIME,
    maxteilnehmer INTEGER
);

CREATE TABLE IF NOT EXISTS mitglied (
    mitglied_id INTEGER PRIMARY KEY,
    vorname TEXT,
    nachname TEXT,
    email TEXT,
    beitrittsdatum DATE
);

CREATE TABLE IF NOT EXISTS anmelden (
    anmelden_id INTEGER PRIMARY KEY,
    kurs_id INTEGER,
    mitglied_id INTEGER,
    anmeldedatum DATE
);
''')

trainer_data = [
    (1, 'Max', 'Mustermann', 'Yoga & Pilates'),
    (2, 'Sarah', 'Schmidt', 'Krafttraining'),
    (3, 'Christian', 'Weber', 'Ausdauer & HIIT')
]

kurs_data = [
    (1, 1, 'Morgen Yoga', 'Montag', '08:00', 15),
    (2, 2, 'Power Lifting', 'Dienstag', '18:30', 10),
    (3, 3, 'Intervall-Lauf', 'Mittwoch', '17:15', 20),
    (4, 1, 'Abend Entspannung', 'Donnerstag', '20:00', 15),
    (5, 2, 'Ganzkörper-Workout', 'Freitag', '16:45', 12)
]
mitglied_data = [
    (1, 'Julia', 'Wagner', 'julia.w@email.de', '2023-01-15'),
    (2, 'Lukas', 'Müller', 'l.mueller@web.de', '2023-03-22'),
    (3, 'Anna', 'Becker', 'becker.anna@gmx.net', '2024-02-10'),
    (4, 'Tom', 'Hoffmann', 'tom_h@outlook.com', '2024-05-05'),
    (5, 'Elena', 'Richter', 'elena.r@provider.de', '2025-11-12'),
    (6, 'Felix', 'Schulz', 'felix.s@online.de', '2026-01-20')
]

anmelden_data = [
    (1, 1, 1, '2026-04-01'),
    (2, 1, 3, '2026-04-02'),
    (3, 2, 2, '2026-04-03'),
    (4, 2, 4, '2026-04-03'),
    (5, 3, 5, '2026-04-05'),
    (6, 4, 1, '2026-04-06'),
    (7, 5, 6, '2026-04-07'),
    (8, 5, 2, '2026-04-07')
]

cursor.executemany('INSERT OR IGNORE INTO trainer VALUES (?,?,?,?)', trainer_data)
cursor.executemany('INSERT OR IGNORE INTO kurs VALUES (?,?,?,?,?,?)', kurs_data)
cursor.executemany('INSERT OR IGNORE INTO mitglied VALUES (?,?,?,?,?)', mitglied_data)
cursor.executemany('INSERT OR IGNORE INTO anmelden VALUES (?,?,?,?)', anmelden_data)

conn.commit()
conn.close()