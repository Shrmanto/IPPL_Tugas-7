import unittest
from kalkulator import hitung

class TestKalkulator(unittest.TestCase):
    def test_jumlah(self):
        result = hitung('1', 5, 3)
        self.assertEqual(result, 'Hasil operasi dari 5 + 3 = 8')

    def test_kurang(self):
        result = hitung('2', 10, 3)
        self.assertEqual(result, 'Hasil operasi dari 10 - 3 = 7')

    def test_kali(self):
        result = hitung('3', 4, 7)
        self.assertEqual(result, 'Hasil operasi dari 4 * 7 = 28')

    def test_bagi(self):
        result = hitung('4', 10, 5)
        self.assertEqual(result, 'Hasil operasi dari 10 / 5 = 2.0')

    def test_invalid_input(self):
        result = hitung('5', 10, 2)
        self.assertEqual(result, 'Tidak Valid')

if __name__ == '__main__':
    unittest.main()
