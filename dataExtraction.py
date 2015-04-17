import rosbag
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

#an = linspace(0,2*pi,100)

px = []
py = []
pz = []

posex = []
posey = []
posez = []

bag = rosbag.Bag('scorn_1_zero_1.bag')

for topic, msg, t in bag.read_messages(topics=['/svo/pose']):
    #print msg

    posex.append(msg.pose.pose.position.x)
    posey.append(msg.pose.pose.position.y)
    posez.append(msg.pose.pose.position.z)

for topic, msg, t in bag.read_messages(topics=['/svo/points']):
    #print msg

    px.append(msg.pose.position.x)
    py.append(msg.pose.position.y)
    pz.append(msg.pose.position.z)

#ax.scatter(px, py, pz, c='r', marker='o')
#ax.scatter(posex, posey, c='b', marker='o')

plt.plot(posex, posey, 'ro')
#plot( 3*cos(an), 3*sin(an) )
plt.axis('equal')
plt.show()
bag.close()