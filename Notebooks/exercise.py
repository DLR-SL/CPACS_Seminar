import os
from tixi3 import tixi3wrapper
tixi_h = tixi3wrapper.Tixi3()


airport_xpath = '/cpacs/airports/airport[1]'
#airport_xpath = tixi_h.uIDGetXPath('FRA')


airport_name = tixi_h.getTextElement(airport_xpath+'/name')
# positionNorth = tixi_h.getDoubleElement(os.path.join(airport_xpath,'positionNorth'))
# positionEast = tixi_h.getDoubleElement(os.path.join(airport_xpath,'positionEast'))

# print('Name: %s\nPosition North: %.3f\nPosition East: %.3f'
 #       %(airport_name, positionNorth, positionEast))