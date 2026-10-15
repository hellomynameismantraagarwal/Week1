The functions and their uses:

1. show(theimage)
|-> This function is just used mostly by me to keep a check whether the output matrix/image is good to go as per the problem
    It basically just prints the matrix in a mannered way.
    It works by iterating through each row and for that row it will print the value of the element/pixel and after that row is finished it will go to the new line
    Applicable for m x n matrices/images
    It does NOT return a new array it just simply prints it hence it is a VOID function.

2. invert(theimage)
|->This function is to give inver the whole array, basically to give the quite opposite of a pixel
    for eg. if a pixel is _50_, the pixel will be converted to _205_ (255-50), quite literally inverting the value of that pixel
    It takes every row first and then the elements/pixels and then assign it to a new variable and store it in a new array
    This function returns a new image/array

3. brightness(theimage)
|->