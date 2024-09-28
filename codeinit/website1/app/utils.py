# Python program to implement Playfair Cipher

# Function to convert the string to lowercase


def toLowerCase(text):
	return text.lower()

# Function to remove all spaces in a string


def removeSpaces(text):
	newText = ""
	for i in text:
		if i == " ":
			continue
		else:
			newText += i
	return newText

# Function to group 2 elements of a string
# as a list element

# This function doesn't take care of odd lenght
# and adjacent similar letters condition

def Diagraph(text):
	Diagraph = []
	group = 0
	for i in range(2, len(text), 2):
		Diagraph.append(text[group:i])

		group = i
	Diagraph.append(text[group:])
	return Diagraph

# Function to fill a letter in a string element
# If 2 letters in the same string matches


def FillerLetter(text):
	k = len(text)
	new_word = ""
	if k % 2 == 0:
		for i in range(0, k, 2):
			if text[i] == text[i+1]:
				if text[i] != 'x':
					new_word = text[0:i+1] + str('x') + text[i+1:]
					new_word = FillerLetter(new_word)
				else:
					new_word = text[0:i+1] + str('w') + text[i+1:]
					new_word = FillerLetter(new_word)
				break
			
			else:
				new_word = text
	else:
		for i in range(0, k-1, 2):
			if text[i] == text[i+1]:
				if text[i] != 'x':
					new_word = text[0:i+1] + str('x') + text[i+1:]
					new_word = FillerLetter(new_word)
					break
				else:
					new_word = text[0:i+1] + str('w') + text[i+1:]
					new_word = FillerLetter(new_word)
					break
			
			else:
				new_word = text
	print (new_word)
	return new_word


list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
		'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to generate the 5x5 key square matrix


def generateKeyTable(word, list1):
	key_letters = []
	# Appends unique letters in word to key_letters
	for i in word:  
		if i not in key_letters:
			key_letters.append(i)

	compElements = [] # Basically key matrix made flat to an array
	for i in key_letters:
		if i not in compElements:
			compElements.append(i)
	for i in list1:
		if i not in compElements:
			compElements.append(i)

	matrix = [] # Matrixification of the compElements
	while compElements != []:
		matrix.append(compElements[:5])
		compElements = compElements[5:]

	return matrix


def search(mat, element): # Search for the position of a single element in the matrix
	for i in range(5):
		for j in range(5):
			if(mat[i][j] == element):
				return i, j


def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
	char1 = ''
	if e1c == 4:
		char1 = matr[e1r][0]
	else:
		char1 = matr[e1r][e1c+1]

	char2 = ''
	if e2c == 4:
		char2 = matr[e2r][0]
	else:
		char2 = matr[e2r][e2c+1]

	return char1, char2


def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
	char1 = ''
	if e1r == 4:
		char1 = matr[0][e1c]
	else:
		char1 = matr[e1r+1][e1c]

	char2 = ''
	if e2r == 4:
		char2 = matr[0][e2c]
	else:
		char2 = matr[e2r+1][e2c]

	return char1, char2


def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
	char1 = ''
	char1 = matr[e1r][e2c]

	char2 = ''
	char2 = matr[e2r][e1c]

	return char1, char2


# plainList is the diagraph list of the plaintext
def encryptByPlayfairCipher(Matrix, plainList):
	CipherText = []
	for i in range(0, len(plainList)):
		c1 = 0
		c2 = 0
		ele1_x, ele1_y = search(Matrix, plainList[i][0])
		ele2_x, ele2_y = search(Matrix, plainList[i][1])

		if ele1_x == ele2_x:
			c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
			# Get 2 letter cipherText
		elif ele1_y == ele2_y:
			c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
		else:
			c1, c2 = encrypt_RectangleRule(
				Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

		cipher = c1 + c2
		CipherText.append(cipher)
	return CipherText

def decryptRowRule(matr, e1r, e1c, e2r, e2c):
	char1 = ''
	if e1c == 0:
		char1 = matr[e1r][4]
	else:
		char1 = matr[e1r][e1c-1]

	char2 = ''
	if e2c == 0:
		char2 = matr[e2r][4]
	else:
		char2 = matr[e2r][e2c-1]

	return char1, char2

def decryptRectangleRule(matr, e1r, e1c, e2r, e2c):
	char1 = ''
	char1 = matr[e1r][e2c]

	char2 = ''
	char2 = matr[e2r][e1c]

	return char1, char2

def decryptColumnRow(matr, e1r, e1c, e2r, e2c):
	char1 = ''
	if e1r == 0:
		char1 = matr[4][e1c]
	else:
		char1 = matr[e1r-1][e1c]

	char2 = ''
	if e2r == 0:
		char2 = matr[4][e2c]
	else:
		char2 = matr[e2r-1][e2c]

	return char1, char2



def decrypt(Matrix, CipherList):
	# Function to decrypt
	deCipherList = []
	for i in CipherList:
		c1 = ''
		c2 = ''
		ele1_x, ele1_y = search(Matrix, i[0])
		ele2_x, ele2_y = search(Matrix, i[1])
		if ele1_x == ele2_x:
			c1, c2 = decryptRowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
		elif ele1_y == ele2_y:
			c1, c2 = decryptColumnRow(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
		else:
			c1, c2 = decryptRectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

		decipher = c1 + c2
		deCipherList.append(decipher)
	return deCipherList
 

# text_Plain = 'hide the gold in the tree stump'

# for i in text_Plain:
# 	if i == 'j':
# 		text_Plain = text_Plain.replace(i, 'i')

# text_Plain = removeSpaces(toLowerCase(text_Plain))
# PlainTextList = Diagraph(FillerLetter(text_Plain))

# if len(PlainTextList[-1]) != 2:
# 	PlainTextList[-1] = PlainTextList[-1]+'z'

# key = "Monarchy"
# print("Key text:", key)
# key = toLowerCase(key)
# Matrix = generateKeyTable(key, list1)

# print("Plain Text:", text_Plain)
# CipherList = encryptByPlayfairCipher(Matrix, PlainTextList)

# deCipher_text = "bfckpdfimpbkrqcfzdiuillzol"
# deCipher_text = removeSpaces(toLowerCase(text_Plain))
# deCipherTextList = Diagraph(FillerLetter(text_Plain))
# deCipherList = decrypt(Matrix, CipherList)


# CipherText = ""
# for i in CipherList:
# 	CipherText += i
# print("CipherText:", CipherText)

# deCipherText = ""
# for i in deCipherList:
# 	deCipherText += i
# print("Deciphered Text:", deCipherText)

# This code is Contributed by Boda_Venkata_Nikith

def finalOutput(text, key, mode):

	if len(text) == 1:
		text += 'z'

	# print(text)
	# print(key)
	# print(mode)

	if(text == "" or key == ""):
		return "Please enter the text and key"
	
	for i in text:
		if i != ' ':
			if not i.isalpha():
				return "Please enter only alphabets in the text"
		
	for i in key:
		if i != ' ':
			if not i.isalpha():
				return "Please enter only alphabets in the key"

	mode = int(mode)

	for i in text:
		if i == 'j':
			text = text.replace(i, 'i')

	if(mode == 0):
		text = removeSpaces(toLowerCase(text))
		PlainTextList = Diagraph(FillerLetter(text))
		if len(PlainTextList[-1]) != 2:
			PlainTextList[-1] = PlainTextList[-1]+'z'

		key = toLowerCase(key)
		Matrix = generateKeyTable(key, list1)
		CipherList = encryptByPlayfairCipher(Matrix, PlainTextList)
		CipherText = ""
		for i in CipherList:
			CipherText += i
		# print(CipherText)
		return CipherText

	else:
		text = removeSpaces(toLowerCase(text))
		PlainTextList = Diagraph(FillerLetter(text))
		if len(PlainTextList[-1]) != 2:
			PlainTextList[-1] = PlainTextList[-1]+'z'

		key = toLowerCase(key)
		Matrix = generateKeyTable(key, list1)
		deCipherList = decrypt(Matrix, PlainTextList)
		deCipherText = ""
		for i in deCipherList:
			deCipherText += i
		return deCipherText

# print(finalOutput("mango", "richie", 0))
# print(finalOutput(finalOutput("mangoe", "richie", 0) ,"richie", 1))
	
def MatrixOut(word):

	word = removeSpaces(toLowerCase(word))
	for i in word:
		if not i.isalpha():
			return "ABCDEFGHIKLMNOPQRSTUVWXYZ"
	key_letters = []
	# Appends unique letters in word to key_letters
	for i in word:  
		if i not in key_letters:
			key_letters.append(i)

	compElements = [] # Basically key matrix made flat to an array
	for i in key_letters:
		if i not in compElements:
			compElements.append(i)
	for i in list1:
		if i not in compElements:
			compElements.append(i)

	for i in compElements:
		# capitalize each element
		compElements[compElements.index(i)] = i.upper()
	
	return compElements

def fillPrev(text, key):
	return text, key
