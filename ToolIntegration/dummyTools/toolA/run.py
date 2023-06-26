import os
import datetime
from tixi3 import tixi3wrapper


def preprocessing():

    # Load Tixi
    try:
        global tixi_h
        tixi_h = tixi3wrapper.Tixi3()
        print("TIXI version: ", tixi_h.version)
    except Exception as e:
        print(f"Could not load TIXI! Error message is: {e}")

    # Open CPACS file
    try:
        tixi_h.open('./cpacsIO/CPACS_in.xml')
    except Exception as e:
        print(e)


def compute():

    pass


def postprocessing():

    writeLogEntry = True

    # Add provenance information
    if writeLogEntry:

        # Current version of the dataset:
        version = tixi_h.getTextElement("/cpacs/header/version")
        changeLog_xPath = f"/cpacs/header/versionInfos/versionInfo[@version='{version}']/changeLog"

        # Create new logEntry
        tixi_h.createElement(changeLog_xPath, "logEntry")

        timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

        logEntry_xPath = changeLog_xPath + "/logEntry[last()]"
        tixi_h.addTextElement(logEntry_xPath, "description", "Added log for testing")
        tixi_h.addTextElement(logEntry_xPath, "timestamp", timestamp)
        tixi_h.addTextElement(logEntry_xPath, "creator", "ToolA")

    # Write CPACS file
    cpacsOut = os.path.join(os.getcwd(), 'cpacsIO', 'CPACS_out.xml')
    tixi_h.save(cpacsOut)
    tixi_h.close()


def main():

    print('========= Welcome to ToolA =========')

    preprocessing()
    compute()
    postprocessing()


if __name__ == "__main__":
    main()
