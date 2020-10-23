from DiffusionModels.Graphs.RD import RDGraph
import matplotlib.pyplot as plt


class RDTest:

    def __init__(self, filePath: str):
        self.RD = RDGraph(filePath)
        self.messageSumAndTimeDist = self.RD.getMessageSumAndTime()
        self.userNumAndTimeDist = self.RD.getUserNumAndTime()

    def getMsgSumOrUserNumAndTimeDict(self, time=0) -> (dict, dict):
        if int(time) == 0:
            return self.messageSumAndTimeDist, self.userNumAndTimeDist
        else:
            timelist = list(self.messageSumAndTimeDist.keys())
            _messageSumAndTimeDist = {}
            _userNumAndTimeDist = {}
            for t in timelist[timelist.index(int(time)):]:
                _messageSumAndTimeDist[t] = self.messageSumAndTimeDist[t]
                _userNumAndTimeDist[t] = self.userNumAndTimeDist[t]
            return _messageSumAndTimeDist, _userNumAndTimeDist

    def getMsgSumAndTimeDist(self, time=0):
        if time == 0:
            return self.messageSumAndTimeDist
        else:
            return self.getMsgSumOrUserNumAndTimeDict(time)[0]

    def getuserNumAndTimeDist(self, time=0):
        if time == 0:
            return self.userNumAndTimeDist
        else:
            return self.getMsgSumOrUserNumAndTimeDict(time)[1]

    def draw(self, PicPath):
        x = list(self.messageSumAndTimeDist.keys())
        y1 = list(self.messageSumAndTimeDist.values())
        y2 = list(self.userNumAndTimeDist.values())
        print("----drawing----")
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.plot(x, y1, c='r', linestyle='-',label='sample data(message)')
        ax1.set_ylabel('MessageNum')
        ax2 = ax1.twinx()
        ax2.plot(x, y2, c='b', linestyle=':', label='sample data(user)')
        ax2.set_ylabel('UserNum')
        ax1.set_xlabel('time')
        #plt.plot(x, y1, label='real data', color='blue')
        #plt.ylabel("Message_Sum")
        #plt.xlabel("time")
        fig.legend(loc=2, bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)
        print("---finish---")
        plt.savefig(PicPath);
        plt.show()
