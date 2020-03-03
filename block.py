import io #io import um Datei zu erstellen vorher benutzt und resultierte nicht in gewünschten hash
import hashing #importiert hashfunktions klasse
import codecs #codes um File mit Kodierung zu erstellen

class block:
    block= None                                                                       #Initialisierung der Variablen
    hash = None
    data = None
    blocknrsave = None
    nonce = None

    def __init__(self, blocknr ,data, chain,noncedata):                                           #Konstruktur von block
        self.data = data                                                                #set data to method input data
        if len(str(blocknr)) != 2:
           self.blocknrsave="0"+blocknr                                                     #if blocknr is not of type xx raise error
            #raise TypeError("blocknumber has to have 2 digits")
        if chain == [] and (blocknr != "0"):                         #if emptychain check blocknr and data
            raise TypeError("blocknumber of an initial block has to be equal to 00")    #raise error if invalid
        if chain.chainlist== []:                                                                  #if chain is empty => initial block => hash = none
            self.hash = 'null'
        else:                                                                           #if no initial block do the following
            length= len(chain.chainlist)
            if len(str(length))!=2:
                length = '0'+str(length)
                                                                                        #length=str(length)
            self.hash= hashing.hashing.get_digest("C:/Users/marti/PycharmProjects/untitled6/" + '0'+str(len(chain.chainlist)-1))  #benutzt hashfunktion anhand des letzten Blocks
        self.block= str(blocknr)
        chain.chainlist.append(self) #Wird zur blockchain hinzugefügt
        addlist=[]
        addlist.append("block="+str(self.block))
        addlist.append("previous_hash="+str(self.hash))
        addlist.append("data=")
        try:
            with codecs.open(str(self.blocknrsave), 'x', encoding="utf_8_sig") as f: #Erstellt block datei
                #f.newline=None
                if noncedata != None :
                    f.write("block=" + self.block + '\n' + 'previous_hash=' + str(self.hash) + '\n' + 'data=' + str(
                        self.data) + '\n' + "nonce=" + noncedata)
                else:
                    f.write("block=" + self.block+'\n' + 'previous_hash=' + str(self.hash) + '\n' + 'data=' + str(self.data)+ '\n')
        except:
            raise FileExistsError("Filename already exists delete it or choose another block number")

    #hashhng done
