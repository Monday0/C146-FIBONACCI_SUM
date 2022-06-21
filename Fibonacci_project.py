# Basic tkinter template
from tkinter import *
root = Tk()

root.title("Fibonacci")
root.geometry("400x400")

enter_word = Entry(root)
label_series = Label(root, text="Fibonacci Series: ")
label_sum = Label(root)

def Fibonacci():
    num = enter_word
    first_no = 0
    second_no = 1
    sum = 0
    sum2 = 0
    counter = 1
   
    while (counter <= num):
        label_series["text"] += str(sum) + " "
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        sum2 = sum2 + sum
        label2["text"] = "Fibonacci Sum : " + str(sum2)
        
    
btn = Button(root, text="Show Fibonacci Series", command=Fibonacci)
btn.pack()
enter_word.pack()
label_series.pack()
label_sum.pack()


root.mainloop()