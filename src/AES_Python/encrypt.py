from AES_Python import AES
from sys import argv


# ---------------
# Encryption function
# ---------------
def encrypt(key, file_path, running_mode, iv=None):

    # Input validation
    if (len(key) / 2) not in [16, 24, 32]:
        raise Exception('Key length is not valid')
    elif running_mode in ["CBC", "CFB", "OFB", "CTR", "GCM"]:
        if (len(iv) / 2) != 16 or iv is None:
            raise Exception('IV length is not valid')

    # Running mode selection
    if running_mode == "ECB":
        AES.ecb_enc(key, file_path)
    elif running_mode == "CBC" and iv is not None:
        AES.cbc_enc(key, file_path, iv)
    else:
        raise Exception("Running mode not supported")


if __name__ == "__main__":
    encrypt(key=argv[0], file_path=argv[1], running_mode=argv[2], iv=argv[3])
