# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 11:43:28 2023

@author: gonca
"""
import numpy as np
# =============================================================================
# 1.reshape() :tupple olarak vermemiz gerekiyor.
# =============================================================================
d1=np.array([1,2,3,4,5,6,7,8,9])
#d1 1 boyutlu,numpy dizisi
#m1 3 e 3 lük yeni bir matris oluşturuyoruz.
m1=d1.reshape((3,3))
d2=np.append(d1,[10]) # d1 matrisine 10 ekledik.
m2=d2.reshape((5,2))
m3=d2.reshape((2,5))

# matrise çevirilecek olan dizinin eleman sayısı ile matrisin eleman sayısının 
#eşleşmesi gerekir.

d3=m1.reshape(-1,1)  # -1,1 parametre
# 1 sütun,eleman sayısı kadar satır olacak şekilde 
# yeniden boyutlandırır.1D 'ye düşmez hala 2D olarak kalıyor.(n,1) olur.

# =============================================================================
# 2.shape(): dizinin boyutunu veir.(property'dir.)
# =============================================================================

s1=m2.shape #2-> boyut anlamında(5,2)
s2=d1.shape #1 boyutlu (9) elemanlı
print(s2) #(9,)

# =============================================================================
# 3.min(),max() :dizideki en küçük ve en büyük sayının değerini verir.
# =============================================================================
d4=np.random.randint(1,50,10)
en_kucuk=d4.min()
en_buyuk=d4.max()

m4=d4.reshape((5,2)) 
mek=np.min(m4) 
meb=np.max(m4)

meks=np.min(m4,axis=0)  #satırdan en küçük değeri döndürür.
mebs=np.max(m4,axis=0)  #satırdan en büyük olan değeri döndürür.

# axis=0 olduğunda en küçük sayının bulunduğu satırın tamamını :
    #1 olduğunda sütunun tamanını verir.


# =============================================================================
# 4.argmin(),argmax(): dizideki en küçük\en büyük elemanın indexini verir.min/max elemanın index değerini verir.
# =============================================================================
eki=d4.argmin()
ebi=d4.argmax()

result=np.where(m4==np.min(m4)) #kkordinatlarını veriyor.
print(result[0],result[1]) #[2] [1]
# [2]satır indexi;[1] sütun indeksi


















