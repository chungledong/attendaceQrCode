import cv2
import decode
import tkinter
from  tkinter import Tk, Frame, BOTH

class mainform(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="while")
        self.parent=parent
        self.initUI()

    def initUI(self):
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)

 # Function Attendace
def check_Attendace():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    while cap.isOpened():
        success, img = cap.read()
        if success == True:
            decode.decode_img(img)
            cv2.imshow("decode", img)
            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            # Break the loop
        else:
            break

    # When everything done, release the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()
if __name__ == '__main__':
    #check_Attendace()
    gui_main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
