# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 11:04:36 2023

@author: gonca
"""
# =============================================================================
# NUMPY METOTLARI
# =============================================================================
import numpy as np 
# =============================================================================
# ctrl+4 :title başlık şeklinde yapıyor.
# run : f5
# =============================================================================
# ctrl+k+c : yorum satırına alıyor.
# ayrıca console kısmını silmek için cls yapıyoruz.
# =============================================================================
# 1.arange():başlangıç,bitiş,artış a göre nparray oluşturuyor.
# pythonda range denk denk geliyor.
# =============================================================================

d1=np.arange(1,100,10)

# =============================================================================
# # 2.zeros(): sıfır matrisi oluşturmak için.
# =============================================================================

d2=np.zeros((3,2),dtype=np.int32) #sıfır matris

# =============================================================================
# 3.ones(): birebir matris
# =============================================================================

d3=np.ones((5,2)) #birebir matris.

# =============================================================================
# 4.eye(): birim matris
# =============================================================================

d4=np.eye(4) #simetrik davranıyor eğer ikinci parametre verilirse köeşegen matris olmuyor.
# =============================================================================
# 5.Linspace(start,stop,num): birbirine eşit uzunluktaki belli sayıda dizi oluşturur.
# =============================================================================

d5=np.linspace(1,5,3)
d6=np.linspace(1,10,5) #1 den 10 a kadar sırala arası 5 olsun demek.

# =============================================================================
# 6.random
# =============================================================================
d7=np.random.randint(1,10,5) # tamsayı rastgele 5 sayı vericek..
d8=np.random.randn(5) #standart normal dağılıma uygun rastgele 5 sayı verir.

# =============================================================================
# 7.transpose():matrisin satır sütunların yer değiştirilmiş versiyonu.
# =============================================================================

m1=np.array([[1,2,3], # (2,3) matris iken :
            [4,5,6]])
t1=np.transpose(m1)   #(3,2) matris olucak.

# =============================================================================
#  8.append()
# =============================================================================
d9=np.append(d1,[101,111]) #d1 91 e kadardı ekleme yaptı 1 boyutlu numpy arrayine ekleme yapar.

#d10=np.append(m1,[[7,8,9]]) # boyut düştü 2 den 1 boyuta geçti.
d10=np.append(m1,[[7,8,9]],axis=0)
d11=np.append(m1,[[10],[20]],axis=1) #axis'e 1 diğerek sütüna ekleme yaptı.[[].[]] 1.sütuna 2 satır ekliyoruz.

# =============================================================================
# 9.delete():silmek istediğimizde.veri ve index vermemiz gerekiyor 2 boyut için.
# =============================================================================

d12=np.delete(d10,1,axis=0) #2.satırdaki 1.indexi siler.
d13=np.delete(d11,2,axis=1)


