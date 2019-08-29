import unittest
import yandex_translate

class TestTranslate(unittest.TestCase):

    def test_translate(self):
        res = yandex_translate.translate('Привет', 'ru')
        self.assertEqual(res[0], 'Hallo')

    def test_status(self):
        res = yandex_translate.translate('Привет', 'ru')
        self.assertIn(200, res)


if __name__ == '__main__':
    unittest.main()