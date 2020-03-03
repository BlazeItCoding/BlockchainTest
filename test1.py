import hashlib
import io

blockchain = []





str1 = hashlib.sha256(b'test123456')

str_hex = str1.hexdigest()

print(str_hex)
print(str1)

with io.open('block.txt', 'x', encoding='utf8') as f:
    f.write(str(str_hex))
    f.close()
