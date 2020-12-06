def binary_search(array,searched_number):
    first = 0
    last = len(array)
    while first < last:   #if last bigger than first 
        x = first + (last - first) // 2 
        val = array[x]
        if searched_number == val: #if searched number equal to val return x
            return x
        elif searched_number > val: #if searched number bigger than value
            if first == x:   # these two are the actual lines
                break        # you're looking for
            first = x
        elif searched_number < val: #if searched number smaller than value
            last = x
            