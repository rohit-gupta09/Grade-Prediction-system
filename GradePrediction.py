# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 23:44:48 2023

@author: DELL
"""

from pydantic import BaseModel
# class which describes bank notes measurements

class Grade(BaseModel):
    first:float
    second:float
    third:int
    fourth:int
    fifth:int
    sixth:int
    seventh:int
    eight:int
    ninth:int
    tenth:int
    eleventh:int