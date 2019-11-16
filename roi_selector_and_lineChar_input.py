import numpy as np
import cv2
import imutils

import numpy as np
import cv2

ix,iy = -1,-1
mouse_down = False
mouse_flag = 0
x = y = w = h = 0
line_type=''
print_flag=0

def line(event,x,y,flags,param):
    global ix, iy, vx, vy, trigger, mouse_down, mouse_flag
    if event == cv2.EVENT_LBUTTONDOWN:
        # cv2.circle(img,(x,y),100,(255,0,0),-1)
        ix, iy = x, y
        print(ix, iy)
        mouse_down = True
        mouse_flag =  0

    if event == cv2.EVENT_LBUTTONUP and mouse_down:
        vx, vy = x, y
        print(vx, vy)
        mouse_down = False
        mouse_flag = 2

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('rtsp://admin:123456@192.168.1.10:554/H264?ch=1&subtype=0&proto=Onvif')
rectangle_flag = 0
line_flag = 0


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame_new = frame
    frame = imutils.resize(frame, width=800)
    frame_new = imutils.resize(frame, width=800)
    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.putText(frame, "first press r to select ROI ..", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (0, 0, 200),
                2, cv2.LINE_AA)
    cv2.putText(frame,
                "then l to draw line..",
                (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (0, 0, 200),
                2, cv2.LINE_AA)
    cv2.putText(frame,
                "q to quit selection mode...(DO NOT QUIT WITHOUT SELECTION) ...",
                (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (0, 0, 200),
                2, cv2.LINE_AA)



    key = cv2.waitKey(1) & 0xFF
    file1 = open("roi_config_file.txt", "w")

    if key == ord("r"):
        initBB = cv2.selectROI("Frame", frame, fromCenter=False,showCrosshair=True)
        print(initBB)
        x = initBB[0]
        y = initBB[1]
        w = initBB[2]
        h = initBB[3]

        file1.write(str(initBB[0]) + "\n")
        file1.write(str(initBB[1]) + "\n")
        file1.write(str(initBB[2]) + "\n")
        file1.write(str(initBB[3]) + "\n")

        cv2.destroyAllWindows()

        rectangle_flag = 1

    if key == ord("w"):
        cv2.destroyAllWindows()
    if key == ord("l"):
        # cv2.imshow('frame_new', frame)
        cv2.destroyAllWindows()

        line_type=input("enter lineType 'h' for Horizontal,'v' for vertical..\n")
        print(line_type)

        while True:
            print_flag = 1
            if (line_type != 'h' and line_type != 'v'):
                if print_flag==1:
                    print("invalid_cradentials,reenter line credentials press l.. ")
                    line_type = input("enter lineType 'h' for Horizontal,'v' for vertical..\n")

                    print_flag = 0
            elif (line_type == 'h' or line_type == 'v'):
                break


        print("\n")
        cv2.destroyAllWindows()

        # cv2.setMouseCallback('frame', line)


        # roi_coord.insert(10, line_type)
        # roi_coord.insert(9, line_type)
        mouse_flag = 2

    if key == ord("q"):
        break

    if rectangle_flag == 1:
        # cv2.rectangle(frame,(384,0),(510,128),(0,255,0),3)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        # framei= frame[y:y + h, x:x + w]

    if mouse_flag == 2:
        if line_type == 'v':
            cv2.line(frame, ((x + x + w) // 2, y), ((x + x + w) // 2, y + h), (255, 0, 0), 5)

        if line_type == 'h':
            cv2.line(frame, (x, (y + y + h) // 2), (x + w, (y + y + h) // 2), (255, 0, 0), 5)




        # cv2.line(frame, (0, 0), (511, 511), (255, 0, 0), 5)
    cv2.imshow('frame', frame)
    print_flag = 1
    #
    file1.write(str(x) + "\n")
    file1.write(str((y + y + h) // 2) + "\n")
    file1.write(str(x + w) + "\n")
    file1.write(str((y + y + h) // 2) + "\n")
    file1.write(str(line_type) + "\n")

file1.close()

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()




