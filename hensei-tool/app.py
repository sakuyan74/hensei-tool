import wx
from view.top import TopFrame


class HenseiTool(wx.App):
    def OnInit(self):
        status = True
        frame = TopFrame(None)
        self.SetTopWindow(frame)
        frame.Show()
        return status
