class person:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_name(self):
        print("Name: ", self.name)

    def get_code(self):
        print("Code: ", self.code)


class account(person):
    def __init__(self, pay):
        self.pay = pay

    def get_pay(self):
        print("Pay: Rs ", self.pay)


class Admin(person):
    def __init__(self, experience):
        self.experience = experience

    def get_experience(self):
        print("Experience: "+str(self.experience)+"yrs")


class Employee(account, Admin):
    def __init__(self, name, code, pay, experience):
        person.__init__(self, name, code)
        account.__init__(self, pay)
        Admin.__init__(self, experience)

    def get_data(self):
        person.get_name(self)
        person.get_code(self)
        account.get_pay(self)
        Admin.get_experience(self)


person1 = Employee("Ram", "03", 112233, 10)
person1.get_data()
