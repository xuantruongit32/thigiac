import cv2
import cvzone
import numpy as np
import os

width, height = 1920, 1080

cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Menu options
options = ["1: QA Game", "2: Flight Time", "3: Country Name"]
selected_option = None
exit_menu = False  # Flag to exit the menu loop

def create_main_menu_overlay(img):
    h, w, _ = img.shape
    imgOverlay = np.zeros((h, w, 3), dtype=np.uint8)
    for i, option in enumerate(options):
        cvzone.putTextRect(imgOverlay, option, (100, 150 + i * 200), scale=5, thickness=5)
    return imgOverlay
def run_program(selected_option):
    try:
        cap.release()  # Release the camera resource
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script

        if selected_option == "1: QA Game":
            script_path = os.path.join(script_dir, "qa_game", "qa_game.py")
            os.system(f'python "{script_path}"')
        elif selected_option == "2: Flight Time":
            script_path = os.path.join(script_dir, "flight_time", "flight_time.py")
            os.system(f'python "{script_path}"')
        elif selected_option == "3: Country Name":
            script_path = os.path.join(script_dir, "country_name", "country_name.py")
            os.system(f'python "{script_path}"')
        
        print(f"Running program: {selected_option}")
    except Exception as e:
        print(f"Failed to start subprocess for {selected_option}: {e}")


while not exit_menu:  # Continue looping until exit_menu is True
    success, img = cap.read()
    imgOutput = img.copy()

    imgOverlay = create_main_menu_overlay(imgOutput)
    imgOutput = cv2.addWeighted(imgOutput, 1, imgOverlay, 0.65, 0)

    cv2.imshow("Output Image", imgOutput)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('1'):
        selected_option = options[0]
        print("Option 1 selected")
        exit_menu = True  # Exit the menu loop after selection
    elif key == ord('2'):
        selected_option = options[1]
        print("Option 2 selected")
        exit_menu = True  # Exit the menu loop after selection
    elif key == ord('3'):
        selected_option = options[2]
        print("Option 3 selected")
        exit_menu = True  # Exit the menu loop after selection

    if selected_option:
        run_program(selected_option)
        break

cap.release()
cv2.destroyAllWindows()

