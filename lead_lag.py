import tools

the_array = tools.parse_prices()

#importing gradients into a list
gradient_ls = []
day = 0
while day < 249:
  gradient_daily = tools.get_every_instr_grad(the_array, day)
  gradient_ls.append(gradient_daily)
  day += 1



#find suitable pairs 
def consec_diff(gradient_ls):
  suitable_pairs_ls = []
  i = 0
  while i < 239:
    m = 0
    while m < 100:
      n = 0
      while n < 100:
        consec_days_ls_a = gradient_ls[i:i+9][m]
        consec_days_ls_b = gradient_ls[i:i+9][n]
        consec_a_arr = np.array(consec_days_ls_a)
        consec_b_arr = np.array(consec_days_ls_b)
        consec_diff_arr = np.subtract(consec_b_arr, consec_a_arr)
        count = 0
        for el in consec_diff_arr:
          if abs(el) < 0.05:
            count += 1

          if count == 10:
            return True

        if m != n and consec_diff(gradient_ls) == True:
          suitable_pairs_ls.append((i,m,n))

        n += 1
      m += 1
    i +=1 
  
  return None

  print(suitable_pairs_ls)






#write the function to find the difference 1 day apart between 
#a) every combo of 2 stocks
#for a specific combo of 2 stocks
#b) every combo of 2 consecutive days - both 12 and 21

#if abs diff less than 0.05? consistent over 100 days, print into new list of candidates


#def gradient_difference (the_array[1])
#lead_lag_pairs = re.findall("gradient_difference",daily_gradient)

#if ()
 # print in a list 


  #the_array[:, 0] #first column of array
#the_array[0, :] #first row of array




# cut_ls = ls[0:9]
  