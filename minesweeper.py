"""
Write a function that will take 3 arugments:
bombs = [[r1, c1], [r2, c2]] - bomb location
rows, columns - the matrix dimensions

we should return an 3 x 4 array (-1) = bomb


""" 
def mine_sweeper(bombs, num_rows, num_cols):
    # create a fill the field 
    mine_field = [[0 for i in range(num_cols)] for j in range(num_rows)]
        
    for bomb_location in bombs:
        (bomb_row, bomb_col) = bomb_location
        mine_field[bomb_row][bomb_col] = -1     # add the location of the bomb

        # create a lookup range
        row_range = range(bomb_row - 1, bomb_row + 2)
        col_range = range(bomb_col - 1, bomb_col + 2)

        for i in row_range:
            current_i = i
            for j in col_range:
                current_j = j
                if (0 <= i < num_rows and 0 <= j < num_cols and mine_field[i][j] != -1):
                    mine_field[i][j] += 1
        
    return mine_field

for row in mine_sweeper([[0, 1], [2, 3]], 5, 5):
    print(row)