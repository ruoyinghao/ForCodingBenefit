#written by Ruoying Hao on 6/19/2016
#My first web scripting tools in python
#Scripted Chinese ONE magazine's essay paragraphs by essays and stored on desktop

from urllib import request  
import re
import os

exist=True

for number in range(10,50):
    exist=True
    #scrap the web page, filter page if not found
    try:
        response = request.urlopen("http://wufazhuce.com/article/"+str(number)) 
        content = response.read().decode('utf-8')
    except:
        print(str(number)+" doesn't exist")
        exist=False
        
    if exist==True:
        #write source code
        f=open("output"+str(number)+".txt","w+",encoding='utf-8')
        f.write(content)
        f.close()
        
        #reopen, need a better method
        z=open("output"+str(number)+".txt","r",encoding='utf-8')
        buff = z.read()

        #clean the web source code,locate target area
        w1='<div class="articulo-contenido">'
        w2 = '</div>'
        buff = buff.replace('\n\t\t\t\t\t\t','')
        buff = buff.replace('<br>','\n')
        buff = buff.replace('<strong>','')
        buff = buff.replace('</strong>','')
        pat = re.compile(w1+'(.*?)'+w2,re.S)
        result = pat.findall(buff)
        
        #output paragraphs/articles
        t=open("article"+str(number)+".txt","w",encoding='utf-8')
        t.write(result[0])
        
        #close documents
        f.close()
        z.close()
        t.close()
