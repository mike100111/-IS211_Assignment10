import sqlite3 as datacontext

db = datacontext.connect('pet.db')
cur = db.cursor()

def get_pets():
	
	id = raw_input('Enter a Person Id to find a pet. Enter -1 to exit -->')
	
	while id >= 0:
		print id
		cur.execute('SELECT * FROM pet INNER JOIN person_pet ON pet.id = person_pet.pet_id WHERE person_pet.person_id = ?', id)
		pets = cur.fetchall()
		for pet in pets:		
			print pet
		id = raw_input('Enter a Person Id to find a pet. Enter -1 to exit -->')
		
get_pets()