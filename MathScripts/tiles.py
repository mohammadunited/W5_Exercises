

each_tile= (1*1)
boxarea =  (each_tile * 12)
bathroom_area = 80
boxes_required = round(bathroom_area/boxarea)
print("Boxes need to cover room is",boxes_required)

import math
tiles_needed = 60 * .1
area_needed = tiles_needed + bathroom_area
final_boxes_needed = round(area_needed / boxarea)
print(final_boxes_needed,"will be required incase")

