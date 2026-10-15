#Image is just a large array of numbers soo...
image = [[0,   100, 200],[50,  150, 250],[255, 128, 10]]
img = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

def show(theimage):
    '''To print the given image'''
    for i in theimage:
        for j in i:
            print(j, end = ' ')
        print()
print(f"The original")
show(img)
print('\n')
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

#doubt
def transpose(theimage):
    '''I thought that for rotating it will be enough to take a transpose of the matrix but was wrong hence this code is of no use'''
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

def crop(theimage, v, n):
    #5x5--> 4x4, remove one row and one column
    # n = input("From where do you want to crop? l-left, r-right, u-up, d-down\t")
    '''Crop'''
    co = theimage.copy()
    if n == 'u':
        for i in range(v):
            del co[0]
    elif n == 'd':
        for i in range(v):
            del co[-1]
    elif n == 'r':
        for i in range(v):
            for row in theimage:
                del row[-1]
    elif n == 'l':
        for i in range(v):
            for row in theimage:
                del row[0]
    return co

def rotate(theimage, s):
    '''Rotate the image by 90 degrees'''
    if s == 'l':
        m = len(theimage[0])
        copi = theimage[::-1].copy()
        result = []
        for i in range(m):
            a = []
            for row in copi:
                a.append(row[0])
            result.append(a)
            crop(copi,1,'l')
        return result
    elif s == 'r':
        m = len(theimage[0])
        copi = theimage.copy()
        result = []
        for i in range(m):
            a = []
            for row in copi:
                a.append(row[-1])
            result.append(a)
            crop(copi,1,'r')
        return result

#Neighbourhood Operation

def blur(theimage):
    k = []
    for i in range(3):
        a = []
        for j in range(3):
            a.append(round(1/9,2))
        k.append(a)
    
    print(k)

blur(image)



#Bonus

def rgb(theimage):
    result = []
    for row in theimage:
        a = []
        k = []
        for ele in row:
            i = round(ele/3,2)
            k.append(i)
        a.append(k)
    result.append(a)
    return result
show(rgb(image))


