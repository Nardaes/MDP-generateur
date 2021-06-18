import string
from tkinter import *
from random import randint,choice


#def
def generator_pwd():
    charMin=10
    charMax=16
    allChars=string.ascii_letters + string.punctuation + string.digits
    
    pwd="".join(choice(allChars) for x in range(randint(charMin,charMax)))
    champPW.delete(0,END)
    champPW.insert(0, pwd)   


#cree fenetre
root = Tk()
root.title("AppMDP")
root.geometry("500x300")
root.config(background="#3D85C6")

#frame
frame=Frame(root,bg="#3D85C6")
frameDroite= Frame(frame,bg="#3D85C6")

#image

image= PhotoImage(file="imageCadenas.png").zoom(105).subsample(32)
canvas = Canvas(frame,width=100,height=100,bg="#3D85C6",bd=0,highlightthickness=0)
canvas.create_image(50,50,image=image)
canvas.grid(row=0,column=0,sticky=W)



#LABEL
lblTitle = Label(frameDroite,text="Crée votre de mot de passe",font=("Arial",20),bg="#3D85C6", fg="white")
lblTitle.pack()

#CHAMP DE PW
champPW = Entry(frameDroite,font=("Arial",15),bg="#3D85C6", fg="white")
champPW.pack()

#bouton

btnChangement = Button(frameDroite,text="Genererer",font=("Arial",10),command=generator_pwd,bg="white",fg="#3D85C6")
btnChangement.pack(fill=X)

#affichage fenetre
frameDroite.grid(row=0,column=1,sticky=W)
frame.pack(expand=YES)
root.mainloop()

