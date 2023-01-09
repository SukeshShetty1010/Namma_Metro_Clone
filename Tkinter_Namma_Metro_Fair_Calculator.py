import base64
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
import mimetypes
import pickle
import os
from apiclient import errors
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

root = Tk()
root.title("Namma Metro Fair Calculator")
root.geometry("700x400")
root.config(bg="Purple")
image1 = ImageTk.PhotoImage(Image.open("C:/Users/sukes/Downloads/images.png"))
root.iconphoto(False, image1)

title1 = Label(root, text = "                         Namma Metro Fair Calculator",font=("Arial", 20),bg="Purple", fg="White")
title1.grid(row=0, column=0, columnspan=3)

mylabel1 = Label(root, text = "        ",font=("Arial", 15),bg="Purple")
mylabel1.grid(row=1, column=0)

boarding_station_label = Label(root, text = "          Select the boarding station",font=("Arial", 15),bg="Purple", fg="White")
boarding_station_label.grid(row=2, column=0)

boarding_station = StringVar()
boarding_station.set("Nagasandra")
station_name = ["Nagasandra", "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya", "Goraguntepalya", "Yeshwanthpur", "Sandal Soap Factory", "Mahalakshmi", "Rajajinagar", "Mahakavi Kuvempu Road", "Srirampura", "Sampige Road", "Majestic", "Chikpete", "Krishna Rajendra Market", "National College", "Lalbagh Botanical Garden", "South End Circle", "Jayanagar", "Rashtreeya Vidyalaya Road", "Banashankari", "Jaya Prakash Nagar", "Yelachenahalli", "Konanakunte Cross", "Doddakallasandra", "Vajarahalli", "Thalaghattapura", "Silk Institute", "Kengeri", "Kengeri Bus Terminal", "Pattanagere", "Jnanabharathi", "Rajarajeshwari Nagar", "Nayandahalli", "Mysuru Road", "Deepanjali Nagara", "Attiguppe", "Vijayanagara", "Balagangadhara Natha Swamiji HOS", "Magadi Road", "City Railway Station", "Majestic","Sir M. Visveshwaraya Station", "Dr BR Ambedkar Vidhana Soudha", "Cubbon Park Sri Chamarajendra Park", "MG Road","Trinity", "Halasuru", "Indiranagara", "Swami Vivekananda Road", "Baiyappanahalli"]
boarding_station_dropdown_menu = OptionMenu(root, boarding_station, *station_name)
boarding_station_dropdown_menu.config(bg="Purple", fg="WHITE", height=2)
boarding_station_dropdown_menu.grid(row=2, column=1)

mylabel2 = Label(root, text = "    ",font=("Arial", 15),bg="Purple")
mylabel2.grid(row=3, column=0)

departure_station_label = Label(root, text = "          Select the departure station",font=("Arial", 15),bg="Purple", fg="White")
departure_station_label.grid(row=4, column=0)

departure_station = StringVar()
departure_station.set("Nagasandra")
departure_station_dropdown_menu = OptionMenu(root, departure_station, *station_name)
departure_station_dropdown_menu.config(bg="Purple", fg="WHITE", height=2)
departure_station_dropdown_menu.grid(row=4, column=1)

mylabel3 = Label(root, text = "    ",font=("Arial", 15),bg="Purple")
mylabel3.grid(row=5, column=0)

Green_line = ["Nagasandra", "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya", "Goraguntepalya", "Yeshwanthpur", "Sandal Soap Factory", "Mahalakshmi", "Rajajinagar","Mahakavi Kuvempu Road", "Srirampura","Sampige Road","Majestic","Chikpete","Krishna Rajendra Market","National College","Lalbagh Botanical Garden","South End Circle","Jayanagar","Rashtreeya Vidyalaya Road","Banashankari","Jaya Prakash Nagar","Yelachenahalli","Konanakunte Cross","Doddakallasandra","Vajarahalli","Thalaghattapura","Silk Institute"]
Purple_line = ["Kengeri","Kengeri Bus Terminal","Pattanagere","Jnanabharathi","Rajarajeshwari Nagar","Nayandahalli","Mysuru Road","Deepanjali Nagara","Attiguppe"," Vijayanagara","Balagangadhara Natha Swamiji HOS","Magadi Road","City Railway Station","Majestic","Sir M. Visveshwaraya Station","Dr BR Ambedkar Vidhana Soudha","Cubbon Park Sri Chamarajendra Park","MG Road","Trinity","Halasuru","Indiranagara","Swami Vivekananda Road","Baiyappanahalli"]

mylabel5 = Label(root, text = " ",font=("Arial", 15),bg="Purple")
mylabel5.grid(row=5, column=0)

mylabel5 = Label(root, text = "Enter your Email",font=("Arial", 15),bg="Purple", fg="White")
mylabel5.grid(row=6, column=0)

email_entry = Entry(root, width= 40, bg = "White", fg = "Black")
email_entry.grid(row=6, column=1)

def check_me():
    global email_entry
    global boarding_station
    global departure_station
    global Green_line
    global Purple_line
    global station_name
    new_window = Toplevel()
    new_window.geometry("500x600")
    new_window.config(bg="Purple")
    new_window.title("Namma Metro Fair Calculator")
    image1 = ImageTk.PhotoImage(Image.open("C:/Users/sukes/Downloads/images.png"))
    new_window.iconphoto(False, image1)
    title1 = Label(new_window, text = "            Namma Metro Fair Calculator",font=("Arial", 20),bg="Purple", fg="White")
    title1.grid(row=1, column=0, columnspan=3)

    if "@" not in email_entry.get():
        warning_message = messagebox.showwarning("Warning", "Please enter a valid email")

    if ((boarding_station.get() in Green_line and departure_station.get() in Green_line) or (boarding_station.get() in Purple_line and departure_station.get() in Purple_line)):
        no_of_stops = abs(station_name.index(boarding_station.get()) - station_name.index(departure_station.get())) - 1

    if (boarding_station.get() in Green_line and departure_station.get() in Purple_line):
        no_of_stops = abs( abs(Green_line.index("Majestic") - Green_line.index(boarding_station.get())) + abs(Purple_line.index("Majestic") - Purple_line.index(departure_station.get())) -1 )

    if (boarding_station.get() in Purple_line and departure_station.get() in Green_line):
        no_of_stops = abs( abs(Purple_line.index("Majestic") - Purple_line.index(boarding_station.get())) + abs(Green_line.index("Majestic") - Green_line.index(departure_station.get())) -1 )
    
    if no_of_stops == -1:
        response= messagebox.showwarning("Warning", "The boarding and departure station are the same")
        new_window.destroy()
    if no_of_stops == 0:
        price = 5
    if no_of_stops == 1:
        price = 9
    if no_of_stops == 2:
        price = 14
    if no_of_stops == 3:
        price = 18
    if no_of_stops > 3:
        price = 18 + (no_of_stops - 3)*2
    if departure_station.get() == "Majestic":
        price = price + 1
    
    mylabel6 = Label(new_window, text = "        ",font=("Arial", 15),bg="Purple")
    mylabel6.grid(row=2, column=0)

    boarding_station_label = Label(new_window, text = "          Boarding station : " + boarding_station.get(),font=("Arial", 15),bg="Purple", fg="White")
    boarding_station_label.grid(row=3, column=0)

    mylabel7 = Label(new_window, text = "    ",font=("Arial", 15),bg="Purple")
    mylabel7.grid(row=4, column=0)

    departure_station_label = Label(new_window, text = "          Departure station : " + departure_station.get(),font=("Arial", 15),bg="Purple", fg="White")
    departure_station_label.grid(row=5, column=0)

    mylabel8 = Label(new_window, text = "    ",font=("Arial", 15),bg="Purple")
    mylabel8.grid(row=6, column=0)

    no_of_stops_label = Label(new_window, text = "          No of Stops : " + str(no_of_stops),font=("Arial", 15),bg="Purple", fg="White")
    no_of_stops_label.grid(row=7, column=0)

    mylabel9 = Label(new_window, text = "    ",font=("Arial", 15),bg="Purple")
    mylabel9.grid(row=8, column=0)

    no_of_stops_label = Label(new_window, text = "          Price : " + str(price),font=("Arial", 15),bg="Purple", fg="White")
    no_of_stops_label.grid(row=9, column=0)

    mylabel9 = Label(new_window, text = "    ",font=("Arial", 15),bg="Purple")
    mylabel9.grid(row=10, column=0)

    no_of_stops_label = Label(new_window, text = "Route" ,font=("Arial", 15),bg="Purple", fg="White")
    no_of_stops_label.grid(row=11, column=0)

    mylabel9 = Label(new_window, text = "    ",font=("Arial", 15),bg="Purple")
    mylabel9.grid(row=12, column=0)

    route = []
    to_reverse = []

    if ((boarding_station.get() in Green_line and departure_station.get() in Green_line) or (boarding_station.get() in Purple_line and departure_station.get() in Purple_line)):
        if station_name.index(boarding_station.get()) < station_name.index(departure_station.get()):
            for i in range((station_name.index(boarding_station.get())), (station_name.index(departure_station.get())+1)):
                route.append(station_name[i])

        if station_name.index(boarding_station.get()) > station_name.index(departure_station.get()):
            for i in range((station_name.index(boarding_station.get())), (station_name.index(departure_station.get())-1), -1):
                route.append(station_name[i])
    
    if (boarding_station.get() in Green_line and departure_station.get() in Purple_line):
        if Green_line.index(boarding_station.get()) < Green_line.index("Majestic"):
            for i in range((Green_line.index(boarding_station.get())), Green_line.index("Majestic")):
                route.append(Green_line[i])
        
        if Green_line.index(boarding_station.get()) > Green_line.index("Majestic"):
            for i in range((Green_line.index(boarding_station.get())), Green_line.index("Majestic"), -1):
                route.append(Green_line[i])

        if Purple_line.index(departure_station.get()) < Purple_line.index("Majestic"):
            for i in range((Purple_line.index(departure_station.get())), (Purple_line.index("Majestic")+1)):
                to_reverse.append(Purple_line[i])
        
        if Purple_line.index(departure_station.get()) > Purple_line.index("Majestic"):
            for i in range((Purple_line.index(departure_station.get())), (Purple_line.index("Majestic")-1), -1):
                to_reverse.append(Purple_line[i])
    
    if (boarding_station.get() in Purple_line and departure_station.get() in Green_line):
        if Purple_line.index(boarding_station.get()) < Purple_line.index("Majestic"):
            for i in range((Purple_line.index(boarding_station.get())), Purple_line.index("Majestic")):
                route.append(Purple_line[i])
        
        if Purple_line.index(boarding_station.get()) > Purple_line.index("Majestic"):
            for i in range((Purple_line.index(boarding_station.get())), Purple_line.index("Majestic"), -1):
                route.append(Purple_line[i])

        if Green_line.index(departure_station.get()) < Green_line.index("Majestic"):
            for i in range((Green_line.index(departure_station.get())), (Green_line.index("Majestic")+1)):
                to_reverse.append(Green_line[i])
        
        if Green_line.index(departure_station.get()) > Green_line.index("Majestic"):
            for i in range((Green_line.index(departure_station.get())), (Green_line.index("Majestic")-1), -1):
                to_reverse.append(Green_line[i])

    
    to_reverse.reverse()
    route = route + to_reverse
    for i in range(len(route)):
        no_of_stops_label = Label(new_window, text = route[i] ,font=("Arial", 15),bg="Purple", fg="White")
        no_of_stops_label.grid(row=i+13, column=0)

    Back_button = Button(new_window, text="Go Back", command=new_window.destroy, fg="Green", font=("Arial", 15))
    Back_button.grid(row=110, column=0)

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sukesh",
    database="namma_metro"
    )

    mycursor = mydb.cursor()

    sql_command = "INSERT INTO no_of_people (boarding_station, departure_station) VALUES (%s, %s)"
    sql_value = (boarding_station.get(), departure_station.get())
    mycursor.execute(sql_command, sql_value)

    mydb.commit()

    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://mail.google.com/']


    def get_service():
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('gmail', 'v1', credentials=creds)

        return service

    def send_message(service, user_id, message):
        try:
            message = service.users().messages().send(userId=user_id,
                    body=message).execute()

            print('Message Id: {}'.format(message['id']))

            return message
        except Exception as e:
            print('An error occurred: {}'.format(e))
            return None


    def create_message_with_attachment(
        sender,
        to,
        subject,
        message_text,
        file,
        ):
        message = MIMEMultipart()
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject

        msg = MIMEText(message_text)
        message.attach(msg)

        (content_type, encoding) = mimetypes.guess_type(file)

        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'

        (main_type, sub_type) = content_type.split('/', 1)

        if main_type == 'text':
            with open(file, 'rb') as f:
                msg = MIMEText(f.read().decode('utf-8'), _subtype=sub_type)

        elif main_type == 'image':
            with open(file, 'rb') as f:
                msg = MIMEImage(f.read(), _subtype=sub_type)
            
        elif main_type == 'audio':
            with open(file, 'rb') as f:
                msg = MIMEAudio(f.read(), _subtype=sub_type)
            
        else:
            with open(file, 'rb') as f:
                msg = MIMEBase(main_type, sub_type)
                msg.set_payload(f.read())

        filename = os.path.basename(file)
        msg.add_header('Content-Disposition', 'attachment',
                    filename=filename)
        message.attach(msg)

        raw_message = \
            base64.urlsafe_b64encode(message.as_string().encode('utf-8'))
        return {'raw': raw_message.decode('utf-8')}
    

    if __name__ == "__main__":
        service = get_service()
        user_id = 'me'
        msg = create_message_with_attachment('globaldeveloperconsortium@gmail.com', 
        email_entry.get(), 
        'Metro Ticket Details',
        "The no of stops and price for your metro ticket from " + boarding_station.get() + " to " + departure_station.get() + " are " + str(no_of_stops) + " stops and " + str(price) + " ruppes respectively. You can pay the price by scanning the QR code attached below.", 
        './QR_code.jpg')
        send_message(service, user_id, msg)


def stats():
    stat_window = Toplevel()
    stat_window.geometry("500x350")
    stat_window.config(bg="Purple")
    stat_window.title("Namma Metro Fair Calculator")
    image1 = ImageTk.PhotoImage(Image.open("C:/Users/sukes/Downloads/images.png"))
    stat_window.iconphoto(False, image1)
    title1 = Label(stat_window, text = "            Namma Metro Fair Calculator",font=("Arial", 20),bg="Purple", fg="White")
    title1.grid(row=1, column=0, columnspan=3)

    mylabel9 = Label(stat_window, text = "    ",font=("Arial", 15),bg="Purple")
    mylabel9.grid(row=2, column=0)

    station_stat_label = Label(stat_window, text = "          Enter the station name: ",font=("Arial", 15),bg="Purple", fg="White")
    station_stat_label.grid(row=3, column=0)

    mylabel9 = Label(stat_window, text = "    ",font=("Arial", 15),bg="Purple")
    mylabel9.grid(row=4, column=0)

    station_name = ["All","Nagasandra", "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya", "Goraguntepalya", "Yeshwanthpur", "Sandal Soap Factory", "Mahalakshmi", "Rajajinagar", "Mahakavi Kuvempu Road", "Srirampura", "Sampige Road", "Majestic", "Chikpete", "Krishna Rajendra Market", "National College", "Lalbagh Botanical Garden", "South End Circle", "Jayanagar", "Rashtreeya Vidyalaya Road", "Banashankari", "Jaya Prakash Nagar", "Yelachenahalli", "Konanakunte Cross", "Doddakallasandra", "Vajarahalli", "Thalaghattapura", "Silk Institute", "Kengeri", "Kengeri Bus Terminal", "Pattanagere", "Jnanabharathi", "Rajarajeshwari Nagar", "Nayandahalli", "Mysuru Road", "Deepanjali Nagara", "Attiguppe", "Vijayanagara", "Balagangadhara Natha Swamiji HOS", "Magadi Road", "City Railway Station", "Majestic","Sir M. Visveshwaraya Station", "Dr BR Ambedkar Vidhana Soudha", "Cubbon Park Sri Chamarajendra Park", "MG Road","Trinity", "Halasuru", "Indiranagara", "Swami Vivekananda Road", "Baiyappanahalli"]

    station_stat = StringVar()
    station_stat.set("All")
    station_stat_dropdown_menu = OptionMenu(stat_window, station_stat, *station_name)
    station_stat_dropdown_menu.config(bg="Purple", fg="WHITE", height=2)
    station_stat_dropdown_menu.grid(row=3, column=1)

    mylabel5 = Label(stat_window, text = " ",font=("Arial", 15),bg="Purple")
    mylabel5.grid(row=5, column=0)

    def acquire_stats():
        acquire_stats_window = Toplevel()
        acquire_stats_window.geometry("500x350")
        acquire_stats_window.config(bg="Purple")
        acquire_stats_window.title("Namma Metro Fair Calculator")
        image1 = ImageTk.PhotoImage(Image.open("C:/Users/sukes/Downloads/images.png"))
        acquire_stats_window.iconphoto(False, image1)
        title1 = Label(acquire_stats_window, text = "            Namma Metro Fair Calculator",font=("Arial", 20),bg="Purple", fg="White")
        title1.grid(row=1, column=0, columnspan=3)

        if station_stat.get() == "All":

            def came_stats():
                came_stats_window = Toplevel()
                came_stats_window.geometry("500x350")
                came_stats_window.config(bg="Purple")
                came_stats_window.title("Namma Metro Fair Calculator")
                image1 = ImageTk.PhotoImage(Image.open("C:/Users/sukes/Downloads/images.png"))
                came_stats_window.iconphoto(False, image1)
                title1 = Label(came_stats_window, text = "            Namma Metro Fair Calculator",font=("Arial", 20),bg="Purple", fg="White")
                title1.grid(row=1, column=0, columnspan=3)

                mylabel9 = Label(came_stats_window, text = "    ",font=("Arial", 15),bg="Purple")
                mylabel9.grid(row=2, column=0)

                station_stat_label = Label(came_stats_window, text = "          No of people came to the station ",font=("Arial", 15),bg="Purple", fg="White")
                station_stat_label.grid(row=3, column=0)

                mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sukesh",
                database="namma_metro"
                )

                mycursor = mydb.cursor()
                mycursor.execute("select departure_station, count(*) as count FROM no_of_people GROUP BY departure_station")

                i=0 
                for no_of_people in mycursor: 
                    for j in range(len(no_of_people)):
                        e = Entry(came_stats_window, width=20, fg='White', bg="Purple", font=("Arial", 15))
                        e.grid(row=i+4, column=j) 
                        e.insert(END, no_of_people[j])
                    i=i+1
            
            def left_stats():
                left_stats_window = Toplevel()
                left_stats_window.geometry("500x350")
                left_stats_window.config(bg="Purple")
                left_stats_window.title("Namma Metro Fair Calculator")
                image1 = ImageTk.PhotoImage(Image.open("C:/Users/sukes/Downloads/images.png"))
                left_stats_window.iconphoto(False, image1)
                title1 = Label(left_stats_window, text = "            Namma Metro Fair Calculator",font=("Arial", 20),bg="Purple", fg="White")
                title1.grid(row=1, column=0, columnspan=3)

                mylabel9 = Label(left_stats_window, text = "    ",font=("Arial", 15),bg="Purple")
                mylabel9.grid(row=2, column=0)

                station_stat_label = Label(left_stats_window, text = "          No of people left to the station ",font=("Arial", 15),bg="Purple", fg="White")
                station_stat_label.grid(row=3, column=0)

                mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sukesh",
                database="namma_metro"
                )

                mycursor = mydb.cursor()
                mycursor.execute("select boarding_station, count(*) as count FROM no_of_people GROUP BY boarding_station")

                i=0 
                for no_of_people in mycursor: 
                    for j in range(len(no_of_people)):
                        e = Entry(left_stats_window, width=20, fg='White', bg="Purple", font=("Arial", 15))
                        e.grid(row=i+4, column=j) 
                        e.insert(END, no_of_people[j])
                    i=i+1

            mylabel9 = Label(acquire_stats_window, text = "    ",font=("Arial", 15),bg="Purple")
            mylabel9.grid(row=2, column=0)

            station_stat_label = Label(acquire_stats_window, text = "          No of people came to the station ",font=("Arial", 15),bg="Purple", fg="White")
            station_stat_label.grid(row=3, column=0)

            btn = Button(acquire_stats_window, text="Give Stats", command=came_stats, fg="Green", font=("Arial", 15))
            btn.grid(row=3, column=1)

            mylabel9 = Label(acquire_stats_window, text = "    ",font=("Arial", 15),bg="Purple")
            mylabel9.grid(row=4, column=0)

            station_stat_label = Label(acquire_stats_window, text = "          No of people left to the station ",font=("Arial", 15),bg="Purple", fg="White")
            station_stat_label.grid(row=5, column=0)

            btn = Button(acquire_stats_window, text="Give Stats", command=left_stats, fg="Green", font=("Arial", 15))
            btn.grid(row=5, column=1)
        
        if station_stat.get() != "All":
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sukesh",
            database="namma_metro"
            )

            mycursor = mydb.cursor()

            sql_command = "select count(departure_station) from no_of_people where departure_station = %s"
            sql_value = [station_stat.get()]
            mycursor.execute(sql_command, sql_value)

            i=0 
            for no_of_people in mycursor: 
                for j in range(len(no_of_people)):
                    demo_window = Toplevel()
                    e = Entry(demo_window, width=20, fg='White', bg="Purple", font=("Arial", 15))
                    e.grid(row=i+4, column=j) 
                    e.insert(END, no_of_people[j])
                    demo_window.destroy()
                i=i+1

            mylabel5 = Label(acquire_stats_window, text = " ",font=("Arial", 15),bg="Purple")
            mylabel5.grid(row=2, column=0)

            station_stat_label = Label(acquire_stats_window, text = "           No of people left to "+station_stat.get()+" are "+ str(no_of_people[0]),font=("Arial", 15),bg="Purple", fg="White")
            station_stat_label.grid(row=3, column=0)

            sql_command = "select count(boarding_station) from no_of_people where boarding_station = %s"
            sql_value = [station_stat.get()]
            mycursor.execute(sql_command, sql_value)

            i=0 
            for no_of_people in mycursor: 
                for j in range(len(no_of_people)):
                    demo_window = Toplevel()
                    e = Entry(demo_window, width=20, fg='White', bg="Purple", font=("Arial", 15))
                    e.grid(row=i+4, column=j) 
                    e.insert(END, no_of_people[j])
                    demo_window.destroy()
                i=i+1

            mylabel5 = Label(acquire_stats_window, text = " ",font=("Arial", 15),bg="Purple")
            mylabel5.grid(row=4, column=0)

            station_stat_label = Label(acquire_stats_window, text = "           No of people came to "+station_stat.get()+" are "+ str(no_of_people[0]),font=("Arial", 15),bg="Purple", fg="White")
            station_stat_label.grid(row=5, column=0)

            

    btn = Button(stat_window, text="Give Stats", command=acquire_stats, fg="Green", font=("Arial", 15))
    btn.grid(row=8, column=1)

mylabel5 = Label(root, text = " ",font=("Arial", 15),bg="Purple")
mylabel5.grid(row=7, column=0)

btn = Button(root, text="Results !!", command=check_me, fg="Green", font=("Arial", 15))
btn.grid(row=8, column=1)

mylabel5 = Label(root, text = " ",font=("Arial", 15),bg="Purple")
mylabel5.grid(row=9, column=0)

btn = Button(root, text="Stats", command=stats, fg="Green", font=("Arial", 15))
btn.grid(row=10, column=1)

root.mainloop()