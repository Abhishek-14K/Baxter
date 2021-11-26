#!/usr/bin/env python

import rospy

import baxter_interface

rospy.init_node('Moving_Only_Right_Arm')

right_arm=baxter_interface.Limb('right')
#left_arm=baxter_interface.Limb('left')

move_right={'right_s0': 0.8147209188966101, 'right_s1': -1.3130711118371998, 'right_w0': -1.017400799548119, 'right_w1': 0.8809559862383226, 'right_w2': 2.1719382375437317, 'right_e0': 0.6199141528909318, 'right_e1': 2.2547720893005927}
#Above values are copied from ik_client output

right_arm.move_to_joint_positions(move_right)

quit()