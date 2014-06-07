import sys

if len(sys.argv) > 1:
	limit = int(sys.argv[1])
else:
	limit = 100	


for count in range(0,limit):
	if not(count %5) and not (count %3):
		print "FizzBuzz"
	elif not(count % 3):
		print "Fizz"
	elif not(count %5):
		print "Buzz"
	else:
		print count

