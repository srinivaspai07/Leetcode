from typing import List
import collections

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupDict = collections.defaultdict(list)
        for index, value in enumerate(groupSizes):
            groupDict[value].append(index)

        # Sorting the dictionary by keys
        sortedgroupDict = dict(sorted(groupDict.items()))

        retList = []
        for key, value in sortedgroupDict.items():
            for i in range(0, len(value), key):
                # Append subgroups to the result list
                retList.append(value[i:i + key])

        return retList

