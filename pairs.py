import numpy as np
import tools

# Vector threshhold searcher
def vec_search(vector: np.ndarray, limit: float, count_max: int) -> bool:
  count = 0
  i = 0
  while i < len(vector):
    if abs(vector[i]) < limit:
      count += 1
    i += 1

  if count >= count_max:
    return True
  else:
    return False


# Function to find suitable pairs - returns tuples with stock numbers of suitable pairs
def suitable_pairs(prices: np.ndarray, limit:float, count_max: int) -> list:
  tup_list = []

  i = 0
  while i < 100:
    vec1 = np.array(prices[:, i])
    j = 0
    while j < 100:
      vec2 = np.array(prices[:, j])
      
      vec = np.subtract(vec2, vec1)
      
      if i != j and vec_search(vec, limit, count_max) == True:
        if (i,j) not in tup_list and (j,i) not in tup_list:
          tup_list.append((i,j))

      j += 1

    i += 1

  return tup_list 



# Function to change position vector when one of the pair goes up and other goes down, returns list with pair tuple, then day of split and stock that goes down (stock to buy) - for instance a possible output is [(32, 64), 17, 64]
def up_and_down(price_array: np.ndarray, pair:tuple, threshold:float) -> list:

  stock_1 = price_array[:, pair[0]]
  stock_2 = price_array[:, pair[1]]

  diff_array = np.subtract(stock_2, stock_1)


  i = 0
  while i < len(diff_array):
    value = float(diff_array[i])
    if abs(value) > threshold:
      if value > 0:
        return [pair, i, pair[1]]

      elif value < 0:
        return [pair, i, pair[0]]
          
    i += 1

  return None


# Function that checks all pairs and returns list of lists
def check_all_pairs(price_array: np.ndarray, pair_list: list, threshold: float) -> list:
  final_ls = []
  for el in pair_list:
    final_ls.append(up_and_down(price_array, el, threshold))

  return final_ls

# Function that creates final list
def final_list(ls: list) -> list:
  final_ls = []
  for el in ls:
    if el != None:
      final_ls.append(el)
    
  return final_ls

    
def main():

  true_array = tools.parse_prices()
  pairs_list = suitable_pairs(true_array, 1.00, 200) #Float to count as pair, number of similar days
  print(final_list(check_all_pairs(true_array, pairs_list, 2.00))) # Float to trigger difference

if __name__ == '__main__':
  main()