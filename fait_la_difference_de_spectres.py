import matplotlib.pyplot as plt
import numpy as np
import statistics as st

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
   


original=transforme_2_colonne_en_2_liste("spectre_son_original.txt")
#print(original)
o_frequences=original[0]
o_niveaux=original[1]
#synt=transforme_2_colonne_en_2_liste("spectre_synt_v1.txt")
synt=transforme_2_colonne_en_2_liste("spectresansnoise.txt")
s_frequences=synt[0]
s_niveaux=synt[1]
#print(o_frequences)
#d=trouve_decibel(2,o_frequences,o_niveaux)
#print(d)
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



grande_liste= soustraction_original_moins_synt(o_frequences,o_niveaux,s_frequences,s_niveaux) 

#print(len(grande_liste), "niveau")   
#print(len(o_frequences),"frequence")

#print(len(o_frequences))
#print(len(o_niveaux))
y=grande_liste
x=o_frequences
#print(y)
#plt.plot(o_frequences,o_niveaux)
#plt.plot(s_frequences,s_niveaux)
o_frequences.remove(o_frequences[-1])
#plt.plot(x,y)
#plt.xlim(20,2000)

#plt.show()
classes=[]
for i in range (1,18):
    valeurs=[]
    for j in range (60*(i-1),60*i):
        valeurs.append(y[j])
    classes.append(valeurs)
#print(classes)
moyennes=[]
for classe in classes:
    moyenne=st.mean(classe)
    moyennes.append(moyenne)
#print(moyennes)
i=0
liste_de_bornes=[]
while True:
    try:
        borne_inferieur=x[60*i]
        borne_superieur=x[(60*(i+1))-1]
        bornes=f"[{borne_inferieur:.0f};{borne_superieur:.0f}]"
        #print(bornes)
        liste_de_bornes.append(bornes)
        i+=1
    except:
        break

v2_liste_borne=[]
for k in range(0,15):
    v2_borne_inferieur=k*200
    v2_borne_superieur=(k+1)*200
    v2_bornes=f"[{v2_borne_inferieur:.0f};{v2_borne_superieur:.0f}]"
    v2_liste_borne.append(v2_bornes)
#print(v2_liste_borne)
#print(o_frequences)

v2_classes=[]
for i in range(0,15):
    valeur_min=200*i
    valeur_max=200*(i+1)
    v2_valeurs=[]
    for j in x:
        if j>=valeur_min and j<=valeur_max:
            index=x.index(j)
            v2_valeurs.append(y[index])
        elif j > valeur_max:
            break
    v2_classes.append(v2_valeurs)
#print((v2_classes[14]))

v2_moyennes=[]
for classe in v2_classes:
    moyenne=st.mean(classe)
    v2_moyennes.append(moyenne)
#print(v2_moyennes)  
incertitudes=[]
for chose in v2_classes:
    incertitude= np.std(chose)
    incertitudes.append(incertitude)
    #print(incertitude)
    





#print(liste_de_bornes)
plt.plot(v2_liste_borne,v2_moyennes,marker="o",markersize=10,color="limegreen",alpha=1)
plt.axhline(0, linestyle=":", alpha=1,color="black")
plt.tick_params(axis='both', which='major', labelsize=7)
plt.grid(axis="x",alpha=0.2)
plt.xlabel("Intervalle de fréquence [Hz]",fontsize=15)
plt.title("Différence de volume moyenne entre le son original et le son synthétique selon l'intervalle de fréquence",fontsize=20)
plt.ylabel("Différence de volume moyenne [dB]",fontsize=15)
plt.annotate("Différence positive",xy=(1.5,3),size=13)
plt.annotate("Différence négative",xy=(7.5,-2.5),size=13)
plt.annotate("Différence positive",xy=(11.5,3),size=13)
plt.errorbar(v2_liste_borne,v2_moyennes,yerr=incertitudes,ecolor="deepskyblue",alpha=0.3, linewidth=1, capsize=5,label= "Barres d'erreur")
plt.fill_between(v2_liste_borne,0,v2_moyennes,hatch="///",facecolor="none",alpha=0.1,edgecolor="gray")
plt.margins(x=0.02)
plt.legend(loc='lower right',fontsize=15)
plt.show()
    




