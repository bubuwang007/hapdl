import unittest
from hapdl.apdl.api.Star.get._ACTIVE import ACTIVE, get_active
from hapdl.apdl.api.Star.get._CMD import CMD, get_cmd
from hapdl.apdl.api.Star.get._COMP import COMP, get_comp

class TestGet(unittest.TestCase):
    
    def test_get(self):
        self.assertEqual(ACTIVE.cpu_time("par"), get_active("par", "TIME", "CPU"))

    def test_get_cmd(self):
        self.assertEqual(CMD.status("par"), get_cmd("par", "STAT"))

    def test_get_comp(self):
        self.assertEqual(COMP.component_number("n"), get_comp("n", 0, "NCOMP"))
        # print(COMP.component_number("aaa"))
        # print(COMP.name("aaa", 1))
        # print(COMP.type("aaa", 'CM1'))
        print(COMP.number_of_subcomponents("aaa", 'CM1'))

if __name__ == '__main__':
    unittest.main()