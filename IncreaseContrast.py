import cv2 as cv
import numpy as np
from PIL import Image


def MyPhantom(N1, N2, PosA1, PosA2, LenA1, LenA2, SIA, PosB1, PosB2, LenB1, LenB2, SIB, PosC1, PosC2, LenC1, LenC2, SIC):
  data = np.zeros((N1, N2, 3), dtype=np.uint8)
  
  #Get max intensity from both objects
  maxIntensity = max(SIB, SIC)
  
  #Normalize both intensities and update SIB and SIC
  SIB = (SIB/maxIntensity) * 255
  SIC = (SIC/maxIntensity) * 255
  
  #Add blank space
  for i in range(N1):
    for j in range(N2):
        if (PosA1 <= i <= PosA1 + LenA1) and (PosA2 <= j <= PosA2 + LenA2):
            data[i,j] = 0
  
  #Add object 1      
  for i in range(N1):
    for j in range(N2):
        if (PosB1 <= i <= PosB1 + LenB1) and (PosB2 <= j <= PosB2 + LenB2):
            data[i,j] = SIB

  #Add object 2
  cv.ellipse(data, (PosC1, PosC2), (LenC1, LenC2), 0, 0, 360, (0, 0, SIC), -1)
  

  img = Image.fromarray(data,'RGB')
  img.show()
  
MyPhantom(100, 100, 0, 0, 100, 100, 255, 40, 20, 30, 30, 100, 75, 65, 10, 15, 100)