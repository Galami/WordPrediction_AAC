# WordPrediction_AAC
Configuration et évaluation d'un système de prédiction de mots au sein d'un logiciel de Communication Améliorée et Alternative (CAA) pour personnes handicapées : Étude de Presage et ACAT

A-Xml : fichier (français) d'abréviations adapté et utilisé dans ACAT

B-Training_corpus : ressources (français) .vocab/.arpa // .db // .txt  créées pour trois des prédicteurs de Presage (NB : le corpus Google Books Ngram n'est pas disponible sur ce repository en raison de la taille des fichiers)

C-Test_corpus : données de test (français) .txt pour l'évaluation par simulateur et le test utilisateur 

D-Scripts : code source pour traiter les différents corpus ou évaluer Presage

E-Logs : fichiers .txt obtenus avec presage_simulator.exe et traités avec presage_simulator_2.py

F-Docs : divers fichiers, dont un dossier intitulé Ggbooks reprenant les fichiers d'uni/bi/trigrammes (français) .csv qui ont été transférés dans les bases de données (chaque fichier a été limité à 1 000 000 de n-grams en raison de la taille des fichiers), images ou relatifs au test utilisateur (avec l'accord du participant de l'étude, le premier enregistrement audiovisuel n'est pas disponible en raison de la taille du fichier)


Presage : Vescovi, GNU General Public License version 2.0 (http://presage.sourceforge.net/)

ACAT : Intel Corporation, Apache License version 2.0 (https://01.org/acat / https://github.com/intel/acat)
