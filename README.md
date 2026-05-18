Les fichiers pythons nommées selon des notes produisent une série d'harmoniques en données brutes .WAV. Il suffit de les lire.
Les données brutes produites doivent être lu par un logiciel pouvant traités ces données et les traiter à 44100Hz.
Les fichiers .WAV sont les produits finis en empilant les fichiers de donnée brute ET en appliquant de l'EQ pour abaisser les
hautes fréquence. 
Les deux derniers fichiers .py servent à recevoir deux paires fréquence-volume .txt produites par Audacity en extrayant l'analyse
spectrale. Les spécifications pour faire fonctionner fait_les_spectres se trouvent dans le fichier.
Pour faire fonctionner fait_la_difference_de_spectres, il faut renommer les fichiers comme dans le .py précédant, mais les
lignes à réécrire sont les lignes 62 et 67
