class Shape:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2
        print("Hey")

    def get_params(self):
        return f"Параметры Shape: {self.param_1}, {self.param_2}"


class Material:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2
        print("Hi")

    def get_params(self):
        return f"Параметры Material: {self.param_1}, {self.param_2}"

    def material_method(self):
        return "Material"


class Triangle(Material, Shape):
    pass


t = Triangle(10, 20)
print(t.get_params())
#print(t.material_method())
