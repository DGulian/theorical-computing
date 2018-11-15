Fim1 = 1
Fim2 = 1
print ("suite Fibo")
p = input('saisir p')
p = int(p)
i = 2
while p >= i :
            Fi = Fim1 + Fim2
            i = i + 1
            Fim2 = Fim1
            Fim1 = Fi
            print (Fim1,Fim2)
print(Fi)
print(i)
            
