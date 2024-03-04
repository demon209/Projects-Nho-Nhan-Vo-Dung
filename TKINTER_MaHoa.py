#Từ điển dịch mã

teen_code= {'a':'4', 'b':'|3', 'd':'|)', 'e':'3', 'i':'j', 'o':'0', 'y':'ij', 'l':'|_', 's':'z', 'g':'q', 'kh':'h', 'ph':'f', 'c ':'k ', 'gi':'j'}
morse={'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..',
        '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----',
        '.':'.-.-.-',',':'--..--','?':'..--..','`':'.---.','!':'-.-.--','/':'-..-.',':':'---...',';':'-.-.-.','=':'-...-','+':'.-.-.','-':'-....-','_':'..--.-','"':'-..-.','@':'.--.-.',' ':'/'}
base64={} # ???
# có thể tự thêm từ điển để mở rộng chương trình


from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox 
#TAO TKINTER
mh=Tk()
mh.title('ENCODER BY QUAN')
mh.geometry('500x100')
mh.resizable(0,0)
mh.attributes("-topmost",False)



#Label 

wcome=Label(mh,font=('Time New Roman',14),text='Lựa chọn chế độ dịch mã: ')
wcome.place(x=10,y=10)
#TAO COMBO BOX  
combo=Combobox(mh,font=('Time New Roman',14),width=20)   #thiet lap hien thi
combo['value']=('Tiếng Việt sang teencode','Mã hóa morse')
combo.current(0)
combo.place(x=250,y=10)

# Tạo Cửa sổ kết quả và auto copy
def XulyDl(vban,mh):
    popup = Toplevel(mh)
    popup.title("Kết quả (Đã Tự Động Copy Vào Clipboard)")
    popup.geometry("500x300")

    # Thêm khung văn bản vào cửa sổ pop-up
    text_frame = Frame(popup)
    text_frame.pack()

    # Tạo widget Label hiển thị kết quả
    result_label = Label(text_frame, text=vban, font=("Courier", 12))
    result_label.pack()

    # Tự động copy vào clipboard
    mh.title("getherefast")
    def gtc(dtxt):
        mh.withdraw()
        mh.clipboard_clear()
        mh.clipboard_append(dtxt)
        mh.update()
    tkinter.Button(text='', command=gtc(vban)).grid(column=1, row=0)

# Tạo hàm button
def click():
    s=combo.get() 
    #get dữ liệu nhập vào
    if s == 'Tiếng Việt sang teencode':
        mh=Tk()
        mh.title('TIẾNG VIỆT SANG TEEN CODE')
        mh.geometry('1500x150')
        mh.attributes("-topmost",False)
        lbl1 = Label(mh, text="Nhập câu không dấu: ",font=('Time New Roman',14)) 
        lbl1.place(x=0,y=0) 
        entry = Entry(mh,width=350,font=('Time New Roman',12))
        entry.place(x=30,y=30)
        entry.focus()
    #tạo button
        def click():
            global teen_code
            s=str(entry.get())
            s=s.lower()+' ';
            i=0
            def ktra(s):
                global teen_code
                if s in teen_code:
                    return True
                return False
            x=''
            while i<len(s):
                if ktra(s[i]) and s[i:i+2]!='gi':
                    x+=teen_code[s[i]]
                    i+=1
                else:
                    if ktra(s[i:i+2]):
                        x+=teen_code[s[i:i+2]]
                        i+=2
                    else:
                        x+=s[i]
                        i+=1
            

            XulyDl(x,mh)

    # Create an previos button.
        b2 = Button(mh, text = "QUAY LẠI",
                    command = mh.destroy)
        b2.place(x=680,y=60)
    # Create an exchange button for encode/decode
        but=Button(mh,text='EXCHANGE',command=click)
        but.place(x=600,y=60)
       
    if s=='Mã hóa morse':
        mh=Tk()
        mh.title('MÃ HÓA MORSE')
        mh.geometry('1500x150')
        mh.attributes("-topmost",False)
        lbl1 = Label(mh, text="Nhập câu không dấu: ",font=('Time New Roman',14)) 
        lbl1.place(x=0,y=0) 
        entry = Entry(mh,width=250,font=('Time New Roman',10))
        entry.place(x=30,y=30)
        entry.focus()
        def click():
            global teen_code
            s=str(entry.get())
            s=s.lower();
            i=0
            def checkmorse(a):
                global morse
                if a in morse:
                    return True
                return False
            s=s.upper()
            i=0;x=''
            while i<len(s):
                if checkmorse(s[i]):
                    x+=morse[s[i]]
                    x+=' '
                    i+=1
                else:
                    x+= '# '
                    i+=1

            XulyDl(x,mh)

     # Create an previos button.
 
        b2 = Button(mh, text = "QUAY LẠI",
                        command = mh.destroy)
        b2.place(x=680,y=60)
    # Create an exchange button for encode/decode
        but=Button(mh,text='EXCHANGE',command=click)
        but.place(x=600,y=60)

# create an choose button
but=Button(mh,text='CHOOSE',command=click)
but.place(x=340,y=50)

#xử lí dữ liệu khi chọn exit (cửa sổ pop_up xác nhận)
def Exit():
    result=tkinter.messagebox.askquestion('Heyy','Bạn có thật sự muốn thoát?')
    if result=='yes':
        mh.destroy() #Closing Tkinter window forcefully.
but2=Button(mh,text='EXIT',command= Exit)
but2.place(x=420,y=50)
mh.mainloop()
