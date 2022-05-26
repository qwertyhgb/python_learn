import wx


class App(wx.App):
    """初始化方法"""

    def OnInit(self):
        frame = wx.Frame(parent=None, title='Hello wxPython')
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
