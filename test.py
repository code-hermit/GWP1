import unittest
from portfolio import PORTFOLIO,stats_dic


class portTest(unittest.TestCase):
    
    

    def test(self):        
      stock_a=list(stats_dic.keys())[0]
      my_port=PORTFOLIO([stock_a,stock_a],[0.4,0.6])
      self.assertEqual(f"{my_port.expected_returns():.2f}",f"{stats_dic[stock_a]['mean']:.2f}")
      self.assertEqual(f"{my_port.standard_deviation():.2f}",f"{stats_dic[stock_a]['std']:.2f}")
  
if __name__ == '__main__':
    unittest.main()