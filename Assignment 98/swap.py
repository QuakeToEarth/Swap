f1 = open('file1.txt')
f2 = open('file2.txt')
data1 = f1.read()
data2 = f2.read()
fw1 = open('file1.txt', 'w')
fw2 = open('file2.txt', 'w')
fw1.write(data2)
fw2.write(data1)