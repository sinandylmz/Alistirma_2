import random
dogruyer=0
yanlısyer=0
    
number=input("Sayıyı giriniz:")
numberr=int(number)
    
computernumber= random.randint(10,98)
computernumberr=str(computernumber)

while True:
        
    if numberr<10 or numberr>98 or number[0]==number[1]:
            print("10 ve 98 arasında ve rakamları farklı bir sayı giriniz!")
    

    elif number[0] in computernumberr or number[1] in computernumberr:
            
        if numberr==computernumber:
            dogruyer+=2
            print("Doğru tahmin ettiniz!")

        elif computernumberr[0]==number[0] and computernumberr[1]!=number[1]:
            dogruyer+=1
            yanlısyer-=1
        else:
            dogruyer+=1
            yanlısyer-=1
    else:
        yanlısyer-=2

    print("Doğru Yer Sayacı=", dogruyer,"Yanlış Yer Sayacı=",yanlısyer)
        

        
        


    
            
        
