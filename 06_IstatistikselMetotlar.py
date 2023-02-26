# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 13:59:17 2023

@author: gonca
"""

import numpy as np
import scipy as sp

# =============================================================================
# AVERAGE :
# =============================================================================

d1=np.array([12,45,22,14])
ortalama=np.mean(d1) #23,25

# =============================================================================
# MEDİAN: küçükten büyüğe sıralanan dizinin ortasındaki değerdir.çift ise ortanın toplam bölümü 2 dir.
# =============================================================================

medyan=np.median(d1) #18.0

# =============================================================================
# standart sapma: 
# =============================================================================
std_sapma=np.std(d1)

# =============================================================================
# Varyans :standart sapmanın karesidir.
# =============================================================================

varyans=np.var(d1)

# =============================================================================
# MOD: dizide en çok tekrar eden sayı.
# =============================================================================
d2=np.array([12,45,22,14,12,11,12,12])
# ayrı olarak scipy kütüphanesini aktif etmemiz gerekiyor.
mode=sp.stats.mode(d2) #12 en çok tekrar eden 4.kere tekrar edilmiştir.