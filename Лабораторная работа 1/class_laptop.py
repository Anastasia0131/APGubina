import doctest


class Laptop:
    turn_on: bool = False

    def __init__(self, memory: int, company: str) -> None:
        """
        Конструктор класса ноутбук

        :param memory: количество оперативной памяти, Гб
        :param company: компания-производитель

        Примеры:
        >>> laptop = Laptop(16, 'Asus')
        """

        if not isinstance(memory, int):
            raise TypeError('Количество оперативной памяти должно быть целым числом')
        if not isinstance(company, str):
            raise TypeError('Название компании должно быть строкой')

        if len(company) < 1:
            raise ValueError('Название компании не может быть пустой строкой')
        if (memory and not (memory & memory - 1)) is False:
            raise ValueError('Количество оперативной памяти должно быть степенью 2')

        self.memory = memory
        self.company = company

    def update_memory(self, new_memory: int) -> None:
        """
        Увеличить количество оперативной памяти

        :param new_memory: память, которую добавляем
        :return: количество оперативной памяти в ноутбуке на данный момент

        Примеры:
        >>> laptop = Laptop(16, 'Asus')
        >>> laptop.update_memory(8)
        Количество оперативной памяти увеличилось до 24 Гб
        """

        if (new_memory and not (new_memory & new_memory - 1)) is False:
            raise ValueError('Новая оперативная память должна быть степенью 2')
        self.memory += new_memory
        print(f"Теперь в ноутбуке {self.memory}Гб оперативной памяти")

    def turn_laptop_on(self) -> None:
        """
        Включить ноутбук

        :return: состояние ноутбука
        Примеры:
        >>> laptop = Laptop(16, 'Asus')
        >>> laptop.turn_laptop_on()
        Ноутбук включен
        """
        self.turn_on = True
        print(f"Ноутбук включен")

    def turn_laptop_off(self) -> None:
        """
        Выключить ноутбук

        :return: состояние ноутбука
        Примеры:
        >>> laptop = Laptop(16, 'Asus')
        >>> laptop.turn_laptop_off()
        Ноутбук выключен
        """
        self.turn_on = True
        print(f"Ноутбук выключен")


if __name__ == '__main__':
    doctest.testmod()
