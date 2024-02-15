import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from glob import glob
from tqdm import tqdm
import cv2 as cv

im_paths = glob('D:/biomag_mentoring-main/2/1/test_folder/*.png')
cnt=0
for path in tqdm(im_paths[:1]):
     img = Image.open(path)
     array = np.array(img) 
     #base = array
     if array.shape[0] & array.shape[1] == 1024:
        
        
        for i in range(len(array)):
             for j in range(len(array[i])):
                r = array[i,j,0]
                g = array[i,j,1]
                b = array[i,j,2]
                grey = ((r*0.299+g*0.587+b*0.114)/3)*4
                array[i,j] = grey
        
        final = Image.fromarray(array)
        final.save('D:/biomag_mentoring-main/2/1/out/out%d.png' % cnt)
        # array[array < 140] = 0
        dn = cv.fastNlMeansDenoising(array,array,10,7,21)
        array[array > 180] = 0
        dn = cv.fastNlMeansDenoising(array,array,10,7,21)
        dn,array = cv.threshold(array,100,255,cv.THRESH_BINARY)
        
        
        mk = Image.fromarray(array)
        mk.save('D:/biomag_mentoring-main/2/1/out/mk%d.png' % cnt)
        
       
       
        cnt+=1