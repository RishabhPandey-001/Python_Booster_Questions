# 15.	Overlapping Rectangles: Check if two rectangles overlap. (GFG problem link included)
# Function to check if two rectangles overlap
def doOverlap(rect1, rect2):
    # rect1 and rect2 are given as [x1, y1, x2, y2] -> (top-left and bottom-right)
    
    # If one rectangle is to the left of the other
    if rect1[2] < rect2[0] or rect2[2] < rect1[0]:
        return False

    # If one rectangle is above the other
    if rect1[1] < rect2[3] or rect2[1] < rect1[3]:
        return False

    return True

# Example usage
rect1 = [0, 10, 10, 0]  # (top-left: 0,10), (bottom-right: 10,0)
rect2 = [5, 5, 15, 0]   # (top-left: 5,5), (bottom-right: 15,0)

print("Do rectangles overlap?", doOverlap(rect1, rect2))
