__all__ = [
	'is_set_bit', 'is_reset_bit', 'set_bit',
	'reset_bit', 'inverse_bit', 'uniq_values_bit_array',
	'uniq_values_count',
]


# binary func tools beginning {

def is_set_bit(number, index, /):
	return (number & (1 << index)) == 1

def is_reset_bit(number, index, /):
	return (number & (1 << index)) == 0


def set_bit(number, index, /):
	return number | (1 << index)

def reset_bit(number, index, /):
	return number & ~(1 << index)


def inverse_bit(number, index, /):
	return number ^ (1 << index)

# } binary func tools end



# utilities func tools beginning {

def uniq_values_bit_array(array, /):
	bit_array = 0

	for value in array:
		bit_array = set_bit(bit_array, value)

	return bit_array

def uniq_values_count(array):
	return uniq_values_bit_array(array).bit_count()

# } utilities func tools end