import cv2
import cv2.aruco as aruco
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


# Kamera başlatma
cap = cv2.VideoCapture(0)
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_5X5_50)
parameters = aruco.DetectorParameters()

#Kalibrasyon 
cameraMatrix = np.array([[1000, 0, 320], [0, 1000, 240], [0, 0, 1]], dtype=float)
distCoeffs = np.zeros((4, 1))  # Distorsiyon katsayıları varsayılan olarak sıfır

# 3D görselleştirme için matplotlib ayarları
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

def update(frame):
    ret, img = cap.read()
    if not ret:
        print("Kamera okuması başarısız.")
        return  # Okuma başarısız olduğunda döngüden çıkmak yerine sadece dönüş yapılıyor.

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    if ids is not None:
        rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners[0], 0.05, cameraMatrix, distCoeffs)
        rotation_matrix, _ = cv2.Rodrigues(rvec)
        ax.clear()
        draw_cube(ax, rotation_matrix)

def draw_cube(ax, rotation_matrix):
    points = np.array([[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
                       [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]])
    for i, point in enumerate(points):
        for j in range(i+1, len(points)):
            if np.sum(np.abs(point - points[j])) == 2:
                start_point = np.dot(rotation_matrix, point)
                end_point = np.dot(rotation_matrix, points[j])
                ax.plot([start_point[0], end_point[0]], [start_point[1], end_point[1]], [start_point[2], end_point[2]], 'b-')

ani = FuncAnimation(fig, update, frames=np.arange(0, 2000, 1), interval=50, repeat=True)
plt.show()


#Preference'dan Qt5'ı açarak diamik plot'u açmanız gerekmektedir. Aksi taktirde kod çalışmaz.