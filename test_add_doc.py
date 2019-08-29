import unittest
import json
import registrar


class TestRegistrar(unittest.TestCase):

    def test_add_doc_1(self):
        res = registrar.add_doc('0', '1', '2', '3')
        self.assertEqual(len(res[0]), 3)
    
    def test_add_doc_2(self):
        res = registrar.add_doc('0', '1', '2', '3')
        self.assertEqual(len(res[1]), 5)

if __name__ == '__main__':
    unittest.main()