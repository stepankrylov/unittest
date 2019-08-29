import unittest
import json
import registrar


class TestRegistrar(unittest.TestCase):

    def setUp(self):
        with open("fixture\documents.json", "r", encoding='utf-8') as file:
            json_list = json.load(file)
            for item in json_list:
                self.x = item["number"]
                self.y = item["name"]

    def test_people(self):
        res = registrar.people(self.x)
        self.assertEqual(res, self.y)


if __name__ == '__main__':
    unittest.main()