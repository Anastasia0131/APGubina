import doctest


class Person:
    def __init__(self, age: int, name: str, surname: str):
        """
        Конструктор класса Человек

        :param age: возраст человека
        :param name: имя человека
        :param surname: фамилия человека

        Примеры:
        >>> andrey = Person(19, 'Анастасия', 'Губина')
        """

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом")
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if not isinstance(surname, str):
            raise TypeError("Фамилия должна быть строкой")

        if (age < 0) or (age > 120):
            raise ValueError("Возраст должен быть в диапазоне от 0 до 120 лет")
        if len(name) < 1 or len(name) > 50:
            raise ValueError("Имя не может быть пустой строкой или превышать 50 символов")
        if len(surname) < 1 or len(surname) > 50:
            raise ValueError("Фамилия не может быть пустой строкой или превышать 50 символов")

        self.age = age
        self.name = name
        self.surname = surname

    def greeting(self) -> None:
        """
        Приветствие человека

        :return: Вывод приветствия с фамилией и именем человека

        Примеры:
        >>> anastasia = Person(19, 'Анастасия', 'Губина')
        >>> anastasia.greeting()
        Привет, я Анастасия Губина
        """
        print(f"Привет, я {self.name} {self.surname}")

    def get_older(self) -> int:
        """
        Увеличить возраст человека на один год

        :return: текущий возраст человека

        Примеры:
        >>> anastasia = Person(19, 'Анастасия', 'Губина')
        >>> print(anastasia.get_older())
        20
        """
        self.age += 1
        return self.age


if __name__ == "__main__":
    doctest.testmod()
