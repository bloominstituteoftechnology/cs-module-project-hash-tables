#Add the salt
import random
salt = None


def make_hashed_password(pw, salt = random.random()):
    # salt = random.random()
    return hex(hash(pw)+salt)

def check_password(plaintext_pw, hashed_pw):
    hash_again = make_hashed_password(plaintext_pw, salt)
    
    return hash_again == hashed_pw

salt = random.random()
mypw = 'hello'
hashed_pw = make_hashed_password(mypw)

 
bcrypt