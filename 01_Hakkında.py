# -*- coding: utf-8 -*-
#NUMPY :numerical python
# büyük verilerle matematiksel,istatistiksel,cebirsel vb işlemlerin yapılmasını sağlayacak
#metotların bulunduğu python kütüphanesidir.


#builtin olmadığı için pip install numpy ile yüklenebilir.


import numpy as np

# 0D,1D,2D,3D diziler oluşturulabilir.
#numpy dizisi

d1=np.array(5) #0D 
print(type(d1)) #<class 'numpy.ndarray'>

# 1D
sayilar=[1,3,1,4,6,2] #python listesi
d2=np.array(sayilar)  #1 boyutlu numpy disizi size olarak (6,):tuple döner.

# 2D: matris
matris=[[1,2,3,11],
        [4,5,6,22],
        [7,8,9,33]]
d3=np.array(matris) # (3,3) matris

# NUMPYDA VERİ TİPLERİ
# int32,int16,int64 -> tam sayıları tutmak için (pythondan biraz farklı) 2 üzeri 32 kadar düşünülebilir.

# float -> ondalık sayıları tutar.
d4=np.array([11,12,13],dtype=np.float32)



