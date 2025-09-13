# pip install qrcode pillow
import qrcode

from PIL import ImageTk


import tkinter as tk # import tkinter


from tkinter import filedialog, messagebox, ttk # import filedialog and messagebox from tkinter


# Function to create QR code
def create_qr(*args):
    data = text_entry.get()
    if data:
        qr = qrcode.make(data)
        qr_resized = qr.resize((280, 250))
        tk_qr = ImageTk.PhotoImage(qr_resized)
        qr_canvas.delete("all") # clear previous QR code
        qr_canvas.create_image(0, 0, anchor=tk.NW, image=tk_qr)
        qr_canvas.image = tk_qr # keep a reference


def save_qr(*args):
    data = text_entry.get()
    if data:
        qr = qrcode.make(data)
        qr_resized = qr.resize((280, 250))
        
        path = filedialog.asksaveasfilename(defaultextension=".png",)
        if path:
            qr_resized.save(path)
            messagebox.showinfo("Success", f"QR code saved to {path}")
        else:
            messagebox.showwarning("Cancelled", "Save operation cancelled")


def on_click(event):
    print('cliked')
    

# GUI window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="#f0f0f0")  # light grey background

frame1 = tk.Frame(root, bg="#f8f6f6", bd=2, relief=tk.FLAT)
frame1.place(x=10, y=0, width=380, height=250) # red frame

cover_img = tk.PhotoImage(file="cover.png") # load cover image
qr_canvas = tk.Canvas(frame1, width=360, height=240)
qr_canvas.create_image(0, 0, anchor=tk.NW, image=cover_img)


qr_canvas.image = cover_img # keep a reference
qr_canvas.bind("<Double-1>", save_qr) # bind double-click event to save_qr function

qr_canvas.pack(fill=tk.BOTH, expand=True)

frame2 = tk.Frame(root, bg="#f8f6f6", bd=2, relief=tk.FLAT)
frame2.place(x=10, y=260, width=380, height=150) # red frame

text_entry = ttk.Entry(frame2, width=20, font=("Arial", 12), justify="center")
text_entry.bind("<Return>", create_qr) # bind Enter key to create_qr function
text_entry.place(x=80, y=20)

text_entry_1 = ttk.Entry(frame2, width=20, font=("Arial", 12), justify="center")
text_entry_1.bind("<KeyRelease>", save_qr) # bind Enter key to create_qr function
text_entry_1.place(x=80, y=50)


btn1 = ttk.Button(frame2, text="Create", command=create_qr)
btn1.place(x=60, y=80)

btn2 = ttk.Button(frame2, text="Save", command=save_qr)
btn2.place(x=135, y=80)

btn3 = ttk.Button(frame2, text="Exit", command=root.quit)
btn3.place(x=210, y=80)

root.mainloop()