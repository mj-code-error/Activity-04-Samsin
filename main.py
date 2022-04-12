
import cv2
import SampleClass as sc

    

file= input("Enter the image filename: ")
filepath = sc.Sample.findpath(file)

counter = False

while counter == False:
    user_input= int(input("Enter flag values 1 for Colored, 0 for Grayscale, -1 for Unchanged : "))
    if user_input == 1 or user_input == 0 or user_input ==-1:
        flag = user_input
        counter = True
    else:
        print("Invalid Input!")


windowTitle = 'Sample Image Output'
readCvImage = cv2.imread(filepath, flag)
cv2.imshow(windowTitle, readCvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
