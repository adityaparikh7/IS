# columnar transposition cipher 

# def encrypt(plaintext, key):
#     key = list(key)
#     key_order = sorted(key)
#     ciphertext = ""
#     for i in range(len(key)):
#         index = key.index(key_order[i])
#         for j in range(index, len(plaintext), len(key)):
#             ciphertext += plaintext[j]
#     return ciphertext

# def decrypt(ciphertext, key):
#     key = list(key)
#     key_order = sorted(key)
#     plaintext = ""
#     for i in range(len(ciphertext)):
#         index = key_order.index(key[i])
#         for j in range(index, len(ciphertext), len(key)):
#             plaintext += ciphertext[j]
#     return plaintext


# plaintext = input("Enter plaintext: ")
# key = input("Enter key: ")
# ciphertext = encrypt(plaintext, key)
# print(ciphertext)
# plaintext = decrypt(ciphertext, key)
# print(plaintext)


def encrypt(message, key):
    # Remove spaces and convert the message to uppercase
    message = ''.join(message.split()).upper()

    # Calculate the number of columns based on the length of the key
    num_columns = len(key)

    # Calculate the number of rows required
    # Equivalent to math.ceil(len(message) / num_columns)
    num_rows = -(-len(message) // num_columns)

    # Create an empty grid to store the message
    grid = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]

    # Fill the grid with the characters of the message
    index = 0
    for col in key:
        col_index = key.index(col)
        for row in range(num_rows):
            if index < len(message):
                grid[row][col_index] = message[index]
                index += 1

    # Read out the grid column by column to get the encrypted message
    encrypted_message = ''
    for row in range(num_rows):
        for col in range(num_columns):
            encrypted_message += grid[row][col]

    return encrypted_message


def decrypt(encrypted_message, key):
    # Calculate the number of columns based on the length of the key
    num_columns = len(key)

    # Calculate the number of rows required
    # Equivalent to math.ceil(len(encrypted_message) / num_columns)
    num_rows = -(-len(encrypted_message) // num_columns)

    # Create an empty grid to store the encrypted message
    grid = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]

    # Fill the grid with the characters of the encrypted message
    index = 0
    for col in key:
        col_index = key.index(col)
        for row in range(num_rows):
            grid[row][col_index] = encrypted_message[index]
            index += 1

    # Read out the grid row by row to get the decrypted message
    decrypted_message = ''
    for row in range(num_rows):
        for col in range(num_columns):
            decrypted_message += grid[row][col]

    return decrypted_message


# Get user input for message and key
message = input("Enter the message: ")
key = input("Enter the key: ")

# Encrypt the message
encrypted_message = encrypt(message, key)
print("Encrypted:", encrypted_message)

# Decrypt the message
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted:", decrypted_message)
