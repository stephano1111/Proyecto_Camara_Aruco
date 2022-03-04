import cv2
import numpy as np
import cv2.aruco as aruco 
import math

capture = cv2.VideoCapture(0)
qrCodeDetector=cv2.aruco

points = np.arange(8).reshape(4,2)
MidP = np.arange(2).reshape(1,2)
Y = np.arange(2).reshape(1,2)
X = np.arange(2).reshape(1,2)

#Main
#----------------------------------------------------------------------------
while (True):
  ret, frame =capture.read()
  if ret == False:
    break  #Por si acaso no detecta nada 
  frame=cv2.resize(frame,(2040,1080)) #Cambiar el tamaño de la ventana que despliega
  window_name='Hola' #Nombre de la ventana
  gray = cv2.cvtColor (frame, cv2.COLOR_BGR2GRAY)
  arucoDict= cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)
  arucoParams= cv2.aruco.DetectorParameters_create()
  points,ids,rejected=qrCodeDetector.detectMarkers(gray, arucoDict,parameters=arucoParams)
    
  if len(points)>0:
   
    # flatten the ArUco IDs list
    ids = ids.flatten()
    # loop over the detected ArUCo corners
    for (markerCorner, markerID) in zip(points, ids):
      	# extract the marker corners (which are always returned in
	    	# top-left, top-right, bottom-right, and bottom-left order)
        corners = markerCorner.reshape((4, 2))
        (topLeft, topRight, bottomRight, bottomLeft) = corners
        # convert each of the (x, y)-coordinate pairs to integers
        topRight = (int(topRight[0]), int(topRight[1]))
        bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
        bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
        topLeft = (int(topLeft[0]), int(topLeft[1]))
        # draw the bounding box of the ArUCo detection

        #Se dibuja el cuadrado 
        cv2.line(frame, topLeft, topRight, (0, 255, 0), 2)
        cv2.line(frame, topRight, bottomRight, (0, 255, 0), 2)
        cv2.line(frame, bottomRight, bottomLeft, (0, 255, 0), 2)
        cv2.line(frame, bottomLeft, topLeft, (0, 255, 0), 2)

        #Obtenemos coordenadas para punto medio y lineas
        MidP[0][0]=(topRight[0]+bottomLeft[0])/2
        MidP[0][1]=(topRight[1]+bottomLeft[1])/2
        Y[0][0]=(topRight[0]+bottomRight[0])/2
        Y[0][1]=(topRight[1]+bottomRight[1])/2
        X[0][0]=(bottomLeft[0]+bottomRight[0])/2
        X[0][1]=(bottomLeft[1]+bottomRight[1])/2

        #Se dibujan las lineas 
        line_thickness =3
        cv2.line(frame, X[0], MidP[0], (0, 0, 255), thickness=line_thickness )
        cv2.line(frame, Y[0], MidP[0], (255, 0, 0), thickness=line_thickness )

        #Se imprime la información del texto 
        cv2.putText(frame, str(MidP[0]), (MidP[0][0], MidP[0][1]-200),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,204,204),2,cv2.LINE_AA )
        cv2.putText(frame, str(f'ID: {markerID}'), (MidP[0][0]-150, MidP[0][1]-200),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,204,204),2,cv2.LINE_AA )
        
        #Calculamos el angulo de inclinación 

        x = (bottomRight[0]-bottomLeft[0])
        y = (bottomRight[1]-bottomLeft[1])
        # Pend= bottomRight[1]-bottomLeft[1]/bottomRight[0]-bottomLeft[0]
        Angulo = math.atan2(y,x)
        Angulo = math.degrees(Angulo)
        #Angulo = round(Angulo)
        Angulo= Angulo *-1
        cv2.putText(frame, str(Angulo), (MidP[0][0]-600, MidP[0][1]-200),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,204,204),2,cv2.LINE_AA )
        



  cv2.imshow(window_name,frame) #Despliega la ventana 
  cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1) #Aparece al frente de otras ventanas
    
  if cv2.waitKey(1) & 0xFF == 27: #Presiona esc para salir 
    break

capture.release()
cv2.destroyAllWindows()