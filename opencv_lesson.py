import cv2 as cv

def basics():

    #load an image
    img = cv.imread("assets/images/eu.jpeg", ) # load an image from files


    cv.imshow("showing image", img)
    k = cv.waitKey(0) #wait util the time in ms or when user press any key, 0 is for wait infinite

    if k == ord('s'): #if the key that was presses was 's', the cv.waitKey returns an integer, that's why it is necessary the ord()
        cv.imwrite("assets/images/eucopia.jpg", img)


def reading_videos():
    video = cv.VideoCapture("assets/videos/pc_fumbica.mp4") # it admits numbers, but it used when you tyind to acess the computer webcam, by default 0 will be the principal camera

    fps = video.get(cv.CAP_PROP_FPS)

    #tehe video variable it is an array of frames
    while True:
        is_true, frame = video.read()
        cv.imshow("Video", frame)

        if cv.waitKey(int(1000 / fps)) == ord('q'):
            break

    video.release()
    cv.destroyAllWindows()

def resize_rescale():
    def rescale(frame, scale = 0.75): #get a frame/image and scale it, by default 75%.
        #Images, videos, live videos.
        width = int(frame.shape[1] * scale)
        height = int (frame.shape[0] * scale)
        dimensions = (width,height)

        return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA) #this function resize the frame to one dimension, the interpolation is the method used to take of frames

    def change_res(frame,width,height):
        frame.set(3,width) # this number represent the ID for the width, this function has many ids to change
        frame.set(4, height)


    img = cv.imread("assets/images/eu.jpeg")

    img = rescale(img,0.3)

    cv.imshow('rescaled img', img)
    k = cv.waitKey(0)



if __name__ == "__main__":
    print(cv.__version__)

    basics()
    resize_rescale()