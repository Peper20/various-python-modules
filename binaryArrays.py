# import numpy as np




def generate_array(size):
	pass


def is_set_bit(number, index):
	return (number & (1 << index)) != 0

def set_bit(number, index):
	return number | (1 << index)

def reset_bit(number, index):
	return number & ~(1 << index)

def inverse_bit(number, index):
	return number ^ (1 << index)

# a = 6
# print(bin(a))
# print(bin(reset_bit(a, 1)))