"""
Milton V. Banos
Process list w/multiple values and return list containing values that appeared only once
"""
from typing import List

def find_unique_value_id(customerIDs: List[int]) -> List[int]:
    list_dict = {}
    for i in customerIDs:
        list_dict[i] = list_dict.get(i, 0) + 1  
    print("Got list", customerIDs)        
    single_list = []    
    for i in list_dict:
        if list_dict[i] == 1:
            single_list.append(i)
    #print(single_list)
    return single_list

list_customer_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 3, 4, 5, 6, 7, 8, 10, 11]    
print(find_unique_value_id(list_customer_id))
