import cv2
import cv2.aruco as aruco
import os


def detect_aruco_marker(frame, marker_id):
    # Convert the frame to grayscale for marker detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Define the ArUco dictionary
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

    # Define the parameters for marker detection
    parameters = aruco.DetectorParameters_create()

    # Detect the specified ArUco marker
    corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    # Find the index of the specified marker ID in the detected IDs
    if marker_id in ids:
        index = np.where(ids == marker_id)[0][0]
        corner = corners[index]
        return corner

    return None


vid = cv2.VideoCapture(0)
color = (0, 200, 0)
save_directory = r"C:\Users\ved.thakare\OneDrive - University of Virginia\Documents\aruco markers"  # Specify the directory to save the ArUco marker
marker_id = 42  # Specify the ID of the ArUco marker to detect and save

while True:
    ret, frame = vid.read()

    # Detect the specified ArUco marker in the frame
    corner = detect_aruco_marker(frame, marker_id)

    if corner is not None:
        # Draw a rectangle around the detected marker
        aruco.drawDetectedMarkers(frame, corner)

        # Save the marker image to the specified directory
        marker_filename = os.path.join(save_directory, f"marker_{marker_id}.jpg")
        cv2.imwrite(marker_filename, frame)
        print(f"Saved marker {marker_id} to {marker_filename}")

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()