num_lst=[] 
for i in range(5): 
    num = int(input('Enter an integer: ')) 
    if num: 
        num_lst.append(num) 
 
print(*[item for item in num_lst if item%5==0]) 
