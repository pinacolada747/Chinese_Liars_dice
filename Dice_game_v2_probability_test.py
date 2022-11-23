

def factorial(number):
    fact = 1
    for i in range(1,number+1):
        fact = i * fact
    return(fact)

def combinations(k):
    return(factorial(5)/(factorial(k)*factorial(5-k)))

def binomial_probability(k):
    #k---> number of succesful trials
    p = 1/6 #p---> probability of success in one trial
    n = 5 #n --> total number of trials
    Pk = (combinations(k)*(p**k))*((1-p)**(n-k))
    return(Pk)


def probability_agregate(k):
    alpha = 0
    for i in range(k,6):
        beta = binomial_probability(i)
        alpha += beta
    return(alpha)

def calculate_probability(list, qty_call, dice_call):
    counted = lambda a, b: a.count(int(b))
    num = counted(list, dice_call) #increased by the number of ones
    op_min_dice_qty = qty_call - num
    print('must have atleast', op_min_dice_qty, dice_call)
    if op_min_dice_qty <= 5:
        return int(round(probability_agregate(op_min_dice_qty),2)*100)
    else:
        return 0
# def calculate_probability(list,qty, dice_call):

def calculate_probability2(list, qty_call, dice_call):
    counted = lambda a, b: a.count(int(b))
    num = counted(list, dice_call)
    num1 = counted(list, 1)
    num_total = num+num1#increased by the number of ones
    op_min_dice_qty = qty_call - num_total
    print('must have atleast', op_min_dice_qty, dice_call)
    if op_min_dice_qty <= 5:
        return int(round(probability_agregate(op_min_dice_qty),2)*100)
    else:
        return 0

dice_list = [4,4,4,3,1]

qty_call = 2
dice_call = 1

#probability of 4 3's
#probability of 3 3's
# 5 of 1
# 3 of 1

print(calculate_probability(dice_list,qty_call,dice_call))

# player actually has 3 of 6 and calls 6 of 6
# qty call of dice value -  actual qty of dice value -