import os
import binascii

def randomstr():
    return str(binascii.b2a_hex(os.urandom(16))).removeprefix("b'").removesuffix("'")

hashes = {}

p = 0
while p<10:
    ranstr = randomstr()
    cuthash = ranstr[:10]
    if cuthash in hashes:
        print("Colission nr:",p+1, "colission: ", cuthash)
        print(ranstr, "and", hashes[cuthash])
        p += 1
    else:
        hashes.update({cuthash: ranstr})