#Image is just a large array of numbers soo...
image = [[0,   100, 200],[50,  150, 250],[255, 128, 10]]

def show(theimage):
    '''To print the given image'''
    for i in theimage:
        for j in i:
            print(j, end = ' ')
        print()
print(f"The original")
show(image)

def invert(theimage):
    """To invert the given image and store it in a new array"""
    c, d = 0, 0
    inverted = theimage.copy()
    c, d = 0, 0
    for i in theimage:
        for j in range(len(i)):
            i[j] = 255-i[j]
    return inverted
print(f"The inverted:")
invert(image)
print("the original?")
invert(image)

def brightness(theimg, amount):
    '''To control the brightness'''
    result = []
    for row in theimg:
        new_row = []
        for v in row:
            new_row.append(min(255, max(0, v + amount)))
        result.append(new_row)
    return result

def brightness(img, amount):   # one-line version, same result
    return [[min(255, max(0, v + amount)) for v in row] for row in img]

def threshold(theimage):
    '''To make the image completely black and white'''
    thresh = []
    for i in theimage:
        o = []
        for j in i:
            o.append(0) if j<128 else o.append(255) #or o.append(0 if j<128 else 255)
        thresh.append(o)
    return thresh

#GEOMETRIC OPERATIONS:
def vflip(theimage):
    '''To flip an image vertically'''
    flipped = []
    for i in range(len(theimage),0,-1):
        flipped.append(theimage[i-1])
    return flipped

def hflip(theimage):
    '''To flip and image horizontally'''
    flipped = []
    for i in theimage:
        flipped.append(i[::-1])
    return flipped

def rotate(theimage):
    '''Rotating an image'''
    m = len(theimage[0])
    n = len(theimage)
    i,j = 0,0
    result = []
    for a in range(0,n): 
        result.append([x for x in range(0,m)])
    for row in theimage:
        for item in row:
            result[i][j] = item
            i+=1
        i=0
        j+=1
    return result
print("\n\nRotation:")
print(rotate(image))