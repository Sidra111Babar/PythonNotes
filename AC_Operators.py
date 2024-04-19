#--------------------------------Arithematic operators (Mathematical opereators)----------------------------------------------
#  https://www.studysmarter.co.uk/explanations/computer-science/computer-programming/python-arithmetic-operators/#:~:text=Basic%20arithmetic%20operators%20in%20Python,such%20as%20integers%20and%20floats.
print("Arithematice operators")
print("1 + 2 = ", 1 + 2)
print("1 - 2 = ", 1 - 2)
print("1 + 2 = ", 1 * 2)
print("1 / 2 = ", 1 / 2)
print("1 / 2 = ", 1 // 2)  #Floor division operator round point kay bad vali value ignore kr de ga
print("10 // 2 = ", 10 // 2)
print("10 // 3 = ", 10 // 3)
print("2 % 5 = ", 2 % 5)
print("2 ** 3 = ", 2 ** 3) # exponential operator  multiply 2 3 times
#--------------------------------Assignment operators (Mathematical opereators)----------------------------------------------
# https://networklessons.com/python/python-assignment-operators
print("Assignment Operators")
x = 5
print(5)
x = 1 + 2
print(x)
x += 3 # output should 6
print(x)
x -= 3 #output should 3 (x = 6 here 6 - 3 = 3)
print(x)
#same for all other operators
#--------------------------------Comparison operators (Mathematical opereators)----------------------------------------------
# https://study.com/learn/lesson/python-not-equal-conditional-operators.html#:~:text=The%20six%20comparison%20operators%20are,such%20as%20integers%20or%20strings.
print("Comparison operators")
a = 5
print(a == 5) #check if a is really equal to 5 return true
print(a != 5)
print(a > 5)
print(a < 5)
print(a >= 5)
print(a <= 5)
#--------------------------------Logical operators (Mathematical opereators)----------------------------------------------
print("Logical Operators(already clear)")
#  https://pieriantraining.com/python-logical-operators-what-is/#:~:text=There%20are%20three%20types%20of,and%20y%20are%20positive.%22)
# three types 1. and         2. or            3. not
#--------------------------------Identity operators (Mathematical opereators)----------------------------------------------
# 1.is 2.is not
# https://www.studysmarter.co.uk/explanations/computer-science/computer-programming/identity-operator-in-python/#:~:text=The%20identity%20operator%20is%20defined,they%20point%20to%20different%20objects.
print("Identity Opertors")
a = 1
b = 2
print(a is b) #return false because both are not equal
print(a is not b) # return true
print(5 is not 6)
print(2 is 2)
#--------------------------------Membership operators (Mathematical opereators)----------------------------------------------
# 1. in         2. not in
# https://www.studysmarter.co.uk/explanations/computer-science/computer-programming/membership-operator-in-python/#:~:text=In%20Python%2C%20there%20are%20two,string%2C%20list%2C%20or%20tuple.
print("Membership operators")
list = [1,2,3,4,5,6]
print(5 in list)
print(5 not in list)
#--------------------------------Bitwise operators (Mathematical opereators)----------------------------------------------
#  https://www.studysmarter.co.uk/explanations/computer-science/computer-programming/membership-operator-in-python/#:~:text=In%20Python%2C%20there%20are%20two,string%2C%20list%2C%20or%20tuple.
# Note : Need to explore more
print("bitwise Operators") # deal with binary numbers
print(0 & 1) # 0 in binary is 00 and 1 in binary is 01 outputis 0 because 0 & 0(one 0 is from binary 0 and other 0 is from binary 1) = 0 , 0 & 1 (0 is from binary 2nd 0 adn 1 is from binary 1) = 0 now match answers of both 0 & 0 so overall answers is 0
print(0 | 1)
