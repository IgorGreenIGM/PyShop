"""
Please for any prblem, write to https://github.com/igorgreenIGM
"""
# modules import
import os
import sys
import tkinter
import time
import tabulate
from tkinter import messagebox, scrolledtext, Scrollbar
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

# main window creation
main_app = tkinter.Tk()
main_app.title("FUTURE'S ELECTRONIC")
main_app.geometry("2048x1200")
main_app.resizable(width=False, height=False)

welcome_frame = tkinter.Label(main_app)
bckg_img = tkinter.PhotoImage(file="./img/background1.png")
welcome_frame['image'] = bckg_img
welcome_frame['text'] = "Background Image"
welcome_frame.place(x=-85, y=0)


# opening GUI method
client_name = tkinter.StringVar()
def welcome(*args):
    label_name = tkinter.Entry(welcome_frame, width=100, textvariable=client_name, background="#bac9d4", font=("Consolas", 11))
    label_name.place(x=513, y=639, width=1137, height=48)
    label_bouton = tkinter.Button(welcome_frame, command=confirm_name, text="        Confirmer     ", font=("Agency FB", 13, 'bold'), height=1, border=0, borderwidth=0, background="#c9d8e6", foreground="Black")
    label_bouton.place(x=950, y=840, height=60)


# confirm name method(related to confirm button)
def confirm_name(*args):
    if client_name.get() == "": 
        messagebox.showerror("error", "Name field cannot be empty !")
    else:    
        continuer = messagebox.askyesno("Confirm ?", "Do you confirm you're {} ?".format(client_name.get().upper()))
        if continuer == True:
            if os.path.exists("./database/{}.txt".format(client_name.get().upper())):
                messagebox.showinfo("", F"Chere , {client_name.get().upper()} we're pride to see you for the again in our shop !")
            else:
                messagebox.showinfo("",F"Chere {client_name.get().upper()}, We're pride to see you for the first time in our shop!")
            for widget in main_app.winfo_children():
                widget.destroy()
            list_articles()
            print_reductions()
            pass_command()
            print_command()
            generate_button = tkinter.Button(main_app, text="Generer", border=2, borderwidth=3, width=20, command=print_command, font=('Friendly Schoolmates',13, 'bold'))
            generate_button.place(x=1550, y=(len(future_electronics) + 1)*65)
            bill = tkinter.Button(main_app, text="Imprimer", border=2, borderwidth=3, width=20, command=print_bill, font=('Friendly Schoolmates',13, 'bold'))
            bill.place(x=1550, y=(len(future_electronics) + 1)*80)
            

# Shop article content
future_electronics = [    
                        ["IMPRIMANTE HP LASERJET SERIES 2200", "IMP364AA", 35000, 18],
                        ["Ordinateur Portable Lenovo 21F563 4Ghz", "ORD45645", 285000, 12],
                        ["Appareil Photo Nicon x1250mm", "APPPHOT7", 23500, 14],
                        ["Ordinateur portable HP CoreDuo Evolution", "ORD456SA", 450000, 3],
                        ["Carte Graphique NVIDIA Geforce GTX 3080", "CARD789D", 75320, 36],
                        ["Processeur Intel Core i7 9th gen @3.8Ghz", "PROC7789", 45320, 21],
                        ["Ventirad WaterGen Evolution x30G", "VENT5445", 15623, 145],
                        ["Iphone 12 pro max", "TEL456DN", 700000, 1],
                        ["IMPRIMANTE RICON LASERJET 5500", "IMP456DK", 4500, 7],
                        ["Kit de Recharge Telephone", "KIT456DK", 1500, 121],
                        ["Ecouteurs Bluetooth 'Airpods' ", "ECOU456A", 4500, 55],
                        ["SAMSUNG GALAXY S10+ EVOLUTION", "TEL456XK", 235000, 1]
                    ]


# List shop articles method
def list_articles():
    articles_frame = tkinter.LabelFrame(main_app, text="Liste des Articles de la boutique : ")
    tkinter.Label(articles_frame, text="N°  ").grid(row=0, column=0, sticky="w")
    tkinter.Label(articles_frame, text="NOM DE L'ARTICLE :                                 ").grid(row=0, column=1, sticky="w")
    tkinter.Label(articles_frame, text="        CODE         ").grid(row=0, column=2,sticky="w")
    tkinter.Label(articles_frame, text="        PRIX        ").grid(row=0, column=3, sticky="w")
    tkinter.Label(articles_frame, text="STOCK").grid(row=0, column=4, sticky="w")
    for i in range(len(future_electronics)):
        tkinter.Label(articles_frame, text="{}  ".format(i + 1)).grid(row=i+1, column=0)
        tkinter.Label(articles_frame, text="{}".format(future_electronics[i][0])).grid(row=i+1, column=1, sticky="w")
        tkinter.Label(articles_frame, text="        {}".format(future_electronics[i][1])).grid(row=i+1, column=2, sticky="w")
        tkinter.Label(articles_frame, text="        {}".format(future_electronics[i][2])).grid(row=i+1, column=3, sticky="w")
        tkinter.Label(articles_frame, text="  {}".format(future_electronics[i][3]), border=10, borderwidth=10).grid(row=i+1, column=4, sticky="w")
    articles_frame.place(x=0, y=0)


# Update command callback method
command_qte = []
command_boxes = []
def updater(*args):
    for i in range(len(command_qte)):
        command_qte[i][1] = command_boxes[i]


# client select article method
def pass_command(*args):
    command_frame = tkinter.LabelFrame(main_app, text="Command")
    global command_boxes 
    global command_qte
    if len(command_boxes) == 0: 
        for i in range(len(future_electronics)):
            tkinter.Label(command_frame).grid(row=0, column=0)
            command_qte.append([future_electronics[i][0], tkinter.StringVar()])
            command_boxes.append(tkinter.Spinbox(command_frame, from_=0, to=future_electronics[i][3], textvariable=command_qte[i][1], width=25))
            command_boxes[i].grid(row=i + 1, column=0, pady=9, sticky="N")
            command_qte[i][1].trace('r', updater)
    else:
        command_qte[i][1].trace('r', updater)
    for i in range(len(command_boxes)):
        command_qte[i][1].trace('r', updater)
    command_frame.place(x=970, y=0, width=385, height=(len(future_electronics) + 1)*58)


# Method for reading the number of visits of the client
def visits_nb(client_name):
    if os.path.exists("./database/" + client_name.get() + ".txt"):
        with open("./database/" + client_name.get() + ".txt", mode='r') as file_in:
            nbre = file_in.readline()
        return int(nbre[0:len(nbre) - 1])
    else:
        return 0


# Method for reading reductions
def read_reductions(client_name:str):
    if not os.path.exists("./database/" + client_name + ".txt") :
        return []
    else:
        red_list = []
        with open("./database/" + client_name + ".txt", mode='r') as file_in:
            content = file_in.readlines()
            for line in content[1:]:
                red_list.append([line[0:50], int(line[50:len(line)-1])])
        return red_list


# Method for printing avaible reductions for the client
def print_reductions(*args):
    reduction_frame = tkinter.LabelFrame(main_app, text="Liste des Réductions")
    list_red = scrolledtext.ScrolledText(reduction_frame, height=13, width=83, state="normal")
    reduction_list = read_reductions(client_name.get())
    nbre_visites = visits_nb(client_name)
    i = 0
    no_reduc = True
    for elt in reduction_list:
        if elt[1] >= 3:
            no_reduc = False  
    if no_reduc:
        list_red.insert('end', F"Here, you'll find all reductions on our different products\n\n")    
    else:
        list_red.insert('end', F"looking about your number of visits, you have 2% of reductions on the following articles :\n\n")
        for elt in reduction_list:   
            if elt[1] >= 3 and nbre_visites >= 3: 
                list_red.insert('end', "{}\n\n".format(elt[0]))
    list_red["state"] = "disable"
    list_red.pack()
    reduction_frame.place(x=0, y=(len(future_electronics) + 1)*58)


# Generating command preview method
def print_command(*args):
    global command_qte
    command_list_frame = tkinter.LabelFrame(main_app, text="Command list")    
    list_command = scrolledtext.ScrolledText(command_list_frame, width=600, height=(len(future_electronics) + 1)*58)
    list_command.insert('end', "Future's Electronics:\n\n")
    list_command.insert('end', "Article Name :                 QTE\n")
    list_command.insert('end', "------------------             --------\n")
    list_empty = True
    for i in range(len(command_qte)):
        if int(command_qte[i][1].get()) != 0:
            list_command.insert('end', "{:<30}      {}\n\n".format(command_qte[i][0][0:29], int(command_qte[i][1].get())))
            list_empty = False
    if list_empty:
        list_command.insert('end', "\nWelcome to future Electronics, \nPlease select one or many article \nIn the left field to pass command.\n")
    list_command['state'] = "disable"
    list_command.pack()
    command_list_frame.place(x=1370, y=0, width=670, height=(len(future_electronics) + 1)*58)


# Printing bill in a file method
def print_bill():
    global command_qte
    reductions = read_reductions(client_name.get())
    nbre_visites = visits_nb(client_name)
    with open(client_name.get() + ".txt", mode='w', encoding="utf-8") as file_out:
        file_out.write("Future's Electronics\n\n")
        file_out.write("Client Name : " + client_name.get() + "\n\n")
        if not os.path.exists(F"./database/{client_name.get()}.txt") :
            to_print = []
            S = 0
            j = 1
            for i in range(len(command_qte)):
                if int(command_qte[i][1].get()) > 0:
                    total_price = future_electronics[i][2] * int(command_qte[i][1].get())
                    S+=total_price
                    to_print.append([F"{j}", F"{command_qte[i][0]}", "{}".format(future_electronics[i][1]), "{}".format(future_electronics[i][2]),  F"{int(command_qte[i][1].get())}", "0%", "{:.2f}".format(total_price)])
                    j+=1
            file_out.write(tabulate.tabulate(to_print, ["N°", "CLIENT NAME", "CODE", "UNIT PRICE", "QUANTITY", "REDUCTION", "TOTAL PRICE"], "double_grid"))
            file_out.write("\n\n{:10}Total Bill :{:.2f}F".format("",S))
        else:
                S = 0
                j = 1
                to_print = []
                for i in range(len(command_qte)):
                    if int(command_qte[i][1].get()) > 0:
                        if reductions[i][1] >= 3 and nbre_visites >= 3:
                            total_price = (future_electronics[i][2] * int(command_qte[i][1].get()))*(1 - (2/100))
                            S+=total_price
                            to_print.append([F"{j}", F"{command_qte[i][0]}", "{}".format(future_electronics[i][1]), "{}".format(future_electronics[i][2]),  F"{int(command_qte[i][1].get())}", "2%", "{:2f}".format(total_price)])
                            j+=1
                        else:
                            total_price = (future_electronics[i][2] * int(command_qte[i][1].get()))
                            S+=total_price
                            to_print.append([F"{j}", F"{command_qte[i][0]}", "{}".format(future_electronics[i][1]), "{}".format(future_electronics[i][2]),  F"{int(command_qte[i][1].get())}", "0%", "{:2f}".format(total_price)])
                            j+=1

                file_out.write(tabulate.tabulate(to_print, ["N°", "ARTICLE NAME", "CODE", "UNIT PRICE", "QUANTITY", "REDUCTION", "TOTAL PRICE"], "double_grid"))
                file_out.write("\n\n                                                                                                                        Total bill:{:.2f}F".format(S))
    os.system(F"\"{client_name.get()}.txt\"")
    if not messagebox.askyesno("Command Again ?", "Do you wish to command again ?") :
        save_reductions()
        messagebox.showinfo("Thanks !", "Thanks for buying in our shop, you're welcome !") 
        sys.exit(0)
    else:
        main()
        save_reductions()


# saving articles in the database
def save_reductions(*args):
    global command_qte
    nbre_visites = visits_nb(client_name)
    if not os.path.exists(F"./database/{client_name.get().upper()}.txt"): 
        with open(F"./database/{client_name.get().upper()}.txt", mode="w") as file_out:
            file_out.write("{}\n".format(nbre_visites + 1))
            for i in range(len(command_qte)):
                file_out.write("{:<50} {}\n".format(command_qte[i][0], int(command_qte[i][1].get())))
    else:
        reductions = read_reductions(client_name.get())
        for i in range(len(reductions)):
            reductions[i][1] = int(command_qte[i][1].get()) + reductions[i][1]
        with open(F"./database/{client_name.get().upper()}.txt", mode="w") as file_out:
            file_out.write("{}\n".format(nbre_visites + 1))
            for i in range(len(reductions)):
                file_out.write("{:<50} {}\n".format(reductions[i][0], reductions[i][1]))


# main method
def main() -> None:
    welcome() # welcom window


# calling
main() 
main_app.mainloop()