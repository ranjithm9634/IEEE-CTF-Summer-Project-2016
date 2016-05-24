a=int(raw_input('Enter octal number to be converted '))

def octtodec(a):
	i=0
	dec=0
	while(a>0):
		dec=dec+(a%10)*(8**i)
		a=a/10
		i=i+1
	return dec
print 'decimal-> ',
print octtodec(a)
def octtobin(a):
	x=octtodec(a)
	bin=' '
	while(x>0):
		if(x%2==1):
			bin='1'+bin
		else:
			bin='0'+bin
		x/=2
	bin.rstrip()
	return bin
print 'binary-> '+octtobin(a)		
	 			
