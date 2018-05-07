import unittest
from rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """ Test case to test the Rectangle class

        The complete set of tests will be:
            optional instantiation arguments
            width properties
            height properties
            number_of_instances class attr
            print_symbol class attr
            area instance method
            perimeter instance method
            __str__
            __repr__
            __del__
            bigger_or_equal static method
            square class method
    """

    def test_init(self):
        # Test __init__ arguments
        self.assertIsInstance(Rectangle(), Rectangle)
        self.assertIsInstance(Rectangle(width=1), Rectangle)
        self.assertIsInstance(Rectangle(height=1), Rectangle)
        self.assertIsInstance(Rectangle(1, 1), Rectangle)

    def test_properties(self):
        # Test that properties work as expected
        rect = Rectangle(2, 3)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        with self.assertRaises(TypeError, rect.width, "hi") as w:
            self.assertIsInstance(w.args, tuple)
            self.assertEqual(w.args[0], "width must be an integer")

        with self.assertRaises(ValueError, rect.width, -1) as wn:
            self.assertIsInstance(wn.args, tuple)
            self.assertEqual(wn.args[0], "width must be >= 0")

        with self.assertRaises(TypeError, rect.height, 2.4) as h:
            self.assertIsInstance(h.args, tuple)
            self.assertEqual(h.args[0], "height must be an integer")

        with self.assertRaises(ValueError, rect.height, -1) as hn:
            self.assertIsInstance(hn.args, tuple)
            self.assertEqual(hn.args[0], "height must be >= 0")

        with self.assertRaises(TypeError, Rectangle, "hi", 1) as wi:
            self.assertIsInstance(wi.args, tuple)
            self.assertEqual(wi.args[0], "width must be an integer")

        with self.assertRaises(ValueError, Rectangle, 1, -1) as hi:
            self.assertIsInstance(hi.args, tuple)
            self.assertEqual(hi.args[0], "height must be >= 0")

    def test_instance_count(self):
        # Tests instance count
        self.assertEqual(Rectangle.number_of_instances, 0)
        r1 = Rectangle()
        self.assertEqual(Rectangle.number_of_instances, 1)
        r2 = Rectangle()
        self.assertEqual(Rectangle.number_of_instances, 2)

    def test_print_symbol(self):
        # Tests print symbol
        rep = "###\n###\n###\n"
        rep2 = "111\n111\n111\n"
        rep3 = "[][][]\n[][][]\n[][][]\n"
        self.assertEqual(Rectangle.print_symbol, '#')
        rect = Rectangle(3, 3)
        self.assertEqual(str(rect), rep)
        Rectangle.print_symbol = 1
        self.assertEqual(str(rect), rep2)
        Rectangle.print_symbol = []
        self.assertEqual(str(rect), rep3)
        rect = Rectangle()
        self.assertEqual(str(rect), '')

    def test_area(self):
        # Test area method
        rect = Rectangle(3, 3)
        self.assertEqual(rect.area(), 9)

    def test_perimeter(self):
        # Test perimeter method
        rect = Rectangle(4, 2)
        self.assertEqual(rect.perimeter(), 12)
        rect = Rectangle(10)
        self.assertEqual(rect.perimeter(), 0)

    def test_repr(self):
        # Tests the __repr__ method
        rect = Rectangle(4, 2)
        assertIsInstance(eval(repr(rect)), Rectangle)

    def test_destructor(self):
        # Test __del__ method
        self.assertEqual(Rectangle.number_of_instances, 0)
        r1 = Rectangle()
        self.assertEqual(Rectangle.number_of_instances, 1)
        del r1
        self.assertEqual(Rectangle.number_of_instances, 0)

    def test_square(self):
        # Test class method square
        sqr = Rectangle.square(size=2)
        assertEqual(sqr.width, 2)
        assertEqual(sqr.height, 2)
        assertEqual(Rectangle.number_of_instances, 1)
        del sqr
        assertEqual(Rectangle.number_of_instances, 0)
