from Crypto.Cipher import AES
from struct import unpack, pack
from binascii import hexlify

"""
[IDACode] Executing /home/bjk/Projects/idaemu/idaemu.py
-------
0x1020dc48[W] : 0xc342daa5
0x1020dc4c[W] : 0xbac5f6b4
0x1020dc50[W] : 0x68c562e1
0x1020dc54[W] : 0x526bdad
0x1020dc58[W] : 0x771ba184
0x1020dc5c[W] : 0x35f963a8
0x1020dc60[W] : 0x48306825
0x1020dc64[W] : 0x87b3933e
0x1020dc08[W] : 0x12
0x1020dc04[W] : 0x1
0x1020dc0c[W] : 0x16
0x1020dc10[W] : 0x1a

0x1020d804[W] : 0x3
0x1020d808[W] : 0x3
0x1020dc00[W] : 0x78
0x1020d400[W] : 0x0
0x1020d800[R] : 0x0
0x1020d418[R] : 0x0
0x1020d804[W] : 0x3

0x1020dc48[W] : 0xf5a181eb
0x1020dc4c[W] : 0x6fb87b96
0x1020dc50[W] : 0x4e0c13e
0x1020dc54[W] : 0x71edb823

0x1020dc04[W] : 0x300240
0x1020dc08[W] : 0x600000
0x1020dc0c[W] : 0x25d3c
0x1020dc14[W] : 0x12
0x1020dc18[W] : 0x1a
0x1020dc1c[W] : 0x1a

0x1020d804[W] : 0x3
0x1020d808[W] : 0x3
0x1020dc00[W] : 0x7e
0x1020d400[W] : 0x0
0x1020d800[R] : 0x0
0x1020d418[R] : 0x0
0x1020d804[W] : 0x3
0x1020dc48[W] : 0x0
0x1020dc4c[W] : 0x0
0x1020dc50[W] : 0x0
0x1020dc54[W] : 0x0
0x1020dc58[W] : 0x0
0x1020dc5c[W] : 0x0
0x1020dc60[W] : 0x0
0x1020dc64[W] : 0x0
0x1020dc68[W] : 0x0
0x1020dc6c[W] : 0x0
0x1020dc70[W] : 0x0
0x1020dc74[W] : 0x0
"""

preloader_key = bytes.fromhex(
    "A5DA42C3B4F6C5BAE162C568ADBD26055572247C05586BAA37818D2868949ADB9C4DEE58E7C7AFD090D8951035F84BEB")
aeskey1 = preloader_key[:16]
aeskey2 = preloader_key[16:32]

seed = bytearray(bytes.fromhex("CEBEA8E5DC1A43A0F0AE425F67AF42047471F1D4B751362F39AE8A5E8BDA0C4C"))
iv = AES.new(aeskey1, AES.MODE_ECB).decrypt(seed[:0x10])

out = bytearray()
for i in range(4):
    val = unpack("<I", seed[0x10 + i * 4:0x10 + (i * 4) + 4])[0]
    val2 = unpack("<I", aeskey2[i * 4:(i * 4) + 4])[0]
    val2 ^= val
    out.extend(pack("<I", val2))

print(hexlify(out))
