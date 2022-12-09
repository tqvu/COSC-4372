import cv2 as cv
import numpy as np
from PIL import Image


def MyPhantom(N1, N2, PosA1, PosA2, LenA1, LenA2, SIA, PosB1, PosB2, LenB1, LenB2, SIB, PosC1, PosC2, LenC1, LenC2, SIC):
  data = np.zeros((N1, N2, 3), dtype=np.uint8)
  
  for i in range(N1):
    for j in range(N2):
        if (PosA1 <= i <= PosA1 + LenA1) and (PosA2 <= j <= PosA2 + LenA2):
            data[i,j] = SIA
            
  for i in range(N1):
    for j in range(N2):
        if (PosB1 <= i <= PosB1 + LenB1) and (PosB2 <= j <= PosB2 + LenB2):
            data[i,j] = SIB

  cv.ellipse(data, (PosC1, PosC2), (LenC1, LenC2), 0, 0, 360, (0, 0, SIC), -1)
  
  ymin = min(PosB1, PosC1)
  for i in range(N1):
    for j in range(N2):
      if i < ymin:
          data[i,j] = 0
          
  ymax = max(PosB1+LenB1, PosC1 + LenC1-5)
  for i in range(N1):
    for j in range(N2):
      if i > ymax:
          data[i,j] = 0
          
  xmin = min(PosB2, PosC2)
  for i in range(N1):
    for j in range(N2):
      if j < xmin:
          data[i,j] = 0
          
  xmax = max(PosB2 + LenB2, PosC2 + LenC2+5)
  for i in range(N1):
    for j in range(N2):
      if j > xmax:
          data[i,j] = 0
  
        
      
      
  img = Image.fromarray(data,'RGB')
  img.show()
  
MyPhantom(100, 100, 0, 0, 100, 100, 255, 40, 20, 30, 30, 150, 75, 65, 10, 15, 150)