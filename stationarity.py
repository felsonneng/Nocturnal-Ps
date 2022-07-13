import numpy as np
import tools

# Must look at stationarity of every instrument at one point in time -> store into array

# range of gradients 
# card-counting for gradients
# how to account for sharper and larger differences that are still have a stationarity?
# how does stationarity influence instrument position?

# how to update base 0 of stationarity?

# how a change in gradient at the end compares to overall range of a stage of stationarity

# no stationarity? irregularity

#constant mean
#constant variance

# combine an analysis of the gradient and mean
# still counting cards of the gradient to determine position
# shifts in mean indicate a shift in centre of stationarity -> backed
# up by the gradient shifts


# given current day
# run through 100 instruments


def main(curr_day: int):
  true_array = tools.parse_prices()
  no_days = tools.no_days(true_array)
  avg_array = tools.get_avg_single_inst(true_array, curr_day, no_days)
  
  
  
  print(avg_array)


main(2)