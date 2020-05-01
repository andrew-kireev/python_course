

class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        cases = ('string', 1.5)
        for b in cases:
            with self.subTest(case=b):
                self.assertRaises(TypeError, factorize, b)

    def test_negative(self):
        cases = [-1, -10, -100]
        for b in cases:
            with self.subTest(case=b):
                self.assertRaises(ValueError, factorize, b)

    def test_zero_and_one_cases(self):
        cases = [1, 0]
        for b in cases:
            with self.subTest(case=b):
                self.assertEqual(factorize(b), (b, ))

    def test_simple_numbers(self):
        cases = [3, 13, 29]
        for b in cases:
            with self.subTest(case=b):
                self.assertEqual(factorize(b), (b, ))

    def test_two_simple_multipliers(self):
        cases = [6, 26, 121]
        result1 = [2, 2, 11]
        result2 = [3, 13, 11]
        i = 0
        for b in cases:
            with self.subTest(case=b):
                self.assertEqual(factorize(b), (result1[i], result2[i]))
                i += 1

    def test_many_multipliers(self):
        cases = [1001, 9699690]
        i = 0
        for b in cases:
            with self.subTest(case=b):
                if i == 0:
                    self.assertEqual(factorize(b), (7, 11, 13))
                else:
                    self.assertEqual(factorize(b), (2, 3, 5, 7, 11, 13, 17, 19))
                i += 1


if __name__ == '__main__':
    unittest.main()
