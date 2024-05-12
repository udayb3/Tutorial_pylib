Interpolation: process of estimating values b/w known data points. it allows us fill the gap if any.

Morphological Operations: They process image based on shape by applying a structure to an input image.
Basic morphological operations are Erosion: Eroding away boundary of the front object and Dilation: Increase the object area.

Interpolation options in openCV
1. INTER_NEAREST: a nearest-neighbor interpolation
2. INTER_LINEAR: a bilinear interpolation
3. INTER_AREA: resampling using pixel area relation
4. INTER_CUBIC: Bi-cubic interpolation over 4*4 pixel neighborhood 
5. INTER_LANCOZOS4


uint8= unsigned int[0-255]

contours: Curves joining all continuous points having same intensity/color(Can be used in shape analysis, object detection).

Image Segmentation: Computer Vision technique to partition digital image into discrete group of pixels- image segments[for object detection tasks.]
