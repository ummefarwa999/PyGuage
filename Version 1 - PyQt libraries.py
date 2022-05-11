import sys
from PyQt4 import QtGui, QtCore

#import serial, time
#import os, sys
#import matplotlib
#import numpy as np
#from matplotlib import cm
#from matplotlib import pyplot as plt
#from matplotlib.patches import Circle, Wedge, Rectangle

########################################################################################################################
def degree_range(n): 
    start = np.linspace(0,180,n+1, endpoint=True)[0:-1]
    end = np.linspace(0,180,n+1, endpoint=True)[1::]
    mid_points = start + ((end-start)/2.)
    return np.c_[start, end], mid_points

def rot_text(ang): 
    rotation = np.degrees(np.radians(ang) * np.pi / np.pi - np.radians(90))
    return rotation

########################################################################################################################
def Init_Gauge(fig,ax,ID='Battery ID'):
    labels=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']
    colors='jet_r'
    cat=6
    title=''
    fname='./meter.png' 

    N = len(labels)
    if isinstance(colors, str):
        cmap = cm.get_cmap(colors, N)
        cmap = cmap(np.arange(N))
        colors = cmap[::-1,:].tolist()
    if isinstance(colors, list): 
        if len(colors) == N:
            colors = colors[::-1]
        else: 
            raise Exception("\n\nnumber of colors {} not equal to number of categories{}\n".format(len(colors), N))

    # begins the plotting
    ang_range, mid_points = degree_range(N)
    labels = labels[::-1]

    # plots the sectors and the arcs
    patches = []
    for ang, c in zip(ang_range, colors): 
        # sectors
        patches.append(Wedge((0.,0.), .02, *ang, facecolor='w', lw=2))
        # arcs
        patches.append(Wedge((0.,0.), .02, *ang, width=0.005, facecolor=c, lw=0.6, alpha=0.5))

    [ax.add_patch(p) for p in patches]

    # set the labels (e.g. 'LOW','MEDIUM',...)
    # 0.15 represent the r of the circule.
    for mid, lab in zip(mid_points, labels): 
        ax.text(0.018 * np.cos(np.radians(mid)), 0.018 * np.sin(np.radians(mid)), lab,horizontalalignment='center', verticalalignment='center', fontsize=6,fontweight='bold', rotation = rot_text(mid))

    # set the bottom banner and the title
    # r = Rectangle((-0.007,-0.001),0.014,0.002, facecolor='w', lw=2,label='Label')
    # ax.add_patch(r)

    ax.text(0, -0.05, title, horizontalalignment='center',verticalalignment='center', fontsize=22, fontweight='bold')

    # plots the arrow now
    ax.add_patch(Circle((0, 0), radius=0.002, facecolor='k'))
    ax.add_patch(Circle((0, 0), radius=0.001, facecolor='w', zorder=11))  # circle in the arrow.

    #removes frame and ticks, and makes axis equal and tight
    ax.set_frame_on(False)
    ax.axes.set_xticks([])
    ax.axes.set_yticks([])
    ax.axis('equal')
    ax.margins(tight=True)


    ang_range, mid_points = degree_range(N*10)
    # Arrow of the first gauge

    ax.text(-0.004,-0.01 ,ID)   #battery ID
    TX = ax.text(-0.004,-0.006 ,'Value : '+ str(0))
    AR = ax.arrow(0, 0, 0.007 * np.cos(np.radians(0)), 0.007 * np.sin(np.radians(0)),width=0.002, head_width=0.002, head_length=0.01, fc='k', ec='k')
    
    return TX,AR,mid_points
########################################################################################################################
def Update(ax,cat,AR,TX,mid_points):
    AR.remove()
    TX.remove()
    # TX = ax.text(-0.003,-0.004 , "")
    TX = ax.text(-0.003,-0.006 ,'Value : '+ str(cat))
    pos = mid_points[abs(cat - 240)]
    AR = ax.arrow(0, 0, 0.007 * np.cos(np.radians(pos)), 0.007 * np.sin(np.radians(pos)),width=0.002, head_width=0.002, head_length=0.01, fc='k', ec='k')
    plt.ion() 
    plt.pause(0.0001)
    return AR,TX
########################################################################################################################

     

def main():
    dialMaxValue = 120
    dialFactor = 5
    fontsize = 30
    app 	= QtGui.QApplication(sys.argv)
    tabs	= QtGui.QTabWidget()
 
    # Create tabs
    tab1	= QtGui.QWidget()	
    tab2	= QtGui.QWidget()
 
    # Resize width and height
    tabs.resize(1000, 500)
 
    # Set layout of first tab
    vBoxlayout	= QtGui.QGridLayout()
    vBoxlayout1	= QtGui.QGridLayout()
    font = QtGui.QFont()
    font.setPointSize(fontsize)
    font.setBold(True)

    dial = QtGui.QDial()
    dial.setNotchesVisible(True)
    label = QtGui.QLabel('0')
    label.setFont(font)
    label.setAlignment(QtCore.Qt.AlignCenter)
    dial.setMaximum(dialMaxValue )
                         

    dial1 = QtGui.QDial()
    dial1.setNotchesVisible(True)
    label1 = QtGui.QLabel('0')
    label1.setFont(font)
    label1.setAlignment(QtCore.Qt.AlignCenter)
    dial1.setMaximum(dialMaxValue)


    dial2 = QtGui.QDial()
    dial2.setNotchesVisible(True)
    label2 = QtGui.QLabel('0')
    label2.setFont(font)
    label2.setAlignment(QtCore.Qt.AlignCenter)
    dial2.setMaximum(dialMaxValue)

    dial3 = QtGui.QDial()
    dial3.setNotchesVisible(True)
    label3 = QtGui.QLabel('0')
    label3.setFont(font)
    label3.setAlignment(QtCore.Qt.AlignCenter)
    dial3.setMaximum(dialMaxValue)

    dial4 = QtGui.QDial()
    dial4.setNotchesVisible(True)
    label4 = QtGui.QLabel('0')
    label4.setFont(font)
    label4.setAlignment(QtCore.Qt.AlignCenter)
    dial4.setMaximum(dialMaxValue)

    dial5 = QtGui.QDial()
    dial5.setNotchesVisible(True)
    label5 = QtGui.QLabel('0')
    label5.setFont(font)
    label5.setAlignment(QtCore.Qt.AlignCenter)
    dial5.setMaximum(dialMaxValue)
                         

    dial6 = QtGui.QDial()
    dial6.setNotchesVisible(True)
    label6 = QtGui.QLabel('0')
    label6.setFont(font)
    label6.setAlignment(QtCore.Qt.AlignCenter)
    dial6.setMaximum(dialMaxValue)


    dial7 = QtGui.QDial()
    dial7.setNotchesVisible(True)
    label7 = QtGui.QLabel('0')
    label7.setFont(font)
    label7.setAlignment(QtCore.Qt.AlignCenter)
    dial7.setMaximum(dialMaxValue)

    dial8 = QtGui.QDial()
    dial8.setNotchesVisible(True)
    label8 = QtGui.QLabel('0')
    label8.setFont(font)
    label8.setAlignment(QtCore.Qt.AlignCenter)
    dial8.setMaximum(dialMaxValue)

    dial9 = QtGui.QDial()
    dial9.setNotchesVisible(True)
    label9 = QtGui.QLabel('0')
    label9.setFont(font)
    label9.setAlignment(QtCore.Qt.AlignCenter)
    dial9.setMaximum(dialMaxValue)

           
    vBoxlayout.addWidget(dial,0,0)
    vBoxlayout.addWidget(dial1,0,1)
    
    
    vBoxlayout.addWidget(dial2,0,2)
    
    vBoxlayout.addWidget(dial3,0,3)
    
    
    vBoxlayout.addWidget(dial4,0,4)

    vBoxlayout.addWidget(label,1,0)
    vBoxlayout.addWidget(label1,1,1)
    vBoxlayout.addWidget(label2,1,2)
    vBoxlayout.addWidget(label3,1,3)
    vBoxlayout.addWidget(label4,1,4)
   
    
    tab1.setLayout(vBoxlayout)
    
    vBoxlayout1.addWidget(dial5,0,0)
        
    
    vBoxlayout1.addWidget(dial6,0,1)
    
    
    vBoxlayout1.addWidget(dial7,0,2)
    
    
    vBoxlayout1.addWidget(dial8,0,3)
    
    
    vBoxlayout1.addWidget(dial9,0,4)

    vBoxlayout1.addWidget(label5,1,0)
    vBoxlayout1.addWidget(label6,1,1)
    vBoxlayout1.addWidget(label7,1,2)
    vBoxlayout1.addWidget(label8,1,3)
    vBoxlayout1.addWidget(label9,1,4)
    

    tab2.setLayout(vBoxlayout1)


    # Set layout of second tab
   
 
    # Add tabs
    tabs.addTab(tab1," 1 ")
    tabs.addTab(tab2," 2 ")
    # Set title and show
    tabs.setWindowTitle('PyGauge')
    tabs.show()

    #SERIALPORT = "/dev/ttyAMA0"
    #BAUDRATE = 9600
    #ser = serial.Serial(SERIALPORT, BAUDRATE)
    #ser.bytesize = serial.EIGHTBITS         #number of bits per bytes
    #ser.parity = serial.PARITY_NONE         #set parity check: no parity
    #ser.stopbits = serial.STOPBITS_ONE      #number of stop bits
    #ser.timeout = None                     #block read
    #ser.timeout = 0                        #non-block read
    #ser.timeout = None                      #timeout block read
    #ser.xonxoff = False                     #disable software flow control
    #ser.rtscts = False                      #disable hardware (RTS/CTS) flow control
    #ser.dsrdtr = False                      #disable hardware (DSR/DTR) flow control
    #ser.writeTimeout = 0                    #timeout for write

    #while True:
    #print 'Starting Up Serial Monitor'

    #if ser.isOpen():
    try:
	#ser.flushInput()            #flush input buffer, discarding all its contents
        #ser.flushOutput()           #flush output buffer, aborting current output
	#ser.write("RB0\r\n")
        #response = ser.readline()
        #VAL1 = int(response)
        VAL1 = 12.6
    	newVAL1=(VAL1*dialFactor)	    # Multiplying factor dialFactor'' for dial's corresponding value
    	dial.setValue(newVAL1)      
    	label.setNum(VAL1)
        #  AR1,TX1 = Update(ax,VAL1,AR1,TX1,mid_points1)

        #ser.write("RB1\r\n")
        #response = ser.readline()
        #VAL2 = int(response)
        VAL2 = 6.6
 	newVAL2=(VAL2*dialFactor)	    
    	dial1.setValue(newVAL2)      
    	label1.setNum(VAL2)
        # AR2,TX2 = Update(ax,VAL2,AR2,TX2,mid_points2)

        #ser.write("RB2\r\n")
        #response = ser.readline()
        #VAL3 = int(response)
        VAL3 = 8.6
    	newVAL3=(VAL3*dialFactor)	    
    	dial2.setValue(newVAL3)      
    	label2.setNum(VAL3)
        # AR3,TX3 = Update(ax,VAL3,AR3,TX3,mid_points3)

        #ser.write("RB3\r\n")
        #response = ser.readline()
        #VAL4 = int(response)
        VAL4 = 15.7
    	newVAL4=(VAL4*dialFactor)	   
    	dial3.setValue(newVAL4)      
 	label3.setNum(VAL4)
	# AR4,TX4 = Update(ax,VAL4,AR4,TX4,mid_points4)

        #ser.write("RB4\r\n")
        #response = ser.readline()
        #VAL5 = int(response)
        VAL5 = 2.2
    	newVAL5=(VAL5*dialFactor)	    
    	dial4.setValue(newVAL5)      
    	label4.setNum(VAL5)
        # AR5,TX5 = Update(ax,VAL5,AR5,TX5,mid_points5)

        #ser.write("RB5\r\n")
        #response = ser.readline()
        #VAL6 = int(response)
        VAL6 = 4.5
    	newVAL6=(VAL6*dialFactor)	   
    	dial5.setValue(newVAL6)      
    	label5.setNum(VAL6)
        #AR6,TX6 = Update(ax,VAL6,AR6,TX6,mid_points6)

        #ser.write("RB6\r\n")
        #response = ser.readline()
        #VAL7 = int(response)
        VAL7 = 19.1
 	newVAL7=(VAL7*dialFactor)	    
 	dial6.setValue(newVAL7)      
 	label6.setNum(VAL7)
        #AR7,TX7 = Update(ax,VAL7,AR7,TX7,mid_points7)

        #ser.write("RB7\r\n")
        #response = ser.readline()
        #VAL8 = int(response)
        VAL8 = 10.6
    	newVAL8=(VAL8*dialFactor)	    
    	dial7.setValue(newVAL8)      
    	label7.setNum(VAL8)
        #AR8,TX8 = Update(ax,VAL8,AR8,TX8,mid_points8)
                   
        #ser.write("RB8\r\n")
        #response = ser.readline()
        #VAL9 = int(response)
        VAL9 = 2.6
    	newVAL9=(VAL9*dialFactor)	    
    	dial8.setValue(newVAL9)      
    	label8.setNum(VAL9)
        #  AR9,TX9 = Update(ax,VAL9,AR9,TX9,mid_points9)

        #ser.write("RB9\r\n")
        #response = ser.readline()
        #VAL10 = int(response)
        VAL10 = 11.6
        newVAL10=(VAL10*dialFactor)	   
    	dial9.setValue(newVAL10)      
    	label9.setNum(VAL10)
        #  AR10,TX10 = Update(ax,VAL10,AR10,TX10,mid_points10)

        #time.sleep(0)
        #numberOfLine = 0

        #ser.close()

    except Exception, e:
                    print "error communicating...: " + str(e)
    #else:
            #print "cannot open serial port "
        
     
    sys.exit(app.exec_())
 
 
if __name__ == '__main__':
    main()
