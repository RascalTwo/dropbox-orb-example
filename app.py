#!/usr/bin/env python3

import os
import time
import random

def gen_row(now: float) -> str:
	return '{}, {}'.format(now, ", ".join([str(random.randint(1, 9)) for _ in range(4)]))

if __name__ == '__main__':
	if os.path.exists('appending.csv'):
		print('Found file, appending')
	else:
		print('File not found, creating new')
		with open('./appending.csv', 'w') as file:
			file.write('When, #1, #2, #3, #4')


	now = time.time()
	with open('./appending.csv', 'a') as file:
		file.write('\n' + gen_row(now))
