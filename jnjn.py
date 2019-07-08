s=input()
count=0
for i in s:
    if i>='a' and i<='z' or i>='A' and i<='Z' or i==" ":
        continue
    else:
        count+=1
print(count)
