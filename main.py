#importer la bibliotheque 
import hashlib

def hacher(text):
     #encoder la chaine de caractères
    texte_coder = text.encode()

    #creation de l'objet sha256
    objet_hacher = hashlib.sha1(texte_coder)

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
            print('\n la valeur de sha1(id||x)  : ',hacher(id + str(x)))
            print('\n le nombre de calcules est :',nb_calcule)
            return x
        
        x += 1
        nb_calcule += 1

id = input("saisisez votre nom et prenom :")    
y = "03b1663dda6549a0939ffdd712a852e0d4234e6b"

x = H(id , y)