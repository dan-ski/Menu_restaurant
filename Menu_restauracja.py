from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super (Application, self).__init__(master)
        self.create_widgets()
        self.grid()

    def create_widgets(self):

        Label(self, text="Witam restauracji orientalnej Kebastian!").grid(row=0, column=0, columnspan=2, sticky=W)
        Label(self, text="Co Państwo zamawiają?").grid(row=1, column=0, sticky=W)

        self.mongolian_frites=BooleanVar()
        Checkbutton(self,
                    text="Frytki mongolskie- 5 zł",
                    variable=self.mongolian_frites,
                    ).grid(row=2, column=0, sticky=W)

        self.talar = BooleanVar()
        Checkbutton(self,
                    text="Talarki- 5 zł",
                    variable=self.talar,
                    ).grid(row=2, column=1, sticky=W)

        self.potatoes = BooleanVar()
        Checkbutton(self,
                    text="Pyry z gzikiem- 6zł",
                    variable=self.potatoes,
                    ).grid(row=2, column=2, sticky=W)

        self.plate = BooleanVar()
        Checkbutton(self,
                    text="Kebab na talerzu- 25 zł",
                    variable=self.plate,
                    ).grid(row=3, column=0, sticky=W)

        self.bread = BooleanVar()
        Checkbutton(self,
                    text="Kebab w bułce- 20 zł",
                    variable=self.bread,
                    ).grid(row=3, column=1, sticky=W)

        self.suprise = BooleanVar()
        Checkbutton(self,
                    text="Kebab wpie****ka- 35 zł",
                    variable=self.suprise
                    ).grid(row=3, column=2, sticky=W)

        self.drink=StringVar()
        self.drink.set(None)

        drinks=["Energetyk- 10 zł", "Wóda-20 zł", "Zielona herbata (dla dzieci)- 15 zł"]

        column=0
        for drink in drinks:
            Radiobutton(self,
                        text=drink,
                        variable=self.drink,
                        value=drink).grid(row=4, column=column, sticky=W)
            column+=1

        Button(self, text="Pokaż rachunek", command=self.order).grid(row=5, column=0, sticky=W)

        self.bill=Text(self, width=50, height=10, wrap=WORD)
        self.bill.grid(row=6, column=0, columnspan=3, sticky=W)

    def order(self):
        self.order_list=""
        self.sum=0

        if self.mongolian_frites.get():
            self.order_list+="Frytki mongolskie- 5 zł"
            self.sum+=5

        if self.talar.get():
            self.order_list+="Talarki- 5 zł"
            self.sum+=5

        if self.potatoes.get():
            self.order_list+="Pyry z gzikiem- 6zł"
            self.sum+=6

        if self.plate.get():
            self.order_list+="\nKebab na talerzu- 25 zł"
            self.sum+=25

        if self.bread.get():
            self.order_list+="\nKebab w bułce- 20 zł"
            self.sum+=20

        if self.suprise.get():
            self.order_list+="\nKebab wpie****ka- 35 zł"
            self.sum+=35

        if self.drink.get()=="Energetyk- 10 zł":
            self.order_list+= "\nEnergetyk- 10 zł"
            self.sum+=10

        if self.drink.get()=="Wóda-20 zł":
            self.order_list+= "\nWóda-20 zł"
            self.sum+=20

        if self.drink.get()=="Zielona herbata (dla dzieci)- 15 zł":
            self.order_list+= "\nZielona herbata (dla dzieci)- 15 zł"
            self.sum+=15

        self.order_list+="\nW sumie: "+str(self.sum)+" zł."
        self.bill.delete(0.0, END)
        self.bill.insert(0.0, self.order_list )

root=Tk()
root.title("Restauracja Kebastian")
app=Application(root)
root.mainloop()
