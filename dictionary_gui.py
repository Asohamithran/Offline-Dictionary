import json
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
from difflib import SequenceMatcher

matched_string=[]
data =json.load(open("H:\\python files\\dictionary\\076 data.json"))

class dict_app:
    def __init__(self,root):

          root.title("offline dictionary")
          root.geometry("800x600")

          lbl=tk.Label(root,text="Dictionary based on json data",font=("Arial Bold",14),bd=2,relief="solid",width=25,height=2)
          lbl.pack()
          lbl2=tk.Label(root,text="Enter your word here ",font=("Arial Bold",12))
          lbl2.pack()
          lbl3=tk.Label(root,text="--Poetry consists in a rhyming dictionary and things seen-- Gertrude Stein",font=("consolas Bold",12))
          #lbl3.place(x=100,y=400)
          lbl3.pack(side='bottom',expand='True')
          self.word=tk.StringVar()
          self.ent=tk.Entry(root,textvariable=self.word,width=20)
          #self.ent.place(x=25,y=65,anchor='center')
          self.ent.pack()
          self.buttons=[]
          find=tk.Button(root,text="Find Word",command= lambda :self.get_wrd(root),anchor='center')
          #print(val)
          find.pack(side="top")

          self.tb= scrolledtext.ScrolledText(root, borderwidth=3, height=10,width=40)
          self.tb['font'] = ('consolas', '12')
          #self.tb.place(x=100,y=300,anchor='center')
          self.tb.pack(side='top',expand="True")

          Quit=tk.Button(root,text="Quit",command=lambda : self.quit(root),anchor='se')
          Quit.pack()
          #val=self.find_word(self.word.get())
          #tb.insert(tk.END,val)
    def find_word(self,root,WORD):
        print("executed")
        #self.Blast(buttons)
        self.tb.delete('1.0',tk.END)
        WORD=WORD.lower()
        if WORD in data:
                meaning=data[WORD]
                val=str(meaning)
                self.tb.insert(tk.END,val)


          #tb.delete('1.0',END)
          #tb.insert(tk.END,meaning)
        else:
            self.tb.insert(tk.END,"check ur spelling\n")
            self.similarity(WORD,root)

    def get_wrd(self,root):
        self.Blast()
        wrd=self.ent.get()
        wrd=str(wrd)
        self.find_word(root,wrd)



    def quit(self,root):
        root.quit()
        root.destroy()
    '''def B_arr(self,d):
        print(d)
        self.buttons.append(d)
    '''
    def Blast(self):
        print("destroyed")
        for i in self.buttons:
            i.destroy()
            print(f"destroyed {i}")



        print(self.buttons)


    def similarity(self,word,root):
                 #c=0
                self.buttons.clear()
                matched_string.clear()
                print (matched_string)
                pos_x=200
                l=0
                for i in data:
                     compare= SequenceMatcher(None,word,i)
                     if(compare.ratio()>=0.7): #compares the similarity ratio
                             matched_string.append(i)
                             result=False
                if (result==False):
                    self.tb.insert(tk.END,"the word does not exist")

                    #self.msg=tk.Label(root,text="sorry the word doent exist",font=("Arial Bold",12))
                    #self.msg.place(x=500,y=500)


                for x in matched_string[:3]:
                         word=str(x)
                         l=l+1
                         self.new_button=tk.Button(root,text=word)
                         self.new_button['command']=lambda x=word,bin=self.new_button:(self.find_word(root,x))
                         self.new_button.pack()
                         print("button created")
                         self.buttons.append(self.new_button)
                         self.new_button.place(relx=0.25*l,y=155,width=50,anchor='center')
                         self.buttons.append(self.new_button)







window=tk.Tk()

dict_app(window)
window.mainloop()
