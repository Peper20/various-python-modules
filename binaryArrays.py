from random import randint




def is_set_bit(number, index):
	return (number & (1 << index)) != 0

def set_bit(number, index):
	return number | (1 << index)

def reset_bit(number, index):
	return number & ~(1 << index)

def inverse_bit(number, index):
	return number ^ (1 << index)



# bit_array = 2 ** (n - 1)

size = 5
max_value = 5
min_value = 0

for i in range(10):
	bit_array = 0
	array = [randint(min_value, max_value) for i in range(size)]
	print(array, end=' ')

	for value in array:
		bit_array = set_bit(bit_array, value)
	
	print('->', bit_array.bit_count())