# Conversion of one datatypes into another datatype is called typescasting 
# https://www.scaler.com/topics/type-casting-in-python/
#  1. explicit ------> built in functions ko use kr ka khud se krna according to the reqiurements of the situation   like int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict()
a = "5"
b = "6"
print(a + b)
print(int(a) +int(b))

#  2. implicit ------> automatically ho jata ha by python, isme datatypes ka precendence order hota ha like agr ak datatype int ha or ak float to inko add krny se jo answer aya ga wo float me aya ga ku kay float ki precendece int se zyada ha
a = 10.5
b = 1
print(a + b)
 # Errors
print("Two types of error")
c = "a"
d = 1
print("error1")
print("error2")
print(int(c) + d)
print(c + d)
