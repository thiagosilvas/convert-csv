#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import os

pasta = r"C:\Users\thiago.silva\Documents\CONVERT"
pasta_de_saida = r"C:\Users\thiago.silva\Documents\OUTPUT"

for count, nome_arquivo in enumerate(os.listdir(pasta)):
    
    read_file = pd.read_excel(os.path.join(pasta,nome_arquivo))
    read_file.to_csv(os.path.join(pasta_de_saida,str(nome_arquivo[:-5]) + str('.csv')), index = False, header=True, sep=';')

print("convertido para csv!")


# In[ ]:




