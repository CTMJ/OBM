class TxtDataExtractor:
    def __init__(self, filepath: str):
        self.data = []
        with open(filepath, mode='r', encoding='utf-8') as file:
            for line in file:
                _data = line.strip("\n").split()
                _userA = _data[0]
                _userB = _data[1]
                _timestamp = int(_data[2])
                _interaction = _data[3]
                self.data.append((_userA, _userB, _timestamp, _interaction))
        file.close()

    def parsed_data(self) -> list:
        return self.data
