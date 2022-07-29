import pandas as pd
import math
corr_df=pd.read_csv('corr.csv',index_col=0)
stats_df=pd.read_csv('data.csv',index_col=0)

stats_dic=stats_df.to_dict()
corr_dic=corr_df.to_dict()
stock_names=list(stats_dic.keys())
class PORTFOLIO:
  def __init__(self,stocks,weights) -> None:
    self.stocks=stocks
    self.weights=weights ##weights given in decimal should add to 1; weights can vary from -1 to 1 in intervals of 0.1
    if len(stocks)!=len(weights):
      print(input('invalid number of stocks'))
    if round(sum(weights))!=1:
      print(sum(weights))
      print(input('invalid weights'))
    for s in stocks:
      if s not in stock_names:
        print(input('invalid stock'))
    
  def expected_returns(self):
    portfolio_return=0
    for i in range(len(self.stocks)):
      stock_name=self.stocks[i]
      stock_weight=self.weights[i]
      portfolio_return+=(stock_weight*stats_dic[stock_name]['mean'])
    return portfolio_return

  def standard_deviation(self):
    portfolio_variance=0
    for i in range(len(self.stocks)):
      stock_a=self.stocks[i]
      weight_a=self.weights[i]
      for j in range(len(self.stocks)):
        stock_b=self.stocks[j]
        weight_b=self.weights[j]

        if stock_a==stock_b:
          corr_term=math.pow(weight_a,2)*math.pow(stats_dic[stock_a]['std'],2)
        else:
          corr_term=2*weight_a*weight_b*stats_dic[stock_a]['std']*stats_dic[stock_b]['std']*corr_dic[stock_a][stock_b]
        
        portfolio_variance+=corr_term
        # print('corrterm',stock_a,stock_b,corr_term,portfolio_variance)
    print(portfolio_variance)

    try:
      return math.pow(portfolio_variance,0.5)
    except:         
      if abs(portfolio_variance)<0.0002:
        return portfolio_variance
      else:
        print(portfolio_variance)
        print(input('portfolio variance too small'))

  def sharpe_ratio(self,rf=0.01):
    return float(self.expected_returns()-rf)/self.standard_deviation()
  def coff_of_variation(self):
    return self.standard_deviation()/self.expected_returns()
