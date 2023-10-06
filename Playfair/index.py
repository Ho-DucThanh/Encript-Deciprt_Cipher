def generate_playfair_key(key): # Xử lí khóa key đầu vào và tạo ra matrix 5*5
    key = key.replace(" ", "").upper()
    key = key.replace("J", "I")  # Thay thế J bằng I
    key_list = list(key) # Chuyển đổi 1 chuỗi sang list: AB -> ['A', 'B'] 
    key_set = [] # Không cho kí tự nào trùng lặp
    for char in key_list:
        if char not in key_set:
            key_set.append(char)

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    remaining_letters = []  # Tạo mảng mới gồm các kí tự thuộc alphabet mà không có trong key_set
    for letter in alphabet:
        if letter not in key_set and letter != 'J': # Loại trừ J
            remaining_letters.append(letter)

    key_matrix = key_set + remaining_letters # Hợp 2 list lại theo thứ tự key_set -> remaining_letters
    key_matrix = [key_matrix[i:i+5] for i in range(0, 25, 5)] # Chia list trên thành matrix 5*5 theo row
    # vòng for -> chuỗi [0, 5, 10, 15, 20]
    # key_matrix[i:i+5] -> lấy các phần tử trong key_matrix từ i -> i+5 
    # matrix chia thành các row theo thứ tự 0->4, 5->9 ..... , 20->24
    return key_matrix


def find_letter(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col


def playfair_encrypt(plaintext, key):
    key_matrix = generate_playfair_key(key)  # tạo key matrix 5*5
    ciphertext = ""
    plaintext = plaintext.replace(" ", "").upper()
    plaintext = plaintext.replace("J", "I")  # Thay thế J bằng I
    
    # Chia văn bản thành cặp ký tự
    for i in range(0, len(plaintext) - 1, 2):
        if (plaintext[i] == plaintext[i+1]):  # Nếu 2 kí tự cạnh nhau giống nhau (AA) và kí tự đó nằm ở vị trí chẵn
            plaintext = plaintext[:i+1] + 'X' + plaintext[i+1:] # Chèn X vào 2 kí tự giống nhau đó
            # [:i + 1] trước i + 1 ,  [i + 1:] sau i + 1 
            
    # Thêm "X" vào cuối nếu chiều dài của plainText là số lẻ
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
        
    pairs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)] # Chia plainText thành 1 list, mỗi phần tử trong list chứa 2 kí tự 
    
    for pair in pairs:  # pair gồm 2 kí tự
        row1, col1 = find_letter(key_matrix, pair[0])  # pair[0] = 'H, L, L, O, E, N, A, L' (lần lượt là các kí tự đầu tiên của chuỗi pair)
        # Lấy ra giá trị của pair[0], check xem nằm ở row và col nào
        row2, col2 = find_letter(key_matrix, pair[1])  # pair[1] = 'E, X, O, N, A, D, L, X' (lần lượt là các kí tự sau của chuỗi pair)
        # Lấy ra giá trị của pair[1], check xem nằm ở row và col nào
        
        if row1 == row2: # pair cùng hàng
            # Dịch phải theo hàng 1 bit (cuối -> đầu (chia dư 5) ) 
            ciphertext += key_matrix[row1][(col1 + 1) %
                                           5] + key_matrix[row2][(col2 + 1) % 5]
            
        elif col1 == col2: # pair cùng cột
            # Dịch xuống dưới theo cột 1 bit (cuối -> đầu (chia dư 5) )
            ciphertext += key_matrix[(row1 + 1) %
                                     5][col1] + key_matrix[(row2 + 1) % 5][col2]
            
        else: # Lấy theo hình chữ nhật (theo thứ tự của pair)
            ciphertext += key_matrix[row1][col2] + key_matrix[row2][col1]

    return ciphertext


def playfair_decrypt(ciphertext, key):
    key_matrix = generate_playfair_key(key)
    plaintext = ""
    ciphertext = ciphertext.replace(" ", "").upper()
    ciphertext = ciphertext.replace("J", "I")  # Thay thế J bằng I
    
    pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    for pair in pairs:
        row1, col1 = find_letter(key_matrix, pair[0])
        row2, col2 = find_letter(key_matrix, pair[1])

        if row1 == row2:
            # Dịch trái theo hàng 1 bit (đầu -> cuối, xử lý trường hợp âm)
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
            plaintext += key_matrix[row1][col1] + key_matrix[row2][col2]
        elif col1 == col2:
            # Dịch lên trên theo cột 1 bit (đầu -> cuối, xử lý trường hợp âm)
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
            plaintext += key_matrix[row1][col1] + key_matrix[row2][col2]
        else:
            # Lấy theo hình chữ nhật (theo thứ tự của pair)
            plaintext += key_matrix[row1][col2] + key_matrix[row2][col1]
            

    # Xử lí đưa về plainText ban đầu 
    new_plaintext = ""
    i = 0
    while i < len(plaintext):
        if i < len(plaintext) - 2 and plaintext[i] == plaintext[i + 2]:
            new_plaintext += plaintext[i]
            i += 1
        else:
            new_plaintext += plaintext[i]
        i += 1

    # Kiểm tra nếu ký tự cuối cùng là 'X' và độ dài của plainText là số chẵn
    if len(plaintext) % 2 == 0 and plaintext[-1] == 'X':  # plaintext[-1]: truy cập đến phần tử cuối cùng
        new_plaintext = new_plaintext[:-1]  # Loại bỏ ký tự 'X' cuối cùng, plaintext[:-1] : xóa phần tử cuối cùng 

    return new_plaintext



while True:
    text = input("Nhập text: ")
    if len(text) < 1 or not text.isalpha():
        print("Text không hợp lệ! Vui lòng nhập lại")
        continue
    break

while True:
    key = input("Nhập key: ")
    if len(text) < 1 or not key.isalpha():
        print("Key không hợp lệ! Vui lòng nhập lại")
        continue
    break

ciphertext = playfair_encrypt(text, key)
print("Encrypted ciphertext:", ciphertext)

while True:
    cipherText = input("Nhập cipher text: ")
    if len(cipherText) < 1 or not cipherText.isalpha():
        print("Cipher không hop le! nhap lai")
        continue
    break



plaintext = playfair_decrypt(ciphertext, key)
print("Decrypted plaintext:", plaintext)

plaintext = playfair_decrypt(cipherText, key)
print("Decrypted ciphertext 1:", plaintext)



