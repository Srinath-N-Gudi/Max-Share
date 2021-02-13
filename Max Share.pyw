from tkinter import *
import utils.EasyCode as eg
import os
import time
from tkinter.filedialog import askopenfile
import socket
import threading
cwd = os.getcwd()
os.chdir("C:/")
if not os.path.exists("Max Share"):
    os.mkdir("Max Share")
    os.chdir(os.path.join(os.getcwd(), "Max Share"))
    open("address.sri", 'x')
    open("received.sri", 'x')
else:
    os.chdir(os.path.join(os.getcwd(), "Max Share"))
    if os.path.exists("address.sri"):
        pass
    else:
        open("address.sri", 'x')
    if os.path.exists("received.sri"):
        pass
    else:
        open('received.sri', 'x')
#D:\Programs\Socket In Python\videoplayback.mp4
os.chdir(cwd)
def getSize(filename):
    return os.stat(filename).st_size

class send_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Send")
        self.root.geometry("1080x720+250+50")
        self.root.maxsize(1080, 720)
        self.root.minsize(1080, 720)

        ################## Creating required frames
        # Creating frame 1
        self.frame1 = Frame(self.root, bg="lightgray", bd=5, relief=GROOVE)
        self.frame1.place(x=10, y=10, width=800, height=625)
        # Creating frame 2
        self.frame2 = Frame(self.root, bd=5, relief=GROOVE)
        self.frame2.place(x=820, y=10, width=250, height=625)
        # Creating fram 3
        self.frame3 = Frame(self.root, bd=5, relief=GROOVE)
        self.frame3.place(x=10, y=645, width=1060, height=65)
        ################## Creating the frames are over

        ################# Working with frame 1
        # Creating the labels
        
        ####Creating the filename label####
        self.label1 =  Label(self.frame1, text="File: ", font=("times new roman", 30), bg="lightgray")
        self.label1.place(x=50, y=50)
        ### Creating the invisible lable for file name label
        self.file_label_value = StringVar()
        self.file_label_value.set("")
        self.file_label = Label(self.frame1, bg="lightgray", text="", font=("times new roman", 30))
        self.file_label.place(x=150, y=50)
        # self.frame1.update()
        self.root.update()
        # Creating the extension label
        self.label2 =  Label(self.frame1, text="Extension: ", font=("times new roman", 30), bg="lightgray")
        self.label2.place(x=50, y=150)
        ### Creating the invisible label for the extension name:
        self.ext_label_value = StringVar()
        self.ext_label_value.set("")
        self.ext_label = Label(self.frame1, bg="lightgray", text="", font=("times new roman", 30))

        self.ext_label.place(x=240, y=150)
        # self.frame1.update()
        self.root.update()
        # Creating the label for the size
        self.label3 =  Label(self.frame1, text="Size: ", font=("times new roman", 30), bg="lightgray")
        self.label3.place(x=50, y=250)
        ### Creating the invisible label for the size:
        self.size_label_value = StringVar()
        self.size_label_value.set("")
        self.size_label = Label(self.frame1, bg="lightgray", text="", font=("times new roman", 30))

        self.size_label.place(x=140, y=250)
        # self.frame1.update()
        self.root.update()
        # Creating a label for the status update to the user
        self.status_label_value = StringVar()
        self.status_label_value.set("None")
        self.label4 =  Label(self.frame1, text="None" , font=("times new roman", 10), bg="lightgray")
        self.label4.place(x=0, y=625-35)
        # Creating the size label for showing the size:
        self.label5 = Label(self.frame1, text=f"Sent: ", bg="lightgray")
        self.label5.place(x=0, y=625-50)
        ############ Working with frame2
        # Creating the buttosn required 
        # Creating the connect button
        self.button1 = Button(self.frame3, text="Connect", font=("times new roman", 10), relief=GROOVE, bd=3, command=self.connect)
        self.button1.place(x=20, y=15, width=150)
        # Creating a refresh button
        self.button2 = Button(self.frame3, text="Refresh", font=("times new roman", 10), relief=GROOVE, bd=3, command=self.refresh)
        self.button2.place(x=520, y=15, width=150)
        # Creating a text field for the ip address
        self.ip_field_entry = Entry(self.frame3, font = ("times new roman", 15))
        self.ip_field_entry.place(x=190, y=15, width=300)
        # Creating the browse button 
        self.button3 = Button(self.frame3, text="Browse", font=("times new roman", 10), relief=GROOVE, bd=3, command=self.browse)
        self.button3.place(x=700, y=15, width=150)
        # Creating the send button 
        self.button3 = Button(self.frame3, text="Send", font=("times new roman", 10), relief=GROOVE, bd=3, command=self.send)
        self.button3.place(x=870, y=15, width=150)

        ########### Working with frame 2
        self.list = Listbox(self.frame2)
        self.list.place(x=0,y=0, width=237, height=612)
        with open("C:/Max Share/address.sri", 'r') as file:
            self.addresses = file.read().splitlines()
        if self.addresses != []:
            for address in self.addresses:
                self.list.insert(END, address)
    def refresh(self):
        self.root.update()
        self.label4['text'] = "Refreshing..."
        self.root.update()
        self.list.delete(0, END)
        self.root.update()
        with open("C:/Max Share/address.sri", 'r') as file:
            addresses = file.read().splitlines()
        
        for address in addresses:
            self.list.insert(END, address)
            self.root.update()
            time.sleep(1)
        time.sleep(3)
        self.label4['text'] = "Refresh complete"
        self.root.update()
        time.sleep(1)
        self.label4['text'] = "None"
        self.root.update()
    def browse(self):
        
            self.path = eg.getPath(askopenfile()) 
            if self.path != "":
                name = self.path.split("/")[-1]
                extension = name.split(".")[-1]
                self.acname = name
                self.size = str(getSize(self.path))+" bytes"
                
                self.file_label["text"] = name.split(".")[0]
                self.ext_label['text'] = extension
                self.size_label['text'] = self.size
                self.root.update()
            else:
                return
    def connect(self):
        self.label4["text"] = "Trying to connect"
        self.root.update()
        time.sleep(2)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        addressp = self.ip_field_entry.get()
        addressl = self.list.get(ACTIVE)
        if addressp != "":
            address, port = addressp.split(":")
            address, port = address, int(port)
            try:
                self.client.connect((address, port))
                self.label4['text'] = "Connecting..."
                self.root.update()
                time.sleep(2)
                
                self.label4['text'] = "Connected"
                self.root.update()
                time.sleep(2)
                with open("C:\\Max Share\\address.sri", 'r') as file:
                    read = file.read().splitlines()
                if addressp not in read:
                    with open("C:\\Max Share\\address.sri", 'a') as file:
                        file.write(addressp+"\n")
                return
            except:
                self.label4["text"] = "Failed to connect to {}".format(address)
                self.root.update()
                time.sleep(5)
        elif addressl != "":
            address, port = addressl.split(":")
            address, port = address, int(port)
            try:
                self.client.connect((address, port))
                self.label4['text'] = "Connecting..."
                self.root.update()
                time.sleep(2)
                
                self.label4['text'] = "Connected"
                self.root.update()
                time.sleep(2)
                with open("C:\\Max Share\\address.sri", 'r') as file:
                    read = file.read().splitlines()
                if addressp not in read:
                    with open("C:\\Max Share\\address.sri", 'a') as file:
                        file.write(addressp+"\n")
                return
            except:
                self.label4["text"] = "Failed to connect to {}".format(address)
                self.root.update()
                time.sleep(5)
        else:
            self.label4['text'] = "No ip address found please enter the ip adress and try again"
            self.root.update()
            time.sleep(6)
        
        self.label4['text'] = "None"
        self.root.update()
    def send(self):
        
        self.client.send(self.acname.encode('utf-8'))
        self.client.send(self.size.encode('utf-8'))
        self.label4["text"] = "Preparing to send..."
        self.root.update()
        time.sleep(3)
        self.label4["text"] = "Sending..."
        self.root.update()
        time.sleep(2)
        # print(self.path)
        file = open(self.path, 'rb')
        data = file.read(1024)
        sent_var = len(data)
        while data:
            self.client.send(data)
            data = file.read(1024)
            sent_var+=(len(data))
            self.label5['text'] = "Sent: "+str(sent_var)+" bytes"
            self.root.update()
            # print("sent 1024 bytes")
        file.close()
        time.sleep(3)
        self.label5['text'] = "Sent: "
        self.label4['text'] = "Sent Successfully"
        self.root.update()
        time.sleep(5)
        self.label4["text"] = 'None'
        self.root.update()
        self.client.close()

class receive_class:
    def __init__(self, root):
        self.root = root
        self.root.title("Receive")
        self.root.geometry("1080x720+250+50")
        self.root.maxsize(1080, 720)
        self.root.minsize(1080, 720)

        ################## Creating required frames
        # Creating frame 1
        self.frame1 = Frame(self.root, bg="lightgray", bd=5, relief=GROOVE)
        self.frame1.place(x=10, y=10, width=800, height=625)
        # Creating frame 2
        self.frame2 = Frame(self.root, bd=5, relief=GROOVE)
        self.frame2.place(x=820, y=10, width=250, height=625)
        # Creating fram 3
        self.frame3 = Frame(self.root, bd=5, relief=GROOVE)
        self.frame3.place(x=10, y=645, width=1060, height=65)
        ################## Creating the frames are over

        ################# Working with frame 1
        # Creating the labels
        
        ####Creating the filename label####
        self.label1 =  Label(self.frame1, text="File: ", font=("times new roman", 30), bg="lightgray")
        self.label1.place(x=50, y=50)
        ### Creating the invisible lable for file name label
        self.file_label_value = StringVar()
        self.file_label_value.set("")
        self.file_label = Label(self.frame1, bg="lightgray", text="", font=("times new roman", 30))
        self.file_label.place(x=150, y=50)
        # self.frame1.update()
        self.root.update()
        # Creating the extension label
        self.label2 =  Label(self.frame1, text="Extension: ", font=("times new roman", 30), bg="lightgray")
        self.label2.place(x=50, y=150)
        ### Creating the invisible label for the extension name:
        self.ext_label_value = StringVar()
        self.ext_label_value.set("")
        self.ext_label = Label(self.frame1, bg="lightgray", text="", font=("times new roman", 30))

        self.ext_label.place(x=240, y=150)
        # self.frame1.update()
        self.root.update()
        # Creating the label for the size
        self.label3 =  Label(self.frame1, text="Size: ", font=("times new roman", 30), bg="lightgray")
        self.label3.place(x=50, y=250)
        ### Creating the invisible label for the size:
        self.size_label_value = StringVar()
        self.size_label_value.set("")
        self.size_label = Label(self.frame1, bg="lightgray", text="", font=("times new roman", 30))

        self.size_label.place(x=140, y=250)
        # self.frame1.update()
        self.root.update()
        # Creating a label for the status update to the user
        self.status_label_value = StringVar()
        self.status_label_value.set("None")
        self.label4 =  Label(self.frame1, text="None" , font=("times new roman", 10), bg="lightgray")
        self.label4.place(x=0, y=625-35)
        # Creating the size label for showing the size:
        self.label5 = Label(self.frame1, text=f"Received: ", bg="lightgray")
        self.label5.place(x=0, y=625-50)
        ############ Working with frame2
        # Creating the buttosn required 
        # Creating the connect button
        self.button1 = Button(self.frame3, text="Refresh", font=("times new roman", 10), relief=GROOVE, bd=3, command=self.refresh)
        self.button1.place(x=20, y=15, width=150)

        # Creating a text field for the pasting the path of the file
        self.path_file_entry = Entry(self.frame3, font = ("times new roman", 15))
        self.path_file_entry.place(x=190, y=15, width=300)
        # Creating a save button for receiving and saving the file 
        self.button2 = Button(self.frame3, text="Receive & Save", font=("times new roman", 10), relief=GROOVE, bd=3, command=self.save)
        self.button2.place(x=500, y=15, width=150)

        
        
        ########### Working with frame 2
        self.list = Listbox(self.frame2)
        self.list.place(x=0,y=0, width=237, height=612)
        with open("C:/Max Share/received.sri", 'r') as file:
            self.addresses = file.read().splitlines()
        if self.addresses != []:
            for address in self.addresses:
                self.list.insert(END, address)
    def refresh(self):
        self.root.update()
        self.label4['text'] = "Refreshing..."
        self.root.update()
        self.list.delete(0, END)
        self.root.update()
        with open("C:/Max Share/received.sri", 'r') as file:
            addresses = file.read().splitlines()
        
        for address in addresses:
            self.list.insert(END, address)
            self.root.update()
            time.sleep(1)
        time.sleep(3)
        self.label4['text'] = "Refresh complete"
        self.root.update()
        time.sleep(1)
    def restart_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ipv4 = socket.gethostbyname(socket.gethostname())
        port = 5050
        self.server.bind((ipv4, port))
        self.listening_at = str(ipv4)+":"+str(port)
        self.server.listen()
        self.label4['text'] = "Listening at {}".format(self.listening_at)
        self.root.update()
        self.client, address = server.accept()
        self.label4['text'] = f"Connected with {str(address)}"
        self.root.update()
        # with open("C:\\Max Share\\received.sri", 'r') as file:
        #     read = file.read().splitlines()
        # if str(address) not in read:
        #     with open("C:\\Max Share\\received.sri", 'a') as file:
        #         file.write(socket.gethostbyaddr(str(address))+"\n")
    def save(self):
        
        path_to_save = self.path_file_entry.get()

        if path_to_save!= "":
            os.chdir(path_to_save)
        else:
            pass
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ipv4 = socket.gethostbyname(socket.gethostname())
        port = 5050
        self.server.bind((ipv4, port))
        self.listening_at = str(ipv4)+":"+str(port)
        self.server.listen()
        self.label4['text'] = "Listening at {}".format(self.listening_at)
        self.root.update()
        self.client, address = self.server.accept()
        self.label4['text'] = f"Connected with {str(address)}"
        self.root.update()
        # with open("C:\\Max Share\\received.sri", 'r') as file:
        #     read = file.read().splitlines()
        # if str(address) not in read:
        #     with open("C:\\Max Share\\received.sri", 'a') as file:
        #         file.write(socket.gethostbyaddr(str(address))+"\n")
        try:
            filename = self.client.recv(1024).decode('utf-8')
            extension = filename.split(".")[-1]
            size = self.client.recv(1024).decode('utf-8')
            self.file_label['text'] = filename.split(".")[0]
            self.ext_label['text'] = extension
            self.size_label['text'] = size
            self.root.update()
            file = open(filename, 'wb')
            total_value = 0
            self.label4['text'] = "Receiving..."
            while True:
                data = self.client.recv(1024)
                if not data:
                    break
                else:
                    file.write(data)
                    total_value += len(data)
                    self.label5['text'] = "Received: "+str(total_value)+" bytes"
                    self.root.update()
        except Exception as e:
            print(e)
        self.label4['text'] = "Done receiving"
        self.root.update()
        time.sleep(5)
        self.client.close()
        self.server.close()
        file.close()
        self.label4['text'] = "None"
        self.root.update()
        return
class first_page:
    def __init__(self, root):
        self.root = root
        self.root.title("Max Share")
        self.root.geometry("700x500+500+150")
        self.root.minsize(700, 500)
        self.root.maxsize(700, 500)
        
        # Creating a heading to my app
        self.label = Label(self.root, text="Max Share", font=("Comic Sans MS", 50, 'italic'))
        self.label.place(x=180, y=100)
        
        # Creating two buttons for sending and receving
        # Creating send button 
        self.button1 = Button(self.root, text="Send", font=("times new roman", 15, 'bold'), bg = "lightgray", command=self.call_send_class)
        self.button1.place(x=270, y=300, width=180)
        # Creating receive button
        self.button2 = Button(self.root, text="Receive", font=("times new roman", 15, 'bold'), bg="lightgray", command=self.call_receive_class)
        self.button2.place(x=270, y=360, width=180)
        

    def call_send_class(self):
        root2 = Tk()
        send_class = send_window(root2)
        root2.mainloop()
    def call_receive_class(self):
        root3 = Tk()
        receive_class_object = receive_class(root3)
        root3.mainloop()

root = Tk()
obj = first_page(root)
root.mainloop()
