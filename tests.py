# Write your code below:
import surfshop
import unittest

class SurfApp(unittest.TestCase):
  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def testAddSurfboard1(self):
    self.assertEqual(self.cart.add_surfboards(1), 'Successfully added 1 surfboard to cart!')

  def testAddSurfboard2(self):
    self.assertEqual(self.cart.add_surfboards(2), 'Successfully added 2 surfboards to cart!')

  #@unittest.skip('Off Season')
  def testTooManyBoardsError(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

  #@unittest.expectedFailure
  def testLocalDiscountIsTrue(self):
    self.assertTrue(self.cart.apply_locals_discount())

unittest.main()