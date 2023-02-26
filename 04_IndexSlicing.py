# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 12:36:26 2023

@author: gonca
"""
import numpy as np
# =============================================================================
# 1.Diziden belli bir indexteki elemanı almak.
# =============================================================================

d1=np.arange(1,21,1)
v1=d1[5]

# =============================================================================
# 2.slicing 
# =============================================================================

v2=d1[:] #tamamını verir.

v3=d1[2:] # 2 dahil değil,2.indexten sonra kadarki sayıları verir.sonuncu dahildir.

v4=d1[:5] #baştan 5.indexe kadar 5.index dahil değil.

v5=d1[2:7] #2.indexten 2.indexe kadar.

v6=d1[-4]
# =============================================================================
# 3.değer değiştirme
# =============================================================================

d1[5]=99 #5.indexteki elemanın değerini 99 yapar.

d1[2:5]=-1  # koşulu sağlayan indexlerin tümünü -11 yapar.

# =============================================================================
# 4.matrislerde slicing 
# =============================================================================

m1=d1.reshape((4,5))

v7=m1[2] #2.indexteki tüm satırı verir.

v8=m1[2,3] #2.index satır;3.index sütundaki elemanı verir.

v9=m1[:,1] #1.index sütuna denk gelen tüm satırlar getirir.

v10=m1[1:3] #1.index satırdan 3.inde satıra kadar olan tüm elemanları verir

v11=m1[1:3,1:4]  #1-3 arasında satırlar ve 1-4 arasındaki sütunların kesiştiği bölgeyi verir.
# 3-4 dahil değildir.

print(v11) #[[ 7  8  9]
            #[12 13 14]]
            









