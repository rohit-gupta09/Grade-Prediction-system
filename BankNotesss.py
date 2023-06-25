# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 21:59:49 2023

@author: DELL
"""

from pydantic import BaseModel
# class which describes bank notes measurements

class BankNot(BaseModel):
    variance:float
    skewness:float
    curtosis:float
    entropy:float
    