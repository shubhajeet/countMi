# -*- coding: utf-8 -*-
import unittest
from collections import Counter

from countminsketch import CountMinSketchMinUpdate


class TestCountMinSketchMinUpdate(unittest.TestCase):
    def test_zero_at_start(self):
        sketch = CountMinSketchMinUpdate(10, 5)
        for thing in (0, 1, -1, tuple, tuple(), "", "yeah", object()):
            self.assertEqual(sketch.query(thing), 0)

    def test_bad_init(self):
        with self.assertRaises(ValueError):
            CountMinSketchMinUpdate(0, 5)
        with self.assertRaises(ValueError):
            CountMinSketchMinUpdate(100, 0)

    def test_simple_usage(self):
        N = 1000
        sketch = CountMinSketchMinUpdate(10, 5)
        for _ in range(N):
            sketch.add("a")
        self.assertEqual(sketch.query("a"), N)
        self.assertEqual(sketch.query("b"), 0)
        self.assertEqual(len(sketch), N)

    def test_syntax_sugar(self):
        sketch = CountMinSketchMinUpdate(10, 5)
        self.assertEqual(sketch.query("a"), sketch["a"])
        sketch.add("a")
        self.assertEqual(sketch.query("a"), sketch["a"])

    def test_counts_overestimate(self):
        text = open(__file__).read()
        counter = Counter(text)
        sketch = CountMinSketchMinUpdate(10, 5)
        for x in text:
            sketch.add(x)
        for x in set(text):
            self.assertGreaterEqual(sketch[x], counter[x])

    def test_counts_donotunderestimate(self):
        text = open(__file__).read()
        sketch = CountMinSketchMinUpdate(10, 5)
        for x in text:
            sketch.add(x)
        for x in text:
            sketch.remove(x)
        for x in set(text):
            self.assertGreaterEqual(sketch[x], 0)

    def test_add_greater_than_one(self):
        sketch = CountMinSketchMinUpdate(10, 5)
        sketch.add("a", 123)
        self.assertEqual(sketch.query("a"), 123)


if __name__ == "__main__":
    unittest.main()
