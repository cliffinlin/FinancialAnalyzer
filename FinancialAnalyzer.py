# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:30:56 2019

@author: ADMIN
"""

import Draw
import Financial


def main():
    # Financial.setup_database()
    # Financial.download_stock_list()
    # Financial.download()
    # Financial.analyze()
    # Financial.update_mark()
    Draw.draw("roe > 15 AND pe > 10", "roi", "DESC")
    # Draw.draw("roe >= 15 AND pe > 10", "pe", "DESC")

if __name__ == "__main__":
    main()
