import os
i="*"
k=eval(input("enter a num: "))
j=1
n=os.get_terminal_size().columns
while k>=j:
    l=j*i
    m=l.center(n)
    print(f"{m}")
    j=j+1