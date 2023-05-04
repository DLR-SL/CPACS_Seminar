tixi_h.createElement(wing_xPath+"/positionings","positioning")
positioning_xPath = wing_xPath+"/positionings/positioning[2]"
tixi_h.addTextAttribute(positioning_xPath,"uID","wingletPos")

tixi_h.addTextElement(positioning_xPath,"name","Winglet position")
tixi_h.addDoubleElement(positioning_xPath,"length",0.25,"%.2f")
tixi_h.addDoubleElement(positioning_xPath,"sweepAngle",70.,"%.1f")
tixi_h.addDoubleElement(positioning_xPath,"dihedralAngle",45.,"%.1f")

tixi_h.addTextElement(positioning_xPath,"fromSectionUID","wing1section2")
tixi_h.addTextElement(positioning_xPath,"toSectionUID","wing1section3")