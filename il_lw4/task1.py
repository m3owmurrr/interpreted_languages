# Класс котопес
# Экземпляр инициализируется двумя целыми числами: первое число относиться к кошке, второе - к собаке
# Класс реализует следующие методы:
# climb_tree() - может лазить по деревьям - возвращает True, если часть кошки больше или равна части собаки
# bark() - если собаки больше, то возвращает строку "Woof!", иначе "Meow!"
# eat(food, value) - может есть только рыбу(fish) или мясо(meat). Если съедает рыбу, то из части собаки вычитается количество
#   съеденного, кошке добавляется, иначе наоборот: у кошки вычитается, а собаке добавляется. Нельзя привысить значение 100 или уменьшить ниже 0
# get_parts() - возвращает список значений [ часть кошки, часть собаки]
#
# создать класс-наследник от класса Котопес, например Космический КотоПес
#
# Обязательно использовать конструктор, декораор и метод __str__

def spacesuit(func):
    def wrapper(*args, **kwargs):
        print(f"shhh... {func(*args, **kwargs)}... shhh...")
        return ''
    return wrapper

class CatDog:
    def __init__(self, catNum, dogNum):
        self.cat = catNum
        self.dog = dogNum

    def __str__(self):
        return f"This catdog is {self.cat} parts of cat and {self.dog} parts of dog"

    def climbTree(self):
        if (self.cat >= self.dog):
            return True
        return False

    def bark(self):
        if (self.cat >= self.dog):
            return "Meow!"
        return "Woof!"

    def eat(self, food, value):
        if (food == "fish"):
                self.cat += value if self.cat + value <= 100 else value - (self.cat + value)%100
                self.dog -= value if self.dog - value >= 0 else value - abs(self.dog - value)
        elif (food == "meat"):
                self.dog += value if self.dog + value <= 100 else value - (self.dog + value)%100
                self.cat -= value if self.cat - value >= 0 else value + abs(self.cat - value)
        else:
            print("Unknown food")

    def getParts(self):
        return [self.cat, self.dog]


class SpaceCatDog(CatDog):
    def bark(self):
        return "..."

    @spacesuit
    def barkInSpace(self):
        if (self.cat >= self.dog):
            return "Meow!"
        return "Woof!"



cd1 = CatDog(50, 50)
cd1.eat("fish", 100)
print(str(cd1))
print(cd1.bark())
print(cd1.getParts())
print("\n")

cd2 = SpaceCatDog(60, 40)
print(str(cd2))
print(cd2.bark())
print(cd2.barkInSpace())
