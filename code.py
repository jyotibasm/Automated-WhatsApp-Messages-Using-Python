import pywhatkit as pwk
import pandas as pd
from datetime import datetime

'''Getting Time(Hour & Minute)'''
# Get the current date and time
current_time = datetime.now()

# Extract hour and minute
hour = current_time.hour
minute = current_time.minute


'''Reading Data From Dataset (Excel), using Pandas'''
data = pd.read_excel("contract_details.xlsx")
print(data) #data from dataset
mylist = list(data.loc[:,"Phone"])

count = 1;
for i in mylist:
    # using Exception Handling to avoid unexpected errors 
    try:
        # Send a Message to 'i'th phone in dataframe 
        pwk.sendwhatmsg("+91"+str(i), "Hi, how are you?", hour,minute+count)
        count+=1
        # Send an Image to a Contact with the no Caption
        pwk.sendwhats_image("+91"+str(i), "hello.jpeg")
        print("Message Sent!") #Prints success message in console
        
    # error message
    except:
        print("Error in sending the message")  