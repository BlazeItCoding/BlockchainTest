from block import block
import reader, hashing

class blockchain:
    chainlist = []

    def __init__(self,listchain):  #Konstruktor einer Chain
        self.chainlist = listchain

    def appendToChain(self, block): #Methode um Block einer chain hinzuzufügen
        self.chainlist.append(block)



#block(22,44,4444,blockchain.chainlist)
#block(44,333,3333,blockchain.chainlist)

#chain1= blockchain([]) #Initialisierung einer leeren Chain mithilfe von blockchain([])
#test1=reader.reader("C:/Users/marti/Desktop/blockchain_ex1/00")
#test2=reader.reader("C:/Users/marti/Desktop/blockchain_ex1/01")
#test3=reader.reader("C:/Users/marti/Desktop/blockchain_ex1/02")
#block1 = block("0",test1.getfiledata(),chain1)
#block1 = block("0",str(test1.getfiledata()),chain1)
#block2 = block("1",test2.getfiledata(),chain1)
#block3 = block("2",test3.getfiledata(),chain1)
#print(hashing.hashing.get_digest('C:/Users/marti/Desktop/blockchain_ex1/00'))
#print(hashing.hashing.get_digest('C:/Users/marti/PycharmProjects/untitled6/00'))
#print(hashing.hashing.get_digest('C:/Users/marti/Desktop/blockchain_ex1/00'))
#print(test1.getfiledata())
#print(test1.filehash)
#print(test1.text3)
#if (blockchain.chainlist == []):
   # print("Empty")

#block("00", "null", blockchain.chainlist)
#print(blockchain.chainlist[0].hash)
#block("01","testdata", blockchain.chainlist)
#print(blockchain.chainlist[1].hash)
#print(blockchain.chhainlist[1].hash)



