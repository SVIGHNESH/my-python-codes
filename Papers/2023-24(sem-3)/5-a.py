# def ret_smaller(l):
#     smallest_list = l[0]
#     for i in l:
#         if len(smallest_list) > len(i):
#             smallest_list = i

#     return smallest_list
# print(ret_smaller([[-2,-1,0,0,12,1,2],[3,4,5],[6,7,8,9,10],[11,12,1,21,13,15]]))


def ret_smaller(l):
    return min(l,key=len)
print(ret_smaller([[-2,-1,0,0,12,1,2],[3,4,5],[6,7,8,9,10],[11,12,1,21,13,15]]))