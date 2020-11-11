def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(n+m) because the while loop has to go through the lengths
     of both items1 and items2
    TODO: Memory usage: O(n+m) because we create an array in which we will append 
    items1 and items2"""
    
    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(items1) and right_pointer < len(items2):
        if items1[left_pointer] < items2[right_pointer]:
            result.append(items1[left_pointer])
            left_pointer += 1
        else:
            result.append(items2[right_pointer])
            right_pointer += 1
    
    result.extend(items1[left_pointer:])
    result.extend(items2[right_pointer:])

    return result

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: O(n log n) we will need O(n) time to do the merge 
    opperation. If that is done properly, we will not need to go through the entire
    n length of elements in the array again
    TODO: Memory usage: O(n + m) for the array we create in the merge function"""

    if len(items) <= 1:
        return items

    mid = len(items) / 2
    left = merge_sort(items[:int(mid)])
    right = merge_sort(items[int(mid):])

    return merge(left, right)


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (I chose the item at the end of the array) 
    from that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: O(n) because we go through each item in the array once
    TODO: Memory usage: O(1) because we only create the pivot variable"""
    pivot = items.pop()

    for item in items:
        if item > pivot:
            high.append(item)
        else:
            low.append(item)

    return items
        



def quick_sort(items):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: O(n log n) because in the best case situation we
    woudln't need to go through every element again if it is partitioned properly
    TODO: Worst case running time: O(n^2) if we don't partition well and therefore
    have to go through each element twice
    TODO: Memory usage: O(2n) because we create the low and high arrays"""
    low = []
    high = []

    if len(items) <= 1:
        return items
    else:
        partition(items, low, high)

    return quick_sort(items)
