f=open("sample_1.csv","r")
s = f.read()
print(s)
f.close()
print()
f=open("sample_1.csv","a")
data = "\n4,four\n5,five"
f.writelines(data)
f.close()
f=open("sample_1.csv","r")
s= f.read()
print(s)

'''Output
1,one
2,two
3,three

1,one
2,two
3,three
4,four
5,five
'''