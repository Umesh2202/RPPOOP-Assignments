from abc import ABC, abstractmethod


class laptop(ABC):
    def __init__(self):
        self.ram = input("enter ram:")
        self.name = input("enter name of laptop:")
        self.cpu = input("enter cpu: ")
        self.storage = input("enter total storage capacity :")

    def specs(self):
        return f"This is a {self.name}  laptop ,with {self.ram} ram,and storage of {self.storage},it is powered by {self.cpu} "

    @abstractmethod
    def usability(self):
        pass


class gaming(laptop):
    def __init__(self):
        print("This is a gaming laptop")
        self.name = input("enter name of laptop :")
        self.storage = input("enter total storage capacity ")
        self.cpu = input("enter cpu: ")
        self.gpu = input("enter gpu: ")
        self.ram = input("enter ram: ")

    def usability(self):
        print("gaming laptop is used for high end gaming , for high end games which requires high refresh rate and peak performance and fast responses, this type of laptop is well supported for such purposes, an ordinary laptop cannot sustain and run such high perforamnce games smoothly ")

    def specs(self):
        return f"This is a {self.name} gaming laptop ,with {self.ram} ram,and storage of {self.storage},it is powered by {self.cpu}, and {self.gpu}graphic card"


class foldable360(laptop):
    def usability(self):
        print("This is a foldable 360 degree laptop")
        print("this laptop is specalized for using laptop very flexibly and according ton one's own convenience it can be folded completely in 360 degree")


class macbook(laptop):
    def __init__(self):
        self.cpu = "m1"
        self.batterylife = "1day"

    def usability(self):
        print("macbooks are used immensely by corporates , mainly because of its simplicity and high performance , it is very light weight and hence easy to carry")


class pro(macbook):
    def __init__(self):
        print("This is macbook pro")
        self.cpu = "m1pro"
        self.batterylife = "2day"


asusrog = gaming()
# lenovo=foldable360()
m1 = macbook()
print(asusrog.specs())
