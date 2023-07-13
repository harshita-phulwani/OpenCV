import cv2

img_file = "img6.jpg"

classifier_file ="cars.xml "  #pre-trained car classifier

img=cv2.imread(img_file) #creates an opencv img

bnw =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #convert into grayscale (needed for haarcascade)

car_tracker =cv2.CascadeClassifier(classifier_file)  #create car classifier

cars = car_tracker.detectMultiScale(bnw)  #detect all cars
print (cars)

for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w, y+h), (0,255,0),2)

cv2.imshow("My Car Detector", img)

cv2.waitKey()

print("Successful")