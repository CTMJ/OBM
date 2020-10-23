from DataExtrraction.FileDataCleanAndMachime import FileDataCleanAndMachine


class fileController:
    def __init__(self, filePath):
        self.dataCM = FileDataCleanAndMachine(filePath).parsed_data()

    def getTimeStampList(self) -> list:
        dataCM = self.dataCM
        timeStampList = []
        for d in dataCM:
            timeStampList.append(d[2])
        return timeStampList

    def getUserListSort(self) -> list:
        dataCM = self.dataCM
        userList = []
        for d in dataCM:
            userList.append(d[0])
            userList.append(d[1])
        userList = list(set(userList))
        userList.sort()
        return userList

    def getUserAndTimeList(self) -> list:
        userAndTimeList = []
        dataCM = self.dataCM
        for d in dataCM:
            userAndTimeList.append((d[0], d[1], d[2]))
        return userAndTimeList
