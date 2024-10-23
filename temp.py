import cv2

def list_available_cameras():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        print(index)
        if not cap.isOpened():
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr

if __name__ == "__main__":
    camera_indices = list_available_cameras()
    print("사용 가능한 카메라 인덱스:", camera_indices)