# WordPrediction_AAC
Configuration et évaluation d'un système de prédiction de mots au sein d'un logiciel de Communication Améliorée et Alternative (CAA) pour personnes handicapées : Étude de Presage et ACAT


Ce mémoire présente la configuration et l'évaluation d'un système de prédiction de mots ainsi que d'un logiciel de Communication Améliorée et Alternative (CAA) pour les personnes handicapées. En plus d'avoir une mobilité réduite, ces utilisateurs ont un usage de la parole plus ou moins altéré qui doit être compensé par une aide technologique proposant des modalités de saisie adaptées à leurs capacités. Afin d'accélérer leur vitesse de communication, différentes techniques de prédiction et de modélisation du langage sont utilisées. Ces approches sont étudiées par le biais de divers systèmes existants. Le paramétrage de prédicteurs statistiques est analysé, leur configuration en français étant évaluée par un simulateur et testée par une personne handicapée. Les résultats montrent qu'un modèle de langage lissé trigramme construit à partir d'un gros corpus littéraire comme Google Books Ngram permet d'économiser plus d'une saisie sur deux, les performances de ces systèmes variant en fonction de divers paramètres tels que les corpus, les prédicteurs (le nombre de n-grammes, le lissage, etc.), le nombre de prédictions lexicales à afficher et l'interface utilisateur.

This thesis investigates the configuration and evaluation of a word prediction system as well as an Augmentative and Alternative Communication (AAC) device for people with disabilities. In addition to having a reduced mobility, these users have a more or less altered use of speech that must be compensated by a technological aid offering input methods adapted to their capabilities. In order to improve their communication speed, different prediction and language modeling techniques are used. A large diversity of AAC systems are nowadays available, which use specifically one or several of these techniques. The parameterization of statistical predictors is investigated, their configuration in French being evaluated by a simulator and tested by a disabled person. The results show that a smoothed trigram language model built from a large literary corpus like Google Books Ngram saves more than one keystroke out of two, the performance of these systems varying according to various parameters such as corpus, prediction model (number of n-grams, smoothing, etc.), number of displayed lexical predictions and user interface.


A-Xml : fichiers d'abréviations françaises (Abbreviations.xml) et de configuration (PresageWordPredictorSettings.xml) adaptés et utilisés dans ACAT**, fichier de configuration (presage.xml) de Presage*, licences et images

B-Training_corpus : ressources françaises .vocab/.arpa // .db // .txt  créées pour trois des prédicteurs de Presage (NB : le corpus Google Books Ngram n'est pas disponible sur ce repository en raison de la taille des fichiers)

C-Test_corpus : données de test françaises .txt pour l'évaluation par simulateur et le test utilisateur 

D-Scripts : code source pour traiter les différents corpus ou évaluer Presage

E-Logs : fichiers .txt obtenus avec presage_simulator.exe et traités avec presage_simulator_2.py

F-Docs : divers fichiers, dont un dossier intitulé Ggbooks reprenant les fichiers français d'uni/bi/trigrammes .csv qui ont été transférés dans les bases de données (chaque fichier a été limité à 1 000 000 de n-grams en raison de la taille des fichiers), images ou relatifs au test utilisateur (avec l'accord du participant de l'étude, le premier enregistrement audiovisuel n'est pas disponible en raison de la taille du fichier)


Presage* : Vescovi, GNU General Public License version 2.0 (http://presage.sourceforge.net/)

ACAT** : Intel Corporation, Apache License version 2.0 (https://01.org/acat / https://github.com/intel/acat)
