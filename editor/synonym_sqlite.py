import sqlite3
import csv
from pkg_resources import resource_filename
DEFAULT_SYNONYM_FILE = resource_filename('editor', 'synonym-database.csv')

def csv_reader():
	synonym_file = open(DEFAULT_SYNONYM_FILE)
	synonym_rows = csv.reader(synonym_file)

	dictionary = {}

	#keys_id_list = []
	#id_synonym_list = []

	for row in synonym_rows:
		if row[4] == "SYN:":
			if len(row[5]) > len(row[2]):
				if row[2] not in dictionary:
					dictionary[row[2]] = [row[5]]

					#for the database
					#keys_id_list.append((row[2], row[0]))
					#id_synonym_list.append((row[0], row[5]))


				else:
					dictionary[row[2]].append(row[5])

					#for the database
					#keys_id_list.append((row[2], row[0]))
					#id_synonym_list.append((row[0], row[5]))

	
	return dictionary



ord_dictionary = {}

#important for Iris
def ordered_dictionary():
	'''
	result = urlparse("postgres://postgres:bd3690a50f66e7de60742dee84fd1e6a@172.23.197.180:59172/team_project_db")
	username = result.username
	password = result.password
	database = result.path[1:]
	hostname = result.hostname
	port = result.port
	#create a connection to the synonym database
	con = psycopg2.connect(
			host = hostname,
			database = database,
			user = username,
			password = password,
			port = port
	)
	cur = con.cursor()
	'''

	ord_dictionary = {}


	#call the csv_reader function
	dicti = csv_reader()
	#for-loop through all the items key and values
	for key, val in dicti.items():
		#sort the values of the dictionary
		cleaned_val = [] 
		cleaned_key = ""
		#check every character in the key
		for char in key:
			#the character have to be alpha
			if char.isalpha():
				#if so, add it to the cleaned key
				cleaned_key += char
		#iterate through the values
		for v in val:
			#create empty string
			cleaned_str = ""
			#check all the characters
			for char in v:
				#the character need to be either alpha or whitespace
				if char.isalpha() or char.isspace():
					#if so, add it to the the empty string
					cleaned_str += char
			#add the cleaned string to the cleaned value
			cleaned_val.append(cleaned_str)
		#sort the cleaned values
		sorted_list = sorted(cleaned_val, key=len, reverse=True)
		#save all the keys with the matching sorted values in the empty ordered dictionary
		ord_dictionary[cleaned_key] = sorted_list


		#all above is for the database
	#------------------------------


		'''
	#create the table for the synonym_list
	cur.execute('''
		#CREATE TABLE IF NOT EXISTS key_list(
		#	keys TEXT PRIMARY KEY,
		#	id TEXT
#)
	''')

	con.commit()

	keys_id_data = csv_reader()[1]
	new_list_avoid = []
	check_dublicates = []
	for x in keys_id_data:
		number_str = ""
		for a in x[1]:
			if a.isspace() == False:
				number_str += a
		if x[0] not in check_dublicates:
			new_list_avoid.append((x[0],int(number_str)))
			check_dublicates.append(x[0])
		else:
			continue

	
	# insert the rows created synonym_list table
	insert_script = 'INSERT INTO key_list(keys,id) VALUES (%s,%s)'
	insert_value = new_list_avoid
	cur.executemany(insert_script, insert_value)

	con.commit()


	cur.execute('''
		#CREATE TABLE IF NOT EXISTS synonym_list(
		#	id INT,
		#	synonym TEXT
		#)
	#''')


	'''
	id_synonym_list = csv_reader()[2]
	new_list_avoid = []
	for x in id_synonym_list:
		number_str = ""
		for a in x[0]:
			if a.isspace() == False:
				number_str += a
			new_list_avoid.append({int(number_str), x[1]})




	insert_script = 'INSERT INTO synonym_list(id,synonym) VALUES {%s, %s}'
	insert_value = new_list_avoid
	cur.executemany(insert_script, insert_value)

	con.commit()

	cur.close()
	'''
	#return the ordered dictionary
	return ord_dictionary

