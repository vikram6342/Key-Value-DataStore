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
	# for key is exist
	if search(file_header,key) != -1:
		delete(file_header, key)   
	#for key is not exist
	file_header.seek(0,2)
	file_header.write(f"\"{key}\",\"{value}\"""\n")
	file_header.flush()

	pass


def delete(file_header : TextIO, key: str) -> None: #jayson
	"""
	Removes the row if key exist
	if not exist Should say key not exist
	"""
	if search(file_header, key) != -1:
		file_header.seek(search(file_header, key))
		a = file_header.tell()
		line=file_header.readline()
		n = file_header.tell()
		while line != "":
			file_header.seek(n)
			line = file_header.readline()
			n = file_header.tell()
			file_header.seek(a)
			file_header.write(line)
			a = file_header.tell()
			s = file_header.tell()
		file_header.seek(s)
		file_header.truncate()
		
	else:
		print("not exsist")

def find_value(file_header : TextIO, key: str) -> None: #Hari
	"""
	Prints the value 
	if value does not exists print key not found!
 	"""
	i = search(file_header,key)
	if(i==-1):
		print("Value Not Found")
	else:
		file_header.seek(i)
		l = file_header.readline()
		l = l.strip("\n")
		fkey,fvalue = parseKeyValue(l)
		print("Value is ",fvalue[1 : len(fvalue) - 1])
		
	pass
	



def keylimit() :
	key = input()
	if(len(key)<=32):
		return key
	else :
		print("Size of Key should be less than 32 char ")
		keylimit()

def valuelimit() :
	value = input()
	if(len(value)<=1048576):
		return value
	else:
		print("Size of Key should be less than 1 mb ")	
		valuelimit()

def func() :
	print("Welcome !!!")
	print("Please choose your menu")
	print("\t1. Insert/Update")
	print("\t2. Deletion")
	print("\t3. Find value")
	print("\t0. EXIT")

	file_header = open("DataStore.txt","r+")
	print("Enter the menu : ")
	menu = int(input())
	
	while(menu<=3 & menu!=0):
		if(menu == 1):
			key = keylimit()
			value = valuelimit()
			insert(file_header,key,value)
		elif(menu == 2):
			key = keylimit()
			delete(file_header,key)
			
		elif(menu == 3):
			key = keylimit()
			find_value(file_header,key)
			
		else :
			print("Enter correct menu ")
		print("Enter the menu : ")
		menu = int(input())
func()	

		

