#!/usr/bin/python3

import os
import re
import json
import logging
from tabulate import tabulate
import argparse

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def loadFlightData(mode):
    data = []
    if mode != None and len(mode) == 2:
        if mode[0] == "decoder_fa":
            file_path = "/var/run/dump1090-fa/"
        elif mode[0] == "decoder_mutability":
            file_path = "/var/run/dump1090-mutability/"
        
        if mode[-1] == "latest":
            file_path = file_path + "aircraft.json"
            try:
                logger.info("Trying to load data from {}".format(file_path))
                with open(file_path, "r") as fobj:
                    data.append(json.load(fobj))
                fobj.close()
                logger.info("Data loaded successfully from file!")
                return data
            except Exception as e:
                logger.error("Failed to load data: \n{}".format(e))
                return None
        elif mode[-1] == "history":
            pattern = r"history_\d+\.json"
            matching_files = [file for file in os.listdir(file_path) if re.match(pattern, file)]
            if not matching_files:
                logger.error("No history_n.json files found under {}".format(file_path))
                return None
            else:
                for filename in matching_files:
                    try:
                        logger.info("Trying to load data from {}".format(file_path+filename))
                        with open(file_path+filename, "r") as fobj:
                            data.append(json.load(fobj))
                        fobj.close()
                        logger.info("Data loaded successfully from file!")
                    except Exception as e:
                        logger.error("Failed to load data: \n{}".format(e))
                if len(data) != 0:
                    return data
                else:
                    return None
    else:
        logger.error("Invalid inputs provided use -h or --help")
        return None

def sanitizeData(data):
    parsedDataset = []
    if data != None and len(data) > 0:
        for file_data in data:
            if "aircraft" in file_data:
                if len(file_data["aircraft"]) > 0:
                    logger.info("Parsing aircraft information")
                    for flight in file_data["aircraft"]:
                        if "flight" in flight:
                            parsedDataset.append(flight)
                        else:
                            logger.info("Skipping dataset [ICAO: {} ] due to missing flight information!".format(flight["hex"]))
                else:
                    logger.warning("Empty aircraft dataset!")
                    return None
            else:
                logger.warning("Did not find any aircraft information!")
                return None
    else:
        logger.warning("Empty dataset passed, check inputs and source files!")
        return None
    return parsedDataset

def pretty(data):
    if data != None and len(data) > 0:
            print(tabulate(data, headers = "keys", tablefmt="grid"))

def verifyInputs(args):
    mode = []
    if args.decoder_fa != None and args.decoder_fa == True:
        mode.append('decoder_fa')
        logger.info("Set to load flight stats from dump1090-fa")
    elif args.decoder_mutability != None and args.decoder_mutability == True:
        mode.append('decoder_mutability')
        logger.info("Set to load flight stats from dump1090-mutability")
    else:
        return None
    
    if args.latest != None and args.latest == True:
        mode.append('latest')
        logger.info("Set to load latest flight stats")
    elif args.history != None and args.history == True:
        mode.append('history')
        logger.info("Set to load historical flight stats")
    else:
        return None
    return mode

def main(args):
    logger.info("---------- START ----------")
    mode = verifyInputs(args)
    aircrafts = loadFlightData(mode)
    data = sanitizeData(aircrafts)
    pretty(data)
    logger.info("---------- END ----------")

if __name__ == "__main__":
    desc = "dump1090 Flight Stats"
    parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.RawDescriptionHelpFormatter)
    # Set prog version
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    # Get Decoder option (dump1090-fa OR dump1090-mutability)
    group1 = parser.add_mutually_exclusive_group(required=True)
    group1.add_argument('--dump1090-fa', action='store_true', dest='decoder_fa', help='Read flight stats from dump1090-fa JSON files')
    group1.add_argument('--dump1090-mutability', action='store_true', dest='decoder_mutability', help='Read flight stats from dump1090-mutability JSON files')
    # Get stats information (latest or historical)
    group2 = parser.add_mutually_exclusive_group(required=True)
    group2.add_argument('--latest', action='store_true', dest='latest', help='Get latest flight stats (from aircraft.json)')
    group2.add_argument('--history', action='store_true', dest='history', help='Get historical flight stats (from history_n.json)')
    args = parser.parse_args()
    main(args)
