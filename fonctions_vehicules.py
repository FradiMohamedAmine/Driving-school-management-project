import json
import datetime
import os
#Initialisation db pour les vehicules
liste=[]
try:
    fichier="fichier4.json"
    taille = os.path.getsize(fichier)
    if taille == 0:
        with open(fichier,'w') as f:
            json.dump(liste,f)
        f.close()       
except FileNotFoundError :
    with open(fichier,'w') as f:
        json.dump(liste,f)
    f.close()
# ---------------------------------------
def test_Mat(M):
    if(M==0):
        return False
    with open(fichier) as f:
        l=json.load(f)
    for i in range(len(l)):
        if( l[i]['numero dimmatriculation '] == M ):
            return False
    return True
# ---------------------------------------
def test(M):
    fichier="fichier4.json"
    with open(fichier) as f:
        l=json.load(f)
    if( M.isnumeric() == True ): 
        M=int(M)   
        for i in range(len(l)):
            if( l[i]['numero dimmatriculation '] == M ):
                return True
        return False
    return False
# ---------------------------------------
def selectionner(M):
    with open(fichier) as f:
        l=json.load(f)
    for i in range(len(l)):
        if( l[i]['numero dimmatriculation '] == M ):
            return l[i]
# ---------------------------------------
def ajout_vehicule():
    fichier="fichier4.json"
    ajout=1
    while ajout==1:
        os.system("cls")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Ajout d' une nouvelle véhicule :  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        cordonnees={}
        Cat=" "
        Mat=0
        test=False
        while(test_Mat(Mat)==False ):
            print(" ---------------- Saisie de la numéro d’immatriculation de vehicule  : ---------------------")
            try:
                Mat=int(input("numéro d’immatriculation  : "))
            except TypeError :
                Mat=0
            if(test_Mat(Mat)==False ): print("Matricule INVALIDE ")
            else: print("//////////////  SAVED   ///////////////")
        while not(Cat in ["A","B","C"]) : 
            Cat=input("   -Merci de donner le type de vehicule (A pour MOTO ou B pour Voiture OU C pour Camion ) : ")
        print("//////////////  SAVED   ///////////////")
        M=input("Merci de donner la marque de la véhicule: ")
        print("//////////////  SAVED   ///////////////")
        y=0;m=0;d=0;
        while(test==False ):
            print(" ---------------- Saisie de date de la mise en service  : ---------------------")
            try:
                y=int(input("l'année : "))
                m=int(input("le mois : "))
                d=int(input("le jour : "))
                test=True
            except TypeError :
                y=0;m=0;d=0;
                test=False
            if(test == True):
                try:
                    x=datetime.datetime(y,m,d)
                    test =True
                except ValueError:
                    test= False 
            if(test==False ): print("DATE INVALIDE ")
            else: print("//////////////  SAVED   ///////////////")                
        kilos_tot=int(input("donner le kilométrage total :   "))
        print("//////////////  SAVED   ///////////////")
        kilos_rest=int(input("donner  le nombre de km qui reste pour le prochain entretient  :    "))
        print("//////////////  SAVED   ///////////////")
        ch=str(y)+'-'+str(m)+'-'+str(d)
        cordonnees={"numero dimmatriculation ":Mat,"Marque":M ,"categorie":Cat,"date_MES":ch,"kilos_tot":kilos_tot,"kilos_rest":kilos_rest}
        print("             ---------       Successfully SAVED  ☻ ")
        with open(fichier) as f:
            aliste=json.load(f)       
        aliste.append(cordonnees)
        with open(fichier,'w') as f:
            json.dump(aliste,f)
        f.close()
        try:     
            ajout=int(input("Voulez vous ajouter un autre véhicule : (0/1)"))    
        except ValueError:    
            ajout=0      
# ---------------------------------------
def affichage_vehicule():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Affichage des véhicules :  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    with open(fichier) as f:
        l=json.load(f)
    if(len(l)== 0 ) : print("Pas encore des véhicles : ")   
    for i in range(len(l)):
        print(l[i])
        print('-------')
# ---------------------------------------
def modifier_vehicule():
    fichier="fichier4.json"
    ajout=1
    while ajout==1:
        os.system("cls")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Modifier un véhicule :  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("IL faut choisir le numéro d’immatriculation de la vehicule qui vous vouler modifier : ")
        affichage_vehicule()
        m=" "
        while( test(m)== False ):
            print("Merci de donner un numéro d’immatriculation  valide parmi votre liste : ")
            m =input(' % - le numéro d’immatriculation de la vehicule qui vous vouler modifier :      ')
        m=int(m)   
        os.system("cls")
        dict = selectionner(m)
        print("////////////////////////////////////////////////")
        print(dict)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Modifier le kilométrage total :  :  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        a=" "
        while( a.isnumeric() == False):
            a =input(' % - le nouveau valeur du  kilométrage total    :  ')
        a=int(a)
        r=a-dict["kilos_tot"]
        dict["kilos_tot"]=a 
        dict["kilos_rest"]=dict["kilos_rest"]-r 
        with open(fichier) as f:
            l=json.load(f)
        for i in range(len(l)):
            if( l[i]['numero dimmatriculation '] == m ):
                    j=i
                    break
        l[j]=dict
        with open(fichier,'w') as f:
            json.dump(l,f)
        print(" ++++++++++++++++++++++  le nombre de km qui reste pour le prochain entretient est rénouvoulé +++++++++")
        print("<<<<<<<<<<<<                       Modification Terimnée                                   >>>>>>>>>>>>")
        ajout= " "
        while( ajout.isnumeric()== False or( ajout != '1' and ajout != '0' )):    
            ajout=input("Voulez vous modifier un autre véhicule : (0/1)")    
        ajout=int(ajout)
# ---------------------------------------
def supprimer_vehicule():
    fichier="fichier4.json"
    ajout=1
    while ajout==1:
        os.system("cls")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Supprimer un véhicule :  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("IL faut choisir le numéro d’immatriculation de la vehicule qui vous vouler Suprimer : ")
        affichage_vehicule()
        m=" "
        while( test(m)== False ):
            print("Merci de donner un numéro d’immatriculation  valide parmi votre liste : ")
            m =input(' % - le numéro d’immatriculation de la vehicule qui vous vouler supprimer :      ')
        m=int(m)   
        os.system("cls")        
        dict = selectionner(m)
        print("////////////////////////////////////////////////")
        print(dict)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Suppression    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        ok=" "
        while( ok.isnumeric()== False or( ok != '1' and ok != '0' )):    
            ok=input("Are u sure ???? ! (0/1) : ")
        ok=int(ok)
        if(ok == 1 ):        
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Suppression    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            with open(fichier) as f:
                l=json.load(f)
            j=0
            for i in range(len(l)):
                if( l[i]['numero dimmatriculation '] == m ):
                        j=i
                        break
            print(l[j])
            del l[j]
            with open(fichier,'w') as f:
                json.dump(l,f)
            f.close()
            #os.system("cls")
            print(" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  Suppression Terminé ++++++++++++++++++")
        else :
            print(" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  Suppression annulé ++++++++++++++++++")  
        ajout=" "
        while( ajout.isnumeric()== False or( ajout != '1' and ajout != '0' )):    
            ajout=input("Voulez vous Supprimer  un autre véhicule (0/1) :  ")    
        ajout=int(ajout)
#---------------------------
def Recherche_Visualiser_vehicule():
    fichier="fichier4.json"
    ajout=1
    while ajout==1:
        os.system("cls")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Rechercher et Visualiser un vehicule :  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("IL faut choisir le numéro d’immatriculation de la vehicule qui vous vouler visualiser : ")
        affichage_vehicule()
        m=" "
        while( test(m)== False ):
            print("Merci de donner un numéro d’immatriculation de la vehicule  valide parmi votre liste : ")
            m =input(' % -  le numéro d’immatriculation de la vehicule  :      ')
        m=int(m)   
        os.system("cls")        
        dict = selectionner(m,fichier)
        print("////////////////////////////////////////////////")
        print(dict)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Details :   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Marque  :", dict["Marque"])
        print("Catégorie :",dict["categorie"])
        print("La date de la mise en service :",dict["date_MES"])
        print("le kilométrage total  :",dict["kilos_tot"])
        print("le nombre de km qui reste pour le prochain entretient ",dict["kilos_rest"])
        print("----------------------------------------------------------------------------------------------")
        ajout=" "
        while( ajout.isnumeric()== False or( ajout != '1' and ajout != '0' )):    
            ajout=input("Voulez vous visualiser  un autre véhicule (0/1) :  ")    
        ajout=int(ajout)
