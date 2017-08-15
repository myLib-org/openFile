Informations générales openFile
===============================

   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Projet:             openFile
   :dépôt GitHub:       https://github.com/poltergeist42-myLib/openFile
   :documentation:      https://poltergeist42-mylib.github.io/openFile/
   :Licence:            CC BY-NC-SA 4.0
   :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/ 

------------------------------------------------------------------------------------------

Déscription
===========

openFile.py permet créer et centraliser les données nécessaires à l'ouverture d'un 
fichier, comme le nom, l'extension, le chemin ou le mode de traitemant. Ce module permet
également de travailler avec le format JSON.

Arborescence du projet
======================

Pour aider à la compréhension de mon organisation, voici un bref déscrptif de 
l'arborescence de se projet. Cette arborescence est à reproduire si vous récupérez ce 
dépôt depuis GitHub. ::

    openFile                 # Dossier racine du projet (non versionner)
    |
    +--project              # (branch master) contient l'ensemble du projet en lui même
    |   |
    |   +--_1_userDoc       # Contien toute la documentation relative au projet
    |   |   |
    |   |   \--source       # Dossier réunissant les sources utilisées par Sphinx
    |   |
    |   \--_3_software      # Contien toute la partie programmation du projet
    |
    \--webDoc               # Dossier racine de la documentation qui doit être publiée
        |
        \--html             # (branch gh-pages) C'est dans se dosier que Sphinx vat 
                            # générer la documentation à publié sur internet