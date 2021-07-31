dic1 = {1:10, 2:20 }
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
final_dic = {}
final_dic.update(dic1)
final_dic.update(dic2)
final_dic.update(dic3)
print(final_dic)

'''output
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''