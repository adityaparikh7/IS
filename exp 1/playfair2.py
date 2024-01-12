# import string


# def create_grid(key=""):
#     if not key:
#         key = "KEYWORD"  # Replace with your own keyword
#     key = key.upper().replace("J", "I")
#     key_set = set(key)
#     alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
#     grid = ""
#     for letter in key:
#         grid += letter
#         key_set.remove(letter)
#     for letter in alphabet:
#         if letter not in key_set:
#             grid += letter
#     return grid


# def find_position(grid, char):
#     index = grid.find(char.upper())
#     row = index // 5
#     col = index % 5
#     return row, col


# def playfair_encrypt(grid, plaintext):
#     plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
#     plaintext = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
#     ciphertext = ""
#     for pair in plaintext:
#         if len(pair) == 1:
#             pair += "X"
#         row1, col1 = find_position(grid, pair[0])
#         row2, col2 = find_position(grid, pair[1])
#         if row1 == row2:
#             ciphertext += grid[row1 * 5 +
#                                (col1 + 1) % 5] + grid[row2 * 5 + (col2 + 1) % 5]
#         elif col1 == col2:
#             ciphertext += grid[((row1 + 1) % 5) * 5 + col1] + \
#                 grid[((row2 + 1) % 5) * 5 + col2]
#         else:
#             ciphertext += grid[row1 * 5 + col2] + grid[row2 * 5 + col1]
#     return ciphertext


# def playfair_decrypt(grid, ciphertext):
#     ciphertext = ciphertext.upper().replace("J", "I").replace(" ", "")
#     ciphertext = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
#     plaintext = ""
#     for pair in ciphertext:
#         row1, col1 = find_position(grid, pair[0])
#         row2, col2 = find_position(grid, pair[1])
#         if row1 == row2:
#             plaintext += grid[row1 * 5 + (col1 - 1) %
#                               5] + grid[row2 * 5 + (col2 - 1) % 5]
#         elif col1 == col2:
#             plaintext += grid[((row1 - 1) % 5) * 5 + col1] + \
#                 grid[((row2 - 1) % 5) * 5 + col2]
#         else:
#             plaintext += grid[row1 * 5 + col2] + grid[row2 * 5 + col1]
#     return plaintext


# if __name__ == "__main__":
#     key = "KEYWORD"  # Replace with your own keyword
#     grid = create_grid(key)

#     plaintext = input("Enter the plaintext: ")
#     ciphertext = playfair_encrypt(grid, plaintext)
#     print(f"Ciphertext: {ciphertext}")

#     decrypted_text = playfair_decrypt(grid, ciphertext)
#     print(f"Decrypted text: {decrypted_text}")


import random

def generate_key_matrix():
    """Generates a random 5x5 key matrix using the alphabet."""
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    random.shuffle(alphabet)
    key_matrix = [alphabet[i:i+5] for i in range(0, 25, 5)]
    return key_matrix

def encrypt(plaintext, key_matrix):
    """Encrypts the plaintext using the Playfair cipher."""
    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        pair = plaintext[i:i+2]
        if len(pair) == 1:
            pair += 'x'  # Add a filler letter if needed

        # Encrypt the pair using the key matrix
        row1, col1 = find_indices(pair[0], key_matrix)
        row2, col2 = find_indices(pair[1], key_matrix)

        if row1 == row2:
            new_col1 = (col1 + 1) % 5
            new_col2 = (col2 + 1) % 5
            ciphertext += key_matrix[row1][new_col1] + key_matrix[row2][new_col2]
        elif col1 == col2:
            new_row1 = (row1 + 1) % 5
            new_row2 = (row2 + 1) % 5
            ciphertext += key_matrix[new_row1][col1] + key_matrix[new_row2][col2]
        else:
            ciphertext += key_matrix[row1][col2] + key_matrix[row2][col1]

    return ciphertext

def find_indices(letter, key_matrix):
    """Finds the row and column indices of a letter in the key matrix."""
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == letter:
                return i, j

# Example usage
key_matrix = generate_key_matrix()
plaintext = "helloworld"
ciphertext = encrypt(plaintext, key_matrix)
print(ciphertext)
