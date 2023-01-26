# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 13:41:16 2023

@author: 0wv72
"""

import tkinter
sum=0
root  = tkinter.Tk()
canvas = tkinter.Canvas(width=400,height=300)
img = tkinter.PhotoImage(file="""haikei1.gif""", width=400, height=300,)
scene = 0
nk=1
font1 =("Terninal",20)
font2 =("Terninal",13)
font3 =("Terninal",30)
img_2 =tkinter.PhotoImage(file="""xdK63QKYmI9Pc0p1674306945_1674307314 (1).gif""", width=400, height=300,)
img_3 =tkinter.PhotoImage(file="haikeiiii.gif", width=400, height=300)
img_4 =tkinter.PhotoImage(file="onnna1.gif", width=400, height=300)
img_5 =tkinter.PhotoImage(file="hukidasi2.gif",width=400,height=300)
img_6 =tkinter.PhotoImage(file="senyakusi2.gif")
img_7 =tkinter.PhotoImage(file="mesuwaka.gif")
img_8 =tkinter.PhotoImage(file="dekaonnnna.gif")

photo=tkinter.PhotoImage(file=r"C:\Users\0wv72\Desktop\新しいフォルダー (2)\manofade.gif",master=root)
gif_index = 0
a=0
y=0
def next_frame():
    if a==0:   
        global gif_index
        try:
            canvas.create_image(200,150,image=photo,tag="AAA")    
            photo.configure(format="gif -index {}".format(gif_index))
        
            gif_index += 1
        except tkinter.TclError:
            canvas.delete("AAA")
            canvas.create_rectangle(0,0,400,300,fill="black",tag="RULE")
            
            canvas.create_image(1,1, image=img_2, anchor=tkinter.NW,tag="RULE")
            canvas.create_text(200,260,text="PRESS a",fill="white",font=font2,tag="RULE")
             
        except key == "a":
                canvas.delete("RULE")
                gif_index = 0 
                scene = 3 
                
                       
        else:
            root.after(100, next_frame) 
def next_frame_2():
    if a==0:   
        global gif_index
        try:
            canvas.create_image(200,150,image=photo,tag="AAA")    
            photo.configure(format="gif -index {}".format(gif_index))
        
            gif_index += 1
        except tkinter.TclError:
            canvas.delete("AAA")
            canvas.create_rectangle(0,0,400,300,fill="black",tag="RULE")
             
            canvas.create_image(1,1, image=img_3, anchor=tkinter.NW,tag="RULE")
            
             
        except key == "s":
                canvas.delete("RULE")
                 
                scene = 4
                
                       
        else:
            root.after(100, next_frame) 
key = ""
def key(e):
    global key
    key = e.keysym


x = 0
def scroll():
    if scene == 0: 
        global x
        x = (x+0.6)%400
        
        canvas.delete("IMAGE")
        
        canvas.create_image(x-200,150,image=bgimage,tag="IMAGE")
        canvas.create_image(x+200,150,image=bgimage,tag="IMAGE")
       
        canvas.create_image(1,1, image=img, anchor=tkinter.NW,tag="IMAGE")
        canvas.create_text(200,250,text="PRESS THE SPACEKEY!!",fill="lime",font=font1,tag="TITLE")

        root.after(100,scroll)
def onnna1():
    
    canvas.create_image(1,1, image=img_4, anchor=tkinter.NW,tag="IMAGE1")

    root.after(1000,onnna1)   
def hukidashi1():
    
    canvas.create_image(200,150, image=img_5,tag="IMAGE3")
    root.after(3000,hukidashi1)
def senntakushi1():
    
    canvas.create_image(200,150, image=img_6,tag="IMAGE2")
    root.after(6000,senntakushi1)
root.title("meikoi")
def hideimage1():
    canvas.delete("IMAGE1")
def main():
    global y
    global scene
    canvas.delete("STATUS")

       

    if scene == 0:
        canvas.delete("RULE")
        y=0
        canvas.delete("TITLE")
        scroll()
        
        
 
     
        
        if key == "space":
            canvas.delete("TITLE")
            canvas.delete("IMAGE")       
            scene = 1

    if scene ==1:
        
        next_frame()
        

    if scene == 2:
        canvas.delete("RULE")
        canvas.delete("IMAGE")
        
            
        canvas.create_rectangle(0,0,400,300,fill="black",tag="RULE")
        
        canvas.create_image(1,1, image=img_2, anchor=tkinter.NW,tag="RULE")
        canvas.create_text(200,260,text="PRESS a",fill="white",font=font2,tag="RULE")
        
    if key == "a":
        canvas.delete("RULE")
            
        scene = 3

    if scene == 3:
        
        canvas.create_image(1,1, image=img_3, anchor=tkinter.NW,tag="RULE") 
        canvas.create_text(200,150,text="PRESS q w e",fill="red",font=font3,tag="TEXT")
        if key =="q" and y==0 :
            canvas.create_image(1,1, image=img_4, anchor=tkinter.NW,tag="IMAGE1")
            canvas.delete("TEXT")
        
        if key =="w" and y==0:
            y=1
        if key =="w" and y==1:
            canvas.create_image(1,1, image=img_4, anchor=tkinter.NW,tag="IMAGE1")
            canvas.create_image(200,150, image=img_6,tag="IMAGE2")
            canvas.delete("TEXT")
        
        if key =="e" and y==1: 
            
            y=2
        if key =="e" and y==2 :
            canvas.create_image(1,1, image=img_4, anchor=tkinter.NW,tag="IMAGE1")
            canvas.create_image(200,150, image=img_6,tag="IMAGE2")
            canvas.create_image(200,150, image=img_5,tag="IMAGE3") 
            canvas.create_text(200,30,text="Where is 212 classroom?",fill="black",font=font2,tag="IMAGE3")
            canvas.create_text(140,180,text="z:第一校舎",fill="black",font=font2,tag="answer")
            canvas.create_text(140,250,text="x:メディア棟",fill="black",font=font2,tag="answer")
            canvas.create_text(250,180,text="c:図書館",fill="black",font=font2,tag="answer")
            canvas.create_text(250,250,text="v:食堂",fill="black",font=font2,tag="answer")
            canvas.delete("TEXT")
        if key=="x" and y==2:
            canvas.create_rectangle(0,0,400,300,fill="green",tag="GAMEOVER")
            canvas.create_text(200,150,text="ゲームオーバー",fill="white",font=font2,tag="GAMEOVER")
            canvas.create_text(200,250,text="PRESS THE gKEY",fill="white",font=font2,tag="GAMEOVER")
            if key == "g":
                canvas.delete("GAMEOVER")
                canvas.delete("RULE")
                scene=0
        if key=="c" and y==2:
            canvas.create_rectangle(0,0,400,300,fill="green",tag="GAMEOVER")
            canvas.create_text(200,150,text="ゲームオーバー",fill="white",font=font2,tag="GAMEOVER")
            canvas.create_text(200,250,text="PRESS THE gKEY",fill="white",font=font2,tag="GAMEOVER")
            if key == "g":
                canvas.delete("GAMEOVER")
                canvas.delete("RULE")
                scene=0
        if key=="v" and y==2:
            canvas.create_rectangle(0,0,400,300,fill="green",tag="GAMEOVER")
            canvas.create_text(200,150,text="ゲームオーバー",fill="white",font=font2,tag="GAMEOVER")
            canvas.create_text(200,250,text="PRESS THE gKEY",fill="white",font=font2,tag="GAMEOVER")
            if key == "g":
                canvas.delete("GAMEOVER")
                canvas.delete("RULE")
                scene=0
        if key=="z" and y==2:
            y=3
        if key=="z" and y==3:
            canvas.create_image(200,150, image=img_6,tag="IMAGE2")
            canvas.create_image(200,150, image=img_5,tag="IMAGE3") 
            canvas.delete("TEXT")
            canvas.create_text(200,30,text="press k!",fill="black",font=font2,tag="TEXT2")
            
        if key=="k" and y==3:
            y=4
        if key=="k" and y==4:
            canvas.delete("TEXT2")
            canvas.delete("TEXT")
            
            canvas.create_image(200,150, image=img_7,tag="IMAGE4") 
            canvas.create_image(200,150, image=img_6,tag="IMAGE2")
            canvas.create_image(200,150, image=img_5,tag="IMAGE3") 
            canvas.create_text(200,30,text="rock paper scissors!",fill="black",font=font2,tag="TEXT2")
            canvas.create_text(140,180,text="z:ぱー",fill="black",font=font2,tag="answer")
            canvas.create_text(140,250,text="x:ぐー",fill="black",font=font2,tag="answer")
            canvas.create_text(250,180,text="c:ちょき",fill="black",font=font2,tag="answer")
            canvas.create_text(250,250,text="v:無視",fill="black",font=font2,tag="answer")
            
        if key=="x":
            y=5
        if key=="x" and y==5:
            canvas.delete("TEXT")
            canvas.create_image(200,150, image=img_6,tag="IMAGE2")
            canvas.create_image(200,150, image=img_5,tag="IMAGE3") 
            canvas.create_text(200,30,text="press j!",fill="black",font=font2,tag="TEXT2")
            
        if key=="z" and y==4:
             canvas.create_rectangle(0,0,400,300,fill="green",tag="GAMEOVER")
             canvas.create_text(200,150,text="ゲームオーバー",fill="white",font=font2,tag="GAMEOVER")
             canvas.create_text(200,250,text="PRESS THE gKEY",fill="white",font=font2,tag="GAMEOVER")
             if key == "g":
                 canvas.delete("GAMEOVER")
                 canvas.delete("RULE")
                 scene=0
        if key=="c" and y==4:
             canvas.create_rectangle(0,0,400,300,fill="green",tag="GAMEOVER")
             canvas.create_text(200,150,text="ゲームオーバー",fill="white",font=font2,tag="GAMEOVER")
             canvas.create_text(200,250,text="PRESS THE gKEY",fill="white",font=font2,tag="GAMEOVER")
             if key == "g":
                 canvas.delete("GAMEOVER")
                 canvas.delete("RULE")
                 scene=0
        if key=="v" and y==4:
             canvas.create_rectangle(0,0,400,300,fill="green",tag="GAMEOVER")
             canvas.create_text(200,150,text="ゲームオーバー",fill="white",font=font2,tag="GAMEOVER")
             canvas.create_text(200,250,text="PRESS THE gKEY",fill="white",font=font2,tag="GAMEOVER")
             if key == "g":
                 canvas.delete("GAMEOVER")
                 canvas.delete("RULE")
                 scene=0
        if key=="j" and y==5:
            y=6
        if key=="j" and y==6:
            canvas.delete("TEXT2")
            canvas.delete("TEXT")
            
            canvas.create_image(200,150, image=img_8,tag="IMAGE4") 
            canvas.create_image(200,150, image=img_6,tag="IMAGE2")
            canvas.create_image(200,150, image=img_5,tag="IMAGE3") 
            canvas.create_text(200,30,text="What gets whiter the dirtier it gets? ",fill="black",font=font2,tag="TEXT2")
            canvas.create_text(140,180,text="z:髪",fill="black",font=font2,tag="answer")
            canvas.create_text(140,250,text="x:心",fill="black",font=font2,tag="answer")
            canvas.create_text(250,180,text="c:消しゴム",fill="black",font=font2,tag="answer")
            canvas.create_text(250,250,text="v:黒板",fill="black",font=font2,tag="answer")
           
        if key=="z" and y==6:
              canvas.create_rectangle(0,0,400,300,fill="green",tag="GAMEOVER")
              canvas.create_text(200,150,text="ゲームオーバー",fill="white",font=font2,tag="GAMEOVER")
              canvas.create_text(200,250,text="PRESS THE gKEY",fill="black",font=font2,tag="GAMEOVER")
              if key == "c":
                  canvas.delete("GAMEOVER")
                  canvas.delete("RULE")
                  scene=0
        if key=="c" and y==6:
              canvas.create_rectangle(0,0,400,300,fill="green",tag="GAMEOVER")
              canvas.create_text(200,150,text="ゲームオーバー",fill="white",font=font2,tag="GAMEOVER")
              canvas.create_text(200,250,text="PRESS THE gKEY",fill="black",font=font2,tag="GAMEOVER")
              if key == "g":
                  canvas.delete("GAMEOVER")
                  canvas.delete("RULE")
                  scene=0
        if key=="ｘ" and y==6:
              canvas.create_rectangle(0,0,400,300,fill="green",tag="GAMEOVER")
              canvas.create_text(200,150,text="ゲームオーバー",fill="white",font=font2,tag="GAMEOVER")
              canvas.create_text(200,250,text="PRESS THE gKEY",fill="black",font=font2,tag="GAMEOVER")
              if key == "g":
                  canvas.delete("GAMEOVER")
                  canvas.delete("RULE")
                  scene=0
        if key=="v" and y==6:
              canvas.create_rectangle(0,0,400,300,fill="yellow",tag="GAMECLEAR")
              canvas.create_text(200,150,text="ゲームクリア！",fill="red",font=font3,tag="GAMECLEAR")
              canvas.create_text(200,250,text="PRESS THE gKEY",fill="black",font=font2,tag="GAMECLEAR")
              if key == "g":
                  canvas.delete("GAMECLEAR")
                  canvas.delete("RULE")
                  scene=0
        
        
        
        if key == "g":
           
           
           scene = 0
        

    
    
    
    root.after(1000, main)

canvas.pack()

    
    
root.bind("<KeyPress>", key)
bgimage = tkinter.PhotoImage(file="""kumo.gif""")

main()
root.mainloop()