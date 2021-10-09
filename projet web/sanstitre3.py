# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 21:19:52 2020

@author: douaa
"""

import mysql.connector
import nltk
from scipy import spatial
from nltk.stem.snowball import FrenchStemmer
from nltk.corpus import stopwords
import numpy as np

def similaritecosinus(idresto1,idresto2):
    return (1-spatial.distance.cosine(MatBin[idresto1],MatBin[idresto2]))

con=mysql.connector.connect(host="localhost",user="root",password="",database="resto")
cursor=con.cursor()
cursor.execute("select * from restaurant")
stop = set(stopwords.words('french'))
stop =list(stop)
stop.extend([".",",","-",";","?","(",")",":","...","«","»"])
stemmer = FrenchStemmer() 
totalmots=set()
NbPro= 0
dictMots={}
for ligne in cursor.fetchall():
    NbPro+=1
    print("Id Restaurant : ", ligne[0])
    #print("Desc Restaurant : ", ligne[2])
    desc= ligne[2]
    mots = nltk.word_tokenize(desc)
    #print(mots)
    Mots=[m for m in mots if m not in stop]     
       
    MotsStem=[]
    for m in Mots:
        MotsStem.append(stemmer.stem(m))
    print("-----------------------------")
    #print(MotsStem)
    for m in MotsStem:
        totalmots.add(m)
    dictMots[ligne[0]]= MotsStem


con.close()
NbMots=len(totalmots)
print(NbPro)
MatBin=np.zeros((NbPro,NbMots))
for i in range(NbPro):
    j=0
    for m in totalmots:
        if m in dictMots[i+1]:
            MatBin[i][j]=1
        j+=1
MatSimBin=np.zeros((NbPro,NbPro))


for s in range(NbPro):
    for z in range(NbPro):
        MatSimBin[s][z]=similaritecosinus(s,z)
print(MatSimBin)

for s in range(NbPro):
    Maxi=0
    for z in range(NbPro):
        if (MatSimBin[s][z]>Maxi) and (MatSimBin[s][z]<1):
            Maxi=MatSimBin[s][z]
            IdRestoMax=z+1
    print(" top 1 du resto d'id ",str(s+1),"est le resto d'id ",IdRestoMax)
    con1=mysql.connector.connect(host="localhost",user="root",password="",database="resto")
    mycursor=con1.cursor()
    sql="UPDATE restaurant SET IdProSim= %s WHERE Id= %s "
    val=(IdRestoMax,s+1)
    mycursor.execute(sql,val)
    con1.commit()
    con1.close()
    