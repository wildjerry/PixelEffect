# let's start with the Imports 
import cv2
import numpy as np
import imageio
from math import sqrt
FPS = 24
EXPONENT = 1/3
def exportPixelGif(imLogo,imName):

    framecount = FPS*4
    stillcount = FPS*1

    with imageio.get_writer(imName+".gif",mode="I") as writer:
        framenumber = 1

        imSize = imLogo.shape
        print(imSize)
        while framenumber < framecount:
            print(framenumber)
            scale_h = framenumber*int((imSize[0]/framecount)**EXPONENT)
            scale_w = framenumber*int((imSize[1]/framecount)**EXPONENT)

            scale_points = (scale_w, scale_h)
            resized_down = cv2.resize(imLogo, scale_points, interpolation= cv2.INTER_NEAREST)
            resized_up = cv2.resize(resized_down,(imSize[0],imSize[1]),interpolation = cv2.INTER_NEAREST)
            writer.append_data(resized_up)
            framenumber += 1
        while framenumber < (framecount+stillcount):
            final_resize = cv2.resize(imLogo,(imSize[0],imSize[1]),interpolation = cv2.INTER_NEAREST)
            framenumber += 1
            writer.append_data(final_resize)
        print(resized_up.shape)



firstLogo = cv2.cvtColor(cv2.imread("FIRST White Background.png"), cv2.COLOR_BGRA2RGBA)
RRlogo = cv2.cvtColor(cv2.imread("RoaringWhite.png"),cv2.COLOR_BGRA2RGBA)
#exportPixelGif(googleLogo,"google")
exportPixelGif(firstLogo,"first")

#press any key to close the windows
cv2.destroyAllWindows()
