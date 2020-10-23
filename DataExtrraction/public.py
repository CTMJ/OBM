def ListToDict(_list: list):
    _Dict = {}
    for i in range(len(_list)):
        _Dict[i] = _list[i]
    return _Dict


def DictToFlipKeyAndValue(Dict):
    _newDict = {}
    for i in list(Dict.keys()):
        _newDict[Dict[i]] = i
    return _newDict
