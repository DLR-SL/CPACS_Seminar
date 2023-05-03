# define the XPath to the 'engines' element we have just created
engine_container_xpath = '/'.join((model_xpath, 'engines'))

# create an 'engine' element as a child
tixi_h.createElement(engine_container_xpath, 'engine')