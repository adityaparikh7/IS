def matrix(x, y, initial):
    return [[initial for _ in range(x)] for _ in range(y)]


def create_matrix():
    key = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_set = set(key)
    result = []

    for c in key:
        if c not in result:
            result.append(c)

    for i in range(65, 91):
        if chr(i) not in result:
            if i == 73 and chr(74) not in result:
                result.append("I")
            elif i != 74:
                result.append(chr(i))

    k = 0
    my_matrix = matrix(5, 5, 0)
    for i in range(5):
        for j in range(5):
            my_matrix[i][j] = result[k]
            k += 1
    return my_matrix


def locindex(matrix, c):
    loc = []
    if c == 'J':
        c = 'I'
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if c == char:
                loc.extend([i, j])
                return loc


def playfair_encrypt(my_matrix, msg):
    msg = msg.upper().replace("J", "I").replace(" ", "")
    i = 0
    for s in range(0, len(msg) + 1, 2):
        if s < len(msg) - 1:
            if msg[s] == msg[s + 1]:
                msg = msg[:s + 1] + 'X' + msg[s + 1:]
    if len(msg) % 2 != 0:
        msg = msg[:] + 'X'
    ciphertext = ""
    while i < len(msg):
        loc = locindex(my_matrix, msg[i])
        loc1 = locindex(my_matrix, msg[i + 1])
        if loc[1] == loc1[1]:
            ciphertext += "{}{}".format(my_matrix[(loc[0] + 1) %
                                        5][loc[1]], my_matrix[(loc1[0] + 1) % 5][loc1[1]])
        elif loc[0] == loc1[0]:
            ciphertext += "{}{}".format(
                my_matrix[loc[0]][(loc[1] + 1) % 5], my_matrix[loc1[0]][(loc1[1] + 1) % 5])
        else:
            ciphertext += "{}{}".format(my_matrix[loc[0]]
                                        [loc1[1]], my_matrix[loc1[0]][loc[1]])
        i = i + 2
    return ciphertext


def playfair_decrypt(my_matrix, msg):
    msg = msg.upper().replace("J", "I").replace(" ", "")
    plaintext = ""
    i = 0
    while i < len(msg):
        loc = locindex(my_matrix, msg[i])
        loc1 = locindex(my_matrix, msg[i + 1])
        if loc[1] == loc1[1]:
            plaintext += "{}{}".format(my_matrix[(loc[0] - 1) %
                                       5][loc[1]], my_matrix[(loc1[0] - 1) % 5][loc1[1]])
        elif loc[0] == loc1[0]:
            plaintext += "{}{}".format(my_matrix[loc[0]][(loc[1] - 1) %
                                       5], my_matrix[loc1[0]][(loc1[1] - 1) % 5])
        else:
            plaintext += "{}{}".format(my_matrix[loc[0]]
                                       [loc1[1]], my_matrix[loc1[0]][loc[1]])
        i = i + 2
    return plaintext


if __name__ == "__main__":
    my_matrix = create_matrix()

    plaintext = input("Enter the plaintext: ")
    ciphertext = playfair_encrypt(my_matrix, plaintext)
    print(f"Ciphertext: {ciphertext}")

    decrypted_text = playfair_decrypt(my_matrix, ciphertext)
    print(f"Decrypted text: {decrypted_text}")
