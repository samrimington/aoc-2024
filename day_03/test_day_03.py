import unittest

from . import get_mul_instructions,\
              get_conditional_mul_instrs

TEST_INPUT_1 = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

TEST_INPUT_2 = """\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

class TestMulInstructions(unittest.TestCase):
    def test_standalone(self):
        self.assertListEqual(get_mul_instructions("mul(44,46)"), [(44, 46)])
        self.assertListEqual(get_mul_instructions("mul(123,4)"), [(123, 4)])
        self.assertEqual(get_mul_instructions("mul(4*"), [])
        self.assertEqual(get_mul_instructions("mul(6,9!"), [])
        self.assertEqual(get_mul_instructions("?(12,34)"), [])
        self.assertEqual(get_mul_instructions("mul ( 2 , 4 )"), [])

    def test_section(self):
        self.assertListEqual(
            get_mul_instructions(TEST_INPUT_1),
            [(2, 4), (5, 5), (11, 8), (8, 5)]
        )
    
    def test_conditional_section(self):
        self.assertListEqual(
            get_conditional_mul_instrs(TEST_INPUT_2),
            [(2, 4), (8, 5)]
        )
