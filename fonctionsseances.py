from calendar import month
import json
import datetime
import os
from fonctions_vehicules import affichage_vehicule,test
#Initialisation seance Code
liste=[]
try:
    fichier="fichier2.json"
    taille = os.path.getsize(fichier)
    if taille == 0:
        with open("fichier2.json",'w') as f:
            json.dump(liste,f)
        f.close()
except FileNotFoundError :
    with open("fichier2.json",'w') as f:
        json.dump(liste,f)
    f.close()

#Initialisation seance Conduite
liste=[]
try:
    fichier="fichier3.json"
    taille = os.path.getsize(fichier)
    if taille == 0:
        with open("fichier3.json",'w') as f:
            json.dump(liste,f)
        f.close()        
except FileNotFoundError :
    with open("fichier3.json",'w') as f:
        json.dump(liste,f)
    f.close()
# ---------------------------------------   
def Num_Seance(fichier):
    with open(fichier) as f:
        l=json.load(f)
    if len(l)==0:
        return 1
    else:
        n=1
        for i in range(len(l)):    
                n+=1
        return n
# ---------------------------------------    
def selectionner(M,fichier):
    with open(fichier) as f:
        l=json.load(f)
    for i in range(len(l)):
        if( l[i]['Num'] == M ):
            return l[i]
# ---------------------------------------

def test1_date(y,m,d,h,mn):
    try:
        x=datetime.datetime(y,m,d,h,mn)
    except ValueError:
        return False
    date=datetime.datetime.now()
    if(date<x):
       return True
    else:
        return False
# ---------------------------------------
def test2(sean : dict,fichier):
    if(sean != {}):
        ing=sean["ingenieur"]
        d=sean["date"]
        h=sean["heure"]
        with open(fichier) as f:
            l=json.load(f)
        for i in range(len(l)):
            if(l[i]["ingenieur"]== ing and l[i]["date"]== d and l[i]["heure"]== h ):
                return False
        return True        
    return False
# ---------------------------------------
def test3(sean : dict,fichier):
    if(sean != {}):
        ing=sean["ingenieur"]
        d=sean["date"]
        h=sean["heure"]
        v=sean["vehicule "]
        with open(fichier) as f:
            l=json.load(f)
        for i in range(len(l)):
            if(l[i]["ingenieur"]== ing and l[i]["date"]== d and l[i]["heure"]== h and l[i]["vehicule "]== v ):
                return False
        return True        
    return False
# ---------------------------------------
def test4(M,fichier):
    with open(fichier) as f:
        l=json.load(f)
    if( M.isnumeric() == True ): 
        M=int(M)   
        for i in range(len(l)):
            if( l[i]['Num'] == M ):
                return True
        return False
    return False
# ---------------------------------------
def ajout_seance_code():
    fichier="fichier2.json"
    seance={}
    while(test2(seance , fichier)==False):
        y=0;m=0;d=0;h=0;mn=0
        while(test1_date(y,m,d,h,mn)==False ):
            print(" ---------------- Saisie de date et de l' heure de la seance : ---------------------")
            try:
                print("********* donner la date de la séance :  ****************")
                y=int(input("l'année : "))
                m=int(input("le mois : "))
                d=int(input("le jour : "))
                print("********* donner l'heure de la séance :  ****************")
                h=int(input(" l'heure  : "))
                mn=int(input("le minute : "))
            except TypeError :
                    y=0;m=0;d=0;h=0;mn=0
            ing=input("donner l'ingenieur de la séance  : ")
            num =Num_Seance(fichier)
        ch=str(y)+'-'+str(m)+'-'+str(d)
        seance={"Num":num,"date":ch,"heure":h,"minute":mn,"ingenieur":ing,"etat":'code'}
        if(test2(seance,fichier)==False): 
            print("Merci de choisir  un date et un heure lorsque cet ingenieur soit dispo :)  ou bien choisir un autre ingenieur !!  ")
        else: 
            print("             ---------       Successfully SAVED  ☻ ")
    with open(fichier) as f:
        aliste=json.load(f)       
    aliste.append(seance)
    with open(fichier,'w') as f:
        json.dump(aliste,f)
    f.close()
    return seance

#-----------------------
def ajout_seance_conduite():
    fichier="fichier3.json"
    seance={}
    while(test2(seance , fichier)==False):
        y=0;m=0;d=0;h=0;mn=0
        while(test1_date(y,m,d,h,mn)==False ):
            print(" ---------------- Saisie de date et de l' heure de la seance : ---------------------")
            try:
                print("********* donner la date de la séance :  ****************")
                y=int(input("l'année : "))
                m=int(input("le mois : "))
                d=int(input("le jour : "))
                print("********* donner l'heure de la séance :  ****************")
                h=int(input(" l'heure  : "))
                mn=int(input("le minute : "))
            except TypeError :
                y=0;m=0;d=0;h=0;mn=0
            print("-------------------Choisir l'ingenieur qui va  asssure cet seance : --------------")    
            ing=input("donner l'ingenieur de la séance : ")
            num =Num_Seance(fichier)
            print("-------------------Choisir le vehicule utilsé dans cet seance : --------------")
            affichage_vehicule()
            v=" "
            while( test(v)== False ):
                v= input(" Donner  sa matricule : ")
            v=int(v)
        ch=str(y)+'-'+str(m)+'-'+str(d)
        seance={"Num":num,"date":ch,"heure":h,"minute":mn,"ingenieur":ing,"vehicule ":v,"etat":'conduite'}
        if(test3(seance,fichier)==False): 
            os.system("cls")
            print(" !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  Erreur !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Merci de choisir  un date et un heure pour que cet ingenieur et cet voiture soit dispo :) ")
            print("**********************  ")
        else: 
            print("--------------------------       Successfully SAVED  ☻ ")
                    
    with open(fichier) as f:
            aliste=json.load(f)       
    aliste.append(seance)
    with open(fichier,'w') as f:
        json.dump(aliste,f)
    f.close()
    return seance
# ---------------------------------------
def affichage_seances_code():
    fichier="fichier2.json"
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Affichage des séances de code :  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    with open(fichier) as f:
        l=json.load(f)
    if(len(l)== 0 ) : print("Pas encore des séance planifié  : ")   
    for i in range(len(l)):
        print(l[i])
        print('-------')
# ---------------------------------------
def affichage_seances_conduite():
    fichier="fichier3.json"
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Affichage des séances de conduit :  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    with open(fichier) as f:
        l=json.load(f)
    if(len(l)== 0 ) : print("Pas encore des séance planifié  : ")   
    for i in range(len(l)):
        print(l[i])
        print('-------')
#-------------------------------------
def supprimer_séance_code():
    fichier="fichier2.json"
    ajout=1
    while ajout==1:
        os.system("cls")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Supprimer un séance de code :  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("IL faut choisir le numéro de la seance  qui vous vouler Suprimer : ")
        affichage_seances_code()
        m=" "
        while( test4(m,fichier)== False ):
            print("Merci de donner un numéro d'une seance valide parmi votre liste : ")
            m =input(' % - le numéro de la seance qui vous vouler supprimer :      ')
        m=int(m)   
        os.system("cls")        
        dict = selectionner(m,fichier)
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
                if( l[i]['Num'] == m ):
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
            ajout=input("Voulez vous Supprimer  une autre séance (0/1) :  ")    
        ajout=int(ajout)
#---------------------------------------------------------------------------------------------------------
def supprimer_séance_conduite():
    fichier="fichier3.json"
    ajout=1
    while ajout==1:
        os.system("cls")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Supprimer un séance de conduite :  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("IL faut choisir le numéro de la seance  qui vous vouler Suprimer : ")
        affichage_seances_conduite()
        m=" "
        while( test4(m,fichier)== False ):
            print("Merci de donner un numéro d'une seance valide parmi votre liste : ")
            m =input(' % - le numéro de la seance qui vous vouler supprimer :      ')
        m=int(m)   
        os.system("cls")        
        dict = selectionner(m,fichier)
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
                if( l[i]['Num'] == m ):
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
            ajout=input("Voulez vous Supprimer  une autre séance (0/1) :  ")    
        ajout=int(ajout)
