customer = [12,13,45,46,89,90]
le = len(customer)
s = int(input("Enter 1 for liner search and 2 for binary search"))
ss=int(input("Enter customer ID to search"))
if (s ==1):
    found=False
    for i in range (le):
        if(customer[i]==ss):
            print("Customer ID found ")
            found=True
            break
    if (found==False):
        print("Customer Not FOund")
elif(s==2):
    high=le-1
    low= 0
    found=False
    while(low<=high):
        mid=(low+high)//2
        if(ss==customer[mid]):
            print("Customer ID found")
            found=True
            break
        elif(ss>customer[mid]):
            low = mid+1
        else:
            high = mid-1
    if (found==False):
        print("Customer Not FOund")
else:
    print("Invalid Option")