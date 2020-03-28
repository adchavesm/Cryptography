def CalcularInversoModular(entero,modular):
    inverso=-1
    for i in range(0,modular+1):
        if (i*entero)%modular == 1:
            inverso=i
            
    return inverso

def Encriptar(TextoPlano,Clave):
    Encriptado = ""
    
    while len(TextoPlano)%4 !=0:
        TextoPlano=TextoPlano+"X"

    for i in range(0,len(TextoPlano),4):
        A=ord(TextoPlano[i])-65
        B=ord(TextoPlano[i+1])-65
        C=ord(TextoPlano[i+2])-65
        D=ord(TextoPlano[i+3])-65
        Encriptado+=chr(((A*Clave[0] + B*Clave[2])%26) +65)
        Encriptado+=chr(((A*Clave[1] + B*Clave[3])%26) +65)
        Encriptado+=chr(((C*Clave[0] + D*Clave[2])%26)+65)
        Encriptado+=chr(((C*Clave[1] + D*Clave[3])%26)+65)

    return Encriptado

def DesEncriptar(TextoCifrado,Clave):

    while len(TextoCifrado)%4 !=0:
        TextoCifrado=TextoCifrado+"X"

    Plano=""
    Determinante=(Clave[0]*Clave[3] - Clave[1]*Clave[2])%26
    if Determinante <0:
        Determinante=Determinante+26 
    
    inversaDeterminante=CalcularInversoModular(Determinante,26)
    matrizInversa=[-1,-1,-1,-1]
    
    matrizInversa[0]=inversaDeterminante*(Clave[3])% 26
    if(matrizInversa[0]<0):
        matrizInversa[0]+=26
    matrizInversa[1]=inversaDeterminante*(-Clave[1])% 26
    if(matrizInversa[1]<0):
        matrizInversa[1]+=26
    matrizInversa[2]=inversaDeterminante*(-Clave[2])% 26
    if(matrizInversa[2]<0):
        matrizInversa[2]+=26
    matrizInversa[3]=inversaDeterminante*(Clave[0])% 26
    if(matrizInversa[3]<0):
        matrizInversa[3]+=26

    for i in range(0,len(TextoCifrado),4):

        A=ord(TextoCifrado[i])-65
        B=ord(TextoCifrado[i+1])-65
        C=ord(TextoCifrado[i+2])-65
        D=ord(TextoCifrado[i+3])-65
        Plano+=chr(((A*matrizInversa[0] + B*matrizInversa[2])%26) +65)
        Plano+=chr(((A*matrizInversa[1] + B*matrizInversa[3])%26) +65)
        Plano+=chr(((C*matrizInversa[0] + D*matrizInversa[2])%26)+65)
        Plano+=chr(((C*matrizInversa[1] + D*matrizInversa[3])%26)+65)

    return Plano



print("\n                   Playfair Cipher\n")
print(" Please, insert the cipher matrix")
key=[-1,-1,-1,-1]
print('inserte la cordenada 1,1: ',end="")
key[0]=int(input())
print('inserte la cordenada 1,2: ',end=""))
key[1]=int(input())
print('inserte la cordenada 2,1: ',end=""))
key[2]=int(input())
print('inserte la cordenada 2,2: ',end=""))
key[3]=int(input())
print("\n  The encryption matrix is:\n")
begin=1
while(begin==1):
    print(" Options: \n 0. To close the program.\n 1. To encrypt\n 2. To decrypt\n Enter value: ", end="")
    instruction=input()
    if(instruction=='1'):
        print("  Enter the phrase to encrypt in CAPITAL LETTER: ", end="")
        plainText=input()
        print("  His encryption was: ",DesEncriptar(plainText,key))
    else:
        if(instruction=='2'):
            print("  Enter the phrase to Decrypt in CAPITAL LETTER:", end="")
            encryptText=input()
            print("  Your Decryption was: ",Encriptar(encryptText,key))
        else: begin=0
    print("\n  Press enter to continue...")
    input()

# 11,8,3,7