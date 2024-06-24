# Vigenère Cipher Calculator

```bash
__     ___                                   ____ _       _               
\ \   / (_) __ _  ___ _ __   ___ _ __ ___   / ___(_)_ __ | |__   ___ _ __ 
 \ \ / /| |/ _` |/ _ \ '_ \ / _ \ '__/ _ \ | |   | | '_ \| '_ \ / _ \ '__|
  \ V / | | (_| |  __/ | | |  __/ | |  __/ | |___| | |_) | | | |  __/ |   
   \_/  |_|\__, |\___|_| |_|\___|_|  \___|  \____|_| .__/|_| |_|\___|_|   
           |___/                                   |_|                    
**************************************************************************
* Copyright of pnasis, 2024 *
```

## Introduction
The Vigenère cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. Named after Blaise de Vigenère, this cipher uses a keyword to determine the shift for each letter of the plaintext.

This tool allows you to easily perform encryption and decryption using the Vigenère cipher.

## How it works
### Encryption


The Vigenère cipher uses a key to encrypt the message. Each letter in the plaintext is shifted along some number of places determined by the corresponding letter in the key.

**Encryption Steps:**
1. Select a key, a word or phrase, and repeat it to match the length of the plaintext.
2. Convert each letter of the plaintext and the key into their numerical equivalents (A=0, B=1, ..., Z=25).
3. Add the numerical values of the plaintext and key letters, and take the result modulo 26.
    - Example:
        - **Plaintext**: HELLO
        - **Key**: KEY
        - Repeat the key to match the plaintext length: KEYKE
4. Convert the resulting numbers back to letters to get the ciphertext.
    - Example:
        - H (7) + K (10) = R (17)
        - E (4) + E (4) = I (8)
        - L (11) + Y (24) = J (9) (since 11 + 24 = 35, and 35 mod 26 = 9)
        - L (11) + K (10) = V (21)
        - O (14) + E (4) = S (18)
    - **Ciphertext**: RIJVS

### Decryption

To decrypt a message encrypted with the Vigenère cipher, the same key is used to reverse the encryption process.

**Decryption Steps:**
1. Use the same key used for encryption.
2. Convert each letter of the ciphertext and the key into their numerical equivalents.
3. Subtract the numerical values of the key from the ciphertext letters, and take the result modulo 26.
    - Example:
        - **Ciphertext**: RIJVS
        - **Key**: KEY
        - Repeat the key to match the ciphertext length: KEYKE
4. Convert the resulting numbers back to letters to get the plaintext.
    - Example:
        - R (17) - K (10) = H (7)
        - I (8) - E (4) = E (4)
        - J (9) - Y (24) = L (11) (since 9 - 24 = -15, and -15 mod 26 = 11)
        - V (21) - K (10) = L (11)
        - S (18) - E (4) = O (14)
    - **Plaintext**: HELLO

## Usage
To execute the python script, simply run the following:
```bash
python3 vigenere.py
```
You will be asked to provide the text to be modified and then the keyword that will be used to create the keystream. Finally, you will be asked to choose whether you wish to encrypt or decrypt the text.

## Contributing
> Pull requests are welcome. **For major changes, please open an issue first to discuss what you would like to change.**

## License
>This project is under [Apache 2.0](https://choosealicense.com/licenses/apache-2.0/) license.
