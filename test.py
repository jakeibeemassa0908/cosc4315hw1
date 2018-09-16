#!/usr/bin/python3
import unittest

import HW1.infinitearithmetic as inf


class TestInfiniteArithmetic(unittest.TestCase):
    def test_pdf_example(self):
        with open('tests/test01.out') as expectedfile:
            expected = expectedfile.read()

        result = inf.run_infinitearithmetic('tests/test01.txt', 1)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
