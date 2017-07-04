#coding:utf-8
import time,re,os
import threading,multiprocessing 
#lock=threading.Lock()                                    #本搜索工具采用多线程同时从c,d,e,f,g,h盘搜索数据，采用正则表达式模糊匹配要搜索的结果
def find_dir_or_all(path,name,x):                         #find_all和find_dir的公用函数，作用批量创建线程
    root=["h:\\","d:\\","e:\\","f:\\","g:\\","c:\\"]      #列出系统磁盘作为参数供线程调用
    tc=td=te=tf=tg=th=0                                   #初始化线程对象，让它可以被放到列表里面
    ta=[tc,td,te,tf,tg,th]                                #把线程对象写入列表，让它可以用循环批量创建线程start，和等待线程join
    tb=[]                                                 #tb用于接受经改变的线程对象
    for  i in range(len(root)):
        ta[i]=threading.Thread(target=find_dir_or_all_sub,args=(root[i],name,x))
        tb.append(ta[i])    
    for ci  in range(len(root)):
        tb[ci].start()
    for cii in range(len(root)):
        tb[cii].join()
def find_dir_or_all_sub(path,name,x):                          #find_dir和find_all公用的最底层搜索函数由x控制是find_dir还是find_all
    global m                                                   #m作为计数器用作搜索结果的序号
    #lock.acquire()
    for path1,d,file in os.walk(path):
        r=re.compile(r".*%s.*" %name,re.I)
        if x==1:   
            for i in file:
                rr=r.findall(i)
                if rr:
                    print("%d."%m,os.path.join(path1,rr[0]))
                    m=m+1
        if x==2:
            for i in d:
                rr=r.findall(i)
                if rr:
                    print("%d."%m,os.path.join(path1,rr[0]))
                    m=m+1
        if x==3:
            if name in file:
                print("%d."%m,os.path.join(path1,name))
                m=m+1
        if x==4:
            if name in d:
                print("%d."%m,os.path.join(path1,name))
                m=m+1
    #lock.release()
def find_all(path,name):
    x=1                                           #函数用作调用搜索函数
    if path=="root":
        find_dir_or_all(path,name,x)
    else:
        find_dir_or_all_sub(path,name,x) 
def find_dir(path,name):                          #函数作为调用底层的搜索函数
    x=2                                           #flag标志是哪个想要进入搜索的最底层函数
    if path=="root":
        find_dir_or_all(path,name,x)   
    else:
        find_dir_or_all_sub(path,name,x)   
def find_file(path,name):
    x=3
    if path=="root":
        find_dir_or_all(path,name,x)   
    else:
        find_dir_or_all_sub(path,name,x)  
def find_dir_allname(path,name):
    x=4
    if path=="root":
        find_dir_or_all(path,name,x)   
    else:
        find_dir_or_all_sub(path,name,x)  
def find_help():                                  #函数输出提示消息
    print(" >python多线程搜索工具<")
    print(" 1.find_all(path,name)          显示在path下面的文件(file)，<模糊匹配>")
    print(" 2.find_dir(path,name)          显示在path下面的文件夹(dir) <模糊匹配>")
    print(" 3.find_file(path,name)         显示在path下面的文件(file)  <非模糊匹配>")       
    print(" 4.find_dir_allname(path,name)  显示在path下面的文件夹(dir) <非模糊匹配>")
    print(" 5.<exit>")
def options(option,tip):
    if option:
        option=int(option)
    path=input("请输入查找的绝对路径path(默认c盘,空格表示root):")
    if path=="":
        path="c:\\"
        print("--->搜索C盘c:\\")
    if path==" ":
        path="root"
        print("--->搜索这台电脑root")
    name=input("%s:"%tip)
    time1=time.time()
    if option=="" or option==1:
        find_all(path,name)
    if option==2:
        find_dir(path,name)
    if option==3:
        print("ok")
        find_file(path,name)
    if option==4: 
        find_dir_allname(path,name)
    time2=time.time()
    time.sleep(1)
    print("Done! all find result as the follow! total(%d),use time(%fs)\n"%(m-1,time2-time1))  
if  __name__=="__main__":
    while True:
        m=1
        find_help()
        option=input("输入查找方式的序号(默认是1):")
        if option=="":
            print("--->1.find_all()")
            tip="请输入想要查找的文件file.*"
            options(option,tip)
        elif option=="1":
            tip="请输入想要查找的文件file.*"
            print("--->1.find_all()")
            options(option,tip)
        elif option=="2":
            tip="请输入想要查找的文件夹dir.*"
            print("--->2.find_dir()")
            options(option,tip)
        elif option=="3":
            tip="请输入想要查找的文件file"
            print("--->3.find_file()")
            options(option,tip)
        elif option=="4":
            tip="请输入想要查找的文件夹dir"
            print("--->4.find_dir_allname()")
            options(option,tip)
        elif option=="5":
            exit()
        else:
            print("警告!输入错误！")
            pass           
 

    



                
            
            

