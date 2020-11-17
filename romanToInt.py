romanDict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


class Solution:
    def romanToInt(self, s: str) -> int:
        romanList = list(s)
        toSubtract = None
        summary = 0
        for i in range(len(romanList) - 1):
            currentElem = romanDict[romanList[i]]
            nextElem = romanDict[romanList[i + 1]]
            if currentElem >= nextElem and toSubtract is None:
                summary += currentElem
            elif currentElem < nextElem and toSubtract is None:
                toSubtract = currentElem
            else:
                summary += currentElem - toSubtract
                toSubtract = None
        if toSubtract is None:
            summary += romanDict[romanList[-1]]
        else:
            summary += romanDict[romanList[-1]] - toSubtract
        return summary