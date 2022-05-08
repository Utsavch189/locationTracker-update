import random


def ID(username):
    a=random.randint(101,999)
    idd=username.upper()+str(a)
    return idd

def password():
    return random.randint(1001,9999)