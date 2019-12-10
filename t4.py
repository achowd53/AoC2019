ans = 0
for x in range(240298,784956+1):
    y = str(x)
    adj = any([(z==0 and y[z] == y[z+1] and y[z] != y[z+2]) or (z == len(y) - 2 and y[z] == y[z+1] and y[z] != y[z-1]) or (z!=0 and z!=len(y)-2 and y[z] == y[z+1] and y[z] != y[z+2] and y[z] != y[z-1]) for z in range(len(y) - 1)])
    dec = any([y[z] < y[z-1] for z in range(1,len(y))])
    if not dec and adj:
        ans += 1
print(ans)        
