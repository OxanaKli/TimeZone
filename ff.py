import sys
from PyQt5.QtWidgets import(QApplication, QWidget,\
    QLabel,QLineEdit,QPushButton,QMessageBox)
from PyQt5.QtGui import QIcon

def Calc():
    t1=int(le1.text())
    m=int(le2.text())
    L1=int(le3.text())
    L2=int(le4.text())
    n=int(le5.text())
    d0=int(le6.text())
    m0=int(le7.text())
    h0=int(le8.text())
    z1=60
    L0=((L1+L2/z1)*4)/z1
    t01=t1-3
    t2=t1+m/z1
    t0=t2-2
    if t0<0:
        t0=t0+24
    h=t0//1
    h1=((t0-h)*z1+0.51)//1
    t3=t0+L0
    if t3>24:
        t4=t3-24
        t5=t4//1
        t6=((t4-t5)*z1+0.51)//1
    else:
        t5=t3//1
        t6=((t3-t5)*z1+0.51)//1
    t7=t0+n
    if t7>24:
        t8=t7-24
        m1=t8//1
        m2=((t8-m1)*z1+0.51)//1
    else:
        m1=t7//1
        m2=((t7-m1)*z1+0.51)//1
    if t3>24 and t7>24:
        d=d0+1
    lb10.setText("Day {}, Month {}, Year {}".format(d,m0,h0))
    lb10.resize(200, lb10.height())
    lb12.setText("{} h. {} min.".format(t5,t6))
    lb12.resize(200, lb12.height())
    lb14.setText("{} h. {} min.".format(m1,m2))
    lb14.resize(200,lb14.height())
    lb16.setText("{} h. {} min.".format(t1,m))
    lb16.resize(200, lb16.height())
    lb18.setText("{} h. {} min.".format(t01,h1))
    lb18.resize(200, lb18.height())
    
   
 
def Check():
    if len(le1.text())>0 and len(le2.text())>0 and len(le3.text())>0 and len(le4.text())>0 and len(le5.text())>0 and len(le6.text())>0 and len(le7.text())>0 and len(le8.text())>0:
        btn1.setEnabled(True)
    else:
        btn1.setEnabled(False)    
    

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('Calculation of local, zone, and world time for a point with a specified longitude')
w.resize(800, 600)
w.move(200, 300)

lb1=QLabel("Msk time hours =",w);lb1.move(20,20)
lb2=QLabel("Msk time minutes =",w);lb2.move(20,60)
lb3=QLabel("Longitude degrees =",w);lb3.move(20,100)
lb4=QLabel("Longitude minutes =  ",w);lb4.move(20,140)
lb5=QLabel("Time zone =",w);lb5.move(350,20)
lb6=QLabel("Day of calculation =",w);lb6.move(350,60)
lb7=QLabel("Month of calculation =",w);lb7.move(350,100)
lb8=QLabel("Year of calculation =",w);lb8.move(350,140)

lb9=QLabel("New data =",w);lb9.move(20,200)
lb10=QLabel("?",w);lb10.move(200,200)
lb11=QLabel("Local time Tm=",w);lb11.move(20,250)
lb12=QLabel("?",w);lb12.move(200,250)
lb13=QLabel("Zone time Tp =",w);lb13.move(20,300)
lb14=QLabel("?",w);lb14.move(200,300)
lb15=QLabel("Msk time Tmsk=",w);lb15.move(20,350)
lb16=QLabel("?",w);lb16.move(200,350)
lb17=QLabel("World time Twrld=",w);lb17.move(20,400)
lb18=QLabel("?",w);lb18.move(200,400)

le1=QLineEdit(w);le1.move(180,20)
le1.textChanged.connect(Check)
le2=QLineEdit(w);le2.move(180,60)
le2.textChanged.connect(Check)
le3=QLineEdit(w);le3.move(180,100)
le3.textChanged.connect(Check)
le4=QLineEdit(w);le4.move(180,140)
le4.textChanged.connect(Check)

le5=QLineEdit(w);le5.move(480,20)
le5.textChanged.connect(Check)
le6=QLineEdit(w);le6.move(480,60)
le6.textChanged.connect(Check)
le7=QLineEdit(w);le7.move(480,100)
le7.textChanged.connect(Check)
le8=QLineEdit(w);le8.move(480,140)
le8.textChanged.connect(Check)


btn1=QPushButton("Calculation",w);btn1.move(350,550)
btn1.clicked.connect(Calc)

w.show()
sys.exit(app.exec_())
