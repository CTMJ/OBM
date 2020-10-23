from Test.OBMtest import OBMTest
from Test.HDtest import HDTest
from Test.RDtest import RDTest
from Test.LTMtest2 import LTMTest2
import DiffusionModels.Models.ICM2 as icm2
import matplotlib.pyplot as plt


class CompareTest:
    def __init__(self, time: int, filePath: str):
        self.time = time
        self.filePath = filePath
        self.RD = RDTest(self.filePath)
        self.HD = HDTest(self.time, self.filePath)
        self.OBM = OBMTest(self.time, self.filePath)
        self.LTM = LTMTest2(self.filePath, self.time)
        self.yICM = icm2.ICM2()
    def draw_RH_DH_OBM_MsgAndTime(self, PicPath):
        print("----draw----")
        #_timeList = list(self.RD.getMsgSumAndTimeDist(self.time).keys())
        _timeList = list(self.RD.getuserNumAndTimeDist(self.time).keys())
        #_messageRDSumList = list(self.RD.getMsgSumAndTimeDist(self.time).values())
        _userRDNumList = list(self.RD.getuserNumAndTimeDist(self.time).values())
        #_messageHDSumList = list(self.HD.getMsgSumAndTimeDict().values())
        _userHDNumList = list(self.HD.getUserNumAndTimeDict().values())
        #_messageOBMSumList = list(self.OBM.getMsgSumAndTimeDict().values())
        _userOBMNumList = list(self.OBM.getUserNumAndTimeDict().values())
        x = _timeList
        #yOBM = _messageOBMSumList
        zOBM = _userOBMNumList
        #yHD = _messageHDSumList
        #yRD = _messageRDSumList
        zRD = _userRDNumList
        zHD = _userHDNumList
        zICM = self.yICM
        zLTM = self.LTM.getYLTM()
        #plt.plot(x, yOBM, marker='o', markevery=10, label='Msg_OBM', color='red', linestyle='-')
        plt.plot(x, zOBM, marker='o', markevery=10, label='OBM', color='red', linestyle='--')
        #plt.plot(x, yHD, marker='s', markevery=10, label='Msg=_HD', color='green', linestyle='-')
        plt.plot(x, zHD, marker='s', markevery=10, label='HD', color='green', linestyle='--')
        #plt.plot(x, yRD, marker='d', markevery=10, label='Msg_RD', color='blue', linestyle='-')
        plt.plot(x, zRD, marker='d', markevery=10, label='RD', color='blue', linestyle='--')
        plt.plot(x, zICM, marker='v', markevery=10, label='ICM', color='orange', linestyle='--')
        plt.plot(x, zLTM, marker='<', markevery=10, label='LTM', color='black', linestyle='--')
        #plt.ylim((0, 18000))
        plt.xlim(71,110)
        #plt.ylabel("Message_Sum")
        plt.ylabel("The total activated users")
        plt.xlabel("Timestamps")
        plt.legend()
        print("----finish----")
        plt.savefig(PicPath);
        plt.show()
