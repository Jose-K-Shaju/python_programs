t=('CAIAS',2,True,3+5j)
print("Tuple: ",t)
length=len(t)
print("Length: ",length)
print("Checking for 'CAIAS' in tuple")
if 'CAIAS' in t:
    print("'CAIAS' is present in tuple t")
else:
    print("'CAIAS' is not present in tuple t")
inx=int(input("Enter the index of item to access: "))
print(f"Item in index {inx} is {t[inx]}")
