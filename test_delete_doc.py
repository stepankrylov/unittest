import unittest
import json
import registrar


class TestRegistrar(unittest.TestCase):

    def test_delete_doc_1(self):
        res = registrar.delete_doc('10006')
        self.assertEqual(len(res[0]), 3)
    
    def test_delete_doc_2(self):
        res = registrar.delete_doc('10006')
        self.assertEqual(len(res[1]), 2)

if __name__ == '__main__':
    unittest.main()