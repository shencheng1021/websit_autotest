#coding UTF-8
import configparser

#获取指定键
def cget(section,options,filename):
    cp=configparser.ConfigParser()
    with open('../data/'+filename+'.ini') as f:
        cp.read_file(f)
        a=cp.get(section,options)
    return a

#设置指定键
def cset(section,options,filename,value):
    cp=configparser.ConfigParser()
    with open('../data/'+filename+'.ini') as f:
        cp.read_file(f)
        cp.set(section,options,value)
    with open('../data/'+filename+'.ini','w') as f:
        cp.write(f)

#获取section下的所以键
def cget_section(section,options,filename):
    cp=configparser.ConfigParser()
    with open('../data/'+filename+'.ini') as f:
        cp.read_file(f)
        data=cp.items(section)
        return dict(data)
