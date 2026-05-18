import matplotlib.pyplot as plt

def transforme_2_colonne_en_2_liste(fichier:str)->list:
    
    liste_frequences=[]
    liste_niveaux=[]
    with open(fichier, "r", encoding="utf-8") as f:
        
        for morceau in f:
            ligne=(morceau.split())
            frequence=ligne[0]
            niveau=ligne[1]
            try:
                niveau=niveau.replace(",",".")
                frequence=frequence.replace(",",".")
                niveau=float(niveau)
                frequence=float(frequence)
            except:
                None
            liste_frequences.append(frequence)
            liste_niveaux.append(niveau)
    #print(liste_frequences, liste_niveaux)
    return liste_frequences, liste_niveaux

    liste_normalise=[]
    donnee_maximum=max(liste)
    for donnee in liste:
        donnée_normalise= donnee/donnee_maximum
        liste_normalise.append(donnée_normalise)
    return liste_normalise 

def trouver_autour(valeur, liste):
    bas = None
    haut = None 
    for x in liste:
        if x <= valeur:
            bas = x
        elif x > valeur and haut is None:
            haut = x
            break
    return bas, haut

def trouve_decibel(valeur:float,liste_frequence:list,liste_niveau:list)->float:
    f=valeur
    bornes=trouver_autour(f,liste_frequence)
    f_1=bornes[0]
    f_2=bornes[1]
    try:
        index_d_1=liste_frequence.index(f_1)
        index_d_2=liste_frequence.index(f_2)
        d_1= liste_niveau[index_d_1]
        d_2= liste_niveau[index_d_2]
        d=((d_2-d_1)/(f_2-f_1)*(f-f_1))+d_1
        return d
    except:
        None

def soustraction_original_moins_synt(o_frequences,o_niveaux,s_frequences,s_niveaux)-> list:
    liste_finale=[]
    for i in range(0,len(o_frequences)-1):
        try:
            o_niveau=o_niveaux[i]
            o_frequence=o_frequences[i]
            s_niveau=trouve_decibel(o_frequence,s_frequences,s_niveaux)
            difference=o_niveau-s_niveau
            liste_finale.append(difference)
            
        except:
            print("il y a un problème à la ",i, "ieme ittération")
    #print(i)
    return liste_finale

def gros_programme_incroyable_qui_fait_tout(fichier_original:str,fichier_synt:str):
    "Gros chose"
    original=transforme_2_colonne_en_2_liste(fichier_original)
    synt=transforme_2_colonne_en_2_liste(fichier_synt)
    o_frequences=original[0]
    o_niveaux=original[1]
    s_frequences=synt[0]
    s_niveaux=synt[1]
    grande_liste= soustraction_original_moins_synt(o_frequences,o_niveaux,s_frequences,s_niveaux)
    y=grande_liste
    x=o_frequences 
    #plt.plot(o_frequences,o_niveaux,label="son original",color="blue",alpha=1)
    #plt.plot(s_frequences,s_niveaux,label="son synthétisé",alpha=0.4,color="darkorange")
    o_frequences.remove(o_frequences[-1])
    plt.plot(x,y,label="différence de volume",alpha=0.8,color="purple")
    plt.axhline(0, linestyle=":", alpha=1,color="black")
    plt.xlim(10,3000)
    plt.legend(fontsize=20)
    plt.xlabel("fréquence [Hz]",fontsize=15)
    plt.ylabel("diff deVolume [dB]",fontsize=15)
    plt.title("différence de volume pour chaque fréquence",fontsize=20)
    plt.minorticks_on()
    plt.grid(alpha=0.05)
    plt.show()










#directive d'utilisation:
# prendre les fichiers original et synthétisé, faits par Audacity
#IMPORTANT!!! 
#!Enlever les titres dans les fichiers txt, pour qu'il ne reste seulement que les chiffres!
# utiliser "gros_programme_incroyable_qui_fait_tout" avec le nom des deux fichiers.
#pour modifier les graphiques, modifier à la fin de la fonction gros_programme_incroyable_qui_fait_tout

gros_programme_incroyable_qui_fait_tout("spectre_son_original.txt","spectresansnoise.txt")