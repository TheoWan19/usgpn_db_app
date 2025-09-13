import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql
from mysql.connector import Error
import qrcode
import os


def create_db_connection(localhost='localhost', user='pewil', password='Pewil1010$@$&', db_name='test_db'):
    connection = None
    try:
        connection = mysql.connect(
            host=localhost,
            user=user,
            passwd=password,
            database=db_name
        )
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def insert_data(*args):
    name = name_entry.get()
    email = email_entry.get()
    
    data = f'{name}-{email}'
    directory_path = 'C:/Users/Theo Wan/Desktop/python_code/qr_code_tkinter/images'
    file_name = f'{data}.png'
    full_path = os.path.join(directory_path, file_name)
    os.makedirs(directory_path, exist_ok=True)
    if data:
        try:
            qr = qrcode.make(data)
            qr_resized = qr.resize((280, 250))
            qr_resized.save(full_path) 
            print(f'File {file_name} successfully saved to {directory_path}!')    
        except IOError as e:
            print(f'Error saving file: {e}')    
    
        connection = create_db_connection()
        if connection:
            file_path = full_path
            if file_path:
                try:
                    with open(file_path, 'rb') as file:
                        binary_data = file.read()
                    
                    cursor = connection.cursor()
                    sql_insert_query = """INSERT INTO users (name, email, photo) VALUES (%s, %s, %s)"""
                    insert_tuple = (name, email, binary_data)
                    cursor.execute(sql_insert_query, insert_tuple)
                    connection.commit()
                    print('Query executed successfully')
                    status_label.config(text='Data inserted successfully!')
                    
                    messagebox.showinfo("Success", "Data inserted successfully")
                except Error as err:
                    messagebox.showerror("Database Error", f"Error: '{err}'")    
                except Exception as e:
                    messagebox.showerror("Error", str(e))
                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close()  

                         
# Tkinter GUI setup


root = tk.Tk()
root.title('Mysql connect photo')
tk.Label(root, text='Name').grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=0, padx=5, pady=5)

tk.Label(root, text='Email').grid(row=0, column=1, padx=5, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=5, pady=5)

status_label = tk.Label(root, text='')
status_label.grid(row=3, column=0, columnspan=2, pady=5)

insert_button = tk.Button(root, text='Insert', command=insert_data)
insert_button.grid(row=2, column=0, columnspan=2, pady=10)


root.mainloop()

