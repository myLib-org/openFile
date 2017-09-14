#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Infos
=====

   :Projet:             openFile
   :Nom du fichier:     openFile.py
   :Auteur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20170913

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
                        de traitement. Ce module permet également de travailler avec
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
import os, sys, shutil, json, argparse


class C_OpenFile( object ) :
    """ Class permettant le traitement des fichiers et l'encapsulation des données
    """
    def __init__( self, v_fileName=None ) :
        """ **__init__()**
        
            Création et initialisation des variables globales de cette Class
        """
        self._v_dir             = os.getcwd()
                                # os.getcwd() : permet de récupérer le chemin
                                # du répertoire local
        
        self._v_srcFilePath         = self._v_dir
        self._v_dstFilePath        = self._v_dir
        
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
            
        
    def f_setFilePath(self, v_localWorkDir=None) :
        """ Permet de définir le chemin dans lequel est créé le fichier. Ce chemin est
            utilisé comme répertoire de travail (workdir).
            
            - Si aucune valeur n'est passé à 'v_localWorkDir', le repertoire de travail
              restera le repertoire courant
            
            - Si un chemin absolu est passé à 'v_localWorkDir',ce dernier serat utiliser
              comme nouveau répertoire de travail (workdir)
        """
        if v_localWorkDir :
            self._v_dir = os.path.normpath(v_localWorkDir)
            os.chdir(self._v_dir)
                # permet de déclarer '_v_dir' comme répertoire courant
        else :
            if __name__ == '__main__':
                print   (
                        "Aucun chemin n'a été spécifié. le chemin par défaut sera" / 
                        "utilisé : \n {}".format(self._v_dir)
                        )
                
                
    def f_getFilePath(self) :
        """ Retourne le chemin dans lequel est créer le fichier.
        
            **N.B** : Ce chemin correspond au répertoire de travail (workdir).
        """
        return self._v_dir
        

    def f_setSrcFilePath( self, v_srcFilePath=None ) :
        """ Permet de définir un chemin d'origine """
        if v_srcFilePath :
            self._v_srcFilePath = os.path.normpath( v_srcFilePath )
        else :
            if __name__ == '__main__':
                print   (
                        "Aucun chemin n'a été spécifié. le chemin d'origine par défaut" / "sera utilisé : \n {}".format(self._v_dir)
                        )
                        
                        
    def f_getSrcFilePat( self ) :
        """ retourne '_v_srcFilePath' """
        return self._v_srcFilePath
        
        
    def f_setDstFilePath( self v_dstFilePath=None ) :
        """ Permet de définir un chemin de destination """
        if v_dstFilePath :
            self._v_dstFilePath = os.path.normpath( v_dstFilePath )
        else :
            if __name__ == '__main__':
                print   (
                        "Aucun chemin n'a été spécifié. le chemin de destination par" /
                        "défaut sera utilisé : \n {}".format(self._v_dir)
                        )
                        
                        
    def f_getDstFilePath( self ) :
        """ Retourne '_v_dstFilePath' """
        return self._v_dstFilePath

        
    def f_setFileName(self, v_fileName=None) :
        """ Permet de définir le nom du fichier.
            **N.B** : Le format attendu est de type 'str'
            
            - Si aucune valeur n'est passée à 'v_fileName', le nom par défaut du fichier
              sera : 'nouveau_fichier.txt'
              
            - Si une valeur est passée à 'v_fileName', cette dernière sera utiliser comme
              nom de fichier
        """
        if not v_fileName :
            if __name__ == '__main__':
                print( "Le nom du fichier sera : {}".format(self._v_fileName))
        else :
            self._v_fileName = v_fileName
            if v_fileName[-4] == '.' :
                self.f_setFileExt( v_fileName[-4:] )


    def f_getFileName(self) :
        """ Retourne le nom du fichier.
        """
        return self._v_fileName
           

    def f_setPrefixFN(self, v_prefix, f_underscore=True) :
        """ Permet d'ajouter un préfixe au nom actuel du fichier
        
            - La valeur de v_prefix sera ajouté avant le nom contenu dans '_v_fileName'.
              le nouveau nom sera enregistrer dans '_v_prefix'
              
            - Si 'f_underscore' est vrai (valeur par défaut), un underscore sera insérer
              entre le nom du fichier et son préfixe
        """
        if f_underscore :
            self._v_prefix = "{}_{}".format( v_prefix, self._v_fileName )
        else :
            self._v_prefix = "{}{}".format( v_prefix, self._v_fileName )


    def f_getPrefixFN( self ) :
        """ Retourne le nom préfixé du fichier
        """
        return self._v_prefix
        

    def f_setSuffixFN(self, v_suffix, f_underscore=True) :
        """ Permet d'ajouter un suffixe au nom actuel du fichier
        
            - La valeur de v_suffix sera ajouté après le nom contenu dans '_v_fileName'.
              le nouveau nom sera enregistrer dans '_v_suffix'
              
            - Si 'f_underscore' est vrai (valeur par défaut), un underscore sera insérer
              entre le nom du fichier et son suffixe
        """
        if f_underscore :
            self._v_suffix = "{}_{}".format( self._v_fileName, v_suffix )
        else :
            self._v_suffix = "{}{}".format( self._v_fileName, v_suffix )


    def f_getSuffixFN( self ) :
        """ Retourne le nom suffixé du fichier
        """
        return self._v_suffix
        

    def f_setFileExt(self, v_fileExt ) :
        """ permet de modifier (ou d'ajouter) l’extension du fichier
            **N.B** : La valeur attendue est de type 'str'
            
            - Si le premier caractère de 'v_fileExt' est un point, on utilise
              directement cette valeur
              
            - Si le premier caractère de 'v_fileExt' n'est pas un point, on ajoute un
              point avant la valeur passée en argument
              
            - Si _v_fileName n'a pas d’extension, cette dernière sera ajouter au nom du
              fichier
              
            - Si _v_fileName a une extension qui ne correspond pas à _v_fileExt, 
              l'extension de _v_fileName sera modifiée
        """
        if v_fileExt[0] == '.' :
            self._v_fileExt = v_fileExt
        else :
            self._v_fileExt = ".{}".format(v_fileExt)
            
        if self._v_fileName[-4] != '.' :
            self._v_fileName = "{}{}".format(self._v_fileName, self._v_fileExt)
        else :
            if self._v_fileName[-4:] != self._v_fileExt :
                self._v_fileName = "{}{}".format(self._v_fileName[:-4], self._v_fileExt)
      

    def f_getFileExt( self ) :
        """ Retourne l'extension du fichier
        """
        return self._v_fileExt


    def f_setFQFN(self) :
        """ Permet de définir le fichier et son chemin (Fully Qualified File Name) sous la
            forme : ::
        
                [chemin_du_fichier]\[nom_du_fichier]
        """
        self._v_FQFN = os.path.join(self._v_dir, self._v_fileName)
        
            
    def f_getFQFN(self) :
        """ Retourne le Nom du fichier précédé se son chemin (Fully Qualified File 
            Name). ::
                
                [chemin_du_fichier]\[nom_du_fichier]
        """
        return self._v_FQFN


    def f_chkIfFile(self, v_file=None, v_path=None) :
        """ Retourne Vrai si le fichier existe et Faux si il n’existe pas.
        
            - Si aucun argument n'est passé à 'v_file', c'est la valeur de _v_fileName qui
              sera utilisé par défaut.
              
            - Si aucun chemin n'est passé à 'v_path', c'est dans le répertoire courant
              que la recherche sera effectuée.
        """
        if not v_file :
            v_file = self._v_fileName
            
        if not v_path :
            v_path = '.'
        
        v_chk = False
        for _, _, l_file in os.walk( v_path ) :
            for i in l_file :
                if i == v_file :
                    return True
            if not v_chk :
                if __name__ == '__main__':
                    print( "Ce fichier n'a pas été trouvé" )
                    
                return False


    def f_getExtList(self, v_ext=None, v_path=None) :
        """ Retourne une liste de l'ensemble des fichiers portant l'extension 'v_ext' à
            partir d'un répertoire donné
        
            - Si aucun argument n'est passé à 'v_ext', c'est la valeur de _v_fileExt qui
              sera utilisé par défaut
              
            - Si aucun chemin n'est passé à 'v_path', c'est dans le répertoire courant
              que la recherche sera effectuée.
        """
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


    def f_manageFile(self, v_dirPath=None, v_fileName=None, v_openMode='r') :
        """ Retourne les argument à fournir pour la commande : ::
        
                open()
                
            **v_dirPath** : Permet de définir le chemin dans lequel est créé le fichier.
            Ce chemin est utilisé comme répertoire de travail (workdir). Si il est 
            définie, la méthode 'f_setFilePath()' sera appelée.
            
            **v_fileName** : Permet de définir le nom du fichier. Si il est définie, la
            méthode 'f_setFileName()' sera appelée.
            
            **N.B** : Le format attendu est de type 'str'
        
            **v_openMode** : Permet d'ouvrir un fichier dans l'un des modes suivant : ::
        
                Lecture     : 'r'
                Ecriture    : 'w'
                Ajout       : 'a'
        """
        if v_dirPath :
            self.f_setFilePath(v_dirPath)
            
        if v_fileName :
            self.f_setFileName(v_fileName)
            
        self.f_setFQFN()
        
        return self.f_getFQFN(), v_openMode
        

    def f_copyFile( self, v_FQFN=False, v_fileName=None,
                    v_srcPath=None, v_dstPath=None ) :
        """ Permet de copier un fichier.
        
            **v_fileName**  : Le nom du fichier à copier
            **v_srcPath**   : Chemin d’origine du fichier à copier
            **v_dstPath     : Chemin de destination du fichier à copier
        """
        if v_FQFN :
            v_src = self.f_getFQFN()
        else :
            if not v_fileName :
                v_fileName = self.f_getFileName()
            
            if not v_srcPath :
                v_srcPath = self.f_getSrcFilePat()
            
            v_src = os.path.normpath(v_srcPath + "/" + v_fileName)
            
        if not v_dstPath :
            v_dstPath = self.f_getDstFilePath()
            
        v_dstPath   = os.path.normpath(v_dstPath)

        try:
            shutil.copy2(v_src, v_dstPath)
            
        except shutil.Error as e:
            print("Error: {}".format(e))
        # eg. source or destination doesn't exist
        except IOError as e:
            print("Error: {}".format(e.strerror))


    def f_moveFile( self, v_FQFN=False, v_fileName=None,
                    v_srcPath=None, v_dstPath=None ) :
        """ Permet de déplacer un fichier d'un répertoire à l'autre.
        
            **v_fileName**  : Le nom du fichier à copier
            **v_srcPath**   : Chemin d’origine du fichier à copier
            **v_dstPath     : Chemin de destination du fichier à copier
        """
        if v_FQFN :
            v_src = self.f_getFQFN()
        else :
            if not v_fileName :
                v_fileName = self.f_getFileName()
            
            if not v_srcPath :
                v_srcPath = self.f_getSrcFilePat()
            
            v_src = os.path.normpath(v_srcPath + "/" + v_fileName)
            
        if not v_dstPath :
            v_dstPath = self.f_getDstFilePath()
            
        v_dstPath   = os.path.normpath(v_dstPath)
        
        try:
            shutil.move(v_src, v_dstPath)
            
        except shutil.Error as e:
            print("Error: {}".format(e))
        # eg. source or destination doesn't exist
        except IOError as e:
            print("Error: {}".format(e.strerror))
        
            
    def f_removeFile(self, v_fileName, v_path=None) :
        """ Permet de supprimer le fichier pointer par 'v_fileName'
        
            - Le fichier pointer par 'v_fileName' sera supprimé si le fichier
              existe ( f_chkIfFile )
              
        """
        if not v_path :
            if self.f_chkIfFile(v_file=v_fileName) :
                os.remove( v_fileName )
            else :
                if __name__ == '__main__':
                    print( "Ce fichier n'a pas été trouvé" )
        else :
            if self.f_chkIfFile(v_filename, v_path) :
                os.remove( "{}/{}".format(v_path, v_fileName ))
            else :
                if __name__ == '__main__':
                    print( "Ce fichier n'a pas été trouvé" )


    def f_renameFile( v_newFilename, v_filetoRename, v_path=None) :
        """ Permet de renommer un fichier
        
            - 'v_newFilename' est le nouveau nom du fichier à renommer
            
            - 'v_filetoRename' est le nom du fichier à renomer
            
            - 'v_path' permet de travailler dans un dossier différent que le répertoire local
        """
        if not v_path :
            if self.f_chkIfFile(v_file=v_fileName) :
                os.rename(v_filetoRename, v_newFilename )
            else :
                if __name__ == '__main__':
                    print( "Ce fichier n'a pas été trouvé" )
        else :
            if self.f_chkIfFile(v_filename, v_path) :
                v_newFilename = "{}/{}".format(v_path, v_filetoRename )
                os.rename(v_filetoRename, v_newFilename )
            else :
                if __name__ == '__main__':
                    print( "Ce fichier n'a pas été trouvé" )
    

    def f_makeJson(self, v_dict, v_fileObject) :
        """ Permet de remplir un fichier qui a été créer au préalable avec 'open()'
            avec le contenu du dictionnaire 'v_dict' formater en 'JSON'.
        """
        json.dump(v_dict, v_fileObject, indent=4, sort_keys=True)
            
            
    def f_loadJson(self, v_fileObject) :
        """ Retourne le contenu du fichier passer en argument. Le fichier pointer par
            'v_fileObject' devant être au format 'JSON' pour pouvoir retourner un
            dictionnaire.
        """
        return json.load(v_fileObject)
       
####
       
## Main
                        
def main() :
    """ Fonction principale 
    
        Permet de tester les différentes méthode de la Class.
    """
    parser = argparse.ArgumentParser()
    # parser.add_argument(    "-d",
                            # "--debug",
                            # action='store_true',
                            # help="activation du mode debug"
                            # )
    # parser.add_argument(  "-t",
                            # "--test",
                            # action='store_true',
                            # help="activation du mode Test"
                            # )
                        
    args = parser.parse_args()
    
    fileName = input("Entrez le nom du fichier : ")

    def makeDict() :
        return {
                "serial":{"port":"com3", "baudrate":115200},
                "serial2":{"port":"com4", "baudrate":9600}
                }
    
    d_monDico = makeDict()
    
    i_ist = C_OpenFile()
    fileArgs = i_ist.f_manageFile(None, fileName, 'w')
    with open( fileArgs[0], fileArgs[1], encoding = "utf-8" ) as f :
        i_ist.f_makeJson(d_monDico, f)
        
    fileArgs = i_ist.f_manageFile(None, fileName, 'r')
    with open( fileArgs[0], fileArgs[1], encoding = "utf-8" ) as g :
        d_monDico2 = i_ist.f_loadJson(g)
        
    for k, v in d_monDico2.items() :
        print(k)
        for kk, vv in v.items() :
            print("{} - {}".format(vv, type(vv)))

    print("\n\n\t\t fin de la séquence ")    

if __name__ == '__main__':
    main()