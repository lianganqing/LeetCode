'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-11 10:50:33
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-11 10:55:15
'''
'''
789. 逃脱阻碍者

你在进行一个简化版的吃豆人游戏。你从 (0, 0) 点开始出发，你的目的地是 (target[0], target[1]) 。地图上有一些阻碍者，第 i 个阻碍者从 (ghosts[i][0], ghosts[i][1]) 出发。

每一回合，你和阻碍者们*可以*同时向东，西，南，北四个方向移动，每次可以移动到距离原位置1个单位的新位置。

如果你可以在任何阻碍者抓住你之前到达目的地（阻碍者可以采取任意行动方式），则被视为逃脱成功。如果你和阻碍者同时到达了一个位置（包括目的地）都不算是逃脱成功。

当且仅当你有可能成功逃脱时，输出 True。

示例 1:
输入： 
ghosts = [[1, 0], [0, 3]]
target = [0, 1]
输出：true
解释：
你可以直接一步到达目的地(0,1)，在(1, 0)或者(0, 3)位置的阻碍者都不可能抓住你。 

示例 2:
输入： 
ghosts = [[1, 0]]
target = [2, 0]
输出：false
解释：
你需要走到位于(2, 0)的目的地，但是在(1, 0)的阻碍者位于你和目的地之间。 

示例 3:
输入： 
ghosts = [[2, 0]]
target = [1, 0]
输出：false
解释：
阻碍者可以和你同时达到目的地。 

说明：

    所有的点的坐标值的绝对值 <= 10000。
    阻碍者的数量不会超过 100。

'''
'''
思路：
直接让ghost到终点占坑，比玩家快，玩家输，否则玩家胜利
'''
def escapeGhosts(ghosts, target):
    """
    :type ghosts: List[List[int]]
    :type target: List[int]
    :rtype: bool
    """
    if [0,0] in ghosts:
        return False
    if target==[0,0]:
        return True
    min_=20001
    temp=abs(target[0])+abs(target[1])
    print('temp=    '+str(temp
    ))
    for i in ghosts:
        destance=abs(target[0]-i[0])+abs(target[1]-i[1])
        if min_>destance:
            min_=destance
        print('min=     '+str(min_))
        if min_<=temp:
            return False
    return True
ghosts=[[1,9],[2,-5],[3,8],[9,8],[-1,3]]
target=[8,-10]
print(escapeGhosts(ghosts, target))