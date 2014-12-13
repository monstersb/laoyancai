#! /usr/bin/env python
#! -*- coding: utf-8 -*-
chess = []
[chess.extend([(j, i + 1) for j in range(4)]) for i in range(13)]
score = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]

import random
import card

def getCard():
	r = random.randint(0, len(chess) - 1)
	return chess.pop(r)


zj = []
wj = []

print '下注......',
print '发牌......',
print '玩家 => 1',
wj.append(getCard())
print '庄家 => 1',
zj.append(getCard())
print '玩家 => 2',
wj.append(getCard())
print '庄家 => 2'
zj.append(getCard())

print '\n'.join(map(lambda a, b: a + '  ' + b, card.card(*wj[0]), card.card(*wj[1])))
if score[zj[0][1]] + score[zj[1][1]] in [8, 9]:
	print '庄家牌'
	if len(zj) == 2:
		print '\n'.join(map(lambda a, b: a + '  ' + b, card.card(*zj[0]), card.card(*zj[1])))
	else:
		print '\n'.join(map(lambda a, b, c: a + '  ' + b + '  ' + c, card.card(*zj[0]), card.card(*zj[1]), card.card(*zj[2])))
		
	print '玩家牌'
	if len(wj) == 2:
		print '\n'.join(map(lambda a, b: a + '  ' + b, card.card(*wj[0]), card.card(*wj[1])))
	else:
		print '\n'.join(map(lambda a, b, c: a + '  ' + b + '  ' + c, card.card(*wj[0]), card.card(*wj[1]), card.card(*wj[2])))
	if zj[0][0] == zj[1][0]:
		print '庄家双倍炸开'
	else:
		print '庄家炸开'
	exit()

if score[wj[0][1]] + score[wj[1][1]] in [8, 9]:
	print '要不要炸开？',
	yby = raw_input().lower()
	if yby[0] == 'y':
		print '庄家牌'
		if len(zj) == 2:
			print '\n'.join(map(lambda a, b: a + '  ' + b, card.card(*zj[0]), card.card(*zj[1])))
		else:
			print '\n'.join(map(lambda a, b, c: a + '  ' + b + '  ' + c, card.card(*zj[0]), card.card(*zj[1]), card.card(*zj[2])))
			
		print '玩家牌'
		if len(wj) == 2:
			print '\n'.join(map(lambda a, b: a + '  ' + b, card.card(*wj[0]), card.card(*wj[1])))
		else:
			print '\n'.join(map(lambda a, b, c: a + '  ' + b + '  ' + c, card.card(*wj[0]), card.card(*wj[1]), card.card(*wj[2])))
		if wj[0][0] == wj[1][0]:
			print '玩家双倍炸开'
		else:
			print '玩家炸开'
		exit()
print '要不要牌？',
yby = raw_input().lower()
if yby[0] == 'y':
	wj.append(getCard())
	print '\n'.join(map(lambda a, b, c: a + '  ' + b + '  ' + c, card.card(*wj[0]), card.card(*wj[1]), card.card(*wj[2])))
	print '玩家要牌'
else:
	print '玩家不要牌'


if score[zj[0][1]] + score[zj[1][1]] > 10:
	print '庄家不要牌'
else:
	print '庄家要牌'
	zj.append(getCard())

szj = reduce(lambda a, b : a + score[b[1]], zj, 0) % 10
swj = reduce(lambda a, b : a + score[b[1]], wj, 0) % 10

print zj, szj
print wj, swj

print '庄家牌'
if len(zj) == 2:
	print '\n'.join(map(lambda a, b: a + '  ' + b, card.card(*zj[0]), card.card(*zj[1])))
else:
	print '\n'.join(map(lambda a, b, c: a + '  ' + b + '  ' + c, card.card(*zj[0]), card.card(*zj[1]), card.card(*zj[2])))
	
print '玩家牌'
if len(wj) == 2:
	print '\n'.join(map(lambda a, b: a + '  ' + b, card.card(*wj[0]), card.card(*wj[1])))
else:
	print '\n'.join(map(lambda a, b, c: a + '  ' + b + '  ' + c, card.card(*wj[0]), card.card(*wj[1]), card.card(*wj[2])))
print '庄家 %d 分， 玩家 %d 分' % (szj, swj)

bs = ''
if szj > swj:
	if len(zj) == 2 and zj[0][1] == zj[1][1]:
		bs = '双倍'
	elif len(zj) == 3 and zj[0][1] == zj[1][1] and zj[0][1] == zj[2][1]:
		bs = '三倍'
	elif len(zj) == 3 and zj[0][0] == zj[1][0] and zj[0][0] == zj[2][0]:
		bs = '五倍'
	print '庄家%s胜' % bs
elif szj == swj:
	print '平手'
else:
	zj = wj
	if len(zj) == 2 and zj[0][1] == zj[1][1]:
		bs = '双倍'
	elif len(zj) == 3 and zj[0][1] == zj[1][1] and zj[0][1] == zj[2][1]:
		bs = '三倍'
	elif len(zj) == 3 and zj[0][0] == zj[1][0] and zj[0][0] == zj[2][0]:
		bs = '五倍'
	print '玩家胜'
