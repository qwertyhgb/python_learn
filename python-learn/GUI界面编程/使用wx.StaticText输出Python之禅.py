import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="创建StaticText类", pos=(200, 200), size=(500, 500))
        panel = wx.Panel(self)  # 创建画板
        # 创建标题，并设置字体
        title = wx.StaticText(panel, lable='Python之禅--Tim Peters', pos=(100, 20))
        font = wx.Font(16, wx.DEFAULT_FRAME_STYLE, wx.FONTSTYLE_NORMAL, wx.NORMAL_FONT)
        title.SetFont(font)
        # 创建文本
        wx.StaticText(panel, label='Python世界第一！！！！！！', pos=(50, 50))


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
