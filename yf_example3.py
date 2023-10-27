# Download stock price data for Qantas for a given year and
# save the information in a CSV file

import os
import toolkit_config as cfg
import yf_example2


# Download Qantas stock prices for a given year into a CSV file
def qan_prc_to_csv(year, pth):
    tic = "QAN.AX"
    start = f'{year}-01-01'
    end = f'{year}-12-31'
    yf_example2.yf_prc_to_csv(tic, pth, start, end)


# Example
if __name__ == "__main__":
    year = 2020
    pth = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')
    qan_prc_to_csv(year, pth)