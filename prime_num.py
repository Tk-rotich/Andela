def find_prime(number):

	a = [1]*number
	b = range
	for i in b(2,number):
	 if a[i]:
	  for j in b(i*i,number,i):
	  	a[j]=0
	print ([i for i in b(len(a))if a[i]==1][2:])


find_prime(1000)


	
		



