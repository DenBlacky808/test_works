def score(dice):
    digits_rez = 100 * max([num if num != 1 and num != 5 and dice.count(num)>=3 else 0 for num in set(dice)])
    one_num = max([dice.count(num) if num == 1 else 0 for num in set(dice)])
    five_num = max([dice.count(num)  if num == 5 else 0 for num in set(dice)])
    if one_num >= 3:
        rez = 1000 + (one_num - 3) * 100 + five_num * 50
    elif five_num >= 3:
        rez = 500 + (five_num - 3) * 50 + one_num * 100
    else: 
        rez = digits_rez + five_num * 50 + one_num * 100
    return rez
    
    
def score_2(dice): 
  sum = 0
  counter = [0,0,0,0,0,0]
  points = [1000, 200, 300, 400, 500, 600]
  extra = [100,0,0,0,50,0]
  for die in dice: 
    counter[die-1] += 1
  
  for (i, count) in enumerate(counter):
    sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)

  return sum