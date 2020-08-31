input = [1,2,3,4,4,6,6,7,8,9]
output = []
uniqItems = {}
for x in input:
   if x not in uniqItems:
      uniqItems[x] = 1
   else:
      if uniqItems[x] == 1:
         output.append(x)
      uniqItems[x] += 1
print(output)