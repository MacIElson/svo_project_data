import rosbag
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

def makePlot(test, save):

    fig = plt.figure()

    #ax = fig.add_subplot(111, projection='3d')

    XSqrPts = [0, 14, 14, 0, 0, 14, 14, 0, 0, 17, 17, -1, -2]
    YSqrPts = [0, 0, 4, 4, 8, 8, 12, 12, 16, 16, -2, -2, -3]

    dataSet = test

    data =  {'scircle_1_zero_1_fast': {'xoffset': 0,'yoffset':0,'scale':4.111672661,'file':"zeroDeg/scircle_1_zero_1_fast.bag"}, #scaling factor averaged
             'scircle_1_zero_2_fast': {'xoffset': 0,'yoffset':0,'scale':4.111672661,'file':"zeroDeg/scircle_1_zero_2_fast.bag"}, #scaling factor averaged
             'scircle_1_zero_3':      {'xoffset': 0,'yoffset':0,'scale':4.111672661,'file':"zeroDeg/scircle_1_zero_3.bag"}, #scaling factor averaged
             'scircle_3_zero_1':      {'xoffset': 0.07,'yoffset':7,'scale':-5.329780147,'file':"zeroDeg/scircle_3_zero_1.bag"},
             'scircle_3_zero_2':      {'xoffset': 0.1,'yoffset':7.136,'scale':-5.294506949,'file':"zeroDeg/scircle_3_zero_2.bag"}, 
             'scircle_3_zero_3':      {'xoffset': 0,'yoffset':0,'scale':5.312143548,'file':"zeroDeg/scircle_3_zero_3.bag"}, #scaling factor averaged 
             'scorn_1_zero_1':        {'xoffset': (14-12.65),'yoffset':0,'scale':-4.101963082,'file':"zeroDeg/scorn_1_zero_1.bag"},
             'scorn_1_zero_2':        {'xoffset': (14 - 13.8388),'yoffset':(-0.0331184),'scale':-4.097161253,'file':"zeroDeg/scorn_1_zero_2.bag"}, 
             'scorn_1_zero_3':        {'xoffset': (14 - 13.5169),'yoffset':(-0.023974),'scale':-4.135893648,'file':"zeroDeg/scorn_1_zero_3.bag"},
             'scorn_3_zero_1':        {'xoffset': (14 - 11.6039),'yoffset':(-0.0548116),'scale':-6.021505376,'file':"zeroDeg/scorn_3_zero_1.bag"},
             'scorn_3_zero_2':        {'xoffset': (14 - 13.613),'yoffset':(-0.0566209),'scale':-6.113537118,'file':"zeroDeg/scorn_3_zero_2.bag"}, 
             'scorn_3_zero_3':        {'xoffset': (14 - 13.171),'yoffset':(-0.0503621),'scale':-6.024096386,'file':"zeroDeg/scorn_3_zero_3.bag"},
             'scircle_1_20deg_1':     {'xoffset': 0,'yoffset':0,'scale':1,'file':"20Deg/scircle_1_20deg_1.bag"}, 
             'scircle_1_20deg_2':     {'xoffset': 0,'yoffset':0,'scale':1,'file':"20Deg/scircle_1_20deg_2.bag"},
             'scircle_1_20deg_3':     {'xoffset': 0,'yoffset':0,'scale':1,'file':"20Deg/scircle_1_20deg_3.bag"},
             'scircle_3_20deg_1':     {'xoffset': 0,'yoffset':0,'scale':-6.086982987,'file':"20Deg/scircle_3_20deg_1.bag"},
             'scircle_3_20deg_2':     {'xoffset': 0,'yoffset':0,'scale':-6.109715211,'file':"20Deg/scircle_3_20deg_2.bag"}, 
             'scircle_3_20deg_3':     {'xoffset': 0,'yoffset':0,'scale':-6.098349099,'file':"20Deg/scircle_3_20deg_3.bag"}, #scaling factor averaged
             'scorn_1_20deg_1':       {'xoffset': 0,'yoffset':0,'scale':1,'file':"20Deg/scorn_1_20deg_1.bag"},
             'scorn_1_20deg_2':       {'xoffset': 0,'yoffset':0,'scale':1,'file':"20Deg/scorn_1_20deg_2.bag"}, 
             'scorn_1_20deg_3':       {'xoffset': 0,'yoffset':0,'scale':1,'file':"20Deg/scorn_1_20deg_3.bag"},
             'scorn_3_20deg_1':       {'xoffset': 0,'yoffset':0,'scale':-6.636352755,'file':"20Deg/scorn_3_20deg_1.bag"},
             'scorn_3_20deg_2':       {'xoffset': 0,'yoffset':0,'scale':-6.675518818,'file':"20Deg/scorn_3_20deg_2.bag"}, 
             'scorn_3_20deg_3':       {'xoffset': 0,'yoffset':0,'scale':-6.706766744,'file':"20Deg/scorn_3_20deg_3.bag"},      
         }

    px = []
    py = []
    pz = []

    posex = []
    posey = []
    posez = []

    bag = rosbag.Bag(data[dataSet]['file'])

    for topic, msg, t in bag.read_messages(topics=['/svo/pose']):
        #print msg

        posex.append(msg.pose.pose.position.x)
        posey.append(msg.pose.pose.position.y)
        posez.append(msg.pose.pose.position.z)

    # for topic, msg, t in bag.read_messages(topics=['/svo/points']):
    #     #print msg

    #     px.append(msg.pose.position.x)
    #     py.append(msg.pose.position.y)
    #     pz.append(msg.pose.position.z)

    if dataSet[-7:-2] == "20deg":
        print "adjusting angle"
        poseym =  [x/cos(0.34906585) for x in posey]
        posey = poseym

    #ax.scatter(posex, posey, posez, c='r', marker='o')
    #ax.scatter(posex, posey, c='b', marker='o')
    plt.plot( [x * data[dataSet]['scale'] + data[dataSet]['xoffset'] for x in posex], [x * data[dataSet]['scale'] + data[dataSet]['yoffset'] for x in posey], 'ro')


    if dataSet[:3] == "sco":
        plt.plot(XSqrPts, YSqrPts, 'b')

    if dataSet[:3] == "sci":
        x = linspace(0,2*pi, 200)
        plt.plot(8*cos(x)+8, 8*sin(x)+8,'b')
        offLineX = [-1, 0]
        offLineY = [-1, 8]
        plt.plot(offLineX, offLineY, 'b')


    plt.title(dataSet)
    plt.xlabel('Inches')
    plt.ylabel('Inches')
    #plot( 3*cos(an), 3*sin(an) )
    plt.axis('equal')

    if save:
        plt.savefig('Graphs/' + dataSet + '.png')
        plt.savefig('Graphs/' + dataSet + '.eps')
        print "saved"

    plt.show()
    bag.close()
    
done = ['scircle_3_zero_1','scircle_3_zero_2','scorn_1_zero_1']

makePlot('scircle_1_zero_1_fast',False)

done = ['scorn_1_zero_2, scorn_1_zero_3, scorn_3_zero_1']
