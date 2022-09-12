from unittest import TestCase, main
from auto.calc import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('5-3'), 2)

    def test_multi(self):
        self.assertEqual(calculator('10*8'), 80)

    def test_dil(self):
        self.assertEqual(calculator('10/2'), 5)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('blablabla')
        self.assertEqual('Вираз повинний мати хоча б один знак (+-/*)', e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2')
        self.assertEqual('Вираз має мати два цілих числа і один знак', e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('55*2+8/4')
        self.assertEqual('Вираз має мати два цілих числа і один знак', e.exception.args[0])

    def test_no_intg(self):
        with self.assertRaises(ValueError) as e:
            calculator('55*2.5+8/4.0')
        self.assertEqual('Вираз має мати два цілих числа і один знак', e.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator('spam+eggs')
        self.assertEqual('Вираз має мати два цілих числа і один знак', e.exception.args[0])


if __name__ == '__main__':
    main()
