#importer la bibliotheque 
import hashlib

def hacher(text):
    #encoder la chaine de caractères
    texte_coder = text.encode()

    #creation de l'objet sha256
    objet_hacher = hashlib.sha256(texte_coder)

    #conversion de l'objet hacher en hexadécimal
    hexV = objet_hacher.hexdigest()

    return hexV

def H(text1,text2):
    id = text1
    y = text2
    x = 0 
    nb_calcule = 1

    while True :
        
        print('\nla valeur de X utilisé : ',x)
        h = hacher( id + str(x) )
        
        if h <= y :
            print('\n la valeur de sha256(id||x)  : ',hacher(id + str(x)))
            print('\n le nombre de calcules est :',nb_calcule)
            return x
        
        x += 1
        nb_calcule += 1

id = input("saisisez votre nom et prenom :")    
y = "00005d10cc11e27bd8d4d1ce91bc725665ddbaa6ca2498ef38a88a58ad48cdb4"

x = H(id , y)