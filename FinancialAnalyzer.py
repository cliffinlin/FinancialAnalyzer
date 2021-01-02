# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:30:56 2019

@author: ADMIN
"""

import Draw
import Financial
import Init


def main():
    Init.initialize()

    Financial.download()
    Financial.analyze()

    Draw.draw(where="market_value > 500", order="roi", sort="DESC", draw_candle_stick=True, save_fig=True)
    # Draw.draw("roe > 30 AND pe > 0 AND dividend > 0", "roi", "DESC")
    # Draw.draw("roi > 15 AND roe > 10 AND pe > 10", "roi", "DESC")
    # Draw.draw("roe > 15", "roi", "DESC")
    # Draw.draw("roe > 15 AND pe > 10", "roi", "DESC")
    # Draw.draw("roe >= 15 AND pe > 10", "pe", "DESC")

if __name__ == "__main__":
    main()
