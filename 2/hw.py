import numpy as np
from PIL import Image
import matplotlib.pyplot as mp
from glob import glob
from tqdm import tqdm


cnt=0
im_paths = glob('D:/biomag_mentoring-main/2/1/test_folder/*.png')


for image_path in im_paths[:1]:
    img = Image.open(image_path)
    array = np.array(img) 
    print(cnt)
    #print('img> %d' % cnt)
    for i in range(len(array)):
        for j in range(len(array[i])):
                red = array[i,j,0]
                green = array[i,j,1]
                blue = array[i,j,2]
                g_val = (red+green+blue)/3
                array[i,j] = g_val * 3 
    
        final = Image.fromarray(array)
        final.save('D:/biomag_mentoring-main/2/1/out/out.png')
        #print('img> %d ok' %cnt)
        cnt+=1
   
