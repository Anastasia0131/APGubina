import random

"""
Этот список просто хранит в себе список лиг для соревнований, 
где F1 - самая высшая лига, F10 - самая низшая
"""
competitions = []
for i in range(10):
    competitions.append(f"F{i}")


class Car:
    """
    Абстрактный класс машины
    """

    def __init__(self, brand: str, year: int) -> None:
        """
        Конструктор абстрактной машины

        :param brand: название бренда машины
        :param year: год выпуска
        """
        self._brand = brand
        self._year = year

    def __str__(self) -> str:
        """
        Строковое представление объекта
        :return: строковое представление объекта
        """
        return f"Машина бренда {self._brand}, год выпуска - {self._year}"

    def __repr__(self) -> str:
        """
        Метод для получения строки, из которой можно воссоздать объект
        :return: строку, из которой можно воссоздать объект
        """
        return f"{self.__class__.__name__}(brand={self._brand!r}, year={self._year!r})"

    @property
    def brand(self) -> str:
        """
        Геттер названия бренда
        :return: название бренда
        """
        return self._brand

    @property
    def year(self) -> int:
        """
        Геттер года выпуска
        :return: год выпуска
        """
        return self._year


class SportCar(Car):
    max_speed: float = 0
    """
    Класс спортивной машины, который наследуется от абстрактной машины
    """

    def __init__(self, brand: str, year: int, max_speed: float) -> None:
        """
        Конструктор класса спортивной машины

        :param brand: название бренда машины
        :param year: год выпуска
        :param max_speed: максимальная скорость
        """
        super().__init__(brand, year)
        if not isinstance(max_speed, float):
            raise TypeError("Максимальная скорость должна быть типа float")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть больше 0")
        self._max_speed = max_speed

    def __repr__(self) -> str:
        """
        Метод для получения строки, из которой можно воссоздать объект
        Метод перегружен, так как добавилось новое поле.

        А метод __str__ остался тем же, потому что самые важные харектеристики для всех машин - бренд и год выпуска

        :return: строку, из которой можно воссоздать объект
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, year={self.year!r}, max_speed={self._max_speed!r})"

    def pick_random_competition(self) -> None:
        """
        Выбираем в каком соревновании будет участвовать машина
        :return: название соревнования
        """
        self._competition = random.choice(competitions)

    @property
    def competition(self) -> str:
        """
        Получение соревнования

        Есть только геттер, потому что машина по моей логике не может сама выбрать соревнование, ей кто-то назначает. В данном случае - рандом.
        :return: имя соревнования
        """
        return self._competition

    @property
    def speed(self):
        """
        Геттер скорости машины
        :return: макс. скорсть машины
        """
        return self._max_speed

    @speed.setter
    def speed(self, max_speed: int) -> None:
        """
        Сеттер скорости машины
        :param max_speed: максимальная скорость машины
        :return: максимальная скорость машины
        """
        self._max_speed = max_speed


if __name__ == "__main__":
    sport_car = SportCar("BMW", 2019, 200.3)
    print(sport_car)
    sport_car.pick_random_competition()
    print(sport_car.competition)
    print(sport_car._max_speed)
    sport_car.speed = 400.3
