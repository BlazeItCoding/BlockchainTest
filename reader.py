import io
import codecs
import hashing
class reader:
    fileblocknr=None #Blocknummer der block files
    filehash=None #Hash der block files
    filedata=None #Data der block files
    text3=None #Hilfsvariable um das letzte \n der Blockdatein zu entfernen
    nonce=None

    def __init__(self, file):     #Konstruktor eines gelesenen Blocks
        with codecs.open(file, 'r') as f:
            text=f.readline()
            text= text.split("=")
            text=text[1]
            text3=str(text)
            self.text3 = text3.split("\n")
            self.fileblocknr = str(self.text3[0])
            text2=f.readline()
            text2= text2.split('=')
            text2=text2[1]
            text2=str(text2)
            text2 = text2.split("\n")
            self.filehash= text2[0]
            text3=f.readline()
            text3=text3[5:]
            #text3= text3.split('=')
            #text3=text3[1]
            text3=str(text3)
            self.text3 = text3.split("\n")
            self.filedata = str(self.text3[0])
            text4 = f.readline()
            if text4[0:5] == "nonce=":
                self.nonce=text4[6:]




    def getfileblocknr(self):
        return self.fileblocknr
    def getfilehash(self):
        return self.filehash
    def getfiledata(self):
        return self.filedata
#test=reader('C:/Users/marti/Desktop/blockchain_ex2_all/blockchain_05/00')
#print(test.getfiledata())
#print(hashing.hashing.get_digest('C:/Users/marti/Desktop/blockchain_ex2_all/blockchain_05/01-corrected_version'))
#print(hashing.hashing.get_digest('C:/Users/marti/Desktop/blockchain_ex2_all/blockchain_05/01-initial_version'))
#Splittet blocknummer=00 in 00