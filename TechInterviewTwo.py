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

#最近并且大于自身的换位数
#思路：尽量保持高位不变，低位在最小的范围内变换顺序。
#逆序区域从后面开始取;
# 从后向前查看逆序区域，找到逆序区域的前一位，也就是数字置换的边界
# 把逆序区域的前一位和逆序区域中刚刚大于它的数字交换位置
# 把原来的逆序区域转为顺序

def maxtNum(num):
    #intput: 12345，out: 12354
    #in: 124653  out:125346
    #in: 54321 out: 54321
    #输入合法性验证
    try:
        a=int(num)
        if a!=num:
            return '输入不合法'
    except:
        return '输入不符合规则'
    lst=[int(i) for i in str(num)] #数值转数组
    j=2
    '''
    if (lst[-2]>lst[-1]):
        lst[-1],lst[-2]=lst[-2],lst[-1]
        return listToInt(lst)
    '''
    #for i in range(1,len(lst)+1): #感觉用-i的计数不够友好
    k=len(lst)
    for i in range(k-2,-1,-1): #或者循环 len(lst)-1,0,-1
        #if i==0 and lst[i]>=lst[i+1]:
            #return listToInt(lst) #循环到0还没有解时，不需要再进行计算下去了
        if lst[i]<lst[i+1]:
            #找到比 lst[i]更大且离其最近的数
            '''
            for j_id,j in enumerate(alst):
                if j >lst[i]:
                    if idx_j[1]>j:
                        idx_j[1]=j
                        idx_j[0]=j_id
            lst[i],lst[i+idx_j[0]]=lst[i+idx_j[0]],lst[i] #交换
            '''
            #同样从后往前找
            for j in range(k-1,i,-1):
                if lst[j]>lst[i]:
                    lst[i],lst[j]=lst[j],lst[i]
                    break  #跳出第二个 for

            a2=lst[i+1:]
            lst=lst[:i+1]  #lst[:i+1].extend(sorted(a2)) 是不对的
            lst.extend(sorted(a2))
            break
            #return listToInt(lst)#也可以用break
    return listToInt(lst)
    
    
#进阶：根据字典序算法输出一个数的全排列

# offer 45
#要求：0到n-1排成一圈，从0开始每次数m个数删除，求最后剩余的数
#可以用模拟的方式求，模拟取数过程，效率低些
#思路：当 n > 1 时： f(n,m) = [f(n-1, m)+m]%n,当 n = 1 时： f(n,m)=0，关键是推导出关系表达式

def last_num(n, m):
    ret = 0
    if n == 1:
        return 0
    for i in range(2, n+1):
        ret = (m + ret) % i
    return ret



