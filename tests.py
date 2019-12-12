import unittest
from main import *

class calcs_check(unittest.TestCase):

    def test_triangle(self):
        test_triangle1 = Triangle(10, 5)
        test_triangle2 = Triangle(3, 2)
        test_triangle3 = Triangle(651, 521)
        self.assertEqual(test_triangle1.calc_surface(), 25)
        self.assertEqual(test_triangle2.calc_surface(), 3)
        self.assertEqual(test_triangle3.calc_surface(), 169585.5)

    def test_square(self):
        test_square1 = Square(5)
        test_square2 = Square(4)
        test_square3 = Square(21)
        self.assertEqual(test_square1.calc_surface(), 25)
        self.assertEqual(test_square2.calc_surface(), 16)
        self.assertEqual(test_square3.calc_surface(), 441)

    def test_rectangle(self):
        test_rectangle1 = Rectangle(10, 5)
        test_rectangle2 = Rectangle(20, 3)
        test_rectangle3 = Rectangle(52, 17)
        self.assertEqual(test_rectangle1.calc_surface(), 50)
        self.assertEqual(test_rectangle2.calc_surface(), 60)
        self.assertEqual(test_rectangle3.calc_surface(), 884)
    
    def test_cube(self):
        test_cube1 = Cube(8)
        test_cube2 = Cube(7)
        test_cube3 = Cube(51)
        self.assertEqual(test_cube1.calc_surface(), 384)
        self.assertEqual(test_cube1.calc_volume(), 512)
        self.assertEqual(test_cube2.calc_surface(), 294)
        self.assertEqual(test_cube2.calc_volume(), 343)
        self.assertEqual(test_cube3.calc_surface(), 15606)
        self.assertEqual(test_cube3.calc_volume(), 132651)
        
    def test_tetrahedron(self):
        test_tetrahedron1 = Tetrahedron(5)
        test_tetrahedron2 = Tetrahedron(19)
        test_tetrahedron3 = Tetrahedron(8)
        self.assertEqual(round(test_tetrahedron1.calc_surface(), 2), 43.30)
        self.assertEqual(round(test_tetrahedron1.calc_volume(), 2), 14.73)
        self.assertEqual(round(test_tetrahedron2.calc_surface(), 2), 625.27)
        self.assertEqual(round(test_tetrahedron2.calc_volume(), 2), 808.34)
        self.assertEqual(round(test_tetrahedron3.calc_surface(), 2), 110.85)
        self.assertEqual(round(test_tetrahedron3.calc_volume(), 2), 60.34)

    def test_oval(self):
        test_oval1 = Oval(3, 2)
        test_oval2 = Oval(6, 1)
        test_oval3 = Oval(21, 10)
        self.assertEqual(round(test_oval1.calc_surface(), 2), 18.85)
        self.assertEqual(round(test_oval2.calc_surface(), 2), 18.85)
        self.assertEqual(round(test_oval3.calc_surface(), 2), 659.73)

if __name__ == "__main__":
    unittest.main()