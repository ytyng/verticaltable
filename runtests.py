#!/usr/bin/env python
# coding: utf-8
import os
import unittest

import verticaltable

current_dir = os.path.dirname(__file__)


class TestUnittest(unittest.TestCase):
    def test__text_1(self):
        source = open(os.path.join(
            current_dir, 'test-fixture', 'test-text-1.txt')).read()

        parsed = verticaltable.loads(source)

        self.assertEqual(len(parsed), 5)
        self.assertEqual(parsed[0]['Q'], 'This is a question.')
        self.assertEqual(parsed[2]['A'], 'Answer 3')
        self.assertEqual(parsed[3]['description'], 'description text')
        self.assertEqual(parsed[4]['help'], 'This is help')

    def test__text_2(self):
        fp = open(os.path.join(
            current_dir, 'test-fixture', 'test-text-2.txt'))

        parsed = verticaltable.load(fp)
        self.assertEqual(len(parsed), 3)
        self.assertEqual(parsed[0]['head'], '概要')
        self.assertIn('自分でパースしてください', parsed[2]['body'])

    def test__text_3(self):
        fp = open(os.path.join(
            current_dir, 'test-fixture', 'test-text-3.txt'))

        parsed = verticaltable.load(fp)
        self.assertTrue(parsed)
        # print(parsed)

    def test__text_4(self):
        fp = open(os.path.join(
            current_dir, 'test-fixture', 'test-text-4.txt'))

        parsed = verticaltable.load(fp)
        self.assertTrue(parsed)
        # print(parsed)

if __name__ == '__main__':
    unittest.main()
