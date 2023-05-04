# Add section:
tixi_h.createElement(wing_xPath+"/sections","section")
section_xPath = wing_xPath+"/sections/section[3]"
tixi_h.addTextAttribute(section_xPath,"uID","wing1section3")
tixi_h.addTextElement(section_xPath,"name","Section 3")

# Rotate the section by 45deg.:
tixi_h.createElement(section_xPath,"transformation")
tixi_h.createElement(section_xPath+"/transformation","rotation")
tixi_h.addDoubleElement(section_xPath+"/transformation/rotation","x",45.,"%.2f")

# Add element to the new section using the pre-defined NACA0009:
tixi_h.createElement(section_xPath,"elements")
tixi_h.createElement(section_xPath+"/elements","element")
element_xPath = section_xPath + "/elements/element[1]"
tixi_h.addTextAttribute(element_xPath,"uID","wing1section3element1")
tixi_h.addTextElement(element_xPath,"name","wing root element")
tixi_h.addTextElement(element_xPath,"airfoilUID","NACA0009")
tixi_h.createElement(element_xPath,"transformation")

# Scale the element:
tixi_h.createElement(element_xPath+"/transformation","scaling")
tixi_h.addDoubleElement(element_xPath+"/transformation/scaling","x",0.2,"%.2f")
tixi_h.addDoubleElement(element_xPath+"/transformation/scaling","z",0.2,"%.2f")