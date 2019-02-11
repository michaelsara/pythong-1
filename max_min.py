#coding=utf-8
def max_min(the_list):
    for i in the_list:
        if the_list.index(i) == 0:
            max_value = i
            min_value = i
        the_list.pop(0)
        for j in the_list:
            if j > max_value:
                max_value = j
            if j < min_value:
                min_value = j
    print(max_value,min_value)
if __name__ == '__main__':
    max_min([4,3,7,9,1,0])
