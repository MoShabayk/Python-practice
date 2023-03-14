def draw_index_table():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rows = []
    for i in range(0, len(letters), 10):
        row = []
        for j in range(i, i + 10):
            if j < len(letters):
                row.append("| {:2} {} ".format(j, letters[j]))
        rows.append(row)
    for row in rows:
        print("".join(row) + "|")
def decrypt_caesar(ciphertext, key):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            char_index = letters.find(char.upper())
            new_index = (char_index + key) % 26
            new_char = letters[new_index]
            if char.islower():
                plaintext += new_char.lower()
            else:
                plaintext += new_char
        else:
            plaintext += char
    return plaintext
def main():
    draw_index_table()

    ciphertext = """Bcyp Qml,

G fytc y dyrfcpjw ybtgac dmp wms:
jcypl rfc Nwrfml npmepykkgle jylesyec!

Jmtc,

Byb"""
    key = int(input("Enter the key: "))
    plaintext = decrypt_caesar(ciphertext, key)
    print(plaintext)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
