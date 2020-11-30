class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n+m) because we need to go through the original array, and 
    the count array
    Memory usage: O(n+m) because we are creating a count array and a sorted array"""
    count_arr = []
    sorted_arr = []
    min_num = numbers[0]
    max_num = numbers[0]
    for num in numbers:
        count_arr[num] += 1
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    for i in range(min_num, max_num):
        while count_arr[i] > 0:
            sorted_arr.append(i)
            count_arr[i] -= 1


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: O(n+m) because we are going through the original array, and then
    the bucket array
    Memory usage: O(nm) because we are creating a hash bucket, so an array with arrays 
    inside it"""
    maxValue = 100
    # Find range of given numbers (minimum and maximum values)
    min_num = numbers[0]
    max_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num

    # Create list of buckets to store numbers in subranges of input range
    bucket = []
    for _ in range(0, num_buckets):
        node = Node(0)
        bucket.append(node)

    # Loop over given numbers and place each item in appropriate bucket
    for i in range(0, num_buckets):
        val = numbers[i]
        index = (val*num_buckets)/maxValue
        add_to_bucket(bucket, val, index)

    # Loop over buckets and append each bucket's numbers into output list
    result = []
    for i in range(0, num_buckets):
        current = bucket[i]
        current = current.next
        while not current == None:
            result.append(current.key)
            current = current.next

def add_to_bucket(bucket, val, index):
    node = Node(val)
    current = bucket[index]
    while not current.next == None:
        if val < current.next.key:
            insert_node(current, node, current.next)
            return
        else:
            current = current.next
    current.next = node

def insert_node(previous, current, next_node):
    previous.next = current
    current.next = next_node

