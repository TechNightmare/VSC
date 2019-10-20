import time

def bubblesort(list):
    """
    Implements Bubblesort using an list as input and
    returning a sorted list

    :param list
    :return: list
    """
    # Bubblesort implementation based on pseudocode at: https://de.wikipedia.org/wiki/Bubblesort

    for i in range(len(list), 1, -1):							# after each iteration border gets decremented(other part of list already sorted)
    	for j in range(len(list) - 1):						
    		if(list[j] > list[j + 1]):							# if order of both elements incorrect
    			list[j], list[j + 1] = list[j + 1], list[j]		# swap --> a,b = b,a
    return list

sum = 0
for i in range(100):
	time1 = time.time()
	sorted_list = bubblesort([ 5, 14, 10, 7, 2, 13, 1, 12, 6, 9, 0, 3, 8, 11, 4 ])
	time2 = time.time()
	sum +=(time2-time1)


print(sorted_list)

print("durchschnittliche Sortierzeit: ", sum / 100)