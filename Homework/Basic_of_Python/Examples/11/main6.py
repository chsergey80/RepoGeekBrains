class MyClass:
    def __init__(self, p):
        self.p = p

    def __del__(self):
        print("Deleted object!")

    def __call__(self, new_p):
        self.p = new_p
        

my_new = MyClass(89)
# del my_new
# print(my_new.p)

my_new.p = 99
print(my_new.p)

my_new(107)
print(my_new.p)