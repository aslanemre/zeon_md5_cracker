import hashlib as cracker
print("""
##########################################
#                                        #
#    Zeon MD5 Password Cracker Tool v1   #
#                                        #
##########################################
      """)
crackMe = input("[ ? ] Enter the md5 hash > ")
passWordlist = input("[ ? ] Enter the wordlist path > ")
def crack(crackMe):
    try:
        wordlist = open(passWordlist, "r")
    except:
        print("[ ! ] Wordlist file not found!")
    for passwd in wordlist:
        encrypted_pass = passwd.encode('utf-8')
        hashed_pass = cracker.md5(encrypted_pass.strip())
        digest = hashed_pass.hexdigest()
        if digest == crackMe:
            print("[ + ] Password found > ", passwd)
            break
        else:
            print("[ ! ] Password not found > ", passwd)
            continue
crack(crackMe)