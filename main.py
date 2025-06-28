class MyClass1:
    x = 10
    y = 20
    sum = x + y

obj1 = MyClass1()
print(obj1.x)
print(obj1.y)
print(obj1.sum)

#class variable & method

class MyClass2:
    a = 20 #class variable
    b = 30

    def addnumber(self,c,d): #class method
        sum = self.a + self.b + c + d
        print(sum)

    def subnumber(self):
        self.addnumber(10,20)

obj2 = MyClass2()
obj2.addnumber(30,20)
obj2.subnumber()

#constructor: __init__

class MyClass3:

    i = 50
    j = 50

    def __init__(self): #constructor method, constructor without parameter

        div = self.i / self.j
        print(div)
        print("Constructor")


obj3 = MyClass3()

class MyClass4:
    def __init__(self,k,l,z,iValue): #constructor with parameter
        self.z = z #instance variable z
        print(self.z)
        self.i = iValue
        print(self.i)
        sum = k + l
        print(sum)

    def addtwo(self): #instance method/class method
        print(self.z + self.i)

obj4 = MyClass4(10,20, 30, 2)
obj4.addtwo()

#static property
class MyClass5:
    n = 5
    g = 5
    u = 9

    @staticmethod
    def addthree():
        print(MyClass5.n + MyClass5.g + MyClass5.u)

MyClass5().addthree()

obj5 = MyClass5()
obj5.addthree()

#inheritance
class Father: #Parent Class
    f = 5
    s = 10

    def sub(self):
        result = self.f - self.s
        print(result)

    def mult(self):
        result2 = self.f * self.s
        print(result2)

class Mother: #Parent Class
    y = 10
    x = 10

    def sub2(self):
        result = self.x - self.y
        print(result)

    def mult2(self):
        result2 = self.x * self.y
        print(result2)


class Son(Father, Mother): #Child Class
    pass

obj6 =  Son()
obj6.sub()
obj6.mult()
obj6.sub2()
obj6.mult2()

class GranFather: #Parent Class
    f = 5
    s = 10

    def sub3(self):
        result = self.f - self.s
        print(result)

    def mult4(self):
        result2 = self.f * self.s
        print(result2)

class Father(GranFather): #Parent Class
    pass

class Son(Father): #Parent Class
    pass

obj7 = GranFather()
obj7.sub3()
obj7.mult4()

obj8 = Father()
obj8.sub3()
obj8.mult4()

obj9 = Son()
obj9.sub3()
obj9.mult4()