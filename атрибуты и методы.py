class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            a = list(range(1, new_floor + 1))
            print(*a, sep='\n')

h1 = House('ЖК Республика', 27)
h2 = House('ЖК Санторини', 4)
h1.go_to(5)
h2.go_to(7)

