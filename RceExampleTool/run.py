import os
from tixi3 import tixi3wrapper

def load_external_libs():
    try:
        global tixi_h
        tixi_h = tixi3wrapper.Tixi3()
        print("TIXI version: ", tixi_h.version)
    except Exception as e:
        print("Could not load TIXI! Error message is: {}".format(e))

def your_function():

    # Get airport information:
    airport_xpath = tixi_h.uIDGetXPath('FRA')

    airport_name = tixi_h.getTextElement('/'.join((airport_xpath, 'name')))
    positionNorth = tixi_h.getDoubleElement('/'.join((airport_xpath, 'positionNorth')))
    positionEast = tixi_h.getDoubleElement('/'.join((airport_xpath, 'positionEast')))

    print('Name: %s\nPosition North: %.3f\nPosition East: %.3f' % (airport_name, positionNorth, positionEast))

    # Some information would be very long if stored as xml-sequence. Thus, we introduced vectors:
    root_xpath = '/'.join((tixi_h.uIDGetXPath('FRAtoEWRID'),'flightPath'))

    vector_size = tixi_h.getVectorSize('/'.join((root_xpath,'waypoints')))

    waypoints = tixi_h.getTextElement('/'.join((root_xpath,'waypoints'))).split(';')
    latitude = tixi_h.getFloatVector('/'.join((root_xpath,'latitude')), vector_size)
    longitude = tixi_h.getFloatVector('/'.join((root_xpath,'longitude')), vector_size)

    for i, wp in enumerate(waypoints):
            print('%10s %.3f %.3f'%(wp, latitude[i], longitude[i]))

    # Let's add information about Braunschweig airport:
    #    - add uID="BWE" to the new <airport> element
    #    - add text element "name" with "Braunschweig, Germany"
    #    - add Positions: 52.3199° north / 10.556° east
    #    - add elevation of 276ft
    apts_xpath = '/cpacs/airports'
    idx = tixi_h.getNamedChildrenCount(apts_xpath,'airport') + 1

    tixi_h.createElementAtIndex(apts_xpath,'airport',idx)

    apt_xpath = '/'.join((apts_xpath,'airport[%i]'%idx))

    tixi_h.addTextAttribute(apt_xpath,'uID','BWE')
    tixi_h.addTextElement(apt_xpath, 'name', 'Braunschweig, Germany')
    tixi_h.addDoubleElement(apt_xpath, 'positionNorth', 52.319, '%.3f')
    tixi_h.addDoubleElement(apt_xpath, 'positionEast', 10.556, '%.3f')
    tixi_h.addIntegerElement(apt_xpath, 'elevation', 84, '%i')

def main():

    workingDir = os.getcwd()

    #Input/Output definition
    cpacsIn = os.path.join(workingDir, 'ToolInput', 'cpacs_in.xml')
    cpacsOut = os.path.join(workingDir, 'ToolOutput', 'cpacs_out.xml')

    #Load Tixi
    load_external_libs()

    #Open cpacs file
    print('Start reading CPACS file...')
    try:
        tixi_h.open(cpacsIn)
    except:
        print('TIXI could not read input file.')

    your_function()

    tixi_h.save(cpacsOut)
    tixi_h.close()


if __name__ == '__main__':
    main()
