Informations générales openFile
===============================

   :Auteur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Projet:             openFile
   :Dépôt_GitHub:       https://github.com/poltergeist42-myLib/openFile
   :Documentation:      https://poltergeist42-mylib.github.io/openFile/
   :Licence:            CC BY-NC-SA 4.0
   :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/ 

------------------------------------------------------------------------------------------

Description
===========

openFile.py permet créer et centraliser les données nécessaires à l'ouverture d'un 
fichier, comme le nom, l'extension, le chemin ou le mode de traitement. Ce module permet
également de travailler avec le format JSON.

------------------------------------------------------------------------------------------

Installation
============

 Depuis une invite de commande, ce placer dans le dossier "_3_software\openFile_pac" puis
 exécuter la commande setup : ::
 
    cd .\_3_software\openFile_pac
    python setup.py install
    
**N.B** : vous devez être Root / administrateur pour effectuer cette opération.

------------------------------------------------------------------------------------------

Arborescence du projet
======================

Pour aider à la compréhension de mon organisation, voici un bref déscrptif de 
l'arborescence de se projet. Cette arborescence est à reproduire si vous récupérez ce 
dépôt depuis GitHub. ::

    openFile                 # Dossier racine du projet (non versionner)
    |
    +--project              # (branch master) contient l'ensemble du projet en lui même
    |   |
    |   +--_1_userDoc       # Contiens toute la documentation relative au projet
    |   |   |
    |   |   \--source       # Dossier réunissant les sources utilisées par Sphinx
    |   |
    |   \--_3_software      # Contiens toute la partie programmation du projet
    |
    \--webDoc               # Dossier racine de la documentation qui doit être publiée
        |
        \--html             # (branch gh-pages) C'est dans se dossier que Sphinx va 
                            # générer la documentation à publié sur internet