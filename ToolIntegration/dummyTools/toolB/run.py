import os
import datetime
from tixi3 import tixi3wrapper


def load_external_libs():

    try:
        global tixi_h
        tixi_h = tixi3wrapper.Tixi3()
        print("TIXI version: ", tixi_h.version)
    except Exception as e:
        print(f"Could not load TIXI! Error message is: {e}")


def preprocessing():

    # Load Tixi
    load_external_libs()

    # Open CPACS file
    cpacsIn = os.path.join(os.getcwd(), 'cpacsIO', 'CPACS_in.xml')
    try:
        tixi_h.open(cpacsIn)
    except Exception as e:
        print(e)

    # Register and read toolspecific data
    px = "tb"
    tixi_h.registerNamespace("http://www.cpacs.de/toolB",px)

    base_xPath = f"/cpacs/toolspecific/tool[name='ToolB']/{px}:toolB/"
    toolSettings["writeLogEntry"] = tixi_h.getBooleanElement(base_xPath+f"{px}:settings/{px}:writeLogEntry")



def compute():

    pass


def postprocessing():

    # Add provenance information
    if toolSettings["writeLogEntry"]:

        # Current version of the dataset:
        version = tixi_h.getTextElement("/cpacs/header/version")
        changeLog_xPath = f"/cpacs/header/versionInfos/versionInfo[@version='{version}']/changeLog"

        # Create new logEntry
        tixi_h.createElement(changeLog_xPath, "logEntry")
        logEntry_xPath = changeLog_xPath + "/logEntry[last()]"
        timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

        tixi_h.addTextElement(logEntry_xPath, "description", "Added log for testing")
        tixi_h.addTextElement(logEntry_xPath, "timestamp", timestamp)
        tixi_h.addTextElement(logEntry_xPath, "creator", "ToolB")

    # Write CPACS file
    cpacsOut = os.path.join(os.getcwd(), 'cpacsIO', 'CPACS_out.xml')
    tixi_h.save(cpacsOut)
    tixi_h.close()


def main():

    print('========= Welcome to ToolB =========')

    global toolSettings
    toolSettings = {
        "writeLogEntry": None,
    }

    preprocessing()
    compute()
    postprocessing()


if __name__ == "__main__":
    main()
