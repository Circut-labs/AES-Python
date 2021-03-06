from AES_Python.encrypt import encrypt
from AES_Python.decrypt import decrypt
from getpass import getpass
from os import get_terminal_size
import AES_Python


def main():
    print("-"*66)
    print(r"""           ______  _____       _____       _   _
     /\   |  ____|/ ____|     |  __ \     | | | |
    /  \  | |__  | (___ ______| |__) |   _| |_| |__   ___  _ __
   / /\ \ |  __|  \___ \______|  ___/ | | | __| '_ \ / _ \| '_ \
  / ____ \| |____ ____) |     | |   | |_| | |_| | | | (_) | | | |
 /_/    \_\______|_____/      |_|    \__, |\__|_| |_|\___/|_| |_|
                                      __/ |
                                     |___/                       """)
    print("-"*66)
    print(f"Version: {AES_Python.__version__}                         {AES_Python.__copyright__}")
    print("-"*66)
    print("""This is a simple AES (Advanced Encryption Standard) implementation
in Python-3. It is a pure Python implementation of AES that is
designed to be used as a educational tool only. It is not intended
to be used in any other use case than educational and no security
is guaranteed for data encrypted or decrypted using this tool.""")
    print("-"*66)
    run()


def run():
    action = input("Do you want to encrypt, decrypt or quit? (e/d/q): ")
    if action == "e":
        running_mode = input("Please select cipher running mode (ECB/CBC/PCBC/CFB/OFB/CTR/GCM): ")

        if running_mode == "ECB":
            key = getpass(prompt="Please enter your key: ")
            file_path = input("Please enter path to file: ")
            confirmation = input("Are you sure you want to encrypt this file? (y/n): ")

            if confirmation == "y":
                encrypt(key, file_path, running_mode, terminal_size=get_terminal_size()[0])
                print("\nEncryption complete!")

            elif confirmation == "n":
                print("Encryption aborted!")
                exit()

            else:
                print("Invalid input!")
                exit()

        elif running_mode in ["CBC", "PCBC", "CFB", "OFB", "CTR", "GCM"]:
            key = getpass(prompt="Please enter your key: ")
            iv = getpass(prompt="Please enter your iv: ")
            file_path = input("Please enter path to file: ")
            confirmation = input("Are you sure you want to encrypt this file? (y/n): ")

            if confirmation == "y":
                encrypt(key, file_path, running_mode, iv, get_terminal_size()[0])
                print("\nEncryption complete!")

            elif confirmation == "n":
                print("Encryption aborted!")
                exit()

            else:
                print("Invalid input!")
                exit()

        else:
            print("Invalid cipher running mode")
            run()

    elif action == "d":
        running_mode = input("Please select cipher running mode (ECB/CBC/PCBC/CFB/OFB/CTR/GCM): ")

        if running_mode == "ECB":
            key = getpass(prompt="Please enter your key: ")
            file_path = input("Please enter path to file: ")
            confirmation = input("Are you sure you want to decrypt this file? (y/n): ")

            if confirmation == "y":
                decrypt(key, file_path, running_mode, terminal_size=get_terminal_size()[0])
                print("\nDecryption complete!")

            elif confirmation == "n":
                print("Decryption aborted!")
                exit()

            else:
                print("Invalid input!")
                exit()

        elif running_mode in ["CBC", "PCBC", "CFB", "OFB", "CTR", "GCM"]:
            key = getpass(prompt="Please enter your key: ")
            iv = getpass(prompt="Please enter your iv: ")
            file_path = input("Please enter path to file: ")
            confirmation = input("Are you sure you want to decrypt this file? (y/n): ")

            if confirmation == "y":
                decrypt(key, file_path, running_mode, iv, get_terminal_size()[0])
                print("\nDecryption complete!")

            elif confirmation == "n":
                print("Decryption aborted!")
                exit()

            else:
                print("Invalid input!")
                exit()

        else:
            print("Invalid cipher running mode")
            run()

    elif action == "q":
        print("Exiting...")
        exit()

    else:
        print("Invalid action (to quit enter 'q')")
        run()


if __name__ == "__main__":
    main()
