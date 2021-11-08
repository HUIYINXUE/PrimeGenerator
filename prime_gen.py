from numba import jit

@jit(nopython=True)
def prime_gen(lower_bound=2, upper_bound=10000):
	assert upper_bound>=3, '2, 3 are all the primes <= 3'
	assert lower_bound>=2, 'no primes <= 2'
	prime_list = [2, 3]
	n_prime_samll = 1
	for i in range(4, upper_bound+1):
		flag = True
		for j in prime_list:
			if j**2 > i:
				continue
			if i % j == 0:
				flag = False
				continue
		if flag == True:
			prime_list.append(i)
			if i<= lower_bound:
				n_prime_samll += 1
	if lower_bound == 2:
		n_prime_samll = 0
	prime_list = prime_list[n_prime_samll:]
	return prime_list

def get_denom(dim, lower_bound=7, upper_bound=10000):
	candidate = prime_gen(lower_bound, upper_bound)
	step = (len(candidate) + 1) // dim
	return candidate[0::step]

def test():
	print('###########test############\n')
	print('the lowest prime between 2 and 10000 is {:d} \n' .format(prime_gen(2, 10000)[0]))
	print('the lowest prime between 3 and 10000 is {:d} \n' .format(prime_gen(3, 10000)[0]))
	print('the lowest prime between 4 and 10000 is {:d} \n' .format(prime_gen(4, 10000)[0]))
	print('the lowest prime between 5 and 10000 is {:d} \n' .format(prime_gen(5, 10000)[0]))
	print('the lowest prime between 6 and 10000 is {:d} \n' .format(prime_gen(6, 10000)[0]))
	print('the lowest prime between 7 and 10000 is {:d} \n' .format(prime_gen(7, 10000)[0]))
	print('there are {:d} primes under 10000 totally \n' .format(len(prime_gen(2, 10000))))
	print('###########################\n')
	assert len(get_denom(1229, 2, 10000)) == 1229, 'length exceed!'



if __name__ == '__main__':
	test()
	print(get_denom(512, 7, 100000))
