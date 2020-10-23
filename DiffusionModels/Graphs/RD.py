# Real Data Graph
import networkx as nx
import numpy as np
from DataExtrraction.FileController import fileController
from DataExtrraction.Generate import Common_matrix


class RDGraph:

    def __init__(self, filePath: str):
        self.filePath = filePath
        self.fileController = fileController(self.filePath)
        self.C_matrix = Common_matrix(self.filePath)

    def getTimeStampList(self) -> list:
        return self.fileController.getTimeStampList()

    def getTimeStampListSort(self) -> list:
        _timestampList = list(set(self.getTimeStampList()))
        _timestampList.sort()
        return _timestampList

    def getUserAndTimeList(self) -> list:
        return self.fileController.getUserAndTimeList()

    def getUserListSort(self) -> list:
        return self.fileController.getUserListSort()

    def getMinTimeStamp(self) -> int:
        return min(self.getTimeStampList())

    def getNodeList(self) -> list:
        return self.getUserListSort()

    def getEdgeList(self) -> list:
        edgeList = []
        for i in self.getUserAndTimeList():
            edgeList.append((i[0], i[1]))
        edgeList = list(set(edgeList))
        edgeList.sort()
        return edgeList

    def getMessageNumAndTime(self) -> dict:
        messageNumAndTimeDict = {}
        timestampList = self.getTimeStampList()
        _minTimestamp = self.getMinTimeStamp()
        _timestampList = self.getTimeStampListSort()
        for i in range(len(_timestampList)):
            messageNumAndTimeDict[_timestampList[i] - _minTimestamp] = timestampList.count(_timestampList[i])
        return messageNumAndTimeDict

    def getMessageSumAndTime(self) -> dict:
        messageSumAndTimeDict = {}
        messageSum = 0
        messageNumAndTimeDict = self.getMessageNumAndTime()
        for i in list(messageNumAndTimeDict.keys()):
            messageSum += messageNumAndTimeDict[i]
            messageSumAndTimeDict[i] = messageSum
        return messageSumAndTimeDict

    def getSeedTime(self, dt: int) -> list:
        userAndTimeList = self.getUserAndTimeList()
        _minTimestamp = self.getMinTimeStamp()
        _userList = []
        for j in range(len(userAndTimeList)):
            if userAndTimeList[j][2] <= _minTimestamp + dt:
                _userList.append(userAndTimeList[j][0])
                _userList.append(userAndTimeList[j][1])
            _userList = list(set(_userList))
        return _userList

    def getUserNumAndTime(self) -> dict:
        userNumAndTimeDict = {}
        userAndTimeList = self.getUserAndTimeList()
        _timestampList = self.getTimeStampListSort()
        _minTimestamp = self.getMinTimeStamp()
        for i in range(len(_timestampList)):
            _userListj = []
            for j in range(len(userAndTimeList)):
                if userAndTimeList[j][2] <= _timestampList[i]:
                    _userListj.append(userAndTimeList[j][0])
                    _userListj.append(userAndTimeList[j][1])
            _userListj = list(set(_userListj))
            _numUser = len(_userListj)
            userNumAndTimeDict[_timestampList[i] - _minTimestamp] = _numUser
        return userNumAndTimeDict

    def getUserAndMessageSumDt(self, dt: int) -> (dict, list):
        dt_userAndMessageSumDict = {}
        userAndTimeList = self.getUserAndTimeList()
        _minTimestamp = self.getMinTimeStamp()
        userList = self.getUserListSort()
        userAList = []
        userBList = []
        for i in range(len(userAndTimeList)):
            if userAndTimeList[i][2] <= (_minTimestamp + dt):
                userAList.append(userAndTimeList[i][0])
                userBList.append(userAndTimeList[i][1])
        for user in userList:
            inMessageNum = userBList.count(user)
            dt_userAndMessageSumDict[user] = inMessageNum
        return dt_userAndMessageSumDict, userAList

    def getUserAList(self, dt: int):
        return self.getUserAndMessageSumDt(dt)[1]

    def getUserAndMessageSumVector(self, dt: int) -> np.ndarray:
        userOfMessageSumDict = self.getUserAndMessageSumDt(dt)[0]
        userOfMessageSumList = list(userOfMessageSumDict.values())
        userOfMessageSumVector = []
        for f in range(len(userOfMessageSumList)):
            userOfMessageSumVector.append([userOfMessageSumList[f]])
        return np.array(userOfMessageSumVector)

    def getAdjacency_matrix(self, time: int):
        return self.C_matrix.getAdjacency_matrix(time)

    def getOutDegrees(self, time: int) -> list:
        _outDegrees = []
        users = self.getUserListSort()
        adjacency_matrix = self.getAdjacency_matrix(time)
        for i in range(len(users)):
            og = 0
            for j in range(len(users)):
                og += adjacency_matrix[i][j]
            _outDegrees.append(og)
        return _outDegrees

    def getInDegrees(self, time: int) -> list:
        _inDegrees = []
        adjacency_matrix = self.getAdjacency_matrix(time)
        users = self.getUserListSort()
        for i in range(len(users)):
            ig = 0
            for j in range(len(users)):
                ig += adjacency_matrix[j][i]
            _inDegrees.append(ig)
        return _inDegrees

    def getOrigin(self, time: int) -> dict:
        adjacency_matrix = self.getAdjacency_matrix(time)
        total_influences = adjacency_matrix.sum(axis=0)
        users = self.getUserListSort()
        _origin = {}
        for i in range(len(users)):
            if total_influences[i] != 0:
                _origin[i] = users[i]
        return _origin
