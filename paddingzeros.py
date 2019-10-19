In Python 2 you can do:

print "%02d" % (1,)
Basically % is like printf or sprintf.

For Python 3.+ the same behavior can be achieved with:

print("{:02d}".format(1))
For Python 3.6+ the same behavior can be achieved with f-strings:

print(f"{1:02d}")
