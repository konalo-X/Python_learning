
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
fi=open("C:\\Users\\konalo\\Downloads\\鼠标消息.md",mode='r',encoding='UTF-8')
fi2=open("C:\\Users\\konalo\\Downloads\\鼠标消息22.md",mode='w',encoding='UTF-8')
lettes=['a','b','c','d','e','f','g','h','i','j','k','l','m']
#for i in range(0,10):
    #for j in range(0,10):
        #for k in range(0,10):
            #for l in range(0,10):
                #for m in lettes:
                #if( i != k ) and (i != j)  and (j != k) : 
                  #  print (i,j,k,l,m)
print ("文件名为: ", fi.name)
str ="414okmh"
fi2.write(str)
for l in fi.readlines():                          #依次读取每行  
    #line = line.strip()                             #去掉每行头尾空白
    
    fi2.write(l)
    print ("%s" % (l))
                    
fi.close()
fi2.close()
