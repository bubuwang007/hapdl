import unittest

from hapdl.core._HapdlObject import HapdlObject
from hapdl.core._HapdlType import HapdlType

class TestObject(unittest.TestCase):
    
    def test_hapdl_object(self):
        typ = HapdlType
        obj = HapdlObject('a', HapdlType)
        print(obj)

    def test_hapdl_type(self):
        self.assertTrue(HapdlType)

if __name__ == '__main__':
    unittest.main()