class GrandFather:

    def work(self):
        print("Work Hard")

    def farm(self):
        print("Granderfather farm and agriculture")

class Father(GrandFather):

    def work(self):
        print("work Smart")

    def office(self):
        print("Father work at office")

class Son(Father):
    pass

s = Son()
s.work()
s.farm()
s.office()