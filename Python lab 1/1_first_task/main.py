import math as M
def pi_evaluater(eps):
    pi_result = 4
    num = 2
    den = 3
    numcount = 1
    dencounter = 0
    return_counter = 0
    pi_round = round(M.pi,eps)

    while round(pi_result,eps) != pi_round:
        pi_result *= (num/den)
        numcount += 1
        dencounter += 1
        if numcount == 2 :
            num += 2
            numcount = 0
        if dencounter == 2:
            den += 2
            dencounter = 0
        return_counter += 1
    return return_counter

eps = 4
result = pi_evaluater(eps)
print(result)