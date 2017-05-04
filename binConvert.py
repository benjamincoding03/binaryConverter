#!/usr/bin/python
import sys, argparse, binascii

def main():
	try:
		p = argparse.ArgumentParser(description='Convert ASCII to binary and vise-versa')
		p.add_argument('-a', '--ascii', dest='ascii', help='If converting from ascii to binary use this option')
		p.add_argument('-b', '--binary', dest='binary', help='If converting from binary to ascii use this option         ')
		args = p.parse_args()

		if type(args.ascii) == str:
			string = args.ascii
			binary = bin(int(binascii.hexlify(string), 16))
			print binary
			sys.exit()

		elif type(args.binary) == str:
			binary = args.binary
			n = int(binary, 2)
			string = binascii.unhexlify('%x' % n)
			print string
			sys.exit()

		else:
			print 'Please enter a value'
			sys.exit()

	except TypeError:
		print 'Please enter a valid value'
		sys.exit()

	except ValueError:
		print 'Please enter a valid value'
		sys.exit()

	except KeyboardInterrupt:
		print 'Error'
		sys.exit()

main()
