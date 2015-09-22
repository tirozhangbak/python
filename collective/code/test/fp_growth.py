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

#全局变量
min_sup = 2
L={}
C=[]


#FP_tree 的数据结构
class Node(object):
    def __init__( self, data = None, sup = 1 ,child = None ):
        self.data = data
        self.sup  = sup 
        self.child = child


#找出频繁1项集的集合
def find_frequent_1_itemsets( D ):

    itemset = {}
    res = [] 

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
    return res

#构造FP_tree
def FP_make_tree( D ):
    #树根
    tree = {'root':{'child':{},'times':0}}

    for buyId in D :
        res = sorted(D[buyId],cmp=compare)
        temp = tree['root']['child']
        for item in res:
            if temp.has_key( item ):
                temp[item]['times'] += 1
            else:
                temp[item] = {}
                temp[item]['child'] = {}
                temp[item]['times'] = 1
            temp = temp[item]['child']
    return tree

#递归实现 挖掘FP_tree 只能返回一条路径
def FP_grouth( fp_tree , item ):
    
    temp = {}
    itemSet =[] 

    if len( fp_tree ) == 0: return None 

    for fp_tree_child in fp_tree['child']:
        if fp_tree_child == item:
            temp[item] = fp_tree['child'][fp_tree_child]['times']
            return temp
        else:
            res = FP_grouth( fp_tree['child'][fp_tree_child] , item )
            if res != None:
                temp[fp_tree_child] = fp_tree['child'][fp_tree_child]['times']
                temp['child'] = {} 
                temp['child'] = res
                return temp 
            else:
                pass

#按支持度计数排序
def sort_sup( item ):
    return item['sup']

#按照1项集排序
def compare(x,y):
    return cmp( C.index(x), C.index(y))

L[1] = find_frequent_1_itemsets(data)
L[1] = sorted(L[1], key=sort_sup, reverse = True)
for x in L[1]:
    C.append(x['item'][0])
FP_tree = FP_make_tree( data )
#print FP_tree
print FP_grouth( FP_tree['root'] ,'a5')

