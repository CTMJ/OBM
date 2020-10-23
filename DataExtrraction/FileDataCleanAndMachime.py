from DataExtrraction.TxtDataExtractor import TxtDataExtractor


class FileDataCleanAndMachine:
    def __init__(self, filePath: str):
        self.data = TxtDataExtractor(filePath).parsed_data()
        self.dataCM = []
        for _data in self.data:
            _userA = _data[0]
            _userB = _data[1]
            _timestamp = int(_data[2] / 3600)
            if _userA != _userB:
                self.dataCM.append((_userA, _userB, _timestamp))

    def parsed_data(self) -> list:
        return self.dataCM
