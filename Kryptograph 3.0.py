import os

print("Kryptograph 4.0\n")

print("to encrypt your text, type [encrypt]")
print("to decrypt your text, type [decrypt]")
print("to clear window, type [clear]")

print("to end program, type [exit]\n")


intab = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
outtab = "Z1T2R3E4W5Q6U7I8O9P0ASDFGuztrüwqiopasdCVBNmHJKLMNbvc"

encryptTranslate = str.maketrans(intab, outtab)
decryptTranslate = str.maketrans(outtab, intab)

Entry = input("\nWelcome!\n")

while Entry != "exit":

    x = input("Entry:")
    
    if x == "encrypt":
        
        
        x = input("\nYour Text(encrypted):")
        encrypt = x.translate(encryptTranslate)
        print(encrypt)
        
    
    elif x == "decrypt":
    
        x = input("\nYour Text(decrypted):")
        decrypt = x.translate(decryptTranslate)
        print(decrypt)
    
    elif x == "clear":
    
        os.system("cls")
        
        print("Kryptograph 4.0\n")

        print("to encrypt your text, type [encrypt]")
        print("to decrypt your text, type [decrypt]")
        print("to clear window, type [clear]")

        print("to end program, type [exit]\n")
    
    
    elif x == "exit":
    
        break
    
    
    else:
    
        print("Sorry?")

print("Have a nice day!")
        
        
input()