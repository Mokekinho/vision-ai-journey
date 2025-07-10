import cv2 as cv



def basics():

    #load an image
    img = cv.imread("assets/eu.jpeg",) # load an image from files


    cv.imshow("showing image", img)
    k = cv.waitKey(0) #wait util the time in ms or when user press any key, 0 is for wait infinite

    if k == ord('s'): #if the key that was presses was 's', the cv.waitKey returns an integer, that's why it is necessary the ord()
        cv.imwrite("assets/eucopia.jpg", img)




if __name__ == "__main__":
    print(cv.__version__)

    basics()