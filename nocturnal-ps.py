import numpy as np
import fair
import lead_lag 
import pairs
import tools

# prices = tools.parse_prices()
def getMyPosition (hist):
  prices = hist
  day = tools.no_days(prices)

  current_pos = []
  max_nostocks = []
  for i in range(100):
    avg_ls = tools.limited_avg(prices, day, i, 10)
    sd = tools.sample_sd(prices, day, i, 10, avg_ls)
    current_pos.append(tools.compare_num(avg_ls,sd))
    max_nostocks.append(10000 / prices[day - 1, i])
  
  max_nostocks = np.array(np.around(max_nostocks, 0))
  current_pos = np.power(current_pos, 1)
  current_pos = np.around(current_pos, 2)
  pos_max = np.amax(current_pos)
  current_pos = (current_pos / pos_max)


  current_pos = np.multiply(np.array(current_pos), max_nostocks)
  current_pos = current_pos.astype(int)
  # print(current_pos)

  return current_pos

# print(getMyPosition(prices))