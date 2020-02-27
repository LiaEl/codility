#def solution(A):
#    prs = []
#    for el in lst:
#        if el not in prs:
#            prs.append(el)
#        else:
#            prs.remove(el)
#    return prs

lst = [9, 3, 9, 3, 9, 7, 9]

for i in lst:
    if lst.count(i) % 2 == 0:
        while i in lst:
            lst.remove(i)
print(lst[0])