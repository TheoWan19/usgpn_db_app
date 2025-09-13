import tkinter as tk


def on_button_click(event):
    print("Button clicked!")
    

def on_key_press(event):
    print(f"Key pressed: {event.keysym}")    


root = tk.Tk()
root.title("Event Binding Example")
root.geometry("300x200")

btn = tk.Button(root, text="Click Me")
btn.pack(pady=20)

btn.bind("<Double-1>", on_button_click)
root.bind("<Key>", on_key_press)

root.mainloop()