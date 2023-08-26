from ultralytics import YOLO
import cv2
import cvzone
import math
import openai
from googletrans import Translator

lan=input("enter the language for output:-\n en = english\n hi = hindi\n ja = japanese \n mr = marathi\n")
cap=cv2.imread("6.jpg")
cv2.imshow("leaf",cap)
cv2.waitKey(0)

model = YOLO("best.pt")

classNames = ['Apple Scab Leaf', 'Apple leaf', 'Apple rust leaf', 'Bell_pepper leaf spot', 'Bell_pepper leaf', 'Blueberry leaf', 'Cherry leaf', 'Corn Gray leaf spot',
              'Corn leaf blight', 'Corn rust leaf', 'Peach leaf', 'Potato leaf early blight', 'Potato leaf late blight', 'Potato leaf', 'Raspberry leaf', 'Soyabean leaf',
              'Soybean leaf', 'Squash Powdery mildew leaf', 'Strawberry leaf', 'Tomato Early blight leaf', 'Tomato Septoria leaf spot', 'Tomato leaf bacterial spot', 'Tomato leaf late blight', 'Tomato leaf mosaic virus',
              'Tomato leaf yellow virus', 'Tomato leaf', 'Tomato mold leaf', 'Tomato two spotted spider mites leaf', 'grape leaf black rot', 'grape leaf']



results = model('6.jpg')
for r in results:
    boxes = r.boxes
    for box in boxes:

        # Confidence
        conf = math.ceil((box.conf[0] * 100)) / 100
        # Class Name
        cls = int(box.cls[0])
        currentClass = classNames[cls]
        print(currentClass)
        str=currentClass

str="how to treat"+str
openai.api_key = "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"


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": str},
        ]
)

result = ''
for choice in response.choices:
    result += choice.message.content


translator=Translator()
text1=translator.translate(result,src='en',dest=lan)
print("\n")
print(text1.text)


