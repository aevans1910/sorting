def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n) because it only checks all the items once
    TODO: Memory usage: O(1) because we are only creating 1 new set variable"""
    # TODO: Check that all adjacent items are in order, return early if so
    count = 0
    for _ in items:
        if count == 0:
            count += 1
            continue
        elif items[count] < items[count - 1]:
            return False
        count += 1
    return True

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: O(n^2) because of nested for loop
    TODO: Memory usage: O(1) because we are only creating 1 new set variable"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    
    while not is_sorted(items):
        count = 0
        for item in items:
            if count == 0:
                count += 1
                continue
            if item < items[count - 1]:
                items[count - 1], items[count] = items[count], items[count - 1]
            count += 1
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: O(n^2) but better then bubble sort, because of nested
    for loop
    TODO: Memory usage: O(1) because we are only creating a few set variables"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    indexing_length = range(0, (len(items) - 1))

    for i in indexing_length:
        min_item = i

        for j in range(i + 1, len(items)):
            if items[j] < items[i] and items[j] < items[min_item]:
                min_item = j

        if min_item != i:
            items[min_item], items[i] = items[i], items[min_item]

    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: O(n^2) but better then bubble sort and selection sort, 
    because nested for loop
    TODO: Memory usage: O(1) because we are only creating small new variables with 
    set values"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    indexing_length = range(1, len(items))

    for i in indexing_length:
        item_to_sort = items[i]

        while items[i - 1] > item_to_sort and i > 0:
            items[i], items[i - 1] = items[i - 1], items[i]
            i = i - 1
    return items
