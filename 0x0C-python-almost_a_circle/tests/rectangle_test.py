import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_attributes(self):
        rect1 = Rectangle(5, 10, 15, 20, 25)
        self.assertEqual(rect1.width, 5)
        self.assertEqual(rect1.height, 10)
        self.assertEqual(rect1.x, 15)
        self.assertEqual(rect1.y, 20)
        self.assertEqual(rect1.id, 25)
        
    def test_id_assignment(self):
        rect2 = Rectangle(5, 10)
        self.assertEqual(rect2.id, 1)

        rect3 = Rectangle(5, 10, 15, 20, 50)
        self.assertEqual(rect3.id, 50)

        rect4 = Rectangle(5, 10)
        self.assertEqual(rect4.id, 2)

if __name__ == '__main__':
    unittest.main()
