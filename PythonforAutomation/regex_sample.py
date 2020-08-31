import re
my_str="This is about python. Python is easy to learn and we have two mahor versions: python2 and python3"
my_pat=r'\b[pP]ython[23]?\b'

'''print(re.findall(my_pat,my_str))
print(re.search(my_pat,my_str))
print(re.split(my_pat,my_str))
'''
pat_ob=re.compile(my_pat,flags=re.I)
print(pat_ob.search(my_str))
print(pat_ob.findall(my_str))