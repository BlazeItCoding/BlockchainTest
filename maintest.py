import block, io


block1 = block.block(2, 22222, 1)
block2= block.block(44,4444,4)
print(block1.blocknr)



#print(block1.hash)
#print(block2.data)
chain= []
#block1.addtoblock(chain)
#print(chain[0].data)



with io.open('block1.txt', 'x', encoding= 'utf8') as f:
    f.write("blocknummer="+ int(block1.blocknr) + '\n'+ "hash="+ hex(block1.hash) +'\n'+"data="+ str(block1.data))


