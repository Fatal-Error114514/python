n =reversed(eval(input()))
# new_list = []
# for i in range(len(n)):
#     lst = []
#     for j in range(len(n)):
#         lst = [n[j][i]] + lst
#     new_list.append(lst)
# new = str(new_list)
# print(new.replace(' ', ''))
print(str(list(map(list,zip(*n)))).replace(' ',''))