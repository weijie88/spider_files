name_list = [x for x in range(10)]

def createGenorator():
	items = []
	for i in name_list:
		print('第{}次调用'.format(i))
		items.append(i)
	return items

def testFunc1():
	generator = createGenorator2()
	for a in generator:
		print('使用第{}次'.format(a))

def createGenorator2():
	for i in name_list:
		print('第{}次调用'.format(i))
		yield i
print(testFunc1())