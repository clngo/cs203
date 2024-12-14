import unittest
import lab1
#unit tests: https://www.youtube.com/watch?v=6tNS--WetLI
class AssignmentTests(unittest.TestCase):

    def test_example(self):
        pass

    def test_product_get_price(self):
        ex1 = lab1.Product("shirt", 100, 500)
        ex2 = lab1.Product("wrist watch", 100, 1200)
        ex3 = lab1.Product("textbook", 100, 800)
        ex4 = lab1.Product("history book", 100, 500)
        ex5 = lab1.Product("memory card", 100, 1400)

        test1 = ex1.get_price(5)
        test2 = ex2.get_price(11)
        test3 = ex3.get_price(100)
        test4 = ex4.get_price(39)
        test5 = ex5.get_price(84)

        self.assertEqual(test1, 2500)
        self.assertNotEqual(test1, 3)
        self.assertEqual(test2, 11880)
        self.assertEqual(test3, 64000)
        self.assertEqual(test4, 17550)
        self.assertEqual(test5, 105840)

    def test_product_make_purchase(self):
        ex4 = lab1.Product("history book", 100, 500)
        ex5 = lab1.Product("memory card", 100, 1400)

        test1 = ex4.make_purchase(18)
        test2 = ex5.make_purchase(32)

        self.assertEqual(test1, 82)
        self.assertEqual(test2, 68)

    def test_convert(self):
        miles = lab1.Converter(13, "mile")
        yard = lab1.Converter(39, "yard")

        test1 = miles.inch()
        test2 = yard.mile()

        self.assertEqual(test1, 823680)
        self.assertAlmostEqual(test2, 0.0221590909)


if __name__ == "__main__":
    unittest.main()
