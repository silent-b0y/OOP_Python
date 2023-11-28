# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union


class Car:
    def __init__(self, color: str, max_speed: int):
        """
         Создание и подготовка к работе объекта "Машина"

        :param color: Цвет машины
        :param max_speed: Максимальная скорость машины в км/ч

        Примеры:
        >>> car = Car("Red", 200)  # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет машины должен быть str")
        self.color = color

        if not isinstance(max_speed, int):
            raise TypeError("Максимальная скорость машины должна быть int")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость машины должна быть положительным числом")
        self.max_speed = max_speed

    def paint(self, new_color: str) -> None:
        """
        Функция, которая перекрашивает машину в новый цвет
        :param new_color: Новый цвет машины

        :raise TypeError: Если новый цвет машины не str

        Примеры:
        >>> car = Car("Red", 200)
        >>> car.paint("Yellow")
        """
        if not isinstance(new_color, str):
            raise TypeError("Новый цвет машины должен быть str")
        ...

    def change_max_speed(self, new_max_speed: int) -> None:
        """
        Функция, которая изменяет максимальную скорость машины
        :param new_max_speed: Новая максимальная скорость машины в км/ч

        :raise TypeError: Если новая максимальная скорость машины не int
        :raise ValueError: Если новая максимальная скорость машины не положительное число

        Примеры:
        >>> car = Car("Red", 200)
        >>> car.change_max_speed(250)
        """
        if not isinstance(new_max_speed, int):
            raise TypeError("Новая максимальная скорость машины должна быть int")
        if new_max_speed <= 0:
            raise ValueError("Новая максимальная скорость машины должна быть положительным числом")
        ...


class Human:
    def __init__(self, name: str, age: int):
        """
         Создание и подготовка к работе объекта "Человек"

        :param name: Имя человека
        :param age: Возраст человека

        Примеры:
        >>> human = Human("Ivan", 20)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя человека должно быть str")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст человека должен быть int")
        if age < 0:
            raise ValueError("Возраст человека должен быть неотрицательным числом")
        self.age = age

    def rename(self, new_name: str) -> None:
        """
        Функция, которая переименовывает человека
        :param new_name: Новое имя человека

        :raise TypeError: Если новое имя человека не str

        Примеры:
        >>> human = Human("Ivan", 20)
        >>> human.rename("Denis")
        """
        if not isinstance(new_name, str):
            raise TypeError("Новое имя человека должно быть str")
        ...

    def celebrate_birthday(self) -> int:
        """
        Функция, которая празднует день рождения
        :return: Возраст человека после дня рождения

        Примеры:
        >>> human = Human("Ivan", 20)
        >>> human.celebrate_birthday()
        """
        ...


class Rectangle:
    def __init__(self, a: Union[int, float], b: Union[int, float]):
        """
         Создание и подготовка к работе объекта "Прямоугольник"

        :param a: Длина прямоугольника
        :param b: Ширина прямоугольника

        Примеры:
        >>> rectangle = Rectangle(2.5, 3.5)  # инициализация экземпляра класса
        """
        if not isinstance(a, (int, float)):
            raise TypeError("Длина прямоугольника должна быть int или float")
        if a <= 0:
            raise ValueError("Длина прямоугольника должна быть положительным числом")
        self.a = a

        if not isinstance(b, (int, float)):
            raise TypeError("Ширина прямоугольника должна быть int или float")
        if b <= 0:
            raise ValueError("Ширина прямоугольника должна быть положительным числом")
        self.b = b

    def calculate_perimeter(self) -> Union[int, float]:
        """
        Функция, которая вычисляет периметр прямоугольника
        :return: Периметр прямоугольника

        Примеры:
        >>> rectangle = Rectangle(2, 4)
        >>> rectangle.calculate_perimeter()
        """
        ...

    def calculate_area(self) -> Union[int, float]:
        """
        Функция, которая изменяет максимальную скорость машины
        :return: Площадь прямоугольника

        Примеры:
        >>> rectangle = Rectangle(2, 4)
        >>> rectangle.calculate_area()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
