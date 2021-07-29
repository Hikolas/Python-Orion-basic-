class NegativeNumber(Exception):
    pass

class CalcTest:

    @staticmethod
    def addition(a, b):
        """ Шукає суму двох чисел
        >>> CalcTest.addition(4, 2)
        6

        :param a: Перше число
        :param b: Друге число
        :return: Результат
        """

        return a + b

    @staticmethod
    def subtraction(a, b):
        """ Шукає різницю чисел
        >>> CalcTest.subtraction(4, 2)
        2

        :param a: Перше число
        :param b: Друге число
        :return: Результат
        """

        return a - b

    @staticmethod
    def multiplication(a, b):
        """ Шукає добуток чисер
        >>> CalcTest.multiplication(4, 2)
        8

        :param a: Перше число
        :param b: Друге число
        :return: Результат
        """

        return a * b

    @staticmethod
    def division(a, b):
        """ Поділити частку чисел
        >>> CalcTest.division(4, 2)
        2

        :param a: Перше число
        :param b: Друге число
        :return: Результат
        """

        return a / b

    @staticmethod
    def degree(a, b):
        """ Піднести число до степиння
        >>> CalcTest.degree(4, 2)
        16

        :param a: Перше число
        :param b: Степінь
        :return: Результат
        """

        return a ** b

    @staticmethod
    def root(a, b):
        """ Шукає n-ий корінь від числа
        >>> CalcTest.root(16, 2)
        4.0

        :param a: Перше число
        :param b: Степінь корення
        :return: Результат
        """

        if a < 0:
            raise NegativeNumber
        else:
            return a ** (1/b)

    @staticmethod
    def percentages(a, b):
        """ Шукає кількість процентів від числа
        >>> CalcTest.percentages(4, 2)
        50.0

        :param a: Перше число
        :param b: Друге число
        :return: Результат
        """
        if b < 0:
            raise NegativeNumber
        else:
            return b * 100 / a

