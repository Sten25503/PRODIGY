import tkinter as tk    
from tkinter import messagebox, ttk
import csv
import os

# File to store contacts
CONTACTS_FILE = 'PRODIGY_SD_03.csv'

# Function to load contacts from the CSV file
def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r', newline='') as file:
            reader = csv.reader(file)
            contacts = list(reader)
    return contacts

# Function to save contacts to the CSV file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

# Custom dialog to add a new contact
def add_contact():
    add_window = tk.Toplevel(root)
    add_window.title("Add New Contact")
    add_window.geometry("350x250")
    
    tk.Label(add_window, text="Name:").pack(pady=5)
    name_entry = tk.Entry(add_window, width=30)
    name_entry.pack(pady=5)
    
    tk.Label(add_window, text="Phone Number:").pack(pady=5)
    phone_entry = tk.Entry(add_window, width=30)
    phone_entry.pack(pady=5)
    
    tk.Label(add_window, text="Email:").pack(pady=5)
    email_entry = tk.Entry(add_window, width=30)
    email_entry.pack(pady=5)
    
    def save_new_contact():
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        
        if name and phone and email:
            contacts.append([name, phone, email])
            save_contacts(contacts)
            update_contact_list()
            add_window.destroy() 
        else:
            messagebox.showerror("Error", "All fields are required!")
    
    tk.Button(add_window, text="Save Contact", command=save_new_contact, bg="lightgreen").pack(pady=20)

# Function to update the displayed contact list in the table
def update_contact_list():
    # Clear the current table rows
    for row in contact_tree.get_children():
        contact_tree.delete(row)
    
    # Add all contacts from the list to the table
    for contact in contacts:
        contact_tree.insert('', tk.END, values=contact)

# Function to delete a selected contact
def delete_contact():
    try:
        selected_item = contact_tree.selection()[0]
        selected_index = contact_tree.index(selected_item)
        contacts.pop(selected_index)
        save_contacts(contacts)
        update_contact_list()
    except IndexError:
        messagebox.showerror("Error", "Please select a contact to delete.")

# Function to edit a selected contact
def edit_contact():
    try:
        selected_item = contact_tree.selection()[0]
        selected_index = contact_tree.index(selected_item)
        contact = contacts[selected_index]

        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Contact")
        edit_window.geometry("350x250") 
        
        tk.Label(edit_window, text="Name:").pack(pady=5)
        name_entry = tk.Entry(edit_window, width=30)
        name_entry.pack(pady=5)
        name_entry.insert(0, contact[0])
        
        tk.Label(edit_window, text="Phone Number:").pack(pady=5)
        phone_entry = tk.Entry(edit_window, width=30)
        phone_entry.pack(pady=5)
        phone_entry.insert(0, contact[1])
        
        tk.Label(edit_window, text="Email:").pack(pady=5)
        email_entry = tk.Entry(edit_window, width=30)
        email_entry.pack(pady=5)
        email_entry.insert(0, contact[2])
        
        def save_edited_contact():
            new_name = name_entry.get()
            new_phone = phone_entry.get()
            new_email = email_entry.get()
            
            if new_name and new_phone and new_email:
                contacts[selected_index] = [new_name, new_phone, new_email]
                save_contacts(contacts)
                update_contact_list()
                edit_window.destroy() 
            else:
                messagebox.showerror("Error", "All fields are required!")
        
        tk.Button(edit_window, text="Save Contact", command=save_edited_contact, bg="lightblue").pack(pady=20)

    except IndexError:
        messagebox.showerror("Error", "Please select a contact to edit.")

# Set up the main window
root = tk.Tk()
root.title("Contact Management System")
root.geometry("550x400")

# Load contacts from file
contacts = load_contacts()

# Label
title_label = tk.Label(root, text="Contact List", font=("Arial", 16))
title_label.pack(pady=10)

# Contact Treeview (table)
columns = ('Name', 'Phone Number', 'Email')
contact_tree = ttk.Treeview(root, columns=columns, show='headings', height=10)

# Define the headings
contact_tree.heading('Name', text='Name')
contact_tree.heading('Phone Number', text='Phone Number')
contact_tree.heading('Email', text='Email')

# Set the column widths
contact_tree.column('Name', width=150)
contact_tree.column('Phone Number', width=150)
contact_tree.column('Email', width=200)

# Pack the treeview into the window
contact_tree.pack(pady=10)

# Add Button
add_button = tk.Button(root, text="Add Contact", command=add_contact, font=("Arial", 12), bg="lightgreen")
add_button.pack(side=tk.LEFT, padx=10, pady=10)

# Edit Button
edit_button = tk.Button(root, text="Edit Contact", command=edit_contact, font=("Arial", 12), bg="lightblue")
edit_button.pack(side=tk.LEFT, padx=10, pady=10)

# Delete Button
delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, font=("Arial", 12), bg="lightcoral")
delete_button.pack(side=tk.LEFT, padx=10, pady=10)

# Initial update of contact list
update_contact_list()

# Start the Tkinter event loop
root.mainloop()
