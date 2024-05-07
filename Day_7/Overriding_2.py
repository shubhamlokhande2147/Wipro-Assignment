class Sim:
    def network(self):
        print("default network!!")

class Jio(Sim):
    def network(self):
        print("Jio network")

class BSNL(Sim):
    def network(self):
        print("BSNL network")
        super().network()

class Idea(Sim):
    def network(self):
        print("Idea network")
        super().network()

s1 = Jio()
s1.network()

s2 = BSNL()
s2.network()

s3 = Idea()
s3.network()
