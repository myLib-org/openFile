#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Infos
=====

   :Projet:             openFile
   :Nom du fichier:     openFile.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20170708

####

   :Licence:            CC-BY-NC-SA
   :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/

####

    :dev language:      Python 3.6
    :framework:         
    
####

Descriptif
==========

    :Projet:            
                        
    :Fichiers:          openFile.py permet créer et centraliser les données nécessaires
                        à l'ouverture d'un fichier, comme le nom, le chemin ou le mode
                        de traitemant. Ce module permet également de travailler avec
                        le format JSON.

####

lexique
=======

   :**v_**:                 variable
   :**l_**:                 list
   :**t_**:                 tuple
   :**d_**:                 dictionnaire
   :**f_**:                 fonction
   :**C_**:                 Class
   :**i_**:                 Instance
   :**m_**:                 Matrice
   
####

Référence Web
=============

    :JSON:   https://docs.python.org/3/library/json.html#basic-usage
    
####

"""
from __future__ import absolute_import
import os, sys
sys.path.insert(0,'..')         # ajouter le repertoire precedent au path (non définitif)
                                # pour pouvoir importer les modules et paquets parent
try :
    from devChk.devChk import C_DebugMsg
    v_dbgChk = True
    i_dbg = C_DebugMsg()
   
except ImportError :
    print( "module devChk non present" )
    v_dbgChk = False
    
import json
import argparse


class C_OpenFile( object ) :
    """ Class permettant le traitemant des fichiers et l'encapsulation des données
    """
    def __init__( self, v_fileName=None ) :
        """ **__init__()**
        
            Creation et initialisation des variables globales de cette Class
        """
        self._v_dir             = os.getcwd()
                                # os.getcwd() : permet de recuperer le chemin
                                # du repertoire local
        if v_fileName :
            self._v_fileName    = v_fileName
        else :
            self._v_fileName        = 'nouveau_fichier.txt'
            
        self._v_FQFN    = os.path.join(self._v_dir, self._v_fileName)
        
        if self._v_fileName[-4] == '.' :
            self._v_fileExt     = self._v_fileName[-4:]
        else :
            self._v_fileExt     = ''
            
        self._v_prefix          = ''
        self._v_suffix          = ''
            

####
        
    def __del__(self) :
        """ **__del__()**
        
            Permet de terminer proprement l'instance de la Class courante
        
            il faut utilise : ::
            
                del [nom_de_l'_instance]
                
            *N.B :* Si l'instance n'est plus utilisee, cette methode est appellee 
            automatiquement.
        """
        ## dbg
        v_dbg = 1
        v_dbg2 = 1
        f_dbg(v_dbg2, "__del__", self.__del__)
        
        ## Action
        v_className = self.__class__.__name__

        ## dbg
        f_dbg( v_dbg, v_className, v_tittle = False  )
        
####

    def f_setFilePath(self, v_localWorkDir=None) :
        """ Permet de définir le chemin dans lequel est créé le fichier. Ce chemin est
            utilisé comme repertoire de travail (workdir).
            
            - Si aucune valeur n'est passé à 'v_localWorkDir', le repertoire de travail
              restera le repertoire courant
            
            - Si un chemin absolu est passé à 'v_localWorkDir',ce dernier serat utiliser
              comme nouveau répertoire de travail (workdir)
        """
        ## dbg
        v_dbg = 1
        v_dbg2 = 1
        f_dbg(v_dbg2, "f_setFilePath", self.f_setFilePath)
        
        ## Action
        if v_localWorkDir :
            self._v_dir = os.path.normpath(v_localWorkDir)
            os.chdir(self._v_dir)
                # permet de déclarer '_v_dir' comme répertoire courrant
        else :
            if __name__ == '__main__':
                print   (
                        "Acun chemin n'a été spécifié. le chemin par défaut sera" / 
                        "utilisé : \n {}".format(self._v_dir)
                        )
                
####
                
    def f_getFilePath(self) :
        """ Retourne le chemin dans lequel est créer le fichier.
        
            **N.B** : Ce chemin correspond au répertoire de travail (workdir).
        """
        ## dbg
        v_dbg = 1
        v_dbg2 = 1
        f_dbg(v_dbg2, "f_getFilePath", self.f_getFilePath)
        
        ## Action
        return self._v_dir
        
####

    def f_setFileName(self, v_fileName=None) :
        """ Permet de définir le nom du fichier.
            **N.B** : Le format attendu est de type 'str'
            
            - Si aucune valeur n'est passée à 'v_fileName', le nom par défaut du fichier
              serat : 'nouveau_fichier.txt'
              
            - Si une valeur est passée à 'v_fileName', cette denière sera utiliser comme
              nom de fichier
        """
        ## dbg
        v_dbg = 1
        v_dbg2 = 1
        f_dbg(v_dbg2, "f_setFileName", self.f_setFileName)
        
        ## Action
        if not v_fileName :
            if __name__ == '__main__':
                print( "Le nom du fichier sera : {}".format(self._v_fileName))
        else :
            self._v_fileName = v_fileName
            if v_fileName[-4] == '.' :
                self.f_setFileExt( v_fileName[-4:] )

####

    def f_getFileName(self) :
        """ Retourne le nom du fichier.
        """
        return self._v_fileName
           
####

    def f_setPrefixFN(self, v_prefix, f_underscore=True) :
        """ Permet d'ajouter un préfix au nom actuel du fichier
        
            - La valeur de v_prefix serat ajouté avant le nom contenu dans '_v_fileName'.
              le nouveau nom sera enregistrer dans '_v_prefix'
              
            - Si 'f_underscore' est vrai (valeur par défaut), un underscore serat insérer
              entre le nom du fichier et son préfix
        """
        if f_underscore :
            self._v_prefix = "{}_{}".format( v_prefix, self._v_fileName )
        else :
            self._v_prefix = "{}{}".format( v_prefix, self._v_fileName )


####

    def f_getPrefixFN( self ) :
        """ Retourne le nom préfixé du fichier
        """
        return self._v_prefix
        
####

    def f_setSuffixFN(self, v_suffix, f_underscore=True) :
        """ Permet d'ajouter un suffixe au nom actuel du fichier
        
            - La valeur de v_suffix serat ajouté après le nom contenu dans '_v_fileName'.
              le nouveau nom sera enregistrer dans '_v_suffix'
              
            - Si 'f_underscore' est vrai (valeur par défaut), un underscore serat insérer
              entre le nom du fichier et son suffixe
        """
        if f_underscore :
            self._v_suffix = "{}_{}".format( self._v_fileName, v_suffix )
        else :
            self._v_suffix = "{}{}".format( self._v_fileName, v_suffix )

####

    def f_getSuffixFN( self ) :
        """ Retourne le nom suffixé du fichier
        """
        return self._v_suffix
        
####

    def f_setFileExt(self, v_fileExt ) :
        """ permet de modifier (ou d'ajouter) l'extention du fichier
            **N.B** : La valeur attendue est de type 'str'
            
            - Si le premier caractère de 'v_fileExt' est un point, on utilise
              directement cette valeur
              
            - Si le premier caractère de 'v_fileExt' n'est pas un point, on ajoute un
              point avant la valeur passée en argument
              
            - Si _v_fileName n'a pas d'extention, cette derniere sera ajouter au nom du
              fichier
              
            - Si _v_fileName a une extension qui ne correspond pas à _v_fileExt, 
              l'extension de _v_fileName sera modifiée
        """
        ## dbg
        v_dbg = 1
        v_dbg2 = 1
        f_dbg(v_dbg2, "f_setFileExt", self.f_setFileExt)
        
        ## Action
        if v_fileExt[0] == '.' :
            self._v_fileExt = v_fileExt
        else :
            self._v_fileExt = ".{}".format(v_fileExt)
            
        if self._v_fileName[-4] != '.' :
            self._v_fileName = "{}{}".format(self._v_fileName, self._v_fileExt)
        else :
            if self._v_fileName[-4:] != self._v_fileExt :
                self._v_fileName = "{}{}".format(self._v_fileName[:-4], self._v_fileExt)
      
####

    def f_getFileExt( self ) :
        """ Retourne l'extension du fichier
        """
        return self._v_fileExt

####      

    def f_setFQFN(self) :
        """ Permet de définir le fichier et son chemin (Fully Qualified File Name) sous la
            forme : ::
        
                [chemin_du_fichier]\[nom_du_fichier]
        """
        ## dbg
        v_dbg = 1
        v_dbg2 = 1
        f_dbg(v_dbg2, "f_setFQFN", self.f_setFQFN)
        
        ## Action
        self._v_FQFN = os.path.join(self._v_dir, self._v_fileName)
        
####
            
    def f_getFQFN(self) :
        """ Retourne le Nom du fichier précédé se son chemin (Fully Qualified File 
            Name). ::
                
                [chemin_du_fichier]\[nom_du_fichier]
        """
        ## dbg
        v_dbg = 1
        v_dbg2 = 1
        f_dbg(v_dbg2, "f_getFQFN", self.f_getFQFN)
        
        ## Action
        return self._v_FQFN

####

    def f_chkIfFile(self, v_file=None, v_path=None) :
        """ Retourne Vrai si le fichier existe et Faux si il n'éxiste pas.
        
            - Si aucun argument n'est passé à 'v_file', c'est la valeur de _v_fileName qui
              serat utilisé par défaut.
              
            - Si aucun chemin n'est passé à 'v_path', c'est dans le répertoire courant
              que la recherche serat effectuée.
        """
        ## dbg
        v_dbg = 1
        v_dbg2 = 1
        f_dbg(v_dbg2, "f_chkIfFile", self.f_chkIfFile)
        
        ## Action
        if not v_file :
            v_file = self._v_fileName
            
        if not v_path :
            v_path = '.'
        
        v_chk = False
        for _, _, l_file in os.walk( v_path ) :
            for i in l_file :
                if i == v_file :
                        v_chk = True
                        ## dbg
                        f_dbg( v_dbg, v_file, v_tittle = "v_file"  )
                        
                        ## Action
                        return True
            if not v_chk :
                if __name__ == '__main__':
                    print( "Aucun fichier de perçage n'a été trouvé" )
                    
                return False

####

    def f_getExtList(self, v_ext=None, v_path=None) :
        """ Retourne une liste de l'ensemble des fichiers portant l'extension 'v_ext' à
            partir d'un répertoire donné
        
            - Si aucun argument n'est passé à 'v_ext', c'est la valeur de _v_fileExt qui
              serat utilisé par défaut
              
            - Si aucun chemin n'est passé à 'v_path', c'est dans le répertoire courant
              que la recherche serat effectuée.
        """
        ## dbg
        v_dbg = 1
        v_dbg2 = 1
        f_dbg(v_dbg2, "f_getExtList", self.f_getExtList)
        
        ## Action
        if not v_ext :
            v_ext = self._v_fileExt
        else :
            if v_ext[0] != '.' :
                v_ext = ".{}".format(v_ext)
            
        if not v_path :
            v_path = '.'
        
        v_chk = False
        l_extList = []
        for _, _, l_file in os.walk( v_path ) :
            for i in l_file :
                if i[-4:] == v_ext :

                    v_chk = True
                    l_extList.append(i)

                return l_extList
            if not v_chk :
                if __name__ == '__main__':
                    print( "Aucun fichier de perçage n'a été trouvé" )
                    
                return False

####

    def f_manageFile(self, v_dirPath=None, v_fileName=None, v_openMode='r') :
        """ Retourne les argument à fournir pour la commande : ::
        
                open()
                
            **v_dirPath** : Permet de définir le chemin dans lequel est créé le fichier.
            Ce chemin est utilisé comme repertoire de travail (workdir). Si il est 
            définie, la méthode 'f_setFilePath()' sera appellée.
            
            **v_fileName** : Permet de définir le nom du fichier. Si il est définie, la
            méthode 'f_setFileName()' sera appellée.
            
            **N.B** : Le format attendu est de type 'str'
        
            **v_openMode** : Permet d'ouvrir un fichier dans l'un des modes suivant : ::
        
                Lecture     : 'r'
                Ecriture    : 'w'
                Ajout       : 'a'
        """
        ## dbg
        v_dbg = 1
        v_dbg2 = 1
        f_dbg(v_dbg2, "f_manageFile", self.f_manageFile)
        
        ## Action
        if v_dirPath :
            self.f_setFilePath(v_dirPath)
            
        if v_fileName :
            self.f_setFileName(v_fileName)
            
        self.f_setFQFN()
        
        return self.f_getFQFN(), v_openMode
        
####

    def f_makeJson(self, v_dict, v_fileObject) :
        """ Permet de remplir un fichier qui a été créer au préallable avec 'open()'
            avec le contenu du dictionnaire 'v_dict' formater en 'JSON'.
        """
        ## dbg
        v_dbg = 1
        v_dbg2 = 1
        f_dbg(v_dbg2, "f_makeJson", self.f_makeJson)
        
        ## Action
        # with open("cfg.cfg", 'w') as f :
        json.dump(v_dict, v_fileObject,  indent=4, sort_keys=True)
            
####
            
    def f_loadJson(self, v_fileObject) :
        """ Retourne le contenu du fichier passer en argument. Le fichier pointer par
            'v_fileObject' devant être au format 'JSON' pour pouvoir retourner un
            dictionnaire.
        """
        ## dbg
        v_dbg = 1
        v_dbg2 = 1
        f_dbg(v_dbg2, "f_loadJson", self.f_loadJson)
        
        ## Action
        # with open("cfg.cfg", 'r') as f :
        return json.load(v_fileObject)
       
        
## Accessoires
            
def f_dbg( v_bool, v_data, v_tittle = False  ) :
    """ Fonction de traitemant du debug """
    if v_dbgChk and v_tittle :
        i_dbg.dbgPrint( v_bool, v_tittle, v_data )
        
    elif v_dbgChk and not v_tittle :
        i_dbg.dbgDel( v_bool, v_data)
        
## Main
                        
def main() :
    """ Fonction principale 
    
        Permet de tester les diférentes méthode de la Class.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(    "-d",
                            "--debug",
                            action='store_true',
                            help="activation du mode debug"
                            )
    # parser.add_argument(  "-t",
                            # "--test",
                            # action='store_true',
                            # help="activation du mode Test"
                            # )
                        
    args = parser.parse_args()
    
    if args.debug :
        print( "Mode Debug active" )
        i_dbg.f_setAffichage( True )
       
    fileName = input("Entrez le nom du fichier : ")

    def makeDict() :
        return {
                "serial":{"port":"com3", "baudrate":115200},
                "serial2":{"port":"com4", "baudrate":9600}
                }
    
    d_monDico = makeDict()
    
    i_ist = C_OpenFile()
    fileArgs = i_ist.f_manageFile(None, fileName, 'w')
    with open( fileArgs[0], fileArgs[1] ) as f :
        i_ist.f_makeJson(d_monDico, f)
        
    fileArgs = i_ist.f_manageFile(None, fileName, 'r')
    with open( fileArgs[0], fileArgs[1] ) as g :
        d_monDico2 = i_ist.f_loadJson(g)
        
    for k, v in d_monDico2.items() :
        print(k)
        for kk, vv in v.items() :
            print("{} - {}".format(vv, type(vv)))

    print("\n\n\t\t fin de la sequence ")    

if __name__ == '__main__':
    main()
