dic = {1:'one', 2:'two', 3:'three', 4:"four", 6:'six', 7:'seven', 5:'five', 8:'eight',10:'ten', 9:'nine'}
lt=[x for x in dic.values()]
lt.sort(key=None, reverse=False)
for i in lt:
     print(i) 
