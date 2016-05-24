a=raw_input('Enter the hexadecimal string to convert ')
def hextodec(a):
	dec=0
	x=0
	hexstr='0123456789ABCDEF'
	while x<len(a):
		i=hexstr.find(a[x])
		dec=dec+i*(16**x)
		x=x+1
	return dec
print 'decimal-> ',
print hextodec(a)	
def hextobin(a):
	x=hextodec(a)
	i=0
	bin=' '
	while(x>0):
		if(x%2==1):
			bin='1'+bin
		else:
			bin='0'+bin
		i=i+1
		x/=2
	bin.rstrip()	
	return bin	
print 'binary-> '+hextobin(a)	
