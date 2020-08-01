# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:30:56 2019

@author: ADMIN
"""

import Draw
import Financial


def main():
    Financial.setup_database()
    Financial.download_stock_list()
    Financial.download()
    Financial.analyze()
    # Financial.update_mark()
    Draw.draw("roi > 0 ", "roi", "DESC")
    # Draw.draw("roe > 15", "pe", "DESC")
    # Draw.draw("roe >= 15 AND pe > 10", "pe", "DESC")
    # Draw.draw("roe >= 15 AND pe > 10", "roe", "DESC")
    # draw.draw("roe > 6 AND pe > 8 AND dividend_yield > 4", "pe", "DESC")
    # draw.draw("mark = 1", "dividend_yield", "DESC")
    # draw.draw("mark = 1", "discount", "ASC")#where=None, order=None, sort=None #"DESC""ASC"
    # draw.draw("discount > 0 AND discount < 1 AND dividend_yield > 3 AND rating = 7", "discount", "ASC")#where=None, order=None, sort=None #"DESC""ASC"
    # draw.draw("mark=1", "dividend_yield", "DESC")#where=None, order=None, sort=None #"DESC""ASC"
    # draw.draw("rating=7", "dividend_yield", "DESC")#where=None, order=None, sort=None #"DESC""ASC"
    # draw.draw("discount > 0 AND discount < 1 AND dividend_yield > 3 AND rating = 7", "discount", "ASC")
    # draw.test("mark = 1", "dividend_yield", "DESC")


if __name__ == "__main__":
    main()
