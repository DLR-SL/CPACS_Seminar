# define the XPath to the 'engine' element we have just created
engine_xpath = '/'.join((engine_container_xpath, 'engine[1]'))

# specify the 'name' of the engine as a TextElement
tixi_h.addTextElement(engine_xpath, 'name', 'My Engine')

# add a 'description' as a TextElement
tixi_h.addTextElement(engine_xpath, 'description', 'this is my engine')