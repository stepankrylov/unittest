import unittest
import json
import registrar


class TestRegistrar(unittest.TestCase):
    def setUp(self):
        with open("fixture\documents.json", "r", encoding='utf-8') as file:
            json_list = json.load(file)
            list_test_2 = []
            for item in json_list:
                list_test_2.append(item)
            self.y = list_test_2

        with open("fixture\directories.json", "r", encoding='utf-8') as file:
            json_list = json.load(file)
            list_test_1 = []
            for item in json_list:
                list_test_1.append(item)
            self.z = list_test_1

    def test_add_doc(self):
        res = registrar.add_doc('0', '1', '2', '3')
        self.assertEqual(len(res[0]), len(self.z))
        self.assertEqual(len(res[1]), len(self.y)+1)
        
if __name__ == '__main__':
    unittest.main()