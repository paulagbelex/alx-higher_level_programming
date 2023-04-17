import unittest
from models.base import Base


class TestBase(unittest.TestCase):
        def test_base_no_id(self):
            b1 = Base()
            b2 = Base()
            self.assertEqual(b1.id, 1)
            self.assertEqual(b2.id, 2)

        def test_base_with_id(self):
            b1 = Base(10)
            b2 = Base(20)
            self.assertEqual(b1.id, 10)
            self.assertEqual(b2.id, 20)

        def test_base_private_attr(self):
            with self.assertRaises(AttributeError):
                print(Base.__nb_objects)

if __name__ == '__main__':
    unittest.main()
