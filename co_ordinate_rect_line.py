import os
import cv2
import imutils
global New_key
New_key = ord("n")

cap = cv2.VideoCapture(0)
def draw_line(event,x,y,flags,param):
    global ix, iy, vx, vy, trigger, mouse_down, mouse_flag, line_flag
    if event == cv2.EVENT_LBUTTONDOWN:
        # cv2.circle(img,(x,y),100,(255,0,0),-1)
        line_flag = 0
        ix, iy = x, y
        print(ix, iy)
        mouse_down = True
        mouse_flag =  0
        file = open('co_ordinate_line.ini', 'w+')
        file.write(str(ix) + "\n")
        file.write(str(iy) + "\n")
        file.close()

    if event == cv2.EVENT_LBUTTONUP and mouse_down:
        vx, vy = x, y
        print(vx, vy)
        mouse_down = False
        mouse_flag = 2

        file = open('co_ordinate_line.ini', 'a')
        file.write(str(vx) + "\n")
        file.write(str(vy) + "\n")
        file.close()
        line_flag = 1

def co_ordinate_file_status_rect():
    global  x, y, w, h ,New_key
    rectangle_flag, line_flag = 0,0
    try:


        count = 0
        file = open('co_ordinate_rect.ini', 'rb')
        with file as f:
            for line in f:
                count += 1
        f.close()
        if count == 4:
            file = open('co_ordinate_rect.ini', 'r+')
            lines = [line for line in file.readlines()]
            x = int(lines[0])
            y = int(lines[1])
            w = int(lines[2])
            h = int(lines[3])
            return 1
        elif count !=4 or New_key==ord('n'):
            # os.remove("co_ordinate_config.ini")
            global cap
            cap = cv2.VideoCapture(0)
            while (True):
                ret, frame = cap.read()
                # frame_new = frame
                frame = imutils.resize(frame, width=800)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, "Press R and then Select ROI in the PopUp Frame", (0, frame.shape[0] - 70), font, 1,
                            (0, 0, 255), 1, cv2.LINE_AA)
                cv2.putText(frame, "Press Space for selection", (0, frame.shape[0] - 40), font, 1, (0, 0, 255), 1,
                            cv2.LINE_AA)
                cv2.putText(frame, "Press Q to exit selection mode OR R to Repeat", (0, frame.shape[0] - 10), font, 1,
                            (0, 0, 255), 1, cv2.LINE_AA)
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q") or key == ord("Q"):
                    break
                if key == ord("n") :
                    New_key = ord("n")
                    break
                if key == ord("r"):
                    initBB = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
                    # ll = list(initBB)
                    x = initBB[0]
                    y = initBB[1]
                    w = initBB[2]
                    h = initBB[3]
                    file = open('co_ordinate_rect.ini', 'w+')
                    file.write(str(initBB[0]) + "\n")
                    file.write(str(initBB[1]) + "\n")
                    file.write(str(initBB[2]) + "\n")
                    file.write(str(initBB[3]) + "\n")
                    file.close()
                    rectangle_flag = 1
                    # cv2.destroyAllWindows()

                if rectangle_flag == 1:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.imshow('frame', frame)
            # cap.release()
            # cv2.destroyAllWindows()
            count = 0
            try:
                file = open('co_ordinate_rect.ini', 'rb')
                with file as f:
                    for line in f:
                        count += 1
                f.close()
            except FileNotFoundError:
                pass
            if count == 4:
                return 1
            else:
                return 0

    except FileNotFoundError:
        # print("except")
        cap = cv2.VideoCapture(0)
        print("try again..")
        while (True):
            ret, frame = cap.read()
            H, W = frame.shape[:2]
            # print(H,W)
            # frame_new = frame
            frame = imutils.resize(frame, width=800)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, "Press R and then Select ROI", (0, frame.shape[0] - 100), 3, 1, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, "Press Space for selection", (0, frame.shape[0] - 70), 3, 1, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, "Press Q to exit selection mode", (0, frame.shape[0] - 40), 3, 1, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, "Press N for New selection", (0, frame.shape[0] - 10), 3, 1, (0, 0, 255), 1, cv2.LINE_AA)


            key = cv2.waitKey(1) & 0xFF
            if key == ord("q") or key == ord("Q"):
                break
            if key == ord("r"):
                initBB = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
                # ll = list(initBB)
                x = initBB[0]
                y = initBB[1]
                w = initBB[2]
                h = initBB[3]
                file = open('co_ordinate_rect.ini', 'w+')
                file.write(str(initBB[0]) + "\n")
                file.write(str(initBB[1]) + "\n")
                file.write(str(initBB[2]) + "\n")
                file.write(str(initBB[3]) + "\n")
                file.close()
                cv2.destroyAllWindows()
                rectangle_flag = 1

            if rectangle_flag == 1:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.imshow('frame', frame)
        # cap.release()
        # cv2.destroyAllWindows()
        count = 0
        try:
            file = open('co_ordinate_rect.ini', 'rb')
            with file as f:
                for line in f:
                    count += 1
            f.close()
        except FileNotFoundError:
            pass
        # print(count)
        if count == 4:
            return 1
        else:
            return 0

def co_ordinate_file_status_line():
    global  ix, iy, vx, vy
    line_flag = 0
    try:
        count = 0
        file = open('co_ordinate_line.ini', 'r+')
        with file as f:
            for line in f:
                count += 1
        f.close()
        if count == 4:
            file = open('co_ordinate_line.ini', 'r+')
            lines = [line for line in file.readlines()]
            ix = int(lines[0])
            iy = int(lines[1])
            vx = int(lines[2])
            vy = int(lines[3])
            return 1
        elif count!=4 or New_key == ord("n"):

            # os.remove("co_ordinate_config.ini")

            # cap = cv2.VideoCapture(0)
            while (True):
                ret, frame = cap.read()
                frame_new = frame
                frame = imutils.resize(frame, width=800)
                # font = cv2.FONT_HERSHEY_SIMPLEX
                font=2
                cv2.putText(frame, "Press L ", (0, frame.shape[0] - 120), font, 1,
                            (0, 0, 255), 1, cv2.LINE_AA)
                cv2.putText(frame, "Press Right Mouse button and drag from point A to B ", (0, frame.shape[0] - 80), font, 1,
                            (0, 0, 255), 1, cv2.LINE_AA)
                cv2.putText(frame, "Press W for selection", (0, frame.shape[0] - 40), font, 1, (0, 0, 255), 1,
                            cv2.LINE_AA)
                cv2.putText(frame, "Press Q to exit selection mode OR L to Repeat", (0, frame.shape[0] - 10), font, 1,
                            (0, 0, 255), 1, cv2.LINE_AA)
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q") or key == ord("Q"):
                    cv2.destroyAllWindows()
                    break
                if key == ord("w"):
                    cv2.destroyAllWindows()
                if key == ord("l"):
                    # cv2.imshow('frame_new', frame)
                    cv2.setMouseCallback('frame_new', draw_line)

                    print("l")

                if key == ord("n"):
                    New_key = ord("n")


                if line_flag == 1:
                    cv2.line(frame, (ix, iy), (vx, vy), (255, 0, 0), 5)
                cv2.imshow('frame', frame)
            # cap.release()
            # cv2.destroyAllWindows()
            count = 0
            try:
                file = open('co_ordinate_line.ini', 'rb')
                with file as f:
                    for line in f:
                        count += 1
                f.close()
            except FileNotFoundError:
                pass
            if count == 4:
                return 1
            else:
                return 0

    except FileNotFoundError:
        # print("except")
        # cap = cv2.VideoCapture(0)
        while (True):
            ret, frame = cap.read()
            H, W = frame.shape[:2]
            # print(H,W)
            # frame_new = frame
            frame = imutils.resize(frame, width=800)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, "Press L ", (0, frame.shape[0] - 120), font, 1,
                        (0, 0, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, "Press Right Mouse button and drag from point A to B ", (0, frame.shape[0] - 80), font,1,
                        (0, 0, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, "Press W for selection", (0, frame.shape[0] - 40), font, 1, (0, 0, 255), 1,
                        cv2.LINE_AA)
            cv2.putText(frame, "Press Q to exit selection mode OR L to Repeat", (0, frame.shape[0] - 10), font, 1,
                        (0, 0, 255), 1, cv2.LINE_AA)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q") or key == ord("Q"):
                cv2.destroyAllWindows()
                break
            if key == ord("w"):
                cv2.destroyAllWindows()
            if key == ord("l"):
                # cv2.imshow('frame_new', frame)
                cv2.setMouseCallback('frame', draw_line)

                print("l")
                line_flag = 1
            if key == ord("n"):
                New_key = ord("n")

            if line_flag == 1:
                cv2.line(frame, (ix, iy), (vx, vy), (255, 0, 0), 5)
            cv2.imshow('frame', frame)
        # cap.release()
        # cv2.destroyAllWindows()
        count = 0
        try :
            file = open('co_ordinate_line.ini', 'rb')
            with file as f:
                for line in f:
                    count += 1
            f.close()
        except FileNotFoundError:
            pass
        # print(count)
        if count == 4:
            return 1
        else:
            return 0

def check_co_ordinates():
    status = co_ordinate_file_status_rect()
    if status == 1:
        print("Rectagle co-ordinates Present")
        status = co_ordinate_file_status_line()
        if status == 1:
            print("Line co-ordinates Present")
            return 1
        else:
            print("Line co-ordinates Failed")
            return 0
    else:
        print("Rectagle co-ordinates Failed")
        return 0
main_exit_flag=0
while True:
    if main_exit_flag==1:
        print('b')

        break
    print('s')

    current_dir = os.getcwd()
    x, y, w, h = 0,0,0,0
    ix, iy, vx, vy = 0,0,0,0

    status = check_co_ordinates()
    if status == 1:
        cap = cv2.VideoCapture(0)
        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()
            frame = imutils.resize(frame, width=800)
            # Display the resulting frame
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.line(frame, (ix, iy), (vx, vy), (255,0, 0), 3)
            cv2.imshow('frame',frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or main_exit_flag ==1:
                print('qq')
                main_exit_flag = 1
                break

            if key == ord('e') or main_exit_flag == 1:
                print('ee')

                break
            if key == ord("n"):
                New_key = ord("n")
                if os.path.isfile('co_ordinate_rect.ini') and os.path.isfile('co_ordinate_line.ini'):

                    os.remove('co_ordinate_rect.ini')
                    os.remove('co_ordinate_line.ini')

                # print("File Removed!")
        cap.release()
        cv2.destroyAllWindows()
    else:
        print("exiting")




