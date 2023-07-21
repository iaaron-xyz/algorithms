from secrets import token_bytes
from typing import Tuple

def random_key(length: int) -> int:
    # generate length random bytes
    tb: bytes = token_bytes(length)
    # convert those bytes into a bit string and return it
    return int.from_bytes(tb, "big")

def encrypt(original: str) -> Tuple[int, int]:
    # convert original string message from str to bytes
    original_bytes: bytes = original.encode()
    # generate dummy random bit string
    dummy: int = random_key(len(original_bytes))
    # get bitstring key from original string
    original_key: int = int.from_bytes(original_bytes, "big")
    # apply XOR operation to dummy and orginal bitstrings
    encrypted: int = original_key ^ dummy #XOR
    # return the 2 keys, dummy and XOR-combined ecrypted message
    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
    # Apply XOR to dummy and encrypted. By XOR rules yo get th 3rd
    # operand, the original_key
    decrypted: int = key1 ^ key2
    # Convert bytes bitstring to bytes
    temporal: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    # convert bytes to string
    return temporal.decode()

if __name__ == "__main__":
    # original
    original = "Testing my unbreakable cncrytpion!"
    print(f'original: {original}')
    # encryption
    key1, key2 = encrypt(original)
    print(f'Encrypted message: {key2}')
    # decryption
    result: str = decrypt(key1, key2)
    print(f'result: {result}')