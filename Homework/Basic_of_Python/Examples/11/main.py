class MyClass:
    def __init__(self, p):
        self.p = p

    def m_1(self):
        # self.m_2()
        # MyClass.m_2()
        # self.m_3()
        # MyClass.m_3()
        return ("Hi")

    @staticmethod
    def m_2():
        #print(self.m_1())
        print(MyClass(8).p)
        #print("Python")
        # MyClass.m_3()

    @classmethod
    def m_3(cls):
        #print(cls)
        #MyClass.m_2()
        print(MyClass(7).p)


my_1 = MyClass(65)
my_1.m_1()
# MyClass.m_1() # не работает

my_1.m_2()
MyClass.m_2()

my_1.m_3()
MyClass.m_3()