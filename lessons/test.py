def checkIPValidity(addressIP):
	# Write your code here
	i = 0
	valid = True
	while i < len(addressIP) and valid:
		number = ''
        print(str(i))
		while addressIP[i] != '.':
			number += addressIP[i]
			i += 1
		if int(number) > 255:
			valid = False
		i += 1

	if valid:
		return "VALID"
	else:
		return "INVALID"

def main():
	#input for addressIP
	addressIP = str(input())
	
	result = checkIPValidity(addressIP)
	print(result)	

if __name__ == "__main__":
	main()