from tkinter import *
from PIL import ImageTk, Image
import  sqlite3


root=Tk()
root.title("Databases")
root.iconbitmap('d:/gui/iconbitmap.ico')
root.geometry("400x400")

#Databases


#Create Cursor


#Create Table
#c.execute("""CREATE TABLE addresses (
        #first_name text,
        #last_name text,
        #address text,
        #city text,
        #state text,
        #zipcode interger
        #)""")

#Create submit function for database
def submit():
    # Create a Database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create Cursor
    c = conn.cursor()

    #Insert Into Table
    c.execute("INSERT INTO address VALUES(:first_name, :last_name, :address, :city, :state, :zipcode )",
              {
                  "first_name": first_name.get(),
                  "last_name": last_name.get(),
                  "address": address_name.get(),
                  "city": city_name.get(),
                  "state": city_name.get(),
                  "zipcode": zipcode_name.get()
              }





              )

    # Changes
    conn.commit()

    # Close connection
    conn.close()



#Create Text Boxes
first_name = Entry(root, width=30)
first_name.grid(row=0, column=0,)

last_name = Entry(root, width=30)
last_name.grid(row=1, column=1)




address_name = Entry(root, width=30)
address_name.grid(row=2, column=1)

city_name = Entry(root, width=30)
city_name.grid(row=3, column=1)


state_name = Entry(root, width=30)
state_name.grid(row=4, column=1)

zipcode_name = Entry(root, width=30)
zipcode_name.grid(row=5, column=1)

#Create Text Box Label
first_name_label = Label(root, text="First Name")
first_name_label.grid(row=0, column=0)

last_name_label = Label(root, text="Last Name")
last_name_label.grid(row=1, column=0)

address_name_label = Label(root, text="Address")
address_name_label.grid(row=2, column=0)

city_name_label = Label(root, text="City")
city_name_label.grid(row=3, column=0)

state_name_label = Label(root, text="State")
state_name_label.grid(row=4, column=0)

zipcode_name_label = Label(root, text="Zipcode")
zipcode_name_label.grid(row=5, column=0)

#Create Sumbit Button
Submit_button =Button(root, text="Add Record to database", command=submit)
Submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)



tatata






root.mainloop()