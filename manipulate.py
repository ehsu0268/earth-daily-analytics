

def manipulate_list(orig_list, add_list, delete_list):
    for val in add_list:
        if val not in orig_list:
            orig_list.append(val)

    for val in delete_list:
        if val in orig_list:
            orig_list.remove(val)

    result_list = sorted(orig_list, key = lambda x: (len(x), x), reverse=True)
    return result_list


print(manipulate_list(['one', 'two', 'three'], ['one', 'two', 'five', 'six', 'ten'], ['two', 'five']))