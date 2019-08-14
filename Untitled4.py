#!/usr/bin/env python
# coding: utf-8

# #                                                Lista de Tareas
# 
# 
# ##  1. Suma de numeros complejos
#        
# La funcion Sumar_r declara las variables para las cuales lee 2 numeros complejos y determina la suma entre ellos.

# In[1]:


from sys import stdin

def Sumar_Comp(C1,C2):
    #declaración de variables para la lectura de numeros complejos, en el cual lee 2 numeros separados por un espacio;
    #El primero es la parte real y el segundo la parte imaginaria
    Real=C1[0]+C2[0]
    Comp=C2[1]+C2[1]

    print('La respectiva suma es:')

    if Comp==0:
        print(Real)
    elif Comp<0:
        print(Real,'-',str(Comp*-1)+'i')
    else:
        print(Real,'+',str(Comp)+'i')
        
    return([Real,Comp])


# In[2]:


Sumar_Comp([-5,4],[1,3])


# ## 2. Multiplicacion de numeros complejos

# In[3]:


from sys import stdin

def Multi_Comp(C1,C2):
    #declaración de variables para la lectura de numeros complejos, en el cual lee 2 numeros separados por un espacio;
    #El primero es la parte real y el segundo la parte imaginaria
    
    Real=(C1[0]*C2[0])-(C1[1]*C2[1])
    Comp=(C1[0]*C2[1])+(C1[1]*C2[0])

    print('La respectiva Multiplicacion es:')

    if Comp==0:
        print(Real)
    elif Comp<0:
        print(Real,'-',str(-Comp)+'i')
    else:
        print(Real,'+',str(Comp)+'i')
    
    return([Real,Comp])


# In[4]:


Multi_Comp([-5,4],[1,3])


# ## 3. Conjugado

# In[5]:


from sys import stdin

def Conjugado_Comp(C1):
    #declaración de variables para la lectura de numeros complejos, en el cual lee 2 numeros separados por un espacio;
    #El primero es la parte real y el segundo la parte imaginaria
    
    Real= C1[0]
    Comp=-C1[1]
    
    print('El conjugado es:')

    if Comp==0:
        print(Real)
    elif Comp<0:
        print(Real,'-',str(Comp*-1)+'i')
    else:
        print(Real,'+',str(Comp)+'i')
    
    return([Real,Comp])
        


# In[6]:


Conjugado_Comp([-5,4])


# ## 4. Division

# In[7]:


from sys import stdin

def Division_Comp(C1,C2):
    #declaración de variables para la lectura de numeros complejos, en el cual lee 2 numeros separados por un espacio;
    #El primero es la parte real y el segundo la parte imaginaria

    
    #Conjugado
    Conj=Conjugado_Comp(C2)
    
    #Multiplicacion Numerador
    Num=Multi_Comp(Conj,C2)
    
    #Multiplicacion Denominador
    Denom=Multi_Comp(C1,Conj)

    print('La respectiva Division es:')

    
    if Num[1]==0:
        print(Num[0],end='')
    elif Num[1]<0:
        print(Num[0],'-',str(-Num[1])+'i',end='')
    else:
        print(Num[0],'+',str(Num[1])+'i',end='')
    
    
    print('  /  ',end='')
    
    
    if Denom[1]==0:
        print(Denom[0])
    elif Denom[1]<0:
        print(Denom[0],'-',str(-Denom[1])+'i')
    else:
        print(Denom[0],'+',str(Denom[1])+'i')
        


# In[8]:


Division_Comp([-5,4],[1,3])


# ## 4. Modulo

# In[9]:


from sys import stdin
import math

def Modulo_Comp(C1):
    #declaración de variables para la lectura de numeros complejos, en el cual lee 2 numeros separados por un espacio;
    #El primero es la parte real y el segundo la parte imaginaria
    
    Real= C1[0]
    Comp= C1[1]
    res= math.sqrt((Real**2)+(Comp**2))
    
    print('El Modulo es:')
    
    print(res)

    return(res)


# In[10]:


Modulo_Comp([-5,4])

