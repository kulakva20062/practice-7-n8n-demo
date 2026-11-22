import unittest

from pricing import discount, format_cents, line_total, subtotal


class PricingTests(unittest.TestCase):
    def test_line_total(self):
        self.assertEqual(line_total(125, 4), 500)

    def test_subtotal(self):
        self.assertEqual(subtotal(125, 500), 625)

    def test_format_cents(self):
        self.assertEqual(format_cents(625), '6.25')

    def test_discount(self):
        self.assertEqual(discount(500, 10), 450)
