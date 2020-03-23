#Function that return matriz-key
def calcularMatriz(Key):
    
    matriz=[[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]
    keyOrder=''
    abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
   
    for i in range(0,len(Key)):
        repet= False
        for k in range(0,len(keyOrder)):
            if keyOrder[k]==Key[i]:
                repet=True
                break
        if repet==False:
            keyOrder+=Key[i]

    for i in range(0,len(abc)):
        repet= False
        for k in range(0,len(keyOrder)):
            if keyOrder[k]==abc[i]:
                repet=True
                break
        if repet==False:
            keyOrder+=abc[i]

    s=0
    ConIJ=False
    for j in range(0,5):
        k=0
        while k<5:
            if (keyOrder[s]== 'I' or keyOrder[s]== 'J'):
                if ConIJ==False:
                    matriz[j][k]='IJ'
                    ConIJ=True
                    k+=1
            else:
                matriz[j][k]=keyOrder[s]
                k+=1
            s=s+1
    return matriz

def encrypt(plainText,matrix):
    encryption=""
    if len(plainText)%2 ==1:
        plainText+='X'
    for i in range(0,len(plainText),2):
        if(plainText[i]==plainText[i+1]):
            plainTextAux=plainText
            plainText=""
            plainText+=plainTextAux[0:i+1]
            plainText+="X"
            plainText+=plainTextAux[i+2:]

    for i in range(0, len(plainText),2):
        A=plainText[i]
        B=plainText[i+1]
        posInMatrixA=[-1,-1]
        posInMatrixB=[-1,-1]
        for j in range(0,5):
            for k in range(0,5):
                if(matrix[j][k].find(A)!=-1):
                    posInMatrixA[0]=j
                    posInMatrixA[1]=k
                else:
                    if(matrix[j][k].find(B)!=-1):
                        posInMatrixB[0]=j
                        posInMatrixB[1]=k
        
        #Asignacion
        if posInMatrixA[0] == posInMatrixB[0]:
            #si la fila es la misma
            
            encryption+=matrix[posInMatrixA[0]][(posInMatrixA[1]+1)%5]
            encryption+=matrix[posInMatrixB[0]][(posInMatrixB[1]+1)%5]
        else:
            if posInMatrixA[1] == posInMatrixB[1]:
                #Si la columna es la misma
                encryption+=matrix[(posInMatrixA[0]+1)%5][posInMatrixA[1]]
                encryption+=matrix[(posInMatrixB[0]+1)%5][posInMatrixB[1]]
            else:
                #other case
                if (matrix[j][k]=='IJ'):
                    encryption+=matrix[posInMatrixA[0]][posInMatrixB[1]]
                    encryption+=matrix[posInMatrixB[0]][posInMatrixA[1]]
                else: 
                    encryption+=matrix[posInMatrixA[0]][posInMatrixB[1]]
                    encryption+=matrix[posInMatrixB[0]][posInMatrixA[1]]
    for s in range(0,len(plainText)):
        if encryption[s]=='I':
            encryptionAux=encryption
            encryption=""
            encryption+=encryptionAux[0:s]
            encryption+='I'
            encryption+=encryptionAux[s+2:]
    return encryption

def Decrypt(plainText,matrix):
    encryption=""
    if len(plainText)%2 ==1:
        plainText+='X'
    for i in range(0,len(plainText),2):
        if(plainText[i]==plainText[i+1]):
            plainTextAux=plainText
            plainText=""
            plainText+=plainTextAux[0:i+1]
            plainText+="X"
            plainText+=plainTextAux[i+2:]

    for i in range(0, len(plainText),2):
        A=plainText[i]
        B=plainText[i+1]
        posInMatrixA=[-1,-1]
        posInMatrixB=[-1,-1]
        for j in range(0,5):
            for k in range(0,5):
                if(matrix[j][k].find(A)!=-1):
                    posInMatrixA[0]=j
                    posInMatrixA[1]=k
                else:
                    if(matrix[j][k].find(B)!=-1):
                        posInMatrixB[0]=j
                        posInMatrixB[1]=k
        
        #Asignacion
        if posInMatrixA[0] == posInMatrixB[0]:
            #si la fila es la misma
            
            encryption+=matrix[posInMatrixA[0]][(posInMatrixA[1]+4)%5]
            encryption+=matrix[posInMatrixB[0]][(posInMatrixB[1]+4)%5]
        else:
            if posInMatrixA[1] == posInMatrixB[1]:
                #Si la columna es la misma
                encryption+=matrix[(posInMatrixA[0]+4)%5][posInMatrixA[1]]
                encryption+=matrix[(posInMatrixB[0]+4)%5][posInMatrixB[1]]
            else:
                #other case
                if (matrix[j][k]=='IJ'):
                    encryption+=matrix[posInMatrixA[0]][posInMatrixB[1]]
                    encryption+=matrix[posInMatrixB[0]][posInMatrixA[1]]
                else: 
                    encryption+=matrix[posInMatrixA[0]][posInMatrixB[1]]
                    encryption+=matrix[posInMatrixB[0]][posInMatrixA[1]]
    for s in range(0,len(plainText)):
        if encryption[s]=='I':
            encryptionAux=encryption
            encryption=""
            encryption+=encryptionAux[0:s]
            encryption+='I'
            encryption+=encryptionAux[s+2:]
    return encryption

print("\n                   Playfair Cipher\n")
print("  Enter the keyword to calculate the encryption matrix: ", end="")
palabraClave=input()
#YOANPIZ
keyMatrix=calcularMatriz(palabraClave)
print("\n  The encryption matrix is:\n")
for i in range(0,5):
    for j in range(0,5):
        if keyMatrix[i][j]=='IJ':
            print(keyMatrix[i][j]," ",end="")
        else:
            print(keyMatrix[i][j],"  ",end="")
    print("")
print()
begin=1
while(begin==1):
    print(" Options: \n 0. To close the program.\n 1. To encrypt\n 2. To decrypt\n Enter value: ", end="")
    instruction=input()
    if(instruction=='1'):
        print("  Enter the phrase to encrypt in CAPITAL LETTER: ", end="")
        plainText=input()
        encryption=encrypt(plainText,keyMatrix)
        print("  His encryption was: ",encryption)
    else:
        if(instruction=='2'):
            print("  Enter the phrase to Decrypt in CAPITAL LETTER:", end="")
            encryptText=input()
            Dencryption=Decrypt(encryptText,keyMatrix)
            print("  Your Decryption was: ",Dencryption)
        else: begin=0
    print("\n  Press enter to continue...")
    input()