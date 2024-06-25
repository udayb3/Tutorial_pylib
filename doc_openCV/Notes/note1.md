## Interpolation: process of estimating values b/w known data points. it allows us fill the gap if any.

## Morphological Operations: They process image based on shape by applying a structure to an input image.
Basic morphological operations are Erosion: Eroding away boundary of the front object and Dilation: Increase the object area.

## Interpolation options in openCV
1. INTER_NEAREST: a nearest-neighbor interpolation
2. INTER_LINEAR: a bilinear interpolation
3. INTER_AREA: resampling using pixel area relation
4. INTER_CUBIC: Bi-cubic interpolation over 4*4 pixel neighborhood 
5. INTER_LANCOZOS4

```python
uint8= unsigned int[0-255]
```
## contours: Curves joining all continuous points having same intensity/color(Can be used in shape analysis, object detection).

## Image Segmentation: Computer Vision technique to partition digital image into discrete group of pixels- image segments[for object detection tasks.]

## Canny image: it is method to detect edges in the image. It can be broken down in 5 steps:
  1. Apply Gaussian filter to smooth the image in order to remove the noise
  2. Find the intensity gradients of the image
  3. Apply gradient magnitude thresholding or lower bound cut-off suppression to get rid of spurious response to edge detection
  4. Apply double threshold to determine potential edges
  5. Track edge by hysteresis: Finalize the detection of edges by suppressing all the other edges that are weak and not connected to strong edges.

## Retrieval modes: The retrieval modes are as follows:
  1. RETR_LIST: It retrievers all the contours[not establishes hierarchial relationship]
  2. RETR_TREE: It retrieves all the contours and constructs full hierarchy of nested contours.
  3. RETR_EXTERNAL: It retrieves only extreme outer colors.
  4. RETR_CCOMP: retrieves all the contours and contructs a 2 level heirarchy.

## Contours Approximations modes: It specifies the contours approximation methods:
  1. CHAIN_APPROX_NONE: Stores all of the contour points.
  2. CHAIN_APPROX_SIMPLE: Only stores the end-points of the vertical, horizontal and diagonal segments.

## Thresholding: A simple segmentation method. Basic thresholding simply means to apply a pixel below which all the pixel will be rejected.

## HSB and LAB Colorspaces:
  1. HSB defines colorspace in terms of Hue[color type, ranges from 0-360], Saturation[intensity of the color, range from 0 to 100%] and Value[brightness of the color, ranges from 0 to 100%].
  2. LAB defines colorspace in terms of human perception. l measures if color is light/dark. a and b represent the chromaticity of the sample.

## Masking: It simply applies us to apply effects to only certain parts of the image. it is done with a sort of mask.

Bilateral blurring: This is an extended version of the gaussian blur where normalization factor and range weight are added to the equation.

use of xml and yml files in storing training result and other things
format of npy type[made from the save method of the numpy class.]
