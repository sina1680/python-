# world.py

def initial_narration():
    """游戏开始介绍"""
    text = """
你被关在一个房间里，周围都是蜘蛛网。

地上好多密密麻麻的小强（蟑螂），

你惊喜的发现，房间门居然是开着的。

打开门一开，不远处有一只恶狗。

它看到你就想冲过来咬你。

你是要关起房门来等待救援呢？

还是撸起袖子跟恶狗决一死战？

（提示：找到钥匙后，到出口处，就可以进入下一关）
"""
    return text

def final_narration_win():
    text = """
在探索低钠卡特尔秘密的所有房间和层次之后

地下巢穴，我们的英雄出现了胜利。美味的计划短缺

猪肉肚已经被挫败了，我们的英雄甚至离开了她的战利品。

勇敢的追求

手里拿着剑，口袋里有金子，还有一大堆蟑螂尸体。

角落，我们的英雄离开家和早餐，咸肉在手。

她把熏肉带回家了。祝贺你！
        """
    return text

def final_narration_lose():
    text = """
在探索低钠卡特尔秘密的所有房间和层次之后

地下巢穴，我们的英雄出现轻微磨损，但士气高昂。

计划中的美味猪肚短缺已经被挫败，但没有

在追寻过程中，我们的英雄偶然发现了烟熏的奇妙木材。

咸肉咸肉。

手里拿着剑，口袋里有金子，还有一大堆蟑螂尸体。

角落，我们的英雄离开家园和早餐，梦想熏肉来。
        """
    return text
    