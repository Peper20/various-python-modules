def is_set_bit(number, index):
	return (number & (1 << index)) != 0

def set_bit(number, index):
	return number | (1 << index)

def reset_bit(number, index):
	return number & ~(1 << index)

def inverse_bit(number, index):
	return number ^ (1 << index)



#123