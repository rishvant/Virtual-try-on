import numpy as np
import cv2
#final_output_1
frame = cv2.imread(r'C:\Users\Shreeaansh Goel\Downloads\sample_single.png')
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# define range of green color in HSV
lower_green = np.array([25, 52, 72])
upper_green = np.array([102, 255, 255])
# Threshold the HSV image to get only blue colors
mask_white = cv2.inRange(hsv, lower_green, upper_green)
mask_black = cv2.bitwise_not(mask_white)

# converting mask_black to 3 channels
mask_black_3CH = cv2.merge([mask_black] * 3)

cv2.imshow('original', frame)
#cv2.imshow('mask_black', mask_black_3CH)

dst3 = cv2.bitwise_and(mask_black_3CH, frame)
cv2.imshow('Pic+mask_inverse', dst3)

# create white mask
mask_white_3CH = cv2.merge([mask_white] * 3)
dst3_wh = cv2.bitwise_or(mask_white_3CH, dst3)
cv2.imshow('Pic+mask_wh', dst3_wh)

# load and resize design image 1
design = cv2.imread(r'C:\Users\Shreeaansh Goel\Downloads\d_1.jpg')
design = cv2.resize(design, mask_black.shape[1::-1])
#cv2.imshow('design resize', design)

# combine design with black mask
design_mask_mixed = cv2.bitwise_or(mask_black_3CH, design)
#cv2.imshow('design_mask_mixed', design_mask_mixed)

# combine design with white mask
final_mask_black_3CH = cv2.bitwise_and(design_mask_mixed, dst3_wh)
cv2.imshow('final_out', final_mask_black_3CH)

# load and resize design image 2 (d_222.jpg)
design2 = cv2.imread(r'C:\Users\Shreeaansh Goel\Downloads\d_222.jpeg')
design2 = cv2.resize(design2, mask_black.shape[1::-1])
#cv2.imshow('design2 resize', design2)

# combine design2 with black mask
design_mask_mixed2 = cv2.bitwise_or(mask_black_3CH, design2)
#cv2.imshow('design_mask_mixed2', design_mask_mixed2)

# combine design2 with white mask
final_mask_black_3CH2 = cv2.bitwise_and(design_mask_mixed2, dst3_wh)
cv2.imshow('final_out2', final_mask_black_3CH2)
##
design3 = cv2.imread(r'C:\Users\Shreeaansh Goel\Downloads\d_5.jpeg')
design3 = cv2.resize(design3, mask_black.shape[1::-1])
#cv2.imshow('design2 resize', design2)

# combine design2 with black mask
# design_mask_mixed3 = cv2.bitwise_or(mask_black_3CH, design3)
# #cv2.imshow('design_mask_mixed2', design_mask_mixed2)

# # combine design2 with white mask
# final_mask_black_3CH3 = cv2.bitwise_and(design_mask_mixed3, dst3_wh)
# cv2.imshow('final_out3', final_mask_black_3CH3)

cv2.waitKey()