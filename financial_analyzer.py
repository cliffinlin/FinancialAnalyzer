# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:30:56 2019

@author: ADMIN
"""

import constant
import os
import draw
import financial

if __name__ == "__main__":
    # financial.download()
    # financial.analyze()
    # financial.update()
    # draw.draw("favorite != 1", "dividend_yield", "DESC")
    # draw.draw("favorite = 1 AND rating = 7", "dividend_yield", "DESC")#where=None, order=None, sort=None #"DESC""ASC"
    # draw.draw("favorite = 1", "discount", "ASC")#where=None, order=None, sort=None #"DESC""ASC"
    draw.draw("discount > 0 AND discount < 1 AND dividend_yield > 3 AND rating = 7", "discount", "ASC")#where=None, order=None, sort=None #"DESC""ASC"
    # draw.test("favorite = 1", "dividend_yield", "DESC")
    # draw.draw("favorite=1", "dividend_yield", "DESC")#where=None, order=None, sort=None #"DESC""ASC"
    # draw.draw("rating=7", "dividend_yield", "DESC")#where=None, order=None, sort=None #"DESC""ASC"
