# This Python file uses the following encoding: utf-8
import feedparser
import re

def getWordCounts( url ):

    wc={}

    #解析xml
    d = feedparser.parse( url )
    for e in d.entries:
        if 'summary' in e: summary=e.summary
        else: summary=e.description

    # Extract a list of words
    words=getWords(e.title+' '+summary)
    for word in words:
        wc.setdefault(word,0)
        wc[word]+=1
    return d.feed.title,wc

def getWords( html ):
    
    #替换html标签为空格
    #txt=re.sub(r'<[^>]+>','',html)
    txt=re.compile(r'<[^>]+>').sub('',html)
    
    #按非字母来分割txt
    words=re.compile(r'[^A-Z^a-z]+').split(txt)

    return [word.lower() for word in words if word!='']

apcount={}
wordcounts={}
feedlist=[line for line in file('data/list.txt')]

for url in feedlist:
    title,wc = getWordCounts( url.strip() )
    wordcounts[title]=wc
    for word,count in wc.items():
        apcount.setdefault(word,0)
        if count>1:apcount[word]+=1

print apcount 
wordlist=[]
