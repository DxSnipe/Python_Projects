import pywhatkit as pw

txt=input("Enter the text: ")
pw.text_to_handwriting(txt,rgb=[0,0,138])
print("Handwritten text is ready!")