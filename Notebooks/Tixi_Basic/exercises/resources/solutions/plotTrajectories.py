xpath_expr = "//*/trajectory"
xpaths = expression_get_xpaths(xpath_expr)
for id, xpath in enumerate(xpaths):
    len = tixi_h.getVectorSize(xpaths[id] + "/flightPoints/flightDistance")
    flightDistance = tixi_h.getFloatVector(xpaths[id] + "/flightPoints/flightDistance", len)
    altitude = tixi_h.getFloatVector(xpaths[id] + "/flightPoints/altitude", len)
    thrust = tixi_h.getFloatVector(xpaths[id] + "/flightPoints/thrust", len)
    name = tixi_h.getTextElement(xpaths[id] + "/name")
    plot_trajectory(flightDistance, altitude, thrust, name)