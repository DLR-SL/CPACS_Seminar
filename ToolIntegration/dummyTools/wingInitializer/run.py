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

def create_cpacs_wing():
    tixi_h.createElement("/cpacs", "vehicles")
    tixi_h.createElement("/cpacs/vehicles", "profiles")
    tixi_h.createElement("/cpacs/vehicles/profiles", "wingAirfoils")
    tixi_h.createElement(
        "/cpacs/vehicles/profiles/wingAirfoils", "wingAirfoil")

    wingAirfoil_xPath = "/cpacs/vehicles/profiles/wingAirfoils/wingAirfoil[1]"
    tixi_h.addTextElement(wingAirfoil_xPath, "name", "NACA0009 Airfoil")
    tixi_h.addTextAttribute(wingAirfoil_xPath, "uID", "NACA0009")

    x = wingParameters["profile"]["x"]
    y = np.zeros(len(x))
    z = wingParameters["profile"]["z"]
    tixi_h.createElement(wingAirfoil_xPath, "pointList")
    pointList_xPath = wingAirfoil_xPath + "/pointList"
    tixi_h.addFloatVector(pointList_xPath, "x", x, len(x), "%.5f")
    tixi_h.addFloatVector(pointList_xPath, "y", y, len(y), "%.1f")
    tixi_h.addFloatVector(pointList_xPath, "z", z, len(z), "%.5f")

    tixi_h.createElement("/cpacs/vehicles", "aircraft")
    tixi_h.createElement("/cpacs/vehicles/aircraft", "model")
    tixi_h.addTextAttribute(
        "/cpacs/vehicles/aircraft/model[1]", "uID", "aircraft")

    model_xPath = "/cpacs/vehicles/aircraft/model"
    tixi_h.addTextElement(model_xPath, "name", "myAircraft")

    tixi_h.createElement(model_xPath, "wings")
    tixi_h.createElement(model_xPath+"/wings", "wing")
    tixi_h.addTextAttribute(model_xPath+"/wings/wing[1]", "uID", "wing1")
    tixi_h.addTextAttribute(
        model_xPath+"/wings/wing[1]", "symmetry", "x-z-plane")
    wing_xPath = model_xPath+"/wings/wing[1]"
    tixi_h.addTextElement(wing_xPath, "name", "Wing")

    tixi_h.createElement(wing_xPath, "transformation")

    tixi_h.createElement(wing_xPath, "sections")
    tixi_h.createElement(wing_xPath+"/sections", "section")
    tixi_h.createElement(wing_xPath+"/sections", "section")

    tixi_h.addTextAttribute(
        wing_xPath+"/sections/section[1]", "uID", "wing1section1")
    tixi_h.addTextAttribute(
        wing_xPath+"/sections/section[2]", "uID", "wing1section2")

    tixi_h.addTextElement(
        wing_xPath+"/sections/section[1]", "name", "Section 1")
    tixi_h.addTextElement(
        wing_xPath+"/sections/section[2]", "name", "Section 2")

    tixi_h.createElement(wing_xPath+"/sections/section[1]", "transformation")
    tixi_h.createElement(wing_xPath+"/sections/section[2]", "transformation")

    tixi_h.createElement(wing_xPath+"/sections/section[1]", "elements")
    tixi_h.createElement(wing_xPath+"/sections/section[1]/elements", "element")
    tixi_h.addTextAttribute(
        wing_xPath+"/sections/section[1]/elements/element[1]", "uID", "wing1section1element1")
    tixi_h.addTextElement(
        wing_xPath+"/sections/section[1]/elements/element[1]", "name", "wing root element")
    tixi_h.addTextElement(
        wing_xPath+"/sections/section[1]/elements/element[1]", "airfoilUID", "NACA0009")
    tixi_h.createElement(
        wing_xPath+"/sections/section[1]/elements/element[1]", "transformation")
    tixi_h.createElement(
        wing_xPath+"/sections/section[1]/elements/element[1]/transformation", "scaling")
    tixi_h.addDoubleElement(
        wing_xPath+"/sections/section[1]/elements/element[1]/transformation/scaling", "x", wingParameters["rootChord"], "%.3f")
    tixi_h.addDoubleElement(
        wing_xPath+"/sections/section[1]/elements/element[1]/transformation/scaling", "z", wingParameters["rootChord"], "%.3f")

    tixi_h.createElement(wing_xPath+"/sections/section[2]", "elements")
    tixi_h.createElement(wing_xPath+"/sections/section[2]/elements", "element")
    tixi_h.addTextAttribute(
        wing_xPath+"/sections/section[2]/elements/element[1]", "uID", "wing1section2element1")
    tixi_h.addTextElement(
        wing_xPath+"/sections/section[2]/elements/element[1]", "name", "wing tip element")
    tixi_h.addTextElement(
        wing_xPath+"/sections/section[2]/elements/element[1]", "airfoilUID", "NACA0009")
    tixi_h.createElement(
        wing_xPath+"/sections/section[2]/elements/element[1]", "transformation")
    tixi_h.createElement(
        wing_xPath+"/sections/section[2]/elements/element[1]/transformation", "scaling")
    tixi_h.addDoubleElement(
        wing_xPath+"/sections/section[2]/elements/element[1]/transformation/scaling", "x", wingParameters["tipChord"], "%.3f")
    tixi_h.addDoubleElement(
        wing_xPath+"/sections/section[2]/elements/element[1]/transformation/scaling", "z", wingParameters["tipChord"], "%.3f")

    tixi_h.createElement(wing_xPath, "positionings")
    tixi_h.createElement(wing_xPath+"/positionings", "positioning")
    tixi_h.addTextAttribute(
        wing_xPath+"/positionings/positioning[1]", "uID", "wingTipPos")

    tixi_h.addTextElement(
        wing_xPath+"/positionings/positioning[1]", "name", "Tip position")
    tixi_h.addDoubleElement(
        wing_xPath+"/positionings/positioning[1]", "length", 0.5*wingParameters["span"], "%.1f")
    tixi_h.addDoubleElement(
        wing_xPath+"/positionings/positioning[1]", "sweepAngle", wingParameters["sweep"], "%.1f")
    tixi_h.addDoubleElement(
        wing_xPath+"/positionings/positioning[1]", "dihedralAngle", wingParameters["dihedral"], "%.1f")

    tixi_h.addTextElement(
        wing_xPath+"/positionings/positioning[1]", "toSectionUID", "wing1section2")

    tixi_h.createElement(wing_xPath, "segments")
    tixi_h.createElement(wing_xPath+"/segments", "segment")
    tixi_h.addTextAttribute(
        wing_xPath+"/segments/segment[1]", "uID", "wing1segment1")

    tixi_h.addTextElement(
        wing_xPath+"/segments/segment[1]", "name", "Wing segment")
    tixi_h.addTextElement(
        wing_xPath+"/segments/segment[1]", "fromElementUID", "wing1section1element1")
    tixi_h.addTextElement(
        wing_xPath+"/segments/segment[1]", "toElementUID", "wing1section2element1")


def preprocessing():

    # Load Tixi
    load_external_libs()

    # Open CPACS file
    cpacsIn = os.path.join(os.getcwd(), 'cpacsIO', 'CPACS_in.xml')
    try:
        tixi_h.open(cpacsIn)
    except:
        print('TIXI could not read input file.')

    
    # Read CPACS data
    ## Register toolspecific namespace
    tixi_h.registerNamespacesFromDocument()

    ## Get toolspecific data
    base_xPath = "/cpacs/toolspecific/tool[name='wingInitializer']/in:wingInitializer/"
    wingParameters["span"] = tixi_h.getDoubleElement(
        base_xPath + "in:wingParameters/in:span")
    wingParameters["rootChord"] = tixi_h.getDoubleElement(
        base_xPath + "in:wingParameters/in:rootChord")
    wingParameters["taperRatio"] = tixi_h.getDoubleElement(
        base_xPath + "in:wingParameters/in:taperRatio")
    wingParameters["sweep"] = tixi_h.getDoubleElement(
        base_xPath + "in:wingParameters/in:sweep")
    wingParameters["dihedral"] = tixi_h.getDoubleElement(
        base_xPath + "in:wingParameters/in:dihedral")


def compute():

    print(wingParameters["taperRatio"])
    wingParameters["tipChord"] = wingParameters["rootChord"] / \
        wingParameters["taperRatio"]

    wingParameters["profile"] = {
        "x": [1.0, 0.99572, 0.98296, 0.96194, 0.93301, 0.89668, 0.85355, 0.80438, 0.75, 0.69134, 0.62941, 0.56526, 0.5, 0.43474, 0.37059, 0.33928, 0.30866, 0.27886, 0.25, 0.22221, 0.19562, 0.17033, 0.14645, 0.12408, 0.10332, 0.08427, 0.06699, 0.05156, 0.03806, 0.02653, 0.01704, 0.00961, 0.00428, 0.00107,
              0.0, 0.00107, 0.00428, 0.00961, 0.01704, 0.02653, 0.03806, 0.05156, 0.06699, 0.08427, 0.10332, 0.12408, 0.14645, 0.17033, 0.19562, 0.22221, 0.25, 0.27886, 0.30866, 0.33928, 0.37059, 0.43474, 0.5, 0.56526, 0.62941, 0.69134, 0.75, 0.80438, 0.85355, 0.89668, 0.93301, 0.96194, 0.98296, 0.99572, 1.0],
        "z": [0.0, 0.00057, 0.00218, 0.00463, 0.0077, 0.01127, 0.01522, 0.01945, 0.02384, 0.02823, 0.03247, 0.03638, 0.03978, 0.04248, 0.04431, 0.04484, 0.04509, 0.04504, 0.04466, 0.04397, 0.04295, 0.04161, 0.03994, 0.03795, 0.03564, 0.03305, 0.03023, 0.0272, 0.02395, 0.02039, 0.01646, 0.01214, 0.00767, 0.00349, 0.0, -0.00349, -
              0.00767, -0.01214, -0.01646, -0.02039, -0.02395, -0.0272, -0.03023, -0.03305, -0.03564, -0.03795, -0.03994, -0.04161, -0.04295, -0.04397, -0.04466, -0.04504, -0.04509, -0.04484, -0.04431, -0.04248, -0.03978, -0.03638, -0.03247, -0.02823, -0.02384, -0.01945, -0.01522, -0.01127, -0.0077, -0.00463, -0.00218, -0.00057, 0.0]
    }


def postprocessing():

    # Add provenance information
    tixi_h.createElement("/cpacs/header/updates", "update")
    xPath = "/cpacs/header/updates/update[last()]"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    tixi_h.addTextElement(xPath, "creator", "Initializer tool")
    tixi_h.addTextElement(xPath, "timestamp", timestamp)
    tixi_h.addTextElement(xPath, "version", "1.0")
    tixi_h.addTextElement(xPath, "cpacsVersion", "3.4")
    tixi_h.addTextElement(xPath, "modification", "Add wing")

    # Create aircraft wing
    create_cpacs_wing()
    
    # Write CPACS file
    cpacsOut = os.path.join(os.getcwd(), 'cpacsIO', 'CPACS_out.xml')
    tixi_h.save(cpacsOut)
    tixi_h.close()


def main():

    print('========= Welcome to Initializer =========')

    global wingParameters
    wingParameters = {
        "span": None,
        "rootChord": None,
        "tipChord": None,
        "taperRatio": None,
        "sweep": None,
        "dihedral": None,
        "profile": None
    }

    preprocessing()
    compute()
    postprocessing()

    


if __name__ == '__main__':
    main()
