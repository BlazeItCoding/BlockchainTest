import reader, block, blockchain, random, os, string

class check:
    blockchain = None

    def __init__(self):
        print("To check a chain type CHECK into the console")
        s = input()
        if s == "CHECK":
            chainresult = []
            self.addgen(chainresult)
    def addgen(self,chainresult):
        print("Type the path of the next block file in the right order")
        genesisIn = input()
        gen= reader.reader(genesisIn)
        testChain = blockchain.blockchain([])
        gent=block.block(gen.fileblocknr,gen.filedata,testChain,gen.nonce)
        print("genesis block has been added to the testchain")
        if gent.hash != gen.filehash:
            chainresult.append("Block 0")
        help = 0
        self.add(testChain,help, chainresult)
    def add(self,blockchain, help, chainresult):
        print("To add more type ADD if you have added all files type END")
        s=input()
        if s == "END":
            if chainresult != []:
                print("Hash von "+str(chainresult)+" ist fehlerhaft.")
                self.blockchain= blockchain
                return
            if chainresult == []:
                block.block(str(help+1),"Blockchain richtig.", "")
                self.blockchain = blockchain
                return
        if s=="ADD":
            print("Type the next block file path")
            file =input()
            help = help +1
            print(blockchain.chainlist)
            print(len(blockchain.chainlist))
            blockfile=reader.reader(file)
            blockf = block.block(blockfile.fileblocknr,blockfile.filedata,blockchain,blockfile.nonce)
            if blockf.hash != blockfile.filehash:
                print(str(blockf.hash)+ " File"+str(blockfile.filehash))
                chainresult.append("Block "+str(help))
            self.add(blockchain, help, chainresult)


#test1= check()
#print(test1.blockchain)
read0 = reader.reader("C:/Users/marti/Desktop/blockchain_ex3/00")
read1 = reader.reader("C:/Users/marti/Desktop/blockchain_ex3/01")
read2 = reader.reader("C:/Users/marti/Desktop/blockchain_ex3/02")
random3=-1
list=blockchain.blockchain([])
b0= block.block(str(read0.fileblocknr),read0.filedata,list,None)
b1= block.block(read1.fileblocknr,read1.filedata,list,None)
b2 = block.block(read2.fileblocknr,read2.filedata,list,None)
hash = None
while hash != "000000":
    if os.path.exists("C:/Users/marti/PycharmProjects/untitled6/03"):
        os.remove("C:/Users/marti/PycharmProjects/untitled6/03")
        list.chainlist.pop(2)
        if os.path.exists("C:/Users/marti/PycharmProjects/untitled6/04"):
            os.remove("C:/Users/marti/PycharmProjects/untitled6/04")
            list.chainlist.pop(3)
    random2 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    #random3= ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    random3 = random3+1
    b3=block.block('3',"Find Zero6",list,str(random3))
    b4=block.block('4',random.random(),list,str(random.random()))
    hash=b4.hash[0:5]
    print(hash)
b5=block.block('4',"data sent",list,"Test")
#print(hashing.hashing.get_digest("C:/Users/marti/Desktop/blockchain_ex2_all/blockchain_01/01"))