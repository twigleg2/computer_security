#gfinch

import crypt

print("enter username: ")
username = str(input())
print("enter password: ")
password = str(input())

passwd_file = open("passwd", "w")
shadow_file = open("shadow", "w")

passwd_file.write(username + ":x:1021:1020:userdata:/home/" + username + ":/bin/bash\n")

hashed_pw = crypt.crypt(password, crypt.METHOD_MD5)
shadow_file.write(username + ":" + hashed_pw + ":13064:0:99999:7:::\n")

passwd_file.close()
shadow_file.close()
