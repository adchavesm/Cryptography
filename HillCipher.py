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
# 11,8,3,7
key=[-1,-1,-1,-1]
print('inserte la cordenada 1,1')
key[0]=int(input())
print('inserte la cordenada 1,2')
key[1]=int(input())
print('inserte la cordenada 2,1')
key[2]=int(input())
print('inserte la cordenada 2,2')
key[3]=int(input())

print(key)
encriptado=Encriptar('HOLA',key)

print(encriptado)
print(DesEncriptar(encriptado,key))

