a=[1,3,2,4,5,6,5,8]
import collections
print([item for item, count in collections.Counter(a).items() if count > 1])
        
