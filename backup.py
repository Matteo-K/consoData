#importation de la bibliothÃ¨que folium pour la carte
import folium
import pandas as pd
import json
#importation de la bibliothÃ¨que matplotlib pour les graphiques
import matplotlib.pyplot as plt
import numpy as np
#importation de la bibliothÃ¨que MySQL pour la database
import requests
import mysql.connector
from mysql.connector import errorcode

# CaractÃ©ristiques de la connection
database    = 'projet3-phyton_sql'
host_ip     = '127.0.0.1'
utilisateur = 'root'
password    = ''

#####################
# CONNECTION à la BDD
#####################
try:   
  conn = mysql.connector.connect(
      user = utilisateur, 
      password = password,
      host = host_ip,
      database = database)

#################################
# la connection à la BDD a échoué   
#################################
except mysql.connector.Error as err:    

    # Si Erreur de nom d'utilisateur ou de mot de passe
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Votre nom d'utilisateur ou votre mot de passe ne correspond pas !")

    # Si Erreur de nom de base de donnÃ©es
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de données",database,"n'existe pas")
    # Si autre Erreur
    else:
        print(err)

#################################
# La connection à  la BDD a réussi 
#################################
else:         
    print("vous êtes connecté à la base", conn._database)

##################################################################  
# On créé un curseur MySQL qui contient le rÃ©sultat de la requête
##################################################################
    curseur = conn.cursor(buffered=True)


def close_data():
    curseur.close()  # fermeture du curseur
    conn.close()     # fermeture du connection

def affichage():
    graphique_Prix_gaz()
    graphique_Consomation_Gaz ()


def Conso_gaz_Asie():
    '''
    cherche dans la table conso_gaz_monde la consomation
    de l'europe par an
    Returns
    -------
    L : une liste contenant la consomation de gaz par an en europe
    '''
    #Il faudrait mettre L sous forme d'un dictionnaire
    Liste = []
    requete=("SELECT consommation_gm3_an, pays,annee FROM conso_gaz_monde WHERE pays='Asie Pacifique' ORDER BY annee;")
    resultat = curseur.execute(requete)
    for (consommation_gm3_an, pays, annee) in curseur:
        M = []
        M.append(int(annee))
        M.append(float(consommation_gm3_an))
        Liste.append(M)
    return Liste
    
def Conso_gaz_US():
    '''
    cherche dans la table conso_gaz_monde la consomation
    de l'europe par an
    Returns
    -------
    L : une liste contenant la consomation de gaz par an en europe
    '''
    #Il faudrait mettre L sous forme d'un dictionnaire
    Liste = []
    requete=("SELECT consommation_gm3_an, pays,annee FROM conso_gaz_monde WHERE country='North America' ORDER BY annee;")
    resultat = curseur.execute(requete)
    for (consommation_gm3_an, pays, annee) in curseur:
        M = []
        M.append(int(annee))
        M.append(float(consommation_gm3_an))
        Liste.append(M)
    return Liste
    
def Conso_Gaz_EU():
    '''
    cherche dans la table conso_gaz_monde la consomation
    de l'europe par an
    Returns
    -------
    L : une liste contenant la consomation de gaz par an en europe
    '''
    #Il faudrait mettre L sous forme d'un dictionnaire
    Liste = []
    requete=("SELECT consommation_gm3_an, pays,annee FROM conso_gaz_monde WHERE pays='Europe' ORDER BY annee;")
    resultat = curseur.execute(requete)
    for (consommation_gm3_an, pays, annee) in curseur:
        M = []
        M.append(int(annee))
        M.append(float(consommation_gm3_an))
        Liste.append(M)
    return Liste

def Evo_Prix_Gaz_EU():
    '''
    cherche dans la table conso_gaz_monde la consomation
    de l'europe par an
    Returns
    -------
    L : une liste contenant la consomation de gaz par an en europe
    '''
    #Il faudrait mettre L sous forme d'un dictionnaire
    Liste = []
    requete=("SELECT date,europe_nbp FROM evo_prix_gaz_monde ORDER BY date;")
    resultat = curseur.execute(requete)
    for (date, europe_nbp) in curseur:
        M = []
        M.append(date)
        M.append(float(europe_nbp))
        Liste.append(M)
    return Liste

def Evo_Prix_Gaz_Japon():
    '''
    cherche dans la table conso_gaz_monde la consomation
    de l'europe par an
    Returns
    -------
    L : une liste contenant la consomation de gaz par an en europe
    '''
    #Il faudrait mettre L sous forme d'un dictionnaire
    Liste = []
    requete=("SELECT date,japon_gnl FROM evo_prix_gaz_monde ORDER BY date;")
    resultat = curseur.execute(requete)
    for (date, japon_gnl) in curseur:
        M = []
        M.append(date)
        M.append(float(japon_gnl))
        Liste.append(M)
    return Liste

def Evo_Prix_Gaz_Etats_Unis():
    '''
    cherche dans la table conso_gaz_monde la consomation
    des états unis par an
    Returns
    -------
    L : une liste contenant la consomation de gaz par an aux Ã©tats unis
    '''
    #Il faudrait mettre L sous forme d'un dictionnaire
    Liste = []
    requete=("SELECT date,etats_unis_henry_hub FROM evo_prix_gaz_monde ORDER BY date;")
    resultat = curseur.execute(requete)
    for (date, etats_unis_henry_hub) in curseur:
        M = []
        M.append(date)
        M.append(float(etats_unis_henry_hub))
        Liste.append(M)
    return Liste

def graphique_Consomation_Gaz ():
    """
    Fais un graphique avec les fonctions Conso_Gaz_EU(), Conso_gaz_Asie() et Conso_gaz_US()
    Enregistrer dans les listes L_Europe, L_Asie et L_US
    Returns
    -------
    Renvoie un graphique montrant l'évolution de la consomation du gaz

    """
    
    L_Europe, L_Asie,L_US, Europe, Asie, US, Date = Conso_Gaz_EU(), Conso_gaz_Asie(),Conso_gaz_US(), [], [], [], []
    
    if len(L_Europe) == len(L_Asie) and len(L_Europe) == len(L_US):
        
        for i in range (len(L_Europe)):
            Date.append((L_Europe[i][0]))
            Europe.append(L_Europe[i][1])
            Asie.append(L_Asie[i][1])
            US.append(L_US[i][1])
        
        plt.rc('lines', linewidth=2.5)
        fig, ax = plt.subplots()
        
        line1, = ax.plot(Date, Europe, label="l'Europe")
        
        line2, = ax.plot(Date, Asie, label="l'Asie")
        
        line3, = ax.plot(Date, US, label="Les Etats Unis")
        
        plt.title('évolution de la consommation du gaz en gm3 par an selon les endroits')
        ax.legend(handlelength=2)
        plt.savefig("évolution de la consommation du gaz par an selon les endroits.png", 
                    dpi=300, bbox_inches='tight',facecolor='grey')
    else :
        print("Le nombre de valeur dans chaque liste n'est pas identique")

def graphique_Prix_gaz():
    
    Prix_gaz_EU, Prix_gaz_Japon, Prix_Gaz_US, Prix_EU, Prix_Japon, Prix_US = Evo_Prix_Gaz_EU(), Evo_Prix_Gaz_Japon(), Evo_Prix_Gaz_Etats_Unis(), [], [], []
    #modifier le programme sql pour que les dates correspondent aux autres dates des diffÃ©rents lieux
    for i in range (10):
        Prix_EU.append(Prix_gaz_EU[i][1])
        Prix_Japon.append(Prix_gaz_Japon[i][1])
        Prix_US.append(Prix_Gaz_US[i][1])
        
    if len(Prix_EU) == len(Prix_Japon) and len(Prix_EU) == len(Prix_US):
        
        #il faut changer la valeur de x pour quelle corresponde au mois
        #x = Date_EU
        x = np.arange(len(Prix_EU))
        
        plt.step(x, Prix_EU, label='Europe en nbp')
        plt.plot(x, Prix_EU, 'o--', color='grey', alpha=0.8)
        
        plt.step(x, Prix_Japon, label='Japon en gnl')
        plt.plot(x, Prix_Japon, 'o--', color='grey', alpha=0.8)
    
        plt.step(x, Prix_US, label='Etat Unis en henry_hub')
        plt.plot(x, Prix_US, 'o--', color='grey', alpha=0.8)
    
        plt.grid(axis='x', color='0.95')
        plt.legend(title='Prix du gaz :')
        plt.title('évolution du prix du gaz par an selon les endroits')
        plt.savefig("évolution du prix du gaz par an selon les endroits.png", 
                    dpi=300, bbox_inches='tight',facecolor='grey')
        
    else :
        print("Le nombre de valeur dans chaque liste n'est pas identique")

#https://youtu.be/rWtvyCXqJOw
#lien pour le HTML

"""
modification à apporté :
.RÃ©diger tout les commentaires des fonctions
.Rendre le Programme lisible
- graphique_Prix_gaz():
.changer le x pour qu'il correspond au date des prix
.Enregistrer le graphique en une image pour l'importer + facilement
dans le programme HTML
- graphique_Consomation_Gaz():
.Ajouter les valeurs des états-unis
.Enregistrer le graphique en une image pour l'importer + facilement
dans le programme HTML
.Ligne 192
"""


"""
SELECT COUNT(date) FROM evo_prix_gaz_monde 
where date LIKE '2020%'
SELECT SUM(europe_nbp) FROM evo_prix_gaz_monde
where date LIKE '2020%'
SELECT SUM(japon_gnl) FROM evo_prix_gaz_monde
where date LIKE '2020%'
SELECT SUM(etats_unis_henry_hub) FROM evo_prix_gaz_monde
where date LIKE '2020%'
"""

SELECT COUNT(date) FROM evo_prix_gaz_monde 
where date LIKE f'{a}%'
a + '%'


