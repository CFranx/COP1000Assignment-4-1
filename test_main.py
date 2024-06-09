import unittest
import main

class TestMain(unittest.TestCase):
  def test_signCost1(self):
    result = main.signCost(numChars=8, color="gold", woodType="oak")
    self.assertEqual(result, "The charge for this sign is $82.00")

  def test_signCost2(self):
    result = main.signCost(numChars=20, color="gold", woodType="pine")
    self.assertEqual(result, "The charge for this sign is $110.00")

  def test_signCost3(self):
    result = main.signCost(numChars=18, color="black", woodType="oak")
    self.assertEqual(result, "The charge for this sign is $107.00")
    
if __name__ == '__main__':
  unittest.main()