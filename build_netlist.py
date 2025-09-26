import cv2



def trace_wires(mask, bboxes):

    num_labels, labels = cv2.connectedComponents(mask)


    for i, (x1, y1, x2, y2, cls) in enumerate(bboxes):


        #i can add a buffer here if needed 
        edge_pixels = []
        nets = {}

        for x in range(x1, x2 + 1):
            edge_pixels.append((x, y1))
            edge_pixels.append((x, y2))

        for y in range(y1, y2 + 1):
            edge_pixels.append((x1, y))
            edge_pixels.append((x2, y))

        #labels of edge pixels to check the wire its connected to
        for x, y in edge_pixels:
            label = labels[y, x]
            if label != 0:
                net = nets.get(label, [])

        pin_id = f"component_{i}_pin_{cls}"
        
def find_connections(wire1, wire2):
    x_max1, y_max1 = wire1
    x_max2, y_max2 = wire2

    if abs(x_max1 - x_max2) < 3 and abs(y_max1 - y_max2) < 3:
        return True
    return False