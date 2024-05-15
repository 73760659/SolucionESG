import unittest
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculoRaices = EcuacionSegundoGrado()
    def tearDown(self):
        self.calculoRaices = None
    def test_calculoESG_dosNumeros_retornaSolucion(self):
      # Arrange
      a=1
      b=2
      c=1
      resultadoEsperadoRaiz1=-1
      resultadoEsperadoRaiz2 = -1
      # Do
      resultadoactuaLRaiz1,resultadoactuaLRaiz2= self.calculoRaices.calculoESG(a,b,c)

      # Assert
      self.assertEqual(resultadoEsperadoRaiz1, resultadoactuaLRaiz1)
      self.assertEqual(resultadoEsperadoRaiz2, resultadoactuaLRaiz2)


if __name__ == '__main__':
    unittest.main()
