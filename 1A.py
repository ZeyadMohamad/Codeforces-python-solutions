import math
 
def tiles_needed(n, m, a):

    tiles_in_row = math.ceil(n / a)
    tiles_in_column = math.ceil(m / a)

    total_tiles = tiles_in_row * tiles_in_column
 
    return total_tiles

n, m, a = map(int, input().split())

result = tiles_needed(n, m, a)
print(result)