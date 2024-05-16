def main():
	a, b, c = tuple(map(int, input().split()))
 
	print(str(max(a+b+c, a+b*c, (a+b)*c, a*b+c, a*(b+c), a*b*c)) + '\n')
 
if __name__ == '__main__':
	main()