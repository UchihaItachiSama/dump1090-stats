#!/usr/bin/python3

import json
from pprint import pprint as pp
import logging
from tabulate import tabulate

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def loadFlightData():
    logger.info("---- START ----")
    try:
        logger.info("Trying to load data from dump1090-mutability...")
        with open("/var/run/dump1090-mutability/aircraft.json", "r") as fobj:
            data = json.load(fobj)
        fobj.close()
        logger.info("Data loaded successfully from file!")
        return data
    except Exception as e:
        logger.error("Failed to load data: \n{}".format(e))
        return None

def sanitizeData(data):
    parsedDataset = []
    if data != None:
        if "aircraft" in data:
            if len(data["aircraft"]) > 0:
                logger.info("Parsing aircraft information...")
                for flight in data["aircraft"]:
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
        logger.warning("Empty dataset passed, check source file!")
        return None
    return parsedDataset

def pretty(data):
    if data != None or len(data) > 0:
        print(tabulate(data, headers = "keys", tablefmt="grid"))
    logger.info("---- END ----")

def main():
    aircrafts = loadFlightData()
    data = sanitizeData(aircrafts)
    pretty(data)

if __name__ == "__main__":
    main()
