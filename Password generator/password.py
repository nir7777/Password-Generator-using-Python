# Random Password Generator.
# Random Module is already install in Python, 
# no need to install it explicitly.


import random
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers    = "1234567890"
symbols    = "@#$&*()"

combine_all = lower_case+upper_case+numbers+symbols
length = 8
generate_password = "".join(random.sample (combine_all, length))
print(generate_password)