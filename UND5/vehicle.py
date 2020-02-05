class Vehicle():

    @property
    def Engine(self):
        return self.__Engine


    @Engine.setter
    def Engine(self, value):
        self.__Engine = value


    def On(self):
        return True


    def Off(self):
        return False


Fusca = Vehicle()

fusca_on = Fusca.On()
fusca_off = Fusca.Off()
Fusca.Engine = 1000

print(f"LIGAR: {fusca_on}")
print(f"DESLIGAR: {fusca_off}")
print(f"CILINDRADAS: {Fusca.Engine}")
