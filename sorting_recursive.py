def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    
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
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    if len(items) <= 1:
        return items

    mid = len(items) / 2
    left = merge_sort(items[:int(mid)])
    right = merge_sort(items[int(mid):])

    return merge(left, right)


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p

    # if len(items) <= 1:
    #     return items
    # else:
    #     pivot = items.pop()

    # low = []
    # high = []

    # for item in items:
    #     if item > pivot:
    #         high.append(item)
    #     else:
    #         low.append(item)

    # return partition(low) + [pivot] + partition(high)
        



def quick_sort(items):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

    if len(items) <= 1:
        return items
    else:
        pivot = items.pop()

    low = []
    high = []

    for item in items:
        if item > pivot:
            high.append(item)
        else:
            low.append(item)

    return quick_sort(low) + [pivot] + quick_sort(high)