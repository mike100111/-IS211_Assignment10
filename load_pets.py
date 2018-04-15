import sqlite3 as datacontext

db = datacontext.connect('pet.db')
cur = db.cursor()

def createDb():
	cur.execute('CREATE TABLE person (id INTEGER PRIMARY KEY,first_name TEXT,last_name TEXT,age INTEGER)')
	cur.execute('CREATE TABLE pet (id INTEGER PRIMARY KEY,name TEXT,breed TEXT,age INTEGER,dead INTEGER)')
	cur.execute('CREATE TABLE person_pet (person_id INTEGER,pet_id INTEGER)')
	
def loadDb():
	
	persons = ((1, 'James', 'Smith', 41),
			(2, 'Diana', 'Greene', 23),
			(3, 'Sara', 'White', 27),
			(4, 'William', 'Gibson', 23))

	pets = ((1, 'Rusty', 'Dalmation', 4, 1),
			(2, 'Bella', 'Alaskan Malamute', 3, 0),
			(3, 'Max', 'Cocker Spaniel', 1, 0),
			(4, 'Rocky', 'Beagle', 7, 0),
			(5, 'Rufus', 'Cocker Spaniel', 1, 0),
			(6, 'Spot', 'Bloodhound', 2, 1))

	#mapping table to connect people to pets, potentially with many to many relationships
	person_pets = ((1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (4, 6))

	db.executemany('INSERT INTO person VALUES (?,?,?,?)',persons)	
	db.executemany('INSERT INTO pet VALUES (?,?,?,?,?)',pets)	
	db.executemany('INSERT INTO person_pet VALUES (?,?)',person_pets)
	db.commit()
	
loadDb()

	
	