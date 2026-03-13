#random password generator
import random as rd
import string as st
length = (int)(input("Enter the length : "))
use_symbol =(input("Want to use symbols(yes/no) : "))
use_numbers = (input("Want to use numbers(yes/no) : "))
#starting of the password must be with simple letters
num = st.digits
upper = st.ascii_uppercase
rests = st.ascii_letters
symbol = st.printable
#creating a emtpy string for password
passwd=""
first_char = rd.choice(num)
second_char = rd.choice(upper)
third = rd.choice(symbol)
for i in range(length-3):
    #generating random different password each time
    ch = rd.choice(rests)
    passwd +=ch
passwd = first_char+second_char+passwd +third
print(f"The password generated is : {passwd}")fgbrtbrtbtbtbbbbbbbbbbbbbbb