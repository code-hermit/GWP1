##coefficient of variation tables for 2 stocks portfolio
import streamlit as st
from portfolio import PORTFOLIO,stats_dic
import pandas as pd
st. set_page_config(layout="wide")
st.title("COEFFICIENT OF VARIATIONS AGAINST WEIGHTS")
weight_range=[k/10 for k in range(-10,10,1) if k!=0]
stocks=list(stats_dic.keys())


corr_coef_dic={}

for stock_a in stocks:
  if stock_a not in corr_coef_dic:
      corr_coef_dic[stock_a]={}
  for stock_b in stocks:
    if stock_a==stock_b:
      continue
    
    if stock_b not in corr_coef_dic[stock_a]:
      corr_coef_dic[stock_a][stock_b]={}
    for w1 in weight_range:
      w2=1-w1
      print(stock_a,stock_b,w1,w2)
      
      cur_port=PORTFOLIO([stock_a,stock_b],[w1,w2])
      coeff_of_var=cur_port.coff_of_variation()
      corr_coef_dic[stock_a][stock_b][w1]=coeff_of_var
  st.title(stock_a)
  df=pd.DataFrame.from_dict(corr_coef_dic[stock_a])
  st.dataframe(df.T)
