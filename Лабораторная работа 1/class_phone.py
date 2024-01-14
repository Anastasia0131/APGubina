import doctest


class Phone:
    def __init__(self, number: str, owner: str) -> None:
        """
        Конструктор класса номер телефона

        :param number: номер телефона
        :param owner: имя владельца

        Примеры:
        >>> phone = Phone('89539347052', 'Анастасия')
        """

        if not isinstance(number, str):
            raise TypeError("Номер телефона должен быть строкой")
        if not isinstance(owner, str):
            raise TypeError("Имя владельца должно быть строкой")

        if len(owner) < 1 or len(owner) > 50:
            raise ValueError("Имя владельца не может быть пустой строкой и не может превышать 50 символов")
        if len(number) != 11:
            raise ValueError("Номер телефона должен состоять из 11 символов (включая код страны)")

        self.number = number
        self.owner = owner

    def call_to_person(self, person_to_call: str) -> None:
        """
        Совершить вызов другому человеку

        :param person_to_call: имя человека, которому звоним
        :return: Совершение звонка

        Примеры:
        >>> iphone = Phone('89539347052', 'Анастасия')
        >>> iphone.call_to_person('Катя')
        Андрей звонит Артём с номера 89539347052
        """

        print(f"{self.owner} звонит {person_to_call} с номера {self.number}")

    def update_phone_number(self, new_number: str) -> None:
        """
        Перезаписать номера телефона

        :param new_number: новый номер телефона
        :return: новый номер телефона
        >>> iphone = Phone('89539347052', 'Анастасия')
        >>> iphone.update_phone_number('89539347053')
        Анастасия обновила номер на 89539347053
        """
        self.number = new_number
        print(f"{self.owner} обновила номер на {self.number}")


if __name__ == '__main__':
    doctest.testmod()
