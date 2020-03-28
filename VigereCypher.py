def encript(plainText,key):
    encryption=""
    s=0
    for i in range(0,len(plainText)):
        encryption+=chr((((ord(plainText[i])-65) + (ord(key[s])-65))%26)+65)
        s=(s+1)%len(key)

    return encryption

def decrypher(cipherText,key):
    decryption=""
    s=0
    for i in range(0,len(cipherText)):
        decryption+=chr((((ord(cipherText[i])-65) - (ord(key[s])-65)+26)%26)+65)
        s=(s+1)%len(key)

    return decryption


print("\n                   Vigere Cipher\n")
print()
begin=1
while(begin==1):
    print(" Options: \n 0. To close the program.\n 1. To encrypt\n 2. To decrypt\n Enter value: ", end="")
    instruction=input()
    if(instruction=='1'):
        print("  Enter the key word in CAPITAL LETTER: ", end="")
        key=input()
        print("  Enter the phrase to encrypt in CAPITAL LETTER: ", end="")
        plainText=input()
        print("  Your Decryption was: ",encript(plainText,key))
    else:
        if(instruction=='2'):
            print("  Enter the key word in CAPITAL LETTER: ", end="")
            key=input()
            print("  Enter the phrase to encrypt in CAPITAL LETTER: ", end="")
            encryptText=input()
            print("  Your Decryption was: ",decrypher(encryptText,key))
        else: begin=0
    print("\n  Press enter to continue...")
    input()


#cipherText=encript("ESTAESUNACARTAPARATODALAGENTEQUEMEQUIERESEPUTOESTO","RELATIONS")
#plainText=decrypher(cipherText,"RELATIONS")
#print(cipherText)
#print(plainText)