# define the XPath for the aircraft-model
model_xpath = tixi_h.uIDGetXPath('MyAircraft')

# create the 'engines' element as a child of that model
tixi_h.createElement(model_xpath, 'engines')