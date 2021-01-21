#!/usr/bin/python3

import Crypto.Cipher.DES3 as DES3
from sys import argv

ciphertext = argv[1]

teamcity_3DES_key = "3d160b396e59ecff00636f883704f70a0b2d47a7159d3633"
key = bytearray.fromhex(teamcity_3DES_key)

des3_ciphertext = ciphertext.lstrip('zxx')
des3_cipherbytes = bytearray.fromhex(des3_ciphertext)

cipher = DES3.new(key, DES3.MODE_ECB)

plaintext_padded = cipher.decrypt(des3_cipherbytes)
plaintext = plaintext_padded[:-plaintext_padded[-1]]

print(plaintext.decode('utf-8'))
