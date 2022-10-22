import pywhatkit as pw
txt = """ Validation of a phone number: 
A simple python program, to check whether a given phone number is valid or not 
(e.g. it’s in an assigned exchange), and to check whether a given phone number is possible or not
 (e.g. it has the right number of digits). Python3 # valid or not import phonenumbers phone_number 
 = phonenumbers.parse ("+91987654321")   """
pw.text_to_handwriting(txt,"kp_hand.png",[0,0,138])#for red colour [255,0,0]
print("yes")