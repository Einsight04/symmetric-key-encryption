MAPPING = {
    'A': '00000', 'B': '00001', 'C': '00010', 'D': '00011',
    'E': '00100', 'F': '00101', 'G': '00110', 'H': '00111',
    'I': '01000', 'J': '01001', 'K': '01010', 'L': '01011',
    'M': '01100', 'N': '01101', 'O': '01110', 'P': '01111',
    'Q': '10000', 'R': '10001', 'S': '10010', 'T': '10011',
    'U': '10100', 'V': '10101', 'W': '10110', 'X': '10111',
    'Y': '11000', 'Z': '11001',
}


def char_to_binary(c: str) -> str:
    binary = MAPPING.get(c.upper())

    if binary is None:
        raise ValueError(f"Invalid character: {c}")

    return binary


def encrypt(plaintext: str, key: int) -> list[int]:
    return [int(char_to_binary(c), 2) ^ key for c in plaintext]


def decrypt(ciphertext: list[int], key: int) -> str:
    return ''.join(chr(int(bin(c ^ key)[2:].zfill(5), 2) + ord('A')) for c in ciphertext)


plaintext_input = "CATS"
key_input = 17

ciphertext_output = encrypt(plaintext_input, key_input)
print(ciphertext_output)

decrypted_text = decrypt(ciphertext_output, key_input)
print(decrypted_text)