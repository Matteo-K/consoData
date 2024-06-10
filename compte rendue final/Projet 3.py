#importation de la bibliothèque matplotlib pour les graphiques
import matplotlib.pyplot as plt
#importation de la biblioth�que MySQL pour la database
import mysql.connector
from mysql.connector import errorcode

# Caract�ristiques de la connection
database    = 'projet3-phyton_sql'
host_ip     = '127.0.0.1'
utilisateur = 'root'
password    = ''

#####################
# CONNECTION � la BDD
#####################
try:   
  conn = mysql.connector.connect(
      user = utilisateur, 
      password = password,
      host = host_ip,
      database = database)

#################################
# la connection �la BDD a �chou�   
#################################
except mysql.connector.Error as err:    

    # Si Erreur de nom d'utilisateur ou de mot de passe
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Votre nom d'utilisateur ou votre mot de passe ne correspond pas !")

    # Si Erreur de nom de base de données
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de donn�es",database,"n'existe pas")
    # Si autre Erreur
    else:
        print(err)

#################################
# La connection � la BDD a r�ussi 
#################################
else:         
    print("vous �tes connect� �la base", conn._database)

##################################################################  
# On cr�� un curseur MySQL qui contient le résultat de la requ�te
##################################################################
    curseur = conn.cursor(buffered=True)


def close_data():
    curseur.close()  # fermeture du curseur
    conn.close()     # fermeture du connection

def affichage():
    """
    demande a l'utilisateur l'ann�e voulu pour la fonction graphique_Prix_gaz
    affiche les deux graphiques
    """
    a = input("A quel ann�e voulez-vous voir l'�voulution du prix du gaz. ex : 2020")
    graphique_Prix_gaz(a)
    graphique_Consomation_Gaz ()


def Conso_gaz_Asie():
    '''
    cherche dans la table conso_gaz_monde la consomation
    en Asie par ans
    Returns
    -------
    L : une liste contenant la consomation de gaz par ans en Asie
    '''
    #Il faudrait mettre L sous forme d'un dictionnaire
    Liste = []
    requete=("SELECT consommation_gm3_an, pays,annee FROM conso_gaz_monde WHERE pays='Asie Pacifique' ORDER BY annee;")
    curseur.execute(requete)
    for (consommation_gm3_an, pays, annee) in curseur:
        M = []
        M.append(int(annee))
        M.append(float(consommation_gm3_an))
        Liste.append(M)
    return Liste
    
def Conso_gaz_US():
    '''
    cherche dans la table conso_gaz_monde la consomation
    des �tats unis par ans
    Returns
    -------
    L : une liste contenant la consomation de gaz par ans des �tats
    '''
    #Il faudrait mettre L sous forme d'un dictionnaire
    Liste = []
    requete=("SELECT consommation_gm3_an, pays,annee FROM conso_gaz_monde WHERE country='North America' ORDER BY annee;")
    curseur.execute(requete)
    for (consommation_gm3_an, pays, annee) in curseur:
        M = []
        M.append(int(annee))
        M.append(float(consommation_gm3_an))
        Liste.append(M)
    return Liste
    
def Conso_Gaz_EU():
    '''
    cherche dans la table conso_gaz_monde la consomation
    de l'europe par ans
    Returns
    -------
    L : une liste contenant la consomation de gaz par ans en europe
    '''
    #Il faudrait mettre L sous forme d'un dictionnaire
    Liste = []
    requete=("SELECT consommation_gm3_an, pays,annee FROM conso_gaz_monde WHERE pays='Europe' ORDER BY annee;")
    curseur.execute(requete)
    for (consommation_gm3_an, pays, annee) in curseur:
        M = []
        M.append(int(annee))
        M.append(float(consommation_gm3_an))
        Liste.append(M)
    return Liste

def Evo_Prix_Gaz_EU():
    '''
    cherche dans la table conso_gaz_monde la consomation
    de l'europe par ans
    Returns
    -------
    L : une liste contenant la consomation de gaz par ans en europe
    '''
    Liste = []
    requete=("SELECT date,europe_nbp FROM evo_prix_gaz_monde ORDER BY date;")
    curseur.execute(requete)
    for (date, europe_nbp) in curseur:
        M = []
        M.append(date)
        M.append(float(europe_nbp))
        Liste.append(M)
    return Liste

def Evo_Prix_Gaz_Japon():
    '''
    cherche dans la table conso_gaz_monde la consomation
    de l'europe par ans
    Returns
    -------
    L : une liste contenant la consomation de gaz par ans au japon
    '''
    Liste = []
    requete=("SELECT date,japon_gnl FROM evo_prix_gaz_monde ORDER BY date;")
    curseur.execute(requete)
    for (date, japon_gnl) in curseur:
        M = []
        M.append(date)
        M.append(float(japon_gnl))
        Liste.append(M)
    return Liste

def Evo_Prix_Gaz_Etats_Unis():
    '''
    cherche dans la table conso_gaz_monde la consomation
    des �tats unis par ans
    -------
    L : une liste contenant la consomation de gaz par ans aux �tats unis
    '''
    Liste = []
    requete=("SELECT date,etats_unis_henry_hub FROM evo_prix_gaz_monde ORDER BY date;")
    curseur.execute(requete)
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
    -------
    Renvoie un graphique montrant l'�volution de la consomation du gaz
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
        
        plt.title('�volution de la consommation du gaz en gm3\n par an selon les pays �mergents')
        ax.legend(handlelength=2)
        plt.savefig("�volution de la consommation du gaz par an selon les endroits.png", 
                    dpi=300, bbox_inches='tight',facecolor='grey')
    else :
        print("Le nombre de valeur dans chaque liste n'est pas identique")

def graphique_Prix_gaz(ann�e):
    """
    fonction qui g�n�re un graphique � partir de plusieurs donn�e
    Ce graphique montre l'�volution du prix du gaz sur l'ann�e choisie
    a repr�sente l'ann�e choisi
    -------
    retourne un graphique
    """
    Prix_gaz_EU, Prix_gaz_Japon, Prix_Gaz_US, Prix_EU, Prix_Japon, Prix_US, date = Evo_Prix_Gaz_EU(), Evo_Prix_Gaz_Japon(), Evo_Prix_Gaz_Etats_Unis(), [], [], [], []
    #on attribut les donn�e a leurs attributs
    mois = ["01","02","03","04","05","05","06","07","08","09","10","11","12"] #mois est une liste repr�sentent tout les mois sur un an
    if len(Prix_gaz_EU) >= len(Prix_gaz_Japon) and len(Prix_gaz_EU) >= len(Prix_Gaz_US):
        longueur, Date = len(Prix_gaz_EU), Prix_gaz_EU
    elif len(Prix_gaz_Japon) >= len(Prix_gaz_EU) and len(Prix_gaz_Japon) >= len(Prix_Gaz_US):
        longueur, Date = len(Prix_gaz_Japon), Prix_gaz_Japon
    elif len(Prix_Gaz_US) >= len(Prix_gaz_EU) and len(Prix_Gaz_US) >= len(Prix_gaz_Japon):
        longueur, Date = len(Prix_Gaz_US), Prix_Gaz_US
    #on d�termine le nombre de valeur a rentr� sur le graphique en comparent la longueur des listes des autres pays

    for i in range (longueur):
        stop = 0    #condition pour arr�ter la boucle
        if Date[i][0].startswith(str(ann�e)) == True: #lance une condition si l'ann�e de la liste Date est la m�me que celle de ann�e
            Prix_EU.append(Prix_gaz_EU[i][1])   #le programme fait des liste des donn�e correspondant au mois s�lectionner
            Prix_Japon.append(Prix_gaz_Japon[i][1])
            Prix_US.append(Prix_Gaz_US[i][1])
            for j in mois:
                if stop == 1: #condition pour arr�ter la boucle
                    pass
                else :
                    if Date[i][0].startswith(j,5) == True : #lance une condition si le mois de la liste mois est la m�me que celle de Date
                        date.append(j)  #ajoute le mois � la liste date
                        stop += 1
                    else :
                        pass
        else :
            pass      
    x = date # x repr�sente l'axe des abcisses 
    
    #on fait les diff�rentes trac�s grace aux listes ci-dessus
    plt.step(x, Prix_EU, label='Europe en nbp')
    plt.plot(x, Prix_EU, 'o--', color='grey', alpha=0.3)
        
    plt.step(x, Prix_Japon, label='Japon en gnl')
    plt.plot(x, Prix_Japon, 'o--', color='grey', alpha=0.3)
    
    plt.step(x, Prix_US, label='Etat Unis en henry_hub')
    plt.plot(x, Prix_US, 'o--', color='grey', alpha=0.3)
    
    #entre les derni�re donn�e pour finir le graphique
    plt.grid(axis='x', color='0.85')
    plt.legend(title='Prix du gaz :')
    plt.title('�volution du prix du gaz en',ann�e)
    #enregistre le graphique
    plt.savefig("�volution du prix du gaz par an selon les endroits.png", 
                    dpi=300, bbox_inches='tight',facecolor='grey')
        
affichage()


