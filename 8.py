nterms = int(input("the terms"))
n1,n2=0,1
count =0
if nterms<=0:
    print("Please enter a positlive integer")
elif nterms==1:
    print("fibbonaci sequence upto",nterms,":")
    print(n1)
else:
    print("fibbonnacci sequence:")
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1 = n2
        n2 = nth
        count += 1
