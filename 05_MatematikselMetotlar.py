# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 13:16:30 2023

@author: gonca
"""

import numpy as np

# [1,2,3]
# [10,11,12]

# add:[11,13,15] index değerlerine göre matematiksel işlem yapar.

m1=np.array([[1,2],
            [3,4],
            [5,6]])

m2=np.array([[10,20],
            [30,40],
            [50,60]])

# Matrisin toplamını bulmak için:
    
toplam=np.add(m1,m2)

#Matrisin farkını bulmak için:
    
fark=np.subtract(m1,m2)

#Matris çarpımı için : 

#carpim=np.multiply(m1,m2) #matris çarpımı yapmaz.
#matris_carpimi=np.dot(m1,m2) #matris çarpımını m1 ve m2 ile yapamayız shapeleri uygun değildir.

# m2'yi transposunu alıp matris çarpımını yapınız.
#m3=np.transpose(m2)
#m_carpim=np.dot(m1,m3)
m_carpim=np.dot(m1,np.transpose(m2))


# Matris bölümü yapmak için :

bolum=np.divide(m1,m2)

#Matris'de mod almak: bölümünden kalanı bulmak için :
    
mode=np.mod(m1,m2) #matematiksel bölümünden kalanı verir.

#Matris üssü bulmak için :
    
karesi=np.power(m1,2) #herbir elemanın karesini almak için kullnılır.

# =============================================================================
# 2.Yuvarlamalar:
# =============================================================================


#y1=np.around(bolum) #decimal parametresi verilmezse tamsayıya yuvarlar.

m4=np.random.randn(10).reshape(5,2)

y1=np.around(m4,decimals=2)
y2=np.ceil(m4)
y3=np.floor(m4)

# =============================================================================
# 3.Açısal işlemler:
# =============================================================================

acilar=[0,30,45,60,90] #derece cinsinden açılar.
radyan_acilar=np.deg2rad(acilar) #dereceden->radyana çevirir.
# tersi : rad2deg
c1=np.cos(radyan_acilar)
sin1=np.sin(radyan_acilar)
tan1=np.tan(radyan_acilar)















