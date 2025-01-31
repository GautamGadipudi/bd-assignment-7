'''
    Author: Gautam Gadipudi
    RIT Id: gg7148
'''

from pg.operations import create_l1_table, create_ln_table, get_ln_row_count, create_final_table

create_l1_table()
i = 2
while True:
    create_ln_table(i)
    n = get_ln_row_count(i)
    if n == 0:
        print(f'No rows in LEVEL {i}. QUITTING...')
        break
    print(f'LEVEL {i} DONE!!')
    i += 1

max_level = i - 1
create_final_table(max_level)
print('PROCESS COMPLETE! Check actors in table - final_level')
