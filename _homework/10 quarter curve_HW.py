def circle(centerX, centerY, diameter):
    radius = diameter / 2
    x = centerX - radius
    y = centerY - radius
    oval(x, y, diameter, diameter)

ratio = .6

width = 281
height = 380

handleProportion = 71
handleProportion = handleProportion / 100

handle1 = width * handleProportion
handle2 = height * handleProportion

width_counter = width * ratio
height_counter = height * ratio

handleProportion_counter = handleProportion * ratio

handle1_counter = width * handleProportion_counter
handle2_counter = height * handleProportion_counter

path = BezierPath()
path.moveTo((0, height))
path.curveTo((handle1, height), (width, handle2), (width, 0))
path.curveTo((width, -handle2), (handle1, -height), (0, -height))
path.curveTo((-handle1, -height), (-width, -handle2), (-width, 0))
path.curveTo((-width, handle2), (-handle1, height), (0, height))
path.reverse()
path.moveTo((0, height_counter))
path.curveTo((handle1_counter, height_counter), (width_counter, handle2_counter), (width_counter, 0))
path.curveTo((width_counter, -handle2_counter), (handle1_counter, -height_counter), (0, -height_counter))
path.curveTo((-handle1_counter, -height_counter), (-width_counter, -handle2_counter), (-width_counter, 0))
path.curveTo((-width_counter, handle2_counter), (-handle1_counter, height_counter), (0, height_counter))


stroke(0)  # black stroke
fill(0)
strokeWidth(3)
translate(500, 500)  # move the origin of the canvas
drawPath(path)

# visualize the points
fill(1, 0, 0)  # red
stroke(None)

for point in path.points:
    x, y = point
    circle(x, y, 15)
    
    
    
    
    
    
