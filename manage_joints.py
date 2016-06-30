import vrep
import commands
import time
import math

# Get the handles of all NAO in the scene
def JointControl(clientID, motionProxy, postureProxy, i, Body):
    # Head
    # velocity_x = vrep.simxGetObjectFloatParameter(clientID,vrep.simxGetObjectHandle(clientID,'NAO#',vrep.simx_opmode_oneshot_wait)[1],11,vrep.simx_opmode_streaming)
    pos = vrep.simxGetObjectPosition(clientID,vrep.simxGetObjectHandle(clientID, 'NAO#', vrep.simx_opmode_oneshot_wait)[1], -1, vrep.simx_opmode_streaming)[1]
    angularPos = vrep.simxGetObjectOrientation(clientID,vrep.simxGetObjectHandle(clientID, 'NAO#', vrep.simx_opmode_oneshot_wait)[1], -1, vrep.simx_opmode_streaming)[1]
    alphaPosRegister = []
    betaPosRegister = []
    gamaPosRegister = []
    j = 0
    li = []
    while vrep.simxGetConnectionId(clientID) != -1:
        for x in range(0, 150):
            commandAngles = motionProxy.getAngles('Body', False)
            j+=1
            pos = vrep.simxGetObjectPosition(clientID, vrep.simxGetObjectHandle(clientID, 'NAO#', vrep.simx_opmode_oneshot_wait)[1], -1, vrep.simx_opmode_buffer)[1]
            angularPos = vrep.simxGetObjectOrientation(clientID, vrep.simxGetObjectHandle(clientID, 'NAO#', vrep.simx_opmode_oneshot_wait)[1], -1, vrep.simx_opmode_buffer)[1]
            alphaPosRegister.append(angularPos[0])
            betaPosRegister.append(angularPos[1])
            gamaPosRegister.append(angularPos[2])

            vrep.simxSetJointTargetPosition(clientID,Body[0][i],commandAngles[0],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[1][i],commandAngles[1],vrep.simx_opmode_streaming)
            # Left Leg
            vrep.simxSetJointTargetPosition(clientID,Body[2][i],commandAngles[8],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[3][i],commandAngles[9],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[4][i],commandAngles[10],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[5][i],commandAngles[11],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[6][i],commandAngles[12],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[7][i],commandAngles[13],vrep.simx_opmode_streaming)
            # Right Leg
            vrep.simxSetJointTargetPosition(clientID,Body[8][i],commandAngles[14],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[9][i],commandAngles[15],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[10][i],commandAngles[16],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[11][i],commandAngles[17],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[12][i],commandAngles[18],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[13][i],commandAngles[19],vrep.simx_opmode_streaming)
            # Left Arm
            vrep.simxSetJointTargetPosition(clientID,Body[14][i],commandAngles[2],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[15][i],commandAngles[3],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[16][i],commandAngles[4],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[17][i],commandAngles[5],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[18][i],commandAngles[6],vrep.simx_opmode_streaming)
            # Right Arm
            vrep.simxSetJointTargetPosition(clientID,Body[19][i],commandAngles[20],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[20][i],commandAngles[21],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[21][i],commandAngles[22],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[22][i],commandAngles[23],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[23][i],commandAngles[24],vrep.simx_opmode_streaming)
            # Left Fingers
            vrep.simxSetJointTargetPosition(clientID,Body[25][i][0],1.0-commandAngles[7],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[25][i][1],1.0-commandAngles[7],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[25][i][2],1.0-commandAngles[7],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[25][i][3],1.0-commandAngles[7],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[25][i][4],1.0-commandAngles[7],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[25][i][5],1.0-commandAngles[7],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[25][i][6],1.0-commandAngles[7],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[25][i][7],1.0-commandAngles[7],vrep.simx_opmode_streaming)
            # Right Fingers
            vrep.simxSetJointTargetPosition(clientID,Body[27][i][0],1.0-commandAngles[25],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[27][i][1],1.0-commandAngles[25],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[27][i][2],1.0-commandAngles[25],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[27][i][3],1.0-commandAngles[25],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[27][i][4],1.0-commandAngles[25],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[27][i][5],1.0-commandAngles[25],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[27][i][6],1.0-commandAngles[25],vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetPosition(clientID,Body[27][i][7],1.0-commandAngles[25],vrep.simx_opmode_streaming)
        motionProxy.stopMove()
        postureProxy.stopMove()
        # postureProxy.goToPosture("Stand",0.5)
        vrep.simxStopSimulation(clientID,vrep.simx_opmode_oneshot_wait)
        break
    print 'End of simulation'
    print 'Final x pos'
    print pos
    calculos = {}
    calcular(alphaPosRegister,calculos)
    desvpadA = calculos['desvio_padrao']
    calculos = {}
    calcular(betaPosRegister,calculos)
    desvpadB = calculos['desvio_padrao']
    calculos = {}
    calcular(gamaPosRegister,calculos)
    desvpadG = calculos['desvio_padrao']
    return [(10*pos[0] - (desvpadA + desvpadB + desvpadG)/3), pos[0]]

def calcular(valores=None, calculos=None):
    if valores:
        if valores.__class__.__name__ == 'list' and calculos.__class__.__name__ == 'dict':
            def somar(valores):
                soma = 0
                for v in valores:
                    soma += v
                return soma

            def media(valores):
                soma = somar(valores)
                qtd_elementos = len(valores)
                media = soma / float(qtd_elementos)
                return media

            def variancia(valores):
                _media = media(valores)
                soma = 0
                _variancia = 0
                for valor in valores:
                    soma += math.pow((valor - _media), 2)
                _variancia = soma / float(len(valores))
                return _variancia

            def desvio_padrao(valores):
                return math.sqrt( variancia(valores) )

            calculos['soma'] = somar(valores)
            calculos['media'] = media(valores)
            calculos['variancia'] = variancia(valores)
            calculos['desvio_padrao'] = desvio_padrao(valores)

# Get the Handle of only one NAO
def get_first_handles(clientID,Body):
    Body[0].append(vrep.simxGetObjectHandle(clientID,'HeadYaw#',vrep.simx_opmode_oneshot_wait)[1])
    Body[1].append(vrep.simxGetObjectHandle(clientID,'HeadPitch#',vrep.simx_opmode_oneshot_wait)[1])
    # Left Leg
    Body[2].append(vrep.simxGetObjectHandle(clientID,'LHipYawPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[3].append(vrep.simxGetObjectHandle(clientID,'LHipRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[4].append(vrep.simxGetObjectHandle(clientID,'LHipPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[5].append(vrep.simxGetObjectHandle(clientID,'LKneePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[6].append(vrep.simxGetObjectHandle(clientID,'LAnklePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[7].append(vrep.simxGetObjectHandle(clientID,'LAnkleRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    # Right Leg
    Body[8].append(vrep.simxGetObjectHandle(clientID,'RHipYawPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[9].append(vrep.simxGetObjectHandle(clientID,'RHipRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[10].append(vrep.simxGetObjectHandle(clientID,'RHipPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[11].append(vrep.simxGetObjectHandle(clientID,'RKneePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[12].append(vrep.simxGetObjectHandle(clientID,'RAnklePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[13].append(vrep.simxGetObjectHandle(clientID,'RAnkleRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    # Left Arm
    Body[14].append(vrep.simxGetObjectHandle(clientID,'LShoulderPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[15].append(vrep.simxGetObjectHandle(clientID,'LShoulderRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[16].append(vrep.simxGetObjectHandle(clientID,'LElbowYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[17].append(vrep.simxGetObjectHandle(clientID,'LElbowRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[18].append(vrep.simxGetObjectHandle(clientID,'LWristYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    # Right Arm
    Body[19].append(vrep.simxGetObjectHandle(clientID,'RShoulderPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[20].append(vrep.simxGetObjectHandle(clientID,'RShoulderRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[21].append(vrep.simxGetObjectHandle(clientID,'RElbowYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[22].append(vrep.simxGetObjectHandle(clientID,'RElbowRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[23].append(vrep.simxGetObjectHandle(clientID,'RWristYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    # Left fingers
    Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LThumbBase#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint8#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LLFingerBase#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint12#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint14#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LRFinger_Base#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint11#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint13#',vrep.simx_opmode_oneshot_wait)[1])
    Body[25].append(Body[24][0:8])
    # Right Fingers
    Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RThumbBase#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint0#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RLFingerBase#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint5#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint6#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RRFinger_Base#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint2#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[27].append(Body[26][0:8])
