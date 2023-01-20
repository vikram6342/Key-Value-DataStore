from typing import TextIO
import re



#file structure - "key","value"

def parseKeyValue(line : str) -> tuple :
	"""
	Returns the key value pair in the line
	
	inputs : line -> type : string
	line is a string with the general format "key","value"
	"""

	search = re.search(r"(\".*\"),(\".*\")", line)
	pair = (search.group(1), search.group(2))
	return pair



def search(file_header : TextIO,key : str) ->int : # vikram
	"""
	returns the positon to be seeked

	-1 if element not found 
	"""
	loc = -1
	file_header.seek(0)
	line = file_header.readline()
	while line:
		line = line.strip("\n")
		foundKey, foundValue = parseKeyValue(line= line)
		foundKey = foundKey[1 : len(foundKey) -1]
		if foundKey == key:
			loc = file_header.tell() - len(line) - 2
			break
		line = file_header.readline()

	return loc



def insert(file_header : TextIO, key: str, value: str) -> None: #dinesh

	"""
	Inserts the contents to the file in the format
	"key","value"
	key -> 32 characters (len)
	value -> 1mb (len(2^20))
	Insetion should update when key exist	

	"""
	pass


def delete(file_header : TextIO, key: str) -> None: #jayson
	"""
	Removes the row if key exist
	if not exist Should say key not exist
	"""
	if search(file_header, key) != -1:
		file_header.seek(search(file_header, key))
		line = f.readlines()
		del line[0]
		f.seek(search(file_header, key))
		for i in line:
			file_header.write(i)
		file_header.truncate()
	else:
		print("not exsist")

def find_value(file_header : TextIO, key: str) -> None: #Hari
	"""
	Prints the value 
	if value does not exists print key not found!
 	"""
	pass


#Hari -> file obj create 
#			Menu driven program 

#1 -> insert
#2 -> delete
#key ->32 value -> 1mb

#Insert/ Update
#Delete
#Find 

#f = open("filename.txt", "r+")
