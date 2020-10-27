def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
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
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
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
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
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
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items