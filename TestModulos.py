import unittest
from Business import ModuloBusiness
business = ModuloBusiness.Modulo()

class TestModulos(unittest.TestCase):

    def test_modul5(self):
        self.assertEqual(business.calculateModulos(10), "IT", "Should be IT")
        self.assertEqual(business.calculateModulos(325), "IT", "Should be IT")
        self.assertEqual(business.calculateModulos(145), "IT", "Should be IT")
        self.assertEqual(business.calculateModulos(290), "IT", "Should be IT")
        self.assertEqual(business.calculateModulos(205), "IT", "Should be IT")
        self.assertEqual(business.calculateModulos(100), "IT", "Should be IT")
        self.assertEqual(business.calculateModulos(80), "IT", "Should be IT")
        self.assertEqual(business.calculateModulos(115), "IT", "Should be IT")
        self.assertEqual(business.calculateModulos(335), "IT", "Should be IT")

    def test_modul3(self):
        self.assertEqual(business.calculateModulos(3), "Linio", "Should be Linio")
        self.assertEqual(business.calculateModulos(96), "Linio", "Should be Linio")
        self.assertEqual(business.calculateModulos(156), "Linio", "Should be Linio")
        self.assertEqual(business.calculateModulos(87), "Linio", "Should be Linio")
        self.assertEqual(business.calculateModulos(174), "Linio", "Should be Linio")
        self.assertEqual(business.calculateModulos(213), "Linio", "Should be Linio")
        self.assertEqual(business.calculateModulos(189), "Linio", "Should be Linio")
        self.assertEqual(business.calculateModulos(186), "Linio", "Should be Linio")
        self.assertEqual(business.calculateModulos(177), "Linio", "Should be Linio")



    def test_modul_both(self):
        self.assertEqual(business.calculateModulos(15), "Linianos", "Should be Linianos")
        self.assertEqual(business.calculateModulos(30), "Linianos", "Should be Linianos")
        self.assertEqual(business.calculateModulos(45), "Linianos", "Should be Linianos")
        self.assertEqual(business.calculateModulos(60), "Linianos", "Should be Linianos")
        self.assertEqual(business.calculateModulos(75), "Linianos", "Should be Linianos")

if __name__ == '__main__':
    unittest.main()
