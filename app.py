#!/usr/bin/env python3

import time
import random

def gen_row(now: float) -> str:
	return '{}, {}'.format(now, ", ".join([str(random.randint(1, 9)) for _ in range(4)]))

if __name__ == '__main__':
	now = time.time()
	with open('appending.csv', 'a') as file:
		file.write('\n' + gen_row(now))

	new_filename = f'{now}.csv'
	with open(new_filename, 'w') as file:
		file.write(gen_row(now))

	print(new_filename)