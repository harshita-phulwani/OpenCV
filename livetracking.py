import cv2

img_file = "img6.jpg"

classifier_file ="cars.xml "  #pre-trained car classifier

img=cv2.imread(img_file) #creates an opencv img

car_tracker =cv2.CascadeClassifier(classifier_file)  #create car classifier


webcam =cv2.VideoCapture(0)



while True:
    read_successful, frame = webcam.read()

    if read_successful:
    
        bnw =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #convert into grayscale (needed for haarcascade)

    else:
        break
    
    cars = car_tracker.detectMultiScale(bnw)


  #detect all cars


    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w, y+h), (0,255,0),2)

    cv2.imshow("My Car Detector", frame)

    key =cv2.waitKey(1)
    if key == 81 or key == 113:
        break


webcam.release()
print("Successful") 