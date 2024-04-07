import sys
import csv
import os.path
import time

import traceback
from typing import List
from colorama import init, Fore, Style

from holding import Holding

TICKER_ALIAS = ["TICKER", "ASX CODE", "SYMBOL"]
EXCHANGE_ALIAS = ["EXCHANGE"]
NAME_ALIAS = ["NAME", "SECURITY NAME", "HOLDING"]
WEIGHT_ALIAS = ["% OF NET ASSETS", "WEIGHT (%)", "WEIGHTING"]

ASX_EXCHANGE_ALIAS = ["AU", "AT", "ASX - All Markets"]
NASDAQ_EXCHANGE_ALIAS = ["NASDAQ", "UW"]
NYSE_EXCHANGE_ALIAS = ["New York Stock Exchange Inc.", "NYSE", "UN"]
JPX_EXCHANGE_ALIAS = ["JP", "JT"]
DKK_EXCHANGE_ALIAS = ["DC"]
DKK_EXCHANGE_ALIAS = ["FP"]

EXCHANGE_ALIAS_LIST = [ASX_EXCHANGE_ALIAS, NASDAQ_EXCHANGE_ALIAS, NYSE_EXCHANGE_ALIAS, JPX_EXCHANGE_ALIAS, DKK_EXCHANGE_ALIAS]
EXCHANGE_ALIAS_NAMES = ["ASX", "NASDAQ", "NYSE", "JPX", "DKK"]

# SOME CONFIG.. TODO: DO THIS SOMEWHERE ELSE

CREATE_OUTPUT_FILE = True
SUPPRESS_WARNINGS = True
HOLDINGS_DIRECTORY = "holdings/"

funds_list = []
csv_list = []

funds_holdings_dict = {}

# COLORAMA SETUP

init()

# SETUP AND FILE EXTRACTION

def read_cmd_args():
    if len(sys.argv) <= 1:
        print("USAGE: python holdings_comparison.py [fund_name] [fund_name] [etc.]")
        return
    for i in range(1, len(sys.argv)):
        if sys.argv[i].upper() == "ALL":
            print("ALL FUNDS")
            for file in os.listdir(HOLDINGS_DIRECTORY):
                funds_list.append(file.strip(".csv"))
            return

        creation_time = os.path.getctime(HOLDINGS_DIRECTORY + sys.argv[i].upper() + ".csv")
        # Convert the modification time to a readable format
        creation_date = time.strftime('%Y-%m-%d', time.localtime(creation_time))

        print(f"Fund  {i} : {sys.argv[i].upper()} as of {creation_date}")
        funds_list.append(sys.argv[i])

def open_file(fund_name):
    try:
        with open("holdings/" + fund_name.upper() + ".csv", 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file)
            return extract_csv(csv_reader)
    except Exception as e:
        print(f"ERROR - Fail to open file: holdings/{fund_name.upper()}.csv\nMessage: {e}")
        traceback.print_exc()
        exit()

def extract_csv(csv_reader):
    holdings_list = []
    ticker_index, exchange_index, name_index, weight_index = -1, -1, -1, -1
    # Get column index for each required field
    for i, header in enumerate(next(csv_reader)):
        if header.strip().upper() in TICKER_ALIAS:
            ticker_index = i
        elif header.strip().upper() in EXCHANGE_ALIAS:
            exchange_index = i
        elif header.strip().upper() in NAME_ALIAS:
            name_index = i
        elif header.strip().upper() in WEIGHT_ALIAS:
            weight_index = i
    
    if ticker_index == -1 or name_index == -1 or weight_index == -1:
        print(f"ERROR - Could not find index for something:\nticker: {ticker_index} \nname: {name_index} \nweight: {weight_index}")
        exit()

    for i, row in enumerate(csv_reader):
        holding = Holding()
        ticker_code = row[ticker_index].split(' ')
        holding.ticker = ticker_code[0]
        
        if(exchange_index != -1):
            holding.exchange = get_exchange(row[exchange_index])
        elif(len(ticker_code) > 1):
            holding.exchange = get_exchange(ticker_code[1])
        else:
            warn("WARNING - Unrecognised exchange code: for ticker \""+ticker_code[0]+"\"")

        holding.name = row[name_index]
        holding.weight = float(row[weight_index].strip('%')) if row[weight_index] != '' else 0
        holdings_list.append(holding)
    return holdings_list

def get_exchange(exchange_alias):
    for i, alias_list in enumerate(EXCHANGE_ALIAS_LIST):
        if exchange_alias in alias_list:
            return EXCHANGE_ALIAS_NAMES[i]
    warn("WARNING - Could not find exchange for \""+exchange_alias+"\"")
    return exchange_alias

# COMPARISONS

def find_overlap(fund1: List[Holding], fund2: List[Holding]):
    print("\n===== FINDING OVERLAPS =====")
    get_holding_set(fund1, fund2)
    find_percent_weight_overlap(fund1, fund2)

def get_holding_set(fund1: List[Holding], fund2: List[Holding], output = True):
    holdings_set = set()
    for holding in fund1:
        holdings_set.add((holding.exchange, holding.ticker))
    for holding in fund2:
        holdings_set.add((holding.exchange, holding.ticker))

    if(output):
        overlapping_hodings = len(fund1) + len(fund2) - len(holdings_set)
        print(f"There are a total of {Fore.YELLOW}{len(holdings_set)}{Style.RESET_ALL} holdings.")
        print(f"{Fore.GREEN}{overlapping_hodings}{Style.RESET_ALL} Holdings Overlap.")
        print(f"{Fore.GREEN}{round(overlapping_hodings/len(fund1) * 100,2)}%{Style.RESET_ALL} of Fund 1's {Fore.GREEN}{len(fund1)}{Style.RESET_ALL} holdings also in Fund 2")
        print(f"{Fore.GREEN}{round(overlapping_hodings/len(fund2) * 100,2)}%{Style.RESET_ALL} of Fund 2's {Fore.GREEN}{len(fund2)}{Style.RESET_ALL} holdings also in Fund 1")
    
    return holdings_set

def find_percent_weight_overlap(fund1: List[Holding], fund2: List[Holding]):
    weight_overlap = 0
    for holding1 in fund1:
        for holding2 in fund2:
            if holding1.is_equal(holding2):
                weight_overlap += min(holding1.weight, holding2.weight)
    print(f"{Fore.GREEN}{round(weight_overlap, 2)}%{Style.RESET_ALL} Overlap by Weight.")

# CSV_OUTPUT

def get_holding_name_by_ticker(exchange, ticker):
    for i, fund in enumerate(funds_holdings_dict):
        for holding in funds_holdings_dict[funds_list[i]]:
            if holding.is_equal_by_ticker(exchange, ticker):
                return holding.name
    print(f"ERROR - Could not find holding name for \"{exchange}:{ticker}\"")
    exit()

def create_output_file(funds_list, funds_holdings_dict):
    output_filename = ""
    for fund_name in funds_list:
        output_filename += fund_name + '_'
    output_filename = "output_files/" + output_filename.strip('_') + ".csv"

    with open(output_filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        first_row = ["Name", "Exchange", "Ticker"]
        for fund in funds_list:
            first_row.append(fund.upper())
        writer.writerow(first_row)
        expected_row_size = len(first_row)

        total_holdings_set = set()
        for i in range(0, len(funds_holdings_dict) - 1):
            total_holdings_set.update(get_holding_set(funds_holdings_dict[funds_list[i]], funds_holdings_dict[funds_list[i + 1]], False))

        for holding_tuple in total_holdings_set:
            row = []
            row.append(get_holding_name_by_ticker(holding_tuple[0], holding_tuple[1]))
            row.append(holding_tuple[0])
            row.append(holding_tuple[1])
            # Loop through all funds
            for i, fund in enumerate(funds_holdings_dict):
                found = False
                # Find holding in fund
                for holding in funds_holdings_dict[funds_list[i]]:
                    if holding.is_equal_by_ticker(holding_tuple[0], holding_tuple[1]):
                        found = True
                        row.append(str(holding.weight) + '%')
                # 0% weight if not found
                if not found:
                    row.append('0%')
            if len(row) != expected_row_size:
                print(f"ERROR: Row size is {len(row)}. Expected {expected_row_size}")
                return

            writer.writerow(row)

# MAIN

# TODO: MOVE SOMEWHERE ELSE. NEW LIB FILE
def warn(message):
    if SUPPRESS_WARNINGS: 
        return
    print(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")

print("\n===== COMPARING FUNDS =====")
print(f"CREATE OUTPUT FILE: {CREATE_OUTPUT_FILE}")
print(f"SUPPRESS WARNINGS: {SUPPRESS_WARNINGS}")

read_cmd_args()
for fund in funds_list:
    funds_holdings_dict[fund] = open_file(fund)

if CREATE_OUTPUT_FILE:
    create_output_file(funds_list, funds_holdings_dict)
else:
    find_overlap(funds_holdings_dict[funds_list[0]], funds_holdings_dict[funds_list[1]])

print("\n===== END =====")