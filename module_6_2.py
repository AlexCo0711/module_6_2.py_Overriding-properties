# Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."

# объявление класса Vehicle - это любой транспорт
class Vehicle:
    # атрибут класса
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    # атрибуты объекта (экземпляра) класса Vehicle
    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        # владелец транспорта. (владелец может меняться)
        self.owner = owner
        # модель (марка) транспорта. (мы не можем менять название модели)
        self.__model = model
        # мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self.__engine_power = engine_power
        # название цвета. (мы не можем менять цвет автомобиля своими руками)
        self.__color = color

    # Метод get_model - возвращает строку: "Модель: <название модели транспорта>" с
    # атрибутом объекта self.__model
    def get_model(self):
        return f'Модель: {self.__model}'

    # Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>" с
    # атрибутом объекта self.__engine_power
    def get_horsepower(self):
        return f'Мощность двиаеля: {self.__engine_power}'

    # Метод get_color - возвращает строку: "Цвет: <цвет транспорта>" с атрибутом
    # объекта self.__color
    def get_color(self):
        return f'Цвет: {self.__color}'

    # Метод print_info - распечатывает результаты методов (в том же порядке)
    # get_model, get_horsepower, get_color; а так же владельца в конце в формате
    # "Владелец: <имя>"
    def print_info(self):
        # вывод на консоль переменных в столбик. Параметр sep определяет порядок вывода (по
        # умолчанию - пробел, \n - каждый элемент print() выводить с новой строки)
        print(self.get_model(), self.get_horsepower(), self.get_color(), f'Владелец: {self.owner}', sep="\n")

    # Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color, если
    # он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить
    # цвет на <новый цвет>".
    def set_color(self, new_color: str):
        # перевод заводских цветов окраски (__COLOR_VARIANTS) в нижний регистр
        factory_color = [color.lower() for color in self.__COLOR_VARIANTS]
        # условие проверки new_color с переводом в нижний регистр заводским цветам
        # окраски (атрибут класса - __COLOR_VARIANTS переведен в нижний регистр - factory_color),
        # т.е. проверка цветов без учета регистра
        if new_color.lower() in factory_color:
            # изменяем цвет окраски согласно заводкому набору цветов
            self.__color = new_color
        else:
            # несоответствие нового цвета заводскому набору цветов
            print(f'Нельзя сменить цвет на {new_color}')

# объявление класса Sedan - наследник класса Vehicle (дочерний класс)
class Sedan(Vehicle):
    # Атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров)
    __PASSENGERS_LIMIT = 5


if __name__ == '__main__':
    # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (цвет)(в т.ч. вызывая методы)
    # цвет не из заводского набора
    vehicle1.set_color('Pink')
    # цвет из заводского набора
    vehicle1.set_color('BLACK')
    # Меняем свойства (владельца)
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()


