# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:30:56 2019

@author: ADMIN
"""

import constant
import draw
import financial


if __name__ == "__main__":
    # financial.download()
    # financial.analyze()
    draw.draw("dividend>1", "dividend_yield", "DESC")#where=None, order=None, sort=None #"DESC""ASC"
    # draw.draw("favorite=1", "dividend_yield", "DESC")#where=None, order=None, sort=None #"DESC""ASC"
    # draw.draw("rating=7", "dividend_yield", "DESC")#where=None, order=None, sort=None #"DESC""ASC"
    # draw.draw("rating > 0 AND frechet < 2", "bvpsr", "DESC")#where=None, order=None, sort=None #"DESC""ASC"
    # draw.draw("rating > 0 AND bvpsr > 100", "bvpsr", "DESC")  # where=None, order=None, sort=None #"DESC""ASC"
    # draw.draw("rating=7 AND bvpsr>0", "bvpsr", "DESC")#where=None, order=None, sort=None #"DESC""ASC"
    # draw.draw("rating=5", "bvpsr", "DESC")#where=None, order=None, sort=None #"DESC""ASC"
    # draw.draw("rating > 0", "bvpsr", "DESC")#where=None, order=None, sort=None #"DESC""ASC"
