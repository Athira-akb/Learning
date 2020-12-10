def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


for x in range(0,20):
  print(x)


my_str = 'hellothere'
print(-len(my_str))

a='Hiabc'
b ='abc'
print(a[-1])
if a[-(len(b)):]==b or b[(-len(a))]==b:
  print(True)
else:
  print(False)