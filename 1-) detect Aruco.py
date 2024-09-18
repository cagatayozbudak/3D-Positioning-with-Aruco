import cv2
import cv2.aruco as aruco

# Kamera başlatma
cap = cv2.VideoCapture(0)

# 5x5 ArUco dictionary
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_5X5_50)
parameters = aruco.DetectorParameters()



if not cap.isOpened():
    print("Kamera açılamıyor.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Kare okunamadı!")
            break

        # Görüntüyü griye çevir
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Marker'ları tespit et
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

       
        if ids is not None:
            # Tespit edilen marker'ları görselleştir
            aruco.drawDetectedMarkers(frame, corners, ids)

        # Sonuçları göster
        cv2.imshow('ArUco Marker Tespiti', frame)

        # 'q' tuşuna basıldığında çık
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
