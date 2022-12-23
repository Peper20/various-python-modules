# binary func tools beginning {

def is_set_bit(number, index):
	return (number & (1 << index)) == 1

def is_reset_bit(number, index):
	return (number & (1 << index)) == 0


def set_bit(number, index):
	return number | (1 << index)

def reset_bit(number, index):
	return number & ~(1 << index)


def inverse_bit(number, index):
	return number ^ (1 << index)

# } binary func tools end



# utilities func tools beginning {

def unique_occurrences_bit_array(array):
	bit_array = 0

	for value in array:
		bit_array = set_bit(bit_array, value)

	return bit_array

def unique_occurrences_count(array):
	return unique_occurrences_bit_array(array).bit_count()



# } utilities func tools end