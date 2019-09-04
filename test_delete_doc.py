import unittest
import json
import registrar


class TestRegistrar(unittest.TestCase):
    def setUp(self):
        with open("fixture\documents.json", "r", encoding='utf-8') as file:
            json_list = json.load(file)
            list_test_2 = []
            for item in json_list:
                self.x = item["number"]
                list_test_2.append(item)
            self.y = list_test_2

        with open("fixture\directories.json", "r", encoding='utf-8') as file:
            json_list = json.load(file)
            list_test_1 = []
            for item in json_list:
                list_test_1.append(item)
            self.z = list_test_1

    def test_delete_doc_1(self):
        res = registrar.delete_doc(self.x)
        self.assertEqual(len(res[0]), len(self.z))

    def test_delete_doc_2(self):
        res = registrar.delete_doc(self.x)
        self.assertEqual(len(res[1]), len(self.y)-1)

if __name__ == '__main__':
    unittest.main()