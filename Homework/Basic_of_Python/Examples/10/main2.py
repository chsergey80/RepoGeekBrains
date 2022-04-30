from abc import ABC, abstractmethod


class MyOwnABC(ABC):
    @abstractmethod
    def m_1(self):
        pass

    @abstractmethod
    def m_2(self):
        pass


class MyClass(MyOwnABC):
    def m_1(self):
        pass

    def m_2(self):
        pass


new_1 = MyClass()
