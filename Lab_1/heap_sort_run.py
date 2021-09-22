import sys
from heap_sort import heap_sort

sort_order = sys.argv[1]
input_array = [int(number) for number in sys.argv[2].split(",")]
heap_sort(input_array, sort_order)
