# Implement Playfair cipher as a substitution cipher: Encryption and decryption both without using a key

import string

def encrypt(plain_text):
    # Remove all spaces and convert to uppercase
    plain_text = plain_text.replace(" ", "").upper()
    # Remove all non-alphabetic characters
    plain_text = ''.join(filter(str.isalpha, plain_text))
    # Replace all J with I
    plain_text = plain_text.replace("J", "I")

    # Initialize the matrix with a size of 5x5
    matrix = [['' for _ in range(5)] for _ in range(5)]

    # Fill the matrix with the plain text
    i = 0
    j = 0
    for c in plain_text:
        matrix[i][j] = c
        j += 1
        if j == 5:
            j = 0
            i += 1

    # Check if the matrix is full
    if i == 5:
        return matrix

    # Fill the remaining cells with the remaining alphabets
    alphabets = list(string.ascii_uppercase)
    alphabets.remove("J")
    alphabets = ''.join(alphabets)
    for c in alphabets:
        if i < 5 and j < 5:  # Ensure we don't go beyond the matrix size
            matrix[i][j] = c
            j += 1
            if j == 5:
                j = 0
                i += 1

    # return matrix

    # Get the cipher text
    cipher_text = ""
    for i in range(0, len(plain_text), 2):
        c1 = plain_text[i]
        c2 = plain_text[i+1]
        r1 = 0
        c1 = 0
        r2 = 0
        c2 = 0
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == c1:
                    r1 = r
                    c1 = c
                if matrix[r][c] == c2:
                    r2 = r
                    c2 = c
        if r1 == r2:
            cipher_text += matrix[r1][(c1+1)%5]
            cipher_text += matrix[r2][(c2+1)%5]
        elif c1 == c2:
            cipher_text += matrix[(r1+1)%5][c1]
            cipher_text += matrix[(r2+1)%5][c2]
        else:
            cipher_text += matrix[r1][c2]
            cipher_text += matrix[r2][c1]

    return cipher_text

def decrypt(cipher_text):
    # Remove all spaces and convert to uppercase
    cipher_text = cipher_text.replace(" ", "").upper()
    # Remove all non-alphabetic characters
    cipher_text = ''.join(filter(str.isalpha, cipher_text))
    # Replace all J with I
    cipher_text = cipher_text.replace("J", "I")

    # Create a 5x5 matrix
    matrix = []
    for i in range(5):
        matrix.append([0] * 5)

    # Fill the matrix with the cipher text
    i = 0
    j = 0
    for c in cipher_text:
        matrix[i][j] = c
        j += 1
        if j == 5:
            j = 0
            i += 1

    # Get the plain text
    plain_text = ""
    for i in range(0, len(cipher_text), 2):
        c1 = cipher_text[i]
        c2 = cipher_text[i+1]
        r1 = 0
        c1 = 0
        r2 = 0
        c2 = 0
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == c1:
                    r1 = r
                    c1 = c
                if matrix[r][c] == c2:
                    r2 = r
                    c2 = c
        if r1 == r2:
            plain_text += matrix[r1][(c1-1)%5]
            plain_text += matrix[r2][(c2-1)%5]
        elif c1 == c2:
            plain_text += matrix[(r1-1)%5][c1]
            plain_text += matrix[(r2-1)%5][c2]
        else:
            plain_text += matrix[r1][c2]
            plain_text += matrix[r2][c1]

    return plain_text


if __name__ == "__main__":
    plain_text = input("Enter plain text: ")
    cipher_text = encrypt(plain_text)
    print("Cipher text:", cipher_text)
    plain_text = decrypt(cipher_text)
    print("Plain text:", plain_text)
