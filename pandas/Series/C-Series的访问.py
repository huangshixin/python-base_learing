from pandas import  Series
from numpy.random import randint,seed
import numpy as np

#支持
1、当个索引值的访问，前提是不越界
2、支持列表中嵌套’列表‘的访问形式，这里嵌套的链表----必须是符合条件的索引值
3、支持bool类型的列表访问形式  arr[[True,False,True,True,False]]

seed(100)
arr = randint(0,100,size=5)
print(arr)
print(arr[0])
print(arr[[0,1,2,1]])
print(arr[[True,False,True,True,False]])


##############################################################################################################################################################
开始使用Series  -----它的优势就是构建【一维数组】。并且带索引值的返回；
s = Series(data=arr,index=['A','B','C','D','E'],dtype='float16')
print(s)
print(s[0])
print(s[[0,1,2,1]])
print(s[[True,False,True,True,False]])

A     8.0
B    24.0
C    67.0
D    87.0
E    79.0
dtype: float16
8.0
A     8.0
B    24.0
C    67.0
B    24.0
dtype: float16
A     8.0
C    67.0
D    87.0
dtype: float16
  
  
  

##############################################################################################################################################################
【loc  和 iloc】
  使用loc函数，索引的是字符串，前后都要取，是属于“前闭后闭”的情况。
  【loc配合’显示索引‘】
  
  print(s.loc['C']) #只返回查询值
    67.0
  print(s.loc[['A','B']]) # 返回一个表，支持【左闭右闭】

    A     8.0
    B    24.0
    dtype: float16

   【iloc配合隐式索引】 隐式索引指的是0~n这种形式；
  
  8.0
A     8.0
B    24.0
C    67.0
dtype: float16

https://www.bilibili.com/video/BV13P4y1f7db?p=12&vd_source=b498949199c494447b72f71d8016104d  
    
      
      
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
