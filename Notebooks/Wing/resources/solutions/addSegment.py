tixi_h.createElement(wing_xPath+"/segments","segment")
segment_xPath = wing_xPath+"/segments/segment[2]"
tixi_h.addTextAttribute(segment_xPath,"uID","wing1segment2")

tixi_h.addTextElement(segment_xPath,"name","Wing segment")
tixi_h.addTextElement(segment_xPath,"fromElementUID","wing1section2element1")
tixi_h.addTextElement(segment_xPath,"toElementUID","wing1section3element1")