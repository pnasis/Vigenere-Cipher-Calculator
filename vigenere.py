def intro():
    print(r"""    
__     ___                                   ____ _       _               
\ \   / (_) __ _  ___ _ __   ___ _ __ ___   / ___(_)_ __ | |__   ___ _ __ 
 \ \ / /| |/ _` |/ _ \ '_ \ / _ \ '__/ _ \ | |   | | '_ \| '_ \ / _ \ '__|
  \ V / | | (_| |  __/ | | |  __/ | |  __/ | |___| | |_) | | | |  __/ |   
   \_/  |_|\__, |\___|_| |_|\___|_|  \___|  \____|_| .__/|_| |_|\___|_|   
           |___/                                   |_|                    
    """)
    print("\n**************************************************************************")
    print("* Copyright of pnasis, 2024 *")

# Function for generating the key
def generateKey(string, key):
	key = list(key)
	if len(string) == len(key):
		return(key)
	else:
		for i in range(len(string) -
					len(key)):
			key.append(key[i % len(key)])
	return("" . join(key))

# Function for the encryption process	
def encrypt(string, key):
	cipher_text = []
	for i in range(len(string)):
		x = (ord(string[i]) +
			ord(key[i])) % 26
		x += ord('A')
		cipher_text.append(chr(x))
	return("" . join(cipher_text))

# Function for the decryption process
def decrypt(cipher_text, key):
	orig_text = []
	for i in range(len(cipher_text)):
		x = (ord(cipher_text[i]) -
			ord(key[i]) + 26) % 26
		x += ord('A')
		orig_text.append(chr(x))
	return("" . join(orig_text))
	
# Driver code
if __name__ == "__main__":
	try:
		intro()
		string = input("Enter text: ")
		keyword = input("Enter keyword: ")
		key = generateKey(string, keyword)
		option = int(input("Encryption(0)/Decryption(1): "))
		if option==0:
			print("Ciphertext:", encrypt(string,key))
		else:
			print("Plaintext:", decrypt(string, key))
	except KeyboardInterrupt:
		print("\nExecution interrupted by user.")