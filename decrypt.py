import hashlib
import sys
from argparse import ArgumentParser

# SQL Cipher 4
# page size: 4096
# KDF iterations: 256000
# HMAC algorithm: SAH512
# KDF algorithm: SHA512
# plaintext header size: 0

def derive_key(db_path: str) -> None:
    hardcoded_bytes = bytes.fromhex("92e418a05804d6fcaa5e0a0f3729b4ee")

    with open(db_path, "rb") as f:
       salt = f.read(16) 

    key = hashlib.pbkdf2_hmac(
            'sha512', 
            hardcoded_bytes, 
            salt, 
            iterations=256000, 
            dklen=64
    )

    key = key[:32]
    print(f"Key (AES-256): 0x{key.hex()}")


def main() -> None:
    parser = ArgumentParser("Recover the SQL Cipher 4 key from HideU.db")
    parser.add_argument("database", help="path to HideU.db file")
    args = parser.parse_args()

    derive_key(args.database)


if __name__ == "__main__":
    main()
