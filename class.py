import unittest

class MyList:
    def __init__(self):
        self.items = [] 

    def add_item(self, item):
        self.items.append(item)  

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)  

    def get_length(self):
        return len(self.items)  

class TestMyList(unittest.TestCase):
    def setUp(self):
        self.my_list = MyList()  

    def test_add_item(self):
        self.my_list.add_item(1)
        self.assertEqual(len(self.my_list.items), 1)

    def test_remove_item(self):
        self.my_list.add_item(1)
        self.my_list.remove_item(1)
        self.assertEqual(len(self.my_list.items), 0)

    def test_get_length(self):
        self.assertEqual(self.my_list.get_length(), 0)
        self.my_list.add_item(1)
        self.assertEqual(self.my_list.get_length(), 1)

if __name__ == '__main__':
    unittest.main()

