if __name__ == "__main__":
    class Car:
        FIRST_CAR_YEAR = 1885

        def __init__(self, year: int, color: str):
            """
            Создание и подготовка к работе объекта "Машина"

            :param year: Год выпуска автомобиля
            :param color: Цвет машины

            :raise TypeError: Если year не int, если color не str
            :raise ValueError: Если year < 1885
            """
            if not isinstance(year, int):
                raise TypeError("Год машины должен быть int")
            if year < 1885:
                raise ValueError("Год машины должен быть >= 1885")
            if not isinstance(color, str):
                raise TypeError("Цвет машины должен быть str")
            self._year = year  # год выпуска автомобиля нельзя изменить, можно только прочитать
            self.color = color

        @property
        def year(self) -> int:
            return self._year

        def paint(self, new_color: str) -> None:
            """
            Метод, который перекрашивает машину в новый цвет
            :param new_color: Новый цвет машины

            :raise TypeError: Если новый цвет машины не str
            """
            if not isinstance(new_color, str):
                raise TypeError("Новый цвет машины должен быть str")
            self.color = new_color

        @staticmethod
        def info() -> str:
            """
            Метод, который возвращает информацию об автомобиле
            :return: строка с информацией
            """
            return "Автомобиль - моторное безрельсовое дорожное или внедорожное, чаще всего автономное, транспортное " \
                   "средство, используемое для перевозки людей или грузов, имеющее от четырёх колёс."

        def __str__(self) -> str:
            """
            Метод, который возвращает текстовое представление об экземпляре класса Car
            :return: строка с информацией об экземпляре
            """
            return f'Машина {self.year} года выпуска, цвет - "{self.color}"'

        def __repr__(self) -> str:
            """
            Метод, который возвращает строку, показывающую, как может быть инициализирован экземпляр класса Car
            :return: валидная python строка
            """
            return f'{self.__class__.__name__}({self.year}, {self.color!r})'


    class Bmw(Car):
        def __init__(self, year: int, color: str, m_series: bool):
            """
            Создание и подготовка к работе объекта "Бмв"

            :param year: Год выпуска автомобиля
            :param color: Цвет машины
            :param m_series: Принадлежит ли бмв серии М

            :raise TypeError: Если year не int, если color не str, если m_series не bool
            :raise ValueError: Если year < 1885
            """
            super().__init__(year, color)
            if not isinstance(m_series, bool):
                raise TypeError("Параметр m_series машины должен быть bool")
            self.m_series = m_series

        @staticmethod
        def info() -> str:
            """
            Функция, которая возвращает информацию о БМВ
            :return: строка с информацией
            """
            return "БМВ - баварская компания с более чем вековой историей, сегодня производит легковые автомобили и " \
                   "мотоциклы."

        def __str__(self) -> str:
            """
            Метод, который возвращает текстовое представление об экземпляре класса Bmw
            :return: строка с информацией об экземпляре
            """
            if self.m_series:
                return f'БМВ {self.year} года выпуска, цвет - "{self.color}", серии M'

            else:
                return f'БМВ {self.year} года выпуска, цвет - "{self.color}"'

        def __repr__(self) -> str:
            """
            Метод, который возвращает строку, показывающую, как может быть инициализирован экземпляр класса Bmw
            :return: валидная python строка
            """
            return f'{self.__class__.__name__}({self.year}, {self.color!r}, {self.m_series})'
    pass
