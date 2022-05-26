class TVshow:
    list_film = ["战狼2", "红海行动", "西游记女儿国", "熊出没"]

    def __init__(self, show):
        self.__show = show

    @property  # 将方法转成属性
    def show(self):
        return self.__show

    @show.setter  # 可以修改属性
    def show(self, value):
        if value in TVshow.list_film:
            self.__show = "你选择了《" + value + "》,稍后就播放！"
        else:
            self.__show = "没有这个电影！"


tvshow = TVshow("战狼2")
print(tvshow.show)
print('你可以从' + str(tvshow.list_film) + '中选择')
film = str(input("请输入你的选择:"))
tvshow.show = film
print(tvshow.show)
