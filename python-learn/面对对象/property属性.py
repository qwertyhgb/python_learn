class TVshow:
    def __init__(self, show):
        self._show = show

    @property  # 将方法转成属性，此属性只读不能修改
    def show(self):
        return self._show


tvshow = TVshow("正在播放电影！")
print(tvshow.show)
