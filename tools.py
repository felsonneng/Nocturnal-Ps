import numpy as np

# Parse prices file
def parse_prices() -> np.ndarray:
  array_ls = []
  # MUST CHANGE IN THE REAL THING TO TXT
  f = open('prices.py', 'r')
  while True:
    line_ls = []
    line = f.readline()
    if line == '':
      break
    line_values = line.split('   ')
    for el in line_values:
      el_float = float(el)
      line_ls.append(el_float)

    array_ls.append(line_ls)

  arr = np.array(array_ls)
  f.close()

  return arr


  
# Find gradient between two points over 1 period
# Returns float gradient
def get_grad(first_point, second_point) -> float:
  return second_point - first_point


  
# Find gradient for every instruments over 1 period
# Returns array of gradients for every instrument
# no inherent block for date exceeding date
def get_every_instr_grad(prices: np.ndarray, day_one: int) -> np.ndarray:
  price_start = np.array(prices[day_one,:])
  price_end = np.array(prices[day_one + 1,:])
  return np.around(np.subtract(price_end, price_start), 2)

  
  
# Find gradient for 1 instrument over entire available period
# Returns list of gradients for 1 instrument
#no inherent block for date exceeding date
def get_single_instr_grad(prices: np.ndarray, curr_day: int, instr: int) -> np.ndarray:
  gradient_ls = []
  # Indexing and day paired with next
  for i in range(curr_day):
    price_start = prices[i, instr]
    price_end = prices[i + 1, instr]
    gradient_ls.append(get_grad(price_start, price_end))
  return np.around(gradient_ls, 2)

# Returns prices of all the days for a single instrument
def get_single_instr_price(prices: np.ndarray, instr: int) -> np.ndarray:
  return np.array(prices[:,instr])

# Average price of all instruments for every day
def get_avg_inst(prices: np.ndarray, curr_day: int) -> np.ndarray:
  
  return

# Average price of 1 instrument until current day
# Returns value average
def avg(prices: np.ndarray, curr_day: int, instr: int) -> np.ndarray:
  day = np.array(prices[:curr_day + 1, instr])
  return np.around(np.average(day), 2)


# Average price of 1 instrument until a curren day
# Returns array of averages of each day
def get_avg_single_inst(prices: np.ndarray, curr_day: int, instr: int) -> np.ndarray:
  avg_ls = []
  for i in range(curr_day):
    avg_ls.append(avg(prices, i, instr))
  return np.around(avg_ls, 2)

  
# Returns number of days
def no_days(prices: np.ndarray) -> int:
  return len(prices)


# average of 1 instrument over a select period repeated across entire timeframe
def limited_avg(prices: np.ndarray, curr_day: int, instr: int, period: int) -> np.ndarray:
  avg_ls = []
  row = 0

  # Loop through each period to find average
  while (row + period <= curr_day):
    days = np.array(prices[row: row + period, instr])
    avg = np.around(np.average(days), 2)
    avg_ls.append(avg)
    row += period
  # Edge case if final period is too small
  if row != curr_day:
    days_left = curr_day - row + 1
    days = np.array(prices[row: row + days_left, instr])
    avg = np.around(np.average(days), 2)
    avg_ls.append(avg)
  return avg_ls



# sample standard deviation of 1 instrument over a select period repeated across entire timeframe
def sample_sd(prices: np.ndarray, curr_day: int, instr: int, period: int, avg_ls: np.ndarray) -> np.ndarray:
  sd_ls = []
  row = 0
  avg_count = 0
  # Loop through each period to find sample sd
  while (row + period <= curr_day):
    array = np.array(prices[row: row + period, instr])
    mean = avg_ls[avg_count]
    temp = np.square(array - mean)
    sd = np.sum(temp) / (period - 1)
    sd_ls.append(sd)
    row += period
    avg_count += 1

  # Edge case if final period is too small
  if row != curr_day:
    days_left = curr_day - row + 1  
    array = np.array(prices[row: row + days_left, instr])
    mean = avg_ls[avg_count]
    temp = np.square(array - mean)
    sd = np.sum(temp) / (period - 1)
    sd_ls.append(sd)
  return np.around(np.sqrt(sd_ls), 4)


# prices = parse_prices()
# day = no_days(prices)
# avg_ls = limited_avg(prices, day, 3, 10)
# # # print(avg_ls)
# sd = sample_sd(prices, day, 3, 10, avg_ls)
# print(sd)

# Find trend line of a set of data
def trendline(index: np.ndarray,data: np.ndarray, order = 1):
    coeffs = np.polyfit(index, data, order)
    slope = coeffs[-2]
    return float(slope)


# Comparison function
# Comparing how close numbers are too each other.
def compare_num(mean: np.ndarray, sd: np.ndarray) -> np.ndarray:
  meanlength = len(mean)
  mean_dif_ls = []

  # finding the difference between the means
  for i in range(meanlength - 1):
    mean_start = mean[i]
    mean_end = mean[i + 1]
    mean_dif_ls.append(get_grad(mean_start, mean_end))
  
  mean_dif_ls = np.around(mean_dif_ls, 2)
  # finding how many sd next mean is from previous mean
  sd_away_ls = []
  for j in range(len(mean_dif_ls) - 1):
    sd_value = sd[j]
    diff_value = mean_dif_ls[j]
    sd_away_ls.append(diff_value / sd_value)

  sd_away_ls = np.around(sd_away_ls, 2)

  # taking only the most significant changes
  nonstat_ls = []
  for k in range(len(sd_away_ls)):
    sd_away = sd_away_ls[k]
    if abs(sd_away) > 1:
      nonstat_ls.append(sd_away)  

  
  # taking the most recent 10 
  index = [x for x in range(0,min(10,len(nonstat_ls)))]
  recent = []
  for i in range(0,min(10,len(nonstat_ls))):
    recent.append(nonstat_ls[-min(10,len(nonstat_ls))+i])

  # print(recent)
  trend = trendline(index, recent)
  # print(trend)

  # taking the logarithm of the trend for more signficant scale
  if trend < 0:
    trend = -np.log(abs(trend))
  else:
    trend = np.log(trend)
  return -trend
# print(compare_num(avg_ls,sd))


# print(get_single_instr_price(parse_prices(),1))

#prices[:, i] -> array of ith column
#prices[i, :] -> array of ith row