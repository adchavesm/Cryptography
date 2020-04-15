
def rotate (Matrix,right):
    MatrixAux = [row[:] for row in Matrix]
    n=len(Matrix)
    if right:
        for i in range(0,n):
            for j in range(0,n):
                MatrixAux[i][j] =Matrix[n-1-j][i] 
        return MatrixAux
    else:
        for i in range(0,n):
            for j in range(0,n):
                MatrixAux[n-1-j][i] =Matrix[i][j] 
        return MatrixAux

def encrypt (Matrix,plainText, right):
    n=len(Matrix)
    plainText_list = list(plainText)
    T=[[0]*n for i in range(n)]
    
    o=0
    for k in range(0,4):
        for i in range(0,n):
            for j in range(0,n):
                if(Matrix[i][j]==1):
                    T[i][j] = plainText_list[o]
                    o+=1
        Matrix= rotate(Matrix,right)
    cypherText=""
    
    for i in range(0,n):
            for j in range(0,n):
                cypherText+=T[i][j]
    return cypherText


def Decrypt (Matrix,cypherText, right):
    n=len(Matrix)
    cypherText_list = list(cypherText)
    T=[[0]*n for i in range(n)]
    
    p=0
    for i in range(0,n):
        for j in range(0,n):
            T[i][j] = cypherText_list[p]
            p+=1
    plainText=""
    for k in range(0,4):
        for i in range(0,n):
            for j in range(0,n):
                if(Matrix[i][j]==1):
                    plainText+=T[i][j]
        Matrix=rotate(Matrix,right)

    return plainText

print("\n                   Griller Cipher\n")
#print("Ingrese, el tamano de la matriz: ")
#n=input()
#Matrix = [ [-1 for columna in range(0,n)] for fila in range (0,n)]
#for i in range(0,n):
#   for j in range(0,n):
#        print("\n  Ingrese, el tamano de la matriz en la posicion \n"," ",i," ",j)
#        Matrix[i][j]=input()
#print("Por Favor ingrese el sentido giratorio(1, para derecha o 0, para izquierda)")
#sentido=input()
#if(sentido==1):
#    sentido=True
#else: sentido=False
#

Matrix=[[1,0,0,0],[0,0,0,0],[0,1,0,1],[0,0,1,0]]
sentido=True

begin=1
while(begin==1):
    print(" Options: \n 0. To close the program.\n 1. To encrypt\n 2. To decrypt\n Enter value: ")
    instruction=input()
    if(instruction==1):
        print("  Enter the phrase to encrypt in CAPITAL LETTER: ")
        plainText=input()
        print("  His encryption was: ",encrypt(Matrix,plainText,sentido))
    else:
        if(instruction==2):
            print("  Enter the phrase to Decrypt in CAPITAL LETTER:")
            encryptText=input()
            print("  Your Decryption was: ",Decrypt(Matrix,encryptText,sentido))
        else: begin=0
    print("\n  Press enter to continue...")
    input()