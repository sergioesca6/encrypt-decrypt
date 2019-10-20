import random

def safetyLock():
	shuffleKey= input('Enter shuffle key:')
	if (shuffleKey != '1996'):
		print ("shuffle key accepted! Running...")
		callMenu(shuffleKey)
	else :
		print ("Initiating safety lock! Print random safe messages here!")

def	encrypt(shuffleKey):
	keyBase = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+'
	keyBaseArray = list(keyBase)
	codeKeyArray = keyBaseArray
	sentence = input("what do you want to encrypt? : ")
	charArray = list(sentence)
	print (shuffleKey)
	for count1,elem in enumerate(charArray):
		shuffleKey = int(shuffleKey)
		shuffleKey += count1
		random.seed(shuffleKey)
		random.shuffle(codeKeyArray)
		for count2,elem2 in enumerate(keyBase):
			if elem == elem2:
				charArray[count1]=codeKeyArray[count2]
	string1 = ''.join(charArray)
	return string1

def decrypt(shuffleKey):
	keyBase = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+'
	keyBaseArray = list(keyBase)
	codeKeyArray = keyBaseArray
	sentence = input("What do you want to decrypt? : ")
	charArray = list(sentence)
	for count1,elem in enumerate(charArray):
		shuffleKey = int(shuffleKey)
		shuffleKey += count1
		random.seed(shuffleKey)
		random.shuffle(codeKeyArray)
		for count2,elem2 in enumerate(codeKeyArray):
			if elem == elem2:
				keyBaseArray = list(keyBase)
				charArray[count1]=keyBaseArray[count2]
	string1 = ''.join(charArray)
	return string1

def callMenu(shuffleKey):
	choice = 0
	while (choice != '3'):
		choice = input("\n1.Encrypt \n2.Decrpyt \n3.Exit \nEnter your choice : ")
		if choice == "1":
			answer = encrypt(shuffleKey)
			print ('Encrypted sentence is : ' + '\033[1m\033[31m' + answer + '\033[0m')

		elif choice == "2":
			answer = decrypt(shuffleKey)
			print ('Encrypted sentence is : ' + '\033[1m\033[31m' + answer + '\033[0m')
		
		elif choice == "3":
			exit()

		else:
			print("Invalid choice, please try again\n")

if __name__ == '__main__':
	try:
		safetyLock()
	except KeyboardInterrupt:
		print('\nExiting...')
