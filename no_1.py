import rospy
from std_msgs.msg import String


rospy.init_node('no_1')
responde = 'Soma 35132'

def recebe_resposta(resposta):
    global responde
    responde = resposta.data

def timerCallBack(event):

    print(responde)
    msg = String()
    msg.data = '35132'
    pub.publish(msg)


pub = rospy.Publisher('/topic1', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(1), timerCallBack)
sub = rospy.Subscriber('/topic2', String, recebe_resposta)

rospy.spin()