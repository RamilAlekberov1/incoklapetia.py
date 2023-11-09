class human:
    def __init__(self, n, a, h):
        print("Создан объект класса human: ")
        self.__name = n
        self.__age = a
        self.__height = h

    def print(self):
        print(f'Имя: {self.__name}')
        print(f'Возраст: {self.__age}')
        print(f'Рост: {self.__height}')
        print('-' * 30)
    
    @property
    def name(self):
        return self.__name.upper()
    
    @name.setter
    def name(self, n):
        self.__name = n.capitalize()
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, a):
        if (a > 0, a < 100):
            self.__age = a
        else:
            print('Некоректный возраст')
            
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if (h > 60, h < 250):
            self.__height = h
        else:
            print('Некоректный рост')

person1 = human('Шамиль', 111, 175)
person1.print()
person1.name = 'Роберт'
person1.age = 16
person1.height = 178
print(person1.name)
print(person1.age)
print(person1.height)