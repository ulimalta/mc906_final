import vrep
import sys
import time

from naoqi import ALProxy
from manage_joints import get_first_handles, JointControl

fitness=[]
def runSimulation(cromossomos):
    idx = 0
    for cromossomo in cromossomos:
        #commands.getoutput('~/Downloads/choregraphe-suite-2.1.4.13-linux64/bin/naoqi-bin -p 50004')
        #subprocess.Popen('ls')
        #subprocess.Popen('/home/gabriel/Downloads/choregraphe-suite-2.1.4.13-linux64/bin/naoqi-bin')
        #subprocess.call('./test.sh&', shell=True)
        vrep.simxFinish(-1)
        clientID=vrep.simxStart('127.0.0.2', 50003, True, True, 5000, 5)

        if clientID != -1:
            print 'Connected to remote API server'
            # vrep.simxLoadScene(clientID,"/home/gabriel/MC906/trabalho/mc906/scenes/test.ttt",1,vrep.simx_opmode_oneshot_wait)
            vrep.simxStartSimulation(clientID,vrep.simx_opmode_streaming)
        else:
            print 'Connection was not successful'
            sys.exit('Could not connect')

        naoIP = "127.0.0.1"
        naoPort = 50004

        motionProxy = ALProxy("ALMotion", naoIP, naoPort)
        postureProxy = ALProxy("ALRobotPosture", naoIP, naoPort)

        # Go to the posture StandInitZero
        posture = 'StandZero'
        motionProxy.stiffnessInterpolation('Body', 1.0, 1.0)

        Head_Yaw = []
        Head_Pitch = []
        L_Hip_Yaw_Pitch = []
        L_Hip_Roll = []
        L_Hip_Pitch = []
        L_Knee_Pitch = []
        L_Ankle_Pitch = []
        L_Ankle_Roll = []
        R_Hip_Yaw_Pitch = []
        R_Hip_Roll = []
        R_Hip_Pitch = []
        R_Knee_Pitchi = []
        R_Ankle_Pitch = []
        R_Ankle_Roll=[];
        L_Shoulder_Pitch = []
        L_Shoulder_Roll = []
        L_Elbow_Yaw = []
        L_Elbow_Roll = []
        L_Wrist_Yaw = []
        R_Shoulder_Pitch = []
        R_Shoulder_Roll = []
        R_Elbow_Yaw=[]
        R_Elbow_Roll = []
        R_Wrist_Yaw = []
        R_H = []
        L_H = []
        R_Hand=[]
        L_Hand=[]
        Body = [Head_Yaw,
                Head_Pitch,
                L_Hip_Yaw_Pitch,
                L_Hip_Roll,
                L_Hip_Pitch,
                L_Knee_Pitch,
                L_Ankle_Pitch,
                L_Ankle_Roll,
                R_Hip_Yaw_Pitch,
                R_Hip_Roll,
                R_Hip_Pitch,
                R_Knee_Pitch,
                R_Ankle_Pitch,
                R_Ankle_Roll,
                L_Shoulder_Pitch,
                L_Shoulder_Roll,
                L_Elbow_Yaw,
                L_Elbow_Roll,
                L_Wrist_Yaw,
                R_Shoulder_Pitch,
                R_Shoulder_Roll,
                R_Elbow_Yaw,
                R_Elbow_Roll,
                R_Wrist_Yaw,
                L_H,
                L_Hand,
                R_H,
                R_Hand]

        get_first_handles(clientID, Body)

        # TARGET VELOCITY
        X         = 1.0
        Y         = 0.0
        Theta     = 0.0
        Frequency = 1.0

        # motionProxy.moveToward(X, Y, Theta, [["Frequency", Frequency]])
        postureProxy.applyPosture('StandZero',0.1)
        motionProxy.moveToward(X, Y, Theta, [["Frequency", Frequency],
                                             ["MaxStepX", 0.01 + cromossomo[0]*0.079],
                                             ["LeftStepHeight", 0.005 + cromossomo[1]*0.035],
                                             ["RightStepHeight", 0.005 + cromossomo[1]*0.035]])

        # fitness.append((JointControl(clientID,motionProxy,postureProxy,0,Body),idx))
        # idx += 1
        return JointControl(clientID, motionProxy, postureProxy, 0, Body)
