from collections import UserString

class Mystring(UserString):
    def head(self, n=1):
        return self.data[:n]

    def tail(self, n=1):
        return self.data[-n:]

s1 = Mystring("prepa big data")
print(s1.data) 
print(s1.head())    
print(s1.head(2))    
print(s1.tail())
print(s1.tail(3))