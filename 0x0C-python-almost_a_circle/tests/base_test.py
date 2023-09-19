#!/usr/bin/python3
import os
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_assignment(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base(24)
        self.assertEqual(base2.id, 24)
        base3 = Base()
        self.assertEqual(base3.id, 2)

        if __name__ == '__main__':
            unittest.main()
