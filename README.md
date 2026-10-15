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
|->This function changes the brightness of the image by increasing or decreasing the intensity of the pixel.
    Like any other function iterates every element from every row and changes it to the desired value
    It requires 2 parameters the image and how much to increase the brightness. The max brightness of a pixel can be 255 and lowest can be 0 hence the use of max and min in it.
    This function returns a new image/array.
    Here I also learnt about one liner for loops, how to use a whole loop in one line.

4. threshold(theimage)
|->This function makes the image completely black and white by changing all the pixels value to 0 or 255
    If the intensity of a pixel is more or equal to 128 then it will be converted to 225 else 0
    This function returns a new array

5. vflip(theimage) and hflip(theimage)
|->vlip() flips the image vertically while hflip() flips the image horizontally
    for vflip() it takes the image and reverses it
    for hflip() it takes the image and its rows and reverses the rows
    They both return a new array/image

6. crop(theimage, v, n)
|->This function crops the image, here v is the amount to be cropped and n is from where to crop, for example if input is   crop(image, 1, 'l') the image will be cropped from the left and 1 unit will be removed from the image. n can be 'l'-left, 'r'-right, 'u'-up, 'd'-down.
    This function returns a new array/image.

7. rotate(theimage, s)
|-> This function rotates the image, and takes s as a parameter for which direction 'l'-clockwise, 'r'-counterclockwise
    Funny thing I did a wrong assumption and thought the rotated matrix would be its transpose and spent a lot of time figuring out how to get the transpose. But later on realising I fixed it. It basically takes the rows first or last element and arrange them in a specific manner to get the rotated image.
    This function can only rotate an image 1 time and can rotate it 90 degrees. It also uses crop function to delete the unwanted row/column.
    Later on I will update it so that it can rotate the image multiple times.

8. 
