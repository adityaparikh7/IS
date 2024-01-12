# rail fence transposition cipher

def encrypt_rail_fence(text, key):
    fence = [[' ' for _ in range(len(text))] for _ in range(key)]

    direction = 1  # 1 for moving down, -1 for moving up
    row, col = 0, 0

    for char in text:
        fence[row][col] = char
        row += direction

        if row == key or row == -1:
            direction = -direction
            row += 2 * direction

        col += 1

    encrypted_text = ''.join(''.join(row) for row in fence)
    return encrypted_text


def decrypt_rail_fence(ciphertext, key):
    fence = [[' ' for _ in range(len(ciphertext))] for _ in range(key)]

    direction = 1
    row, col = 0, 0

    for _ in ciphertext:
        fence[row][col] = 'X'
        row += direction

        if row == key or row == -1:
            direction = -direction
            row += 2 * direction

        col += 1

    index = 0

    for r in range(key):
        for c in range(len(ciphertext)):
            if fence[r][c] == 'X':
                fence[r][c] = ciphertext[index]
                index += 1

    decrypted_text = ''
    direction = 1
    row, col = 0, 0

    for _ in ciphertext:
        decrypted_text += fence[row][col]
        row += direction

        if row == key or row == -1:
            direction = -direction
            row += 2 * direction

        col += 1

    return decrypted_text


plaintext = input("Enter the plaintext: ")
rails = int(input("Enter the number of rails: "))

encrypted_text = encrypt_rail_fence(plaintext, rails)
print("Encrypted:", encrypted_text)

decrypted_text = decrypt_rail_fence(encrypted_text, rails)
print("Decrypted:", decrypted_text)
