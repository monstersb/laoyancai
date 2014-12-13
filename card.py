with open('pattern.data', 'r') as f:
	data = [[f.readline().strip('\n') for i in range(8)] for i in range(4)]


def card(s, n):
	k = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
	c = [30, 31]
	result = ['\033[40;37;1m*\033[0m' * 13]
	result.append("\033[40;37;1m*\033[46;%d;1m%9s  \033[40;37;1m*\033[0m" % (c[s % 2], k[n]))
	result.extend(['\033[40;37;1m*\033[46;' + str(c[s % 2]) + ';1m ' + i + ' \033[40;37;1m*\033[0m' for i in data[s][:-1]])
	result.append('\033[40;37;1m*\033[0m' * 13)
	return result

if __name__ == '__main__':
	a = card(1, 2)
	b = card(2, 7)
	c = card(3, 11)
	d = card(0, 1)
	print '\n'.join(map(lambda a, b, c, d: a + b + c + d, a, b, c, d))
