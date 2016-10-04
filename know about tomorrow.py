
#coding=UTF-8
#tomorrow never knows的各种实现
def Tmrnks():
    #普通版
    import datetime
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    #y=int('2016')
    #m=int('9')
    #t=int('1')
    #tiday=datetime.date(y,m,t)
    #print(tiday)
    #ye = datetime.date.today()
    return today+oneday

def Tmrnknow(today):
    pass
    #格式需要很多处理，不好玩
def TmrnksGui():
    import datetime
    import easygui as g
    today=datetime.date.today()
    nowy=today.year #不需要 str()
    nowm = today.month
    nowd = today.day
    msgx=g.multenterbox('分别输入年 月 日','T N K 1.0',\
           fields=('年：','月：','日:'),values=(nowy,nowm,nowd))

    chobox=[0,'1']
    #chobox = g.multenterbox('输入向前向后的天数：', 'T N K 1.0', \
    #                        fields=('时间矢量', '天数',), values=('向后','1'))

    oneday = datetime.timedelta(days=int(chobox[1]))
    toDay=datetime.date(int(msgx[0]),int(msgx[1]),int(msgx[2]))
    tomorrow=toDay+oneday
    tew=g.msgbox('输入日子对应的“明天”为：'+str(tomorrow))




if __name__=='__main__':
    #print(Tmrnks())
    #TmrnksGui()
    #import Qsci
    print(Tmrnks())
