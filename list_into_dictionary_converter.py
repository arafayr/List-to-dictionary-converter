#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def dictionary(keys,values,d={}):

  if len(keys) != len(values):
    return False

  elif len(keys) == 0 or len(values) == 0:
    return d

  else:
    d[keys[0]] = values[0]

    dictionary(keys[1:],values[1:],d)

  return d

print(dictionary(["a",'b','c','d','e','f'],[1,2,3,4,5,6]))

