def ret_max_avg(nested_list):
    return max(nested_list,key=lambda x: sum(x)/len(x))
print(ret_max_avg([[3, 4, 5], [3, 4, 5]]))