import random
passlen = int(input("enter the lenght of password"))
s="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+?"
p="".join(random.sample(s,passlen))
print(p)