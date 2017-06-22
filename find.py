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
    for path,d,file in os.walk(path):
        r=re.compile(r".*%s.*" %name,re.I)
        if x==1:
            mm=file
        if x==2:
            mm=d
        for i in mm:
            rr=r.findall(i)
            if rr:
                print("%d."%m,os.path.join(path,rr[0]))
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
def find_help():                                  #函数输出提示消息
    print(" >python多线程搜索工具<")
    print(" 1.find_all(path,name) 显示在path下面的文件，name不是全称root代表根目录")
    print(" 2.find_dir(path,name) 显示在path下面的名称为name的文件夹")
    print(" 3.<退出>\n")
def option1():
    path=input("请输入查找的绝对路径path(回车表示c盘,空格表示root):")
    if path=="":
        path="c:\\"
        print("--->搜索C盘c:\\")
    if path==" ":
        path="root"
        print("--->搜索这台电脑root")
    name=input("请输入要查找文件的名称(.*):")
    time1=time.time()
    find_all(path,name)
    time2=time.time()
    time.sleep(1)
    print("Done! all find result as the follow! total(%d),use time(%fs)\n"%(m-1,time2-time1))#函数输出结果包括全局变量m和搜索用时
if  __name__=="__main__":
    while True:
        m=1
        find_help()
        option=input("输入查找方式的序号(默认是1):")
        if option=="":
            print("--->1.find_all()")
            option1()
        elif option=="1":
            option1()
        elif option=="2":
            print("--->3.find_dir()")
            path=input("请输入查找的绝对路径path(回车表示c盘,空格表示root):")
            if path=="":
                path="c:\\"
                print("--->搜索C盘C:\\")
            if path==" ":
                path="root"
                print("--->搜索这台电脑root")
            name=input("请输入要查找的文件夹名:")
            time1=time.time()
            find_dir(path,name)
            time2=time.time()
            time.sleep(1)
            print("Done! all find result as the follow! toatal(%d),use time(%fs)\n"%(m-1,time2-time1))
        elif option=="3":
            exit()
        else:
            print("警告!输入错误！")
            pass
            
        
    



                
            
            

