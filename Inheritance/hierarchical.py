class Ceo:
    def role(self):
        print("I am ceo")

    def organization(self):
        print("AD")

class Cto(Ceo):

    def role(self):
        print("i am cto")

    def Tech_department(self):
        print("Techinical")

class Cfo(Ceo):

    def role(self):
        print("i am cfo")

    def Finance_department(self):
        print("Financial")

class Dev(Cto):

    def role(self):
        print("i am developer")

class Cashier(Cfo):

    def role(self):
        print("i am Cashier")

d = Dev()
d.role()
d.Tech_department()

c = Cashier()
c.role()
c.Finance_department()

c.organization()
d.organization()

# c cant call Tech_department()
# d cant call Finance_department()
# MRO : method resolution order 

    