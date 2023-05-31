import os
import datetime
import numpy as np
from tixi3 import tixi3wrapper


def load_external_libs():

    try:
        global tixi_h
        tixi_h = tixi3wrapper.Tixi3()
        print("TIXI version: ", tixi_h.version)
    except Exception as e:
        print("Could not load TIXI! Error message is: {}".format(e))


def preprocessing():

    # Load Tixi
    load_external_libs()

    # Open CPACS file
    cpacsIn = os.path.join(os.getcwd(), 'ToolInput', 'CPACS_in.xml')
    try:
        tixi_h.open(cpacsIn)
    except:
        print('TIXI could not read input file.')

    # Read CPACS data:
    toolData["length"] = tixi_h.getDoubleElement(
        "/cpacs/vehicles/aircraft/model[1]/wings/wing[1]/positionings/positioning[1]/length")


def compute():

    toolData["length"] *= toolData["multiplicationFactor"]


def postprocessing():

    # Add provenance information:
    tixi_h.createElement("/cpacs/header/updates", "update")
    xPath = "/cpacs/header/updates/update[last()]"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    tixi_h.addTextElement(xPath, "creator", "wingModifier")
    tixi_h.addTextElement(xPath, "timestamp", timestamp)
    tixi_h.addTextElement(xPath, "version", "1.0")
    tixi_h.addTextElement(xPath, "cpacsVersion", "3.4")
    tixi_h.addTextElement(xPath, "modification", "Modify wing span")

    # Update wing length in CPACS:
    tixi_h.updateDoubleElement(
        "/cpacs/vehicles/aircraft/model[1]/wings/wing[1]/positionings/positioning[1]/length",
        toolData["length"],
        "%.5f")

    # Write CPACS file;
    cpacsOut = os.path.join(os.getcwd(), 'ToolOutput', 'CPACS_out.xml')
    tixi_h.save(cpacsOut)
    tixi_h.close()


def main():

    print('========= Welcome to wingModifier =========')

    global toolData
    toolData = {
        "length": None,
        "multiplicationFactor": 2.6
    }

    preprocessing()
    compute()
    postprocessing()


if __name__ == "__main__":
    main()
