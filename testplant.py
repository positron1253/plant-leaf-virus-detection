from ultralytics import YOLO
import cv2
import cvzone
import math
# import openai
from googletrans import Translator

lan=input("enter the language for output:-\n en = english\n hi = hindi\n ja = japanese \n mr = marathi\n")
cap=cv2.imread("6.jpg")
# cv2.imshow("leaf",cap)
cv2.waitKey(0)

model = YOLO("best.pt")
myColor = (0, 0, 255)
str=""

classNames = ['Apple Scab Leaf', 'Apple leaf', 'Apple rust leaf', 'Bell_pepper leaf spot', 'Bell_pepper leaf', 'Blueberry leaf', 'Cherry leaf', 'Corn Gray leaf spot',
              'Corn leaf blight', 'Corn rust leaf', 'Peach leaf', 'Potato leaf early blight', 'Potato leaf late blight', 'Potato leaf', 'Raspberry leaf', 'Soyabean leaf',
              'Soybean leaf', 'Squash Powdery mildew leaf', 'Strawberry leaf', 'Tomato Early blight leaf', 'Tomato Septoria leaf spot', 'Tomato leaf bacterial spot', 'Tomato leaf late blight', 'Tomato leaf mosaic virus',
              'Tomato leaf yellow virus', 'Tomato leaf', 'Tomato mold leaf', 'Tomato two spotted spider mites leaf', 'grape leaf black rot', 'grape leaf']


img=r"C:\Users\ASUS\Downloads\download.jpg"
img=cv2.imread(img)
results = model(img)

for r in results:
    boxes = r.boxes
    for box in boxes:
        # Bounding Box
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
        w, h = x2 - x1, y2 - y1
        print(x1,y1,x2,y2)
        # print(currentClass)
        # cvzone.cornerRect(img, (x1, y1, w, h))

        # Confidence
        conf = math.ceil((box.conf[0] * 100)) / 100
        print(conf)
        # Class Name
        cls = int(box.cls[0])
        currentClass = classNames[cls]
        print(currentClass)
        if conf > 0.2:
            str = currentClass
            if currentClass == 'Tomato leaf' or currentClass == 'Soybean leaf' or currentClass == 'Potato leaf' or currentClass == 'Apple leaf':
                myColor = (0, 255, 0)

            else:
                myColor = (255, 0, 0)

            cvzone.putTextRect(img, f'{classNames[cls]} {conf}',
                               (max(0, x1), max(35, y1)), scale=1, thickness=1, colorB=myColor,
                               colorT=(255, 255, 255), colorR=myColor, offset=5)
            cv2.rectangle(img, (x1, y1), (x2, y2), myColor, 3)
            str = currentClass

    cv2.imshow("Image", img)
    cv2.waitKey(0)
# str="how to treat"+str
# openai.api_key = "**********************************"
#
#
# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#             {"role": "system", "content": "You are a chatbot"},
#             {"role": "user", "content": str},
#         ]
# )
#
# result = ''
# for choice in response.choices:
#     result += choice.message.content
#
#
# translator=Translator()
# text1=translator.translate(result,src='en',dest=lan)
# print("\n")
# print(text1.text)


