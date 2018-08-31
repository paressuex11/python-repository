#温度转换程序
TempStr = input('请输入温度及类型:')
if TempStr[-1] in ["F",'f']:
    c = (eval(TempStr[0:-1])-32)/1.8
    print ("转换的结果是{:.2f}".format(c))
elif TempStr[-1] in ["C","c"]:
    c=eval(TempStr[0:-1])*1.8+32
    print('转换的结果是{:.2f}'.format(c))      
else:
    print('输入格式错误')    
    
