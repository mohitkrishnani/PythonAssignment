f=open("sample.txt","r")
s = f.read()
print(s)
f.close()
f = open("sample.txt","a")
f.write("Hello added this")
f.close()
f=open("sample.txt","r")

s2 = f.read()
print(s2)
f.close()


'''Hello Printed this
Hello Printed thisHello added this'''