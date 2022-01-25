from itertools import combinations,combinations_with_replacement


a=[1,2,3,4]

# Give combination 2nd arg is length which is 
# mandatory to give
comb=combinations(a,2)
print(list(comb))

comb_wf=combinations_with_replacement(a,2)
print(list(comb_wf))