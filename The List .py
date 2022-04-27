from tkinter import*
import random
root=Tk()
root.title("The List")
root.geometry("500x500")
label1=Label(root)
label2=Label(root)
List1=["Bottle","Tissues","Tiffin","Picnic Mat"]
label1["text"]="Listed_items : "+ str(List1)
def bag_contents():
    random_list=random.sample(range(0,7),1)
    label2["text"]="Put Item no "+ str(List1)
label1.place(relx=0.5,rely=0.4, anchor=Center) 
  btn = Button(root, text="Which item to put in bag?",command = bag_contents,bg="orange",fg="white")
  btn.place(relx=0.5,rely = 0.5, anchor = CENTER) 
  label2.place(relx=0.5,rely = 0.6, anchor = CENTER)
  root.mainloop() 
    





