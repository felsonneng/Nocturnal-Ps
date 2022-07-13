import numpy as np
import tools

# Find average gradient across market
def gradient_av(prices: np.ndarray, day_one: int):
    grad_array_one_period = tools.get_every_instr_grad(prices, day_one)
  
    return grad_array_one_period.mean()


# Create list of market values and output correct element
def market_val_day(prices: np.ndarray, day_one: int):
    market_val_ls = []
    market_val = 0
    j = 0

    while j < 249:
        market_val += gradient_av(prices, j)
        market_val_ls.append(round(market_val, 3))
 
        j += 1

    return market_val_ls[day_one]


# List of averages of stocks for certain day
def avg_list(prices: np.ndarray, curr_day: int) -> list:
    list_of_avg = []
    i = 0
    while i < 100:
        list_of_avg.append(tools.avg(prices, curr_day, i))
        i += 1

    return list_of_avg


# List of fair prices of stocks for certain day
def fair_list(prices: np.ndarray, curr_day: int) -> list:
    world_fairness = []
    world_peace = avg_list(prices, curr_day)
    
    i = 0
    while i < 100:
        world_fairness.append(world_peace[i] + market_val_day(prices, curr_day))
        i += 1

    return world_fairness


# Returns the position vector given a single day
def pos_vector(prices: np.ndarray, curr_day: int) -> np.ndarray:
    fairray = np.array(fair_list(prices, curr_day))
    all_prices = tools.parse_prices()
    curray = all_prices[curr_day, :]
    diff_array = np.subtract(curray, fairray) # Current - Fair Price

    max = diff_array.max()
    min = diff_array.min()

    if abs(max) >= abs(min):
        factor = 10000/max
        final_array = np.multiply(diff_array, -factor)
        true_final_array = np.around(final_array, 0)
        true_final_array = true_final_array.astype(int)

        return true_final_array

  
    elif abs(min) > abs(max):
        factor = 10000/min
        final_array = np.multiply(diff_array, -factor)
        true_final_array = np.around(final_array, 0)
        true_final_array = true_final_array.astype(int)
        
        return true_final_array
  

# Returns position vector for current day -> START AT 1, because of gradients
def main(day_up_to):
    prices = tools.parse_prices()
    
    pos_vec_ls = []
    j = 1
  
    while j < day_up_to:
        pos_vec_ls.append(pos_vector(prices, j))
    
        j += 1  
    
    
    print(pos_vec_ls)
    return pos_vec_ls



if __name__ == '__main__':
  main(250)