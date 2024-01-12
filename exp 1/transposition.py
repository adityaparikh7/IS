# # implement transposition cipher Encryption and decryption both with a key

# def encryption(plaintext, key):
#     plaintext = plaintext.replace(" ","")

#     rows = len(plaintext)//key
#     if len(plaintext) % key != 0:
#         rows += 1

#     grid = [['' for _ in range(key)] for _ in range(rows)]
#     index = 0
#     for i in range(rows):
#         for j in range(key):
#             if index < len(plaintext):
#                 grid[i][j] = plaintext[index]
#                 index += 1

#     ciphertext = ""
#     for j in range(key):
#         for i in range(rows):
#             ciphertext += grid[i][j]

#     return ciphertext


# def decryption(ciphertext, key):
#     rows = len(ciphertext)//key
#     if len(ciphertext) % key != 0:
#         rows += 1

#     grid = [['' for _ in range(key)] for _ in range(rows)]
#     index = 0
#     for j in range(key):
#         for i in range(rows):
#             if index < len(ciphertext):
#                 grid[i][j] = ciphertext[index]
#                 index += 1

#     plaintext = ""
#     for i in range(rows):
#         for j in range(key):
#             plaintext += grid[i][j]

#     return plaintext


# # def main():
# plaintext = input("Enter plaintext: ")
# key = input("Enter key as positive number: ")
# key = int(key)
# ciphertext = encryption(plaintext, key)
# print(ciphertext)
# plaintext = decryption(ciphertext, key)
# print(plaintext)


def validate_key(key):
    if key <= 0:
        raise ValueError("Key should be a positive integer.")


def encrypt_transposition(plaintext, key):
    validate_key(key)

    # Remove spaces from the plaintext and calculate length
    plaintext = plaintext.replace(" ", "")
    if not plaintext:
        raise ValueError("Plaintext cannot be empty.")

    num_chars = len(plaintext)

    # Calculate number of rows needed
    num_rows = (num_chars + key - 1) // key

    # Create the grid and fill it with the plaintext
    grid = [['' for _ in range(key)] for _ in range(num_rows)]
    index = 0
    for j in range(key):
        for i in range(num_rows):
            if index < num_chars:
                grid[i][j] = plaintext[index]
                index += 1

    # Read the grid column-wise to get the ciphertext
    ciphertext = ''.join(''.join(row) for row in grid)
    return ciphertext


def decrypt_transposition(ciphertext, key):
    validate_key(key)

    # Calculate number of rows needed
    num_rows = (len(ciphertext) + key - 1) // key

    # Create the grid and fill it with the ciphertext
    grid = [['' for _ in range(key)] for _ in range(num_rows)]
    index = 0
    for i in range(num_rows):
        for j in range(key):
            if index < len(ciphertext):
                grid[i][j] = ciphertext[index]
                index += 1

    # Read the grid row-wise to get the plaintext
    plaintext = ''.join(''.join(row) for row in grid)
    return plaintext


# Example
plaintext = input("Enter plaintext: ")
key = input("Enter the key: ")

key = int(key)

ciphertext = encrypt_transposition(plaintext, key)
print(f"Ciphertext: {ciphertext}")

decrypted_text = decrypt_transposition(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")
