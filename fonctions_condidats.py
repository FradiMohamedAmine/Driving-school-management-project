import os
import json
from fonctionsseances import ajout_seance_code,ajout_seance_conduite
#Initialisation condidat liste
liste=[]
try:
    fichier="fichier1.json"
    taille = os.path.getsize(fichier)
    if taille == 0:
        with open("fichier1.json",'w') as f:
            json.dump(liste,f)
        f.close()
except FileNotFoundError :
    with open("fichier1.json",'w') as f:
        json.dump(liste,f)
    f.close()

# ---------------------------------------
def test1(Cin):
    with open("fichier1.json") as f:
        liste=json.load(f)   
    for i in range(len(liste)):      
        if(liste[i]["CIN"]== Cin):
            return False
    return True
# ---------------------------------------
def test2(cat):
    with open("fichier1.json") as f:
        liste=json.load(f)   
    for i in range(len(liste)):      
        if(liste[i]["categorie"]== cat):
            return False
    return True
# ---------------------------------------
def test3(M,fichier):
    with open(fichier) as f:
        l=json.load(f)
    if( M.isnumeric() == True ): 
        M=int(M)  
         
        for i in range(len(l)):
            print("ok")
            if( l[i]["CIN"] == M ):
                return True
        return False
    return False
# ---------------------------------------    
def selectionner(M,fichier):
    with open(fichier) as f:
        l=json.load(f)
    for i in range(len(l)):
        if( l[i]['CIN'] == M ):
            return l[i]
#-----------------------
def ajout_condidat():
    os.system("cls")
    print("-------------------  Ajouter un nouveau candidat :   --------------------------------------- ")
    CIN = ''
    Cat = ''
    while  ( CIN.isnumeric() == False or len(CIN) != 8 ):
            CIN=input("  - Merci de donner le num de CIN  : ")
    CIN=int(CIN)
    print("------------------")
    print("Saved  :) ")
    print("------------------")
    Nom=input("  - Merci de donner le nom et le prenom du condidat  : ")
    print("------------------")
    print("Saved  :) ")
    print("------------------")
    while not(Cat in ["A","B","C"]) : 
         Cat=input("   -Merci de donner la catégorie du permis(A pour MOTO ou B pour Voiture OU C pour Camion ) : ")
    print("------------------")
    print("Saved  :) ")
    print("------------------")
    tabseanceC=[]
    tabseanceCn=[]
    montant=0
    reste=0
    montant2=0
    condidat={"CIN":CIN,"nom":Nom ,"categorie":Cat,"Tableau_num_seance_code":tabseanceC,"Tableau_num_seance_conduit":tabseanceCn,"montant_tot":montant,"montant_paye":montant2,"reste":reste}
    with open("fichier1.json") as f:
        aliste=json.load(f) 
    aliste.append(condidat)
    with open("fichier1.json",'w') as f:
        json.dump(aliste,f)
    f.close()
#-------------------------------
def affichage_condidat():
    fichier="fichier1.json"
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Affichage des condidats  :  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    with open(fichier) as f:
        l=json.load(f)
    if(len(l)== 0 ) : print("Pas encore des condidats inscrit  : ")   
    for i in range(len(l)):
        print(l[i])
        print('-------')    
    f.close()
#-------------------------------
def modifier_condidat():
    fichier="fichier1.json"
    ajout=1
    while ajout==1:
        os.system("cls")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Modifier le condiadat :  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("IL faut choisir le numéro CIN de la condidat  qui vous vouler  modifier : ")
        affichage_condidat()
        m=" "
        while( test3(m,fichier)== False ):
            print(" Merci de donner un numéro CIN de condidat valide parmi votre liste : ")
            m =input(' % - le numéro CIN de condidat qui vous vouler  modifier :      ')
        m=int(m)   
        os.system("cls")
        dict = selectionner(m,fichier)
        print("////////////////////////////////////////////////")
        print(dict)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Modifier le montant à Payer :  :  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        a=" "
        while( a.isnumeric() == False):
            a =input(' % - le nouveau montant payé     :  ')
        a=int(a)
        dict["montant_paye"]+=a
        dict["reste"]=dict["montant_tot"]-dict["montant_paye"]
        with open(fichier) as f:
            l=json.load(f)
        for i in range(len(l)):
            if( l[i]['CIN'] == m ):
                    j=i
                    break
        l[j]=dict
        with open(fichier,'w') as f:
            json.dump(l,f)
        print(" ++++++++++++++++++++++  le montant reste à payé est rénouvoulé +++++++++")
        print("<<<<<<<<<<<<                       Modification Terimnée                                   >>>>>>>>>>>>")
        ajout= " "
        while( ajout.isnumeric()== False or( ajout != '1' and ajout != '0' )):    
            ajout=input("Voulez vous modifier un autre véhicule : (0/1)")    
        ajout=int(ajout)
# ---------------------------------------
def planifier_seance_code():
    fichier="fichier1.json"
    ajout=1
    while ajout==1:
        os.system("cls")
        print("-----------------------------------   Planification__des_seances_codes :  ------------------------------------------------")
        print("IL faut choisir le numéro CIN de la condidat  qui vous voulez ajouter une seance de code  : ")
        affichage_condidat()
        m=" "
        while( test3(m,fichier)== False ):
            print(" Merci de donner un numéro CIN de condidat valide parmi votre liste : ")
            m =input(' % - le numéro CIN de condidat qui vous vouler  modifier :      ')
        m=int(m)   
        dict = selectionner(m,fichier)
        print("-------------------------------------------------------------------------")
        print(dict)
        if (dict["categorie"]=="A"): a =15 +15*0.02
        elif (dict["categorie"]=="B"): a =15 +15*0.03
        elif (dict["categorie"]=="C"): a =15 +15*0.05
        dict["montant_tot"]=dict["montant_tot"]+a
        with open(fichier) as f:
            aliste=json.load(f)       
        j=0
        for i in range(len(aliste)):
            if( aliste[i]['CIN'] == m ):
                j=i
                break
        aliste[j]=dict
        with open(fichier,'w') as f:
            json.dump(aliste,f)
        f.close()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Planifier une seance de code :  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        d=ajout_seance_code()
        dict["Tableau_num_seance_code"].append(d["Num"])
        ajout=" "
        while( ajout.isnumeric()== False or( ajout != '1' and ajout != '0' )):    
            ajout=input("Voulez vous ajouter  une autre séance (0/1) :  ")    
        ajout=int(ajout)
#-------------------------------
def planifier_seance_conduit():
    fichier="fichier1.json"
    ajout=1
    while ajout==1:
        os.system("cls")
        print("-----------------------------------   Planification__des_seances_conduit :  ------------------------------------------------")
        print("IL faut choisir le numéro CIN de la condidat  qui vous voulez ajouter une seance de conduit  : ")
        affichage_condidat()
        m=" "
        while( test3(m,fichier)== False ):
            print(" Merci de donner un numéro CIN de condidat valide parmi votre liste : ")
            m =input(' % - le numéro CIN de condidat qui vous vouler  modifier :      ')
        m=int(m)   
        dict = selectionner(m,fichier)
        print("-------------------------------------------------------------------------")
        print(dict)
        if (dict["categorie"]=="A"): a =15 +15*0.04
        elif (dict["categorie"]=="B"): a =15 +15*0.06
        elif (dict["categorie"]=="C"): a =15 +15*0.08
        dict["montant_tot"]=dict["montant_tot"]+a
        with open(fichier) as f:
            aliste=json.load(f)       
        j=0
        for i in range(len(aliste)):
            if( aliste[i]['CIN'] == m ):
                j=i
                break
        aliste[j]=dict
        with open(fichier,'w') as f:
            json.dump(aliste,f)
        f.close()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Planifier une seance de conduit :  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        d=ajout_seance_conduite()
        dict["Tableau_num_seance_conduit"].append(d["Num"])
        ajout=" "
        while( ajout.isnumeric()== False or( ajout != '1' and ajout != '0' )):    
            ajout=input("Voulez vous ajouter  une autre séance (0/1) :  ")    
        ajout=int(ajout)
#-------------------------------
def supprimer_condidat():
    fichier="fichier1.json"
    ajout=1
    while ajout==1:
        os.system("cls")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Supprimer un séance de conduite :  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("IL faut choisir le numéro CIN de la condidat  qui vous vouler Suprimer : ")
        affichage_condidat()
        m=" "
        while( test3(m,fichier)== False ):
            print("Merci de donner un numéro CIN de condidat valide parmi votre liste : ")
            m =input(' % -  le numéro CIN de condidat qui vous vouler supprimer :      ')
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
                if( l[i]['CIN'] == m ):
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
#-----------------------------    
def Recherche_Visualiser_condidat():
    fichier="fichier1.json"
    ajout=1
    while ajout==1:
        os.system("cls")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Rechercher et Visualiser un condidat :  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("IL faut choisir le numéro CIN de la condidat  qui vous vouler Visualiser : ")
        affichage_condidat()
        m=" "
        while( test3(m,fichier)== False ):
            print("Merci de donner un numéro CIN de condidat valide parmi votre liste : ")
            m =input(' % -  le numéro CIN de condidat :      ')
        m=int(m)   
        os.system("cls")        
        dict = selectionner(m,fichier)
        print("////////////////////////////////////////////////")
        print(dict)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Details :   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Nom  :", dict["nom"])
        print("Permis Catégorie :",dict["categorie"])
        print("Le nombre des seances de code qu'il a fait :",len(dict["Tableau_num_seance_code"]))
        print("Le nombre des seances de code qu'il a fait :",len(dict["Tableau_num_seance_conduit"]))
        print("Montant totale à payer ",dict["montant_tot"])
        print("Reste à  payeé ",dict["reste"])
        print("----------------------------------------------------------------------------------------------")
        ajout=" "
        while( ajout.isnumeric()== False or( ajout != '1' and ajout != '0' )):    
            ajout=input("Voulez vous visualiser  un autre condidat (0/1) :  ")    
        ajout=int(ajout)