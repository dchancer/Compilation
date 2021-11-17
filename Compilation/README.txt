README 

Pour lancer le programme : 
Tout d'abord, si le programme n'est pas lancé 
correctement (avec les bons arguments), un "Usage : ..."
sera affiché à l'utilisateur.

Notre programme attend donc un lancement de ce type :
python compilateur.py fichierATester.* fichierCodesourceGenere.*

Ensuite, pour executer le code source généré, il suffit de faire cette commande :
./msm (-d) fichierCodesourceGenere.* 

Le fichierATester.* peut être placé n'importe où sur votre ordianteur, 
s'il n'est pas dans le dossier où se trouve compilateur.py il faudra écrire le path complet.

De même, le fichierCodesourceGenere.* est par défaut placé au même endroit que compilateur.py.
Vous pouvez définir l'endroit de sauvegarde de ce fichier en écrivant le path complet.


IMPORTANT:
Nos fichiers de tests sont dans le dossier Tests qui se situe au même endroit que compilateur.py,
un exemple de ligne de cmd a effectué est donc:
#python compilateur.py Tests/test_fonctions_appels.c codeSource.txt
#./msm codeSource.txt

Merci de votre lecture, 
Claire Bauchu et Damien Chancerel