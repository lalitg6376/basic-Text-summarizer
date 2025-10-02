import tkinter as tk
from transformers import pipeline

try:
    summarizer = pipeline("summarization")
except Exception as e:
    print("Error in loading model:", e)

root = tk.Tk()
root.geometry("800x700")  # Phone/Tablet friendly size
root.title("Text Summarizer")

# UI Colors
bg_color = "#f0f0f0"
btn_color = "#4CAF50"
btn_text_color = "white"
copy_btn_color = "#2196F3"

root.configure(bg=bg_color)

def limit_input(event,textbox,limit=600):
    content = textbox.get("1.0","end-1c")
    if len(content) >= limit and event.keysym != "BackSpace":
        return "break"
    
label = tk.Label(root,text="Enter your text for summarization:", font=("Arial", 14), bg=bg_color)
label.pack(padx=20, pady=10, anchor="w")

entry = tk.Text(root,height=15,width=80, font=("Arial", 12), wrap="word", bd=2, relief="solid")
entry.pack(padx=20, pady=10)

def summrize():
    result = entry.get("1.0","end-1c")
    output = summarizer(result,min_length=25,max_length=70)
    summary = output[0]['summary_text']

    answer.config(state="normal")
    answer.delete("1.0","end")
    answer.insert("1.0",summary)
    answer.config(state="disabled")

def copy_output():
    root.clipboard_clear()
    root.clipboard_append(answer.get("1.0","end-1c"))
    root.update()
    
btn = tk.Button(root,text="Summarize",command=summrize, bg=btn_color, fg=btn_text_color, font=("Arial", 12), width=15, height=2)
btn.pack(pady=15)

entry.bind("<Key>",lambda e:limit_input(e,entry,limit=600))

answer = tk.Text(root,height=15,width=80, font=("Arial", 12), wrap="word", bd=2, relief="solid", state="disabled")
answer.pack(padx=20, pady=10)

copy_btn = tk.Button(root,text="Copy Output",command=copy_output, bg=copy_btn_color, fg="white", font=("Arial", 12), width=15, height=2)
copy_btn.pack(pady=10)

root.mainloop()
