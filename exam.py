m=0
factorial=1
pi_sum=0
while True:
    k=int(input("k value entry[5-9]:"))
    t=int(input(" t value entry[2-8]:"))
    if((k>=5 and k<=9)and(t>=2 and t<=8)):
        for n in range(1,k+1):
            factorial*=n
            m=n
            pi=1# more importend this example if 2,4,6,8,10,12,14,16 4,6,8,10,12,14,16 
            #6...,8...,10.... oll to  multiply mistake pi number was would be
            # but to write for lop in "pi=1" to be not mistake pi number 
            for m in range(m,t+1):
                pi*=m*2
                pi_multiply=pi
            pi_factor_sum=pi+factorial# this  "to sum pi multiply and factorial"
            pi_sum=pi_factor_sum+pi_sum
            print(factorial,pi_multiply,pi_factor_sum)
        print("\nsum:",pi_sum)                                                       
        break
