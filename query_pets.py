import sqlite3 as datacontext

# open database connnection
db = datacontext.connect('pet.db')
cur = db.cursor()

def get_pets():
		
	id = 0
		
	while id >= 0:

		id = input('Enter a Person Id to find a pet. Enter -1 to exit -->')
	
		# Get person
		cur.execute('SELECT * FROM person WHERE id= ? limit 1', [id,])
		person = cur.fetchone()	
		# If no one was found
		if person == None:
			print 'No one was found with that id.'
			continue
		# print person info
		print 'You selected ' + person[1] + ' ' + person[2] + ' who is ' + str(person[3]) + ' years old.'
		
		# Get Pets
		cur.execute('SELECT * FROM pet INNER JOIN person_pet ON pet.id = person_pet.pet_id WHERE person_pet.person_id = ?', [id,])
		pets = cur.fetchall()
		# Print pet info
		for pet in pets:		
			print 'They has a ' + pet[2] + ' named ' + pet[1] + ' who is ' + str(pet[3]) + ' years old and ' + ('has passed.' if pet[4] == 1 else 'is alive')
		
get_pets()