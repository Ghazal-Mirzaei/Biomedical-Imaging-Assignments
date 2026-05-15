Task one: Read Files

import pandas as pd
excel_data = pd.read_excel('Book1.xlsx')
print(excel_data.head())

csv_data = pd.read_csv('Book1.csv' , delimiter = ';')
print(csv_data.head())

Task Two: Read Images And Display Images
#numpy  as a powerful library for manipulating arrays and matrics
#scipy for higher-order mathematical operations
#matplotlib for plotting and visualization

#Here we use cv2 to read an image into an ndarray and convert it to a grayscale image
import cv2
import matplotlib.pyplot as plt

gray_img = cv2.imread('garden.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(gray_img, cmap='gray')
plt.axis('off')
plt.show()

Task Three: Read DICOM
# Using pip install pydicom
from pydicom import dcmread
fpath = "1-001.dcm"
ds = dcmread(fpath)  #ds = dataset

# Normal mode:
print()
print(f"File path........: {fpath}")
print(f"SOP Class........: {ds.SOPClassUID} ({ds.SOPClassUID.name})") #shows the type of DICOM object
print()

pat_name = ds.PatientName
print(f"Patient's Name...: {pat_name.family_comma_given()}") #PatientName
print(f"Patient ID.......: {ds.PatientID}")
print(f"Modality.........: {ds.Modality}") #Modality = type of medical device
print(f"Study Date.......: {ds.StudyDate}") #The date the imaging was performed
print(f"Image size.......: {ds.Rows} x {ds.Columns}") #Number of pixels/resolution/image size

#“Try to get the value of SliceLocation.
# use .get() if not sure the item exists, and want a default value if missing
print(f"Slice location...: {ds.get('SliceLocation', '(missing)')}") 
#If it doesn’t exist, return '(missing)' instead of crashing.”
plt.imshow(ds.pixel_array, cmap=plt.cm.gray) #cmap = colormaps
plt.show()

Task Four: Write Image
#cv2.imwrite for saving image
cv2.imwrite('output_image.jpg', ds.pixel_array)

Task Five: Analyse The Code
#Usinng matplotlib for plotting
import  matplotlib as plt
import matplotlib.image as mpimg
import numpy as np

#making tiled image
def imag_X(img,n,m=1):
  if n==1:
    tiled_img = img
  else:
    lst_imgs = []
    for i  in range (n):
      lst_imgs.append(img)
     tiled_img = np.concatenate(lst_imgs, axis=1)
  if m>1:
    lst_imgs = []
    for i in range (m):
      lst_imgs.append(tiled_img)
     tiled_img = np.concatenate(lst_imgs, axis=0)
  return tiled_img

basic_pattern=mpimg.imread('garden.jpg') #load an image and convert it into a multi-dimensional NumPy array
decorators_img=imag_X(basic_pattern,2,3)
plt.axis('off')
plt.imshow(decorators_img)

Task Six: Analyse The Code, Cropping, Histogram

basic_pattern = mpimg.imread ('garden.jpg')
print(basic_pattern.shape)
cropped = basic_pattern[800:950,800:1000]
plt.axis('off')
plt.imshow(cropped)


import matplotlib.pyplot  as plt
import numpy  as np

# assume 'cropped' is your image from earlier
gray = cropped.mean(axis=2)   # convert to grayscale if needed

plt.figure(figsize=(12,6))

#Histogram with 256 bins
plt.subplot(1,2,1)
plt.hist(gray.ravel(), bins=256, color='green')
plt.title("Histogram with 256 bins")

#Histogram with 16 bins
plt.subplot(1,2,2)
plt.hist(gray.ravel(), bins=16, color='green')
plt.title("Histogram with 16 bins")

plt.show()
















