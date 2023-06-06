from menus import*
from fonctions_condidats import*
from fonctionsseances import*
from fonctions_vehicules import*
import os
import fonctions_condidats
import fonctionsseances
import fonctions_vehicules

choix = 1
while(choix != 0  ):
    os.system("cls") 
    menu1()
    choix=" "
    choix2= 5
    while(choix.isnumeric()== False or (choix != "1" and choix != "2" and choix != "3" and choix != "0"  )):
        choix=input("Votre choix  :                     ")
    choix=int(choix)
    if(choix == 1 ):
        choix2 = 1
        while(choix2 != 0 ):
            menu_condidats()
            choix2=" "
            while(choix2.isnumeric()== False  or (choix2 != "1" and choix2 != "2" and choix2 != "3" and choix2 != "4" and choix2 != "0"  )):
                choix2=input("Votre choix  :                     ")
            choix2=int(choix2)
            if(choix2 == 1 ): ajout_condidat()
            elif(choix2 == 2 ): modifier_condidat()
            elif(choix2 == 3 ): Recherche_Visualiser_condidat()
            elif(choix2 == 4 ): supprimer_condidat()
    if(choix == 2 ):
        choix2 = 1
        while(choix2 != 0 ):
            menu_vehicules()
            choix2=" "
            while(choix2.isnumeric()== False  or (choix2 != "1" and choix2 != "2" and choix2 != "3" and choix2 != "4" and choix2 != "0"  )):
                choix2=input("Votre choix  :                     ")
            choix2=int(choix2)
            if(choix2 == 1 ): ajout_vehicule()
            elif(choix2 == 2 ): modifier_vehicule()
            elif(choix2 == 3 ): Recherche_Visualiser_vehicule()
            elif(choix2 == 4 ): supprimer_vehicule()       
    if(choix == 3 ):
        choix2 = 1
        while(choix2 != 0 ):
            menu_séances()
            choix2=" "
            while(choix2 not in ['1','2','3','4','5','6','0']  ):
                choix2=input("Votre choix  :                     ")
            choix2=int(choix2)
            if(choix2 == 1 ): planifier_seance_code()
            elif(choix2 == 2 ): planifier_seance_conduit()
            elif(choix2 == 3 ): affichage_seances_code()
            elif(choix2 == 4 ): affichage_seances_conduite()
            elif(choix2 == 5 ): supprimer_séance_code()
            elif(choix2 == 6 ):supprimer_séance_conduite()