# This Python file uses the following encoding: utf-8
import copy
from itertools import *

data={
       't1':['a1','a2','a5'],
       't2':['a2','a4'],
       't3':['a2','a3'],
       't4':['a1','a2','a4'],
       't5':['a1','a3'],
       't6':['a2','a3'],
       't7':['a1','a3'],
       't8':['a1','a2','a3','a5'],
       't9':['a1','a2','a3'],
}
min_sup = 2
C = []
C.append([])

#找出频繁1项集的集合
def find_frequent_1_itemsets( D ):

    itemset = {}
    res = [] 
    tempList = []

    for buyId in D :
        for itemId in D[buyId]:
            if itemset.has_key( itemId ): 
                itemset[itemId] +=1
            else:
                itemset[itemId] =1

    for itemId in itemset:
        if itemset[itemId] >= min_sup:
            temp={}
            temp['item'] = [itemId]
            temp['sup']  = itemset[itemId]
            res.append(temp)
            tempList.append(itemId)
    C.append(tempList)
    return res
#apriori 连接和剪枝
def apriori_gen( L ):

    itemset =[]
    res = []
    tempList = []
    startY = 0 

    for x in L:
        startY += 1
        for y in L[startY:]:
            if x == y : continue
            if x['item'][:-1] == y['item'][:-1]:
                temp={}
                temp['item'] = copy.deepcopy(x['item'])
                temp['item'].append( y['item'][-1] )
                temp['item'].sort()
                if has_infrequent_subset(temp['item']):
                    temp['sup']  = get_sup( temp['item'] ) 
                    itemset.append(temp)
    for item in itemset:
        if item['sup'] >= min_sup:
            res.append(item)
            tempList.append(item['item'])
    C.append(tempList)
    return res

#先验性质
def has_infrequent_subset( c ):
    K = len(c) - 1
    for x in  permutations( c ,K ):
        if x not in C[K] : continue
        return 0
    return 1 
#获取支持度计数
def get_sup( c ):
    sub = len( data )
    for buyId in data :
        for itemId in c:
            if itemId not in data[buyId]: 
                sub -=1
                break
    return sub

L={}
L[1] = find_frequent_1_itemsets(data)
res = apriori_gen( L[1] )
L[2] = res
res = apriori_gen( L[2] )
L[3] = res 
res = apriori_gen( L[3] )
L[4] = res 
print L

