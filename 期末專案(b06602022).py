#姓名/系級/學號: 馬紹勻/生工二/b06602022
#程式名稱:賭博小幫手
#使用套件:BeautifulSoup、requests、tkinter
#=============================================
#輸出GUI介面
import tkinter
#----條件式
def select():
    num2=num1.get()
    if num2 == 1:
        data_1()
    elif num2 == 2:
        data_2()
    elif num2 == 3:
        data_3()
    elif num2 == 4:
        data_4()
    else:
        print('請輸入正確類別')
#----
win = tkinter.Tk()
win.title('賭博小幫手(Gambler)')
win.geometry('380x220')
text1 = '歡迎來到賭博小幫手~以下是我們提供的服務項目:\n[一、查詢當期號碼(熱門類別) 1.大樂透 2.威力彩 3.今彩539 4.四星彩]'
text2 = '輸入服務選項：'
num1 = tkinter.IntVar()
Label1=tkinter.Label(win,text=text1)
Label2=tkinter.Label(win,text=text2)
item1=tkinter.Entry(win,width=5,textvariable=num1)
btn=tkinter.Button(win,width=5,text='ok',command=select)
Label1.pack()
Label2.pack(side='left')
item1.pack(side='left')
btn.pack(side='left')

#==============================================
#大樂透
def data_1():
    from bs4 import BeautifulSoup
    import requests
    url = 'http://www.taiwanlottery.com.tw/index_new.aspx/'
    html = requests.get(url)
    bs = BeautifulSoup(html.text, 'html.parser')
    data1 = bs.select(".contents_box02") 
    data2 = data1[2].find_all('div', {'class':'ball_tx'})
    text3 ='===================='
    Label3=tkinter.Label(win,text=text3)
    Label3.pack()
#大樂透號碼
    text4 ='〔欲查詢項目: 大樂透〕'
    Label4=tkinter.Label(win,text=text4)
    Label4.pack()
    text5 ="[開出順序]"
    Label5=tkinter.Label(win,text=text5)
    Label5.pack()
    list1=[]
    for n in range(0,6):
        list1.append(data2[n].text)
    text6=str(list1)
    Label6=tkinter.Label(win,text=text6)
    Label6.pack()
    text7 ="[大小順序]"
    Label7=tkinter.Label(win,text=text7)
    Label7.pack()
    list2=[]
    for n in range(6,len(data2)):
        list2.append(data2[n].text)
    text8=str(list2)
    Label8=tkinter.Label(win,text=text8)
    Label8.pack()
#特別號
    red=data1[2].find('div', {'class':'ball_red'})#在第3個區塊中抓出紅球      
    text9 ="[特別號]"
    Label9=tkinter.Label(win,text=text9)
    Label9.pack()
    text10=red.text
    Label10=tkinter.Label(win,text=text10)
    Label10.pack()
    text11='===================='
    Label11=tkinter.Label(win,text=text11).pack()
#===============================================
#威力彩
def data_2():
    from bs4 import BeautifulSoup
    import requests
    url = 'http://www.taiwanlottery.com.tw/index_new.aspx/'
    html = requests.get(url)
    bs = BeautifulSoup(html.text, 'html.parser')
    data1 = bs.select(".contents_box02") 
    data2 = data1[0].find_all('div', {'class':'ball_tx'})
    text3 ='===================='
    Label3=tkinter.Label(win,text=text3)
    Label3.pack()
#威力彩號碼
    text4 ='〔欲查詢項目: 威力彩〕'
    Label4=tkinter.Label(win,text=text4)
    Label4.pack()
    text5 ="[開出順序]"
    Label5=tkinter.Label(win,text=text5)
    Label5.pack()
    list1=[]
    for n in range(0,6):
        list1.append(data2[n].text)
    text6=str(list1)
    Label6=tkinter.Label(win,text=text6)
    Label6.pack()
    text7 ="[大小順序]"
    Label7=tkinter.Label(win,text=text7)
    Label7.pack()    
    list2=[]
    for n in range(6,len(data2)):
        list2.append(data2[n].text)
    text8=str(list2)
    Label8=tkinter.Label(win,text=text8)
    Label8.pack()
#特別號
    red=data1[0].find('div', {'class':'ball_red'})#在第3個區塊中抓出紅球      
    text9 ="[特別號]"
    Label9=tkinter.Label(win,text=text9)
    Label9.pack()
    text10=red.text
    Label10=tkinter.Label(win,text=text10)
    Label10.pack()
    text11='===================='
    Label11=tkinter.Label(win,text=text11).pack()
#==============================================
#今彩539
def data_3():
    from bs4 import BeautifulSoup
    import requests
    url = 'http://www.taiwanlottery.com.tw/index_new.aspx/'
    html = requests.get(url)
    bs = BeautifulSoup(html.text, 'html.parser')
    data1 = bs.select(".contents_box03") 
    data2 = data1[0].find_all('div', {'class':'ball_tx'})
    text3 ='===================='
    Label3=tkinter.Label(win,text=text3)
    Label3.pack()
#號碼
    text4 ='〔欲查詢項目: 今彩539〕'
    Label4=tkinter.Label(win,text=text4)
    Label4.pack()
    text5 ="[開出順序]"
    Label5=tkinter.Label(win,text=text5)
    Label5.pack()
    list1=[]
    for n in range(0,5):
        list1.append(data2[n].text)
    text6=str(list1)
    Label6=tkinter.Label(win,text=text6)
    Label6.pack() 
    text7 ="[大小順序]"
    Label7=tkinter.Label(win,text=text7)
    Label7.pack()   
    list2=[]
    for n in range(5,len(data2)):
        list2.append(data2[n].text)
    text8=str(list2)
    Label8=tkinter.Label(win,text=text8)
    Label8.pack()
    text11='===================='
    Label11=tkinter.Label(win,text=text11).pack()
#==============================================
#四星彩
def data_4():
    from bs4 import BeautifulSoup
    import requests
    url = 'http://www.taiwanlottery.com.tw/index_new.aspx/'
    html = requests.get(url)
    bs = BeautifulSoup(html.text, 'html.parser')
    data1 = bs.select(".contents_box04") 
    data2 = data1[1].find_all('div', {'class':'ball_tx'})
    text3 ='===================='
    Label3=tkinter.Label(win,text=text3)
    Label3.pack()
#號碼
    text4 ='〔欲查詢項目: 四星彩〕'
    Label4=tkinter.Label(win,text=text4)
    Label4.pack()
    text5 ="[開出順序]"
    Label5=tkinter.Label(win,text=text5)
    Label5.pack()
    list1=[]
    for n in range(0,4):
        list1.append(data2[n].text)
    text6=str(list1)
    Label6=tkinter.Label(win,text=text6)
    Label6.pack()
    text11='===================='
    Label11=tkinter.Label(win,text=text11).pack()

win.mainloop()
#============================================
