import cv2



def trace_wires(mask, bboxes):

    num_labels, labels = cv2.connectedComponents(mask)
    nets = {}
    pin_to_net = {}

    for i, (x1, y1, x2, y2, cls) in enumerate(bboxes):
        #i can add a buffer here if needed 
        edge_pixels = set()
        

        for x in range(x1 - 5, x2 + 5):
            edge_pixels.add((x, y1))
            edge_pixels.add((x, y2))

        for y in range(y1 - 5, y2 + 5):
            edge_pixels.add((x1, y))
            edge_pixels.add((x2, y))
        
        net_ids = set()
        #labels of edge pixels to check the wire its connected to
        for x, y in edge_pixels:
            label = labels[y, x]
            if label != 0:
                net_ids.add(label)
                
        pin_id = f"component_{i}_pin_{cls}"
        pin_to_net[pin_id] = list(net_ids)

        for net in net_ids:
            nets.setdefault(net, []).append(pin_id)

    return nets, pin_to_net
        