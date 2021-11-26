from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read
key = RSA.generate(2048, random_generator)  # Creates RSA keys

private_key = key.export_key()  # Exports private key
public_key = key.public_key().export_key()  # Exports public key

#  Writes keys into files
with open('private.pem', 'wb') as f:
    f.write(private_key)

with open('public.pem', 'wb') as f:
    f.write(public_key)






