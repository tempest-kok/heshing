import hashlib

def sign_up(file, login, password):
    file.write(login + " : " + password + "\n")

def sign_in(file, login, password):
    if login + " : " + password in file.read():
        return ("Welcome!!!")
    file.seek(0)
    if not login in file.read():
        return ("User not found")
    else:
        return ("Password is wrong")

a = int(input())
file_a = open(r"C:\Users\Admin\Desktop\LogandPass.txt", "a")
file_r = open(r"C:\Users\Admin\Desktop\LogandPass.txt", "r")
login = input()
password = input()
password = hashlib.sha256(password.encode())
password = password.hexdigest()

if a == 1:
    sign_up(file_a, login, password)
elif a == 2:
    print(sign_in(file_r, login, password))

file_a.close()
file_r.close()
