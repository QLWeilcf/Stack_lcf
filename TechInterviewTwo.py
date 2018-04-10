#TechInterview


#数组转字符串的4种方法
'''
''.join(map(str,lst)) #注意直接写str也是可以的
''.join(i.__str__() for i in lst)
''.join(str(i) for i in lst)
''.join(i.__repr__() for i in lst)
'''

def listToInt(lst):
    return int(''.join(map(str,lst)))




