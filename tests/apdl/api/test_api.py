import unittest
from hapdl.apdl.api._api import _api
from hapdl.apdl.api._Exception import NotaValidAPDLCommand

class TestApi(unittest.TestCase):

    def test_call(self):
        self.assertEqual(_api.call("a","b"), "_api,a,b")

    def test_check(self):
        with self.assertRaises(NotaValidAPDLCommand):
            _api.check("b")

if __name__ == '__main__':
    unittest.main()