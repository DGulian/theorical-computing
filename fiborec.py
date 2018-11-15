from math import * 

def parite(a):
    if(a%2==0):
        print('le nombre est pair')
    else:
        print('le nombre est impaire')

def polynome(a,b,c):
    d = pow(b,2) - 4 * a * c
    print(d)
    if(d==0):
        s = -b / 2*a
        float(s) 
        print(s, 'est la solution ')
    elif(d > 0):
        sa = -b - sqrt(d) / 2*a
        float(sa)
        sb = -b + sqrt(d) / 2*a
        float(sb)
        print(sa, sb, 'sont les solutions de l equation')
    else:
        print('il n y a pas de solution')

def bissextile(a):
    if(a%4==0 and a%100!=0 or a%400==0):
        print('l annee ', a, ' est bissextile') 
    else:
        print('l annee ',a, 'n est pas bissextile')


def convert(n):
    if(n<0):
        return 'Must be an positiv int'
    elif(n==0):
        return ''
    else:
        return(convert(n//2)+str(n%2))
print(convert(4589461))
               
def facto(n):
    if(n<2):
        return 1
    else:
        return(facto(n-1)*n)

print(facto(5))

def syracuse(n):
    if(n%2==0):
        n = n / 2
        print(n)
        return (syracuse(n))
    else:
        n = 3 * n + 1
        print(n)
        return (syracuse(n))
    


def flot(n,acc):
	if (acc == 1):
		if (n>=0.5 and n!= 1.0):
			return "1"
		return "0"

	if(n == 1.0):
		return "0" + flot(1.0,acc-1)
	else:
		if (str(n)[0]=="1"):
			n -= 1
		n *= 2
		return str(n)[0] + flot(n,acc-1)

def mantiss(n):
    ent = int(n)
    dec = n - int(n)

    #Conversion binaire

    binEnt = convert(ent)
    binDec = flot(dec,23-len(str(ent)))
    print(binEnt + binDec)
    exposant = (len(str(binEnt))) - 1
    print(exposant)
    binExp= convert(exposant+127)
    print(binExp)
    print(binEnt, binDec, binExp)
    binEnt = binEnt[1:]
    print(binEnt, binDec, binExp)
    flott = binDec+binEnt+binExp
    if(n>0):
        flott = "0" + flott
    else:
        flott = "1" + flott

    print(flott, len(str(flott)))    




