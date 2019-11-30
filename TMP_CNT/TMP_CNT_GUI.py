import wx

class Color():
    def __init__(self):
        self.color1 = '#FCF8F0'
        self.color2 = '#FC4000'
        self.color3 = '#C70230'
        self.color4 = '#0000FF'
        self.color5 = '#C70230'

class frame(wx.Frame):

    def __init__(self,title):
        wx.Frame.__init__(self,None,-1,title,size=(1024,768))
        
        #layout
        self.panel = wx.Panel(self)
        
        self.panel_1 = wx.Panel(self.panel,wx.ID_ANY)
        self.panel_2 = wx.Panel(self.panel,wx.ID_ANY)
        self.panel_3 = wx.Panel(self.panel,wx.ID_ANY)
        
        self.panel_1.SetBackgroundColour(Color().color5)
        self.panel_2.SetBackgroundColour(Color().color2)
        self.panel_3.SetBackgroundColour(Color().color5)
        
        layout_1 = wx.BoxSizer(wx.VERTICAL)
        layout_1.Add(self.panel_1,proportion = 1,flag=wx.EXPAND)
        layout_1.Add(self.panel_2,proportion = 10,flag=wx.EXPAND)
        layout_1.Add(self.panel_3,proportion = 1,flag=wx.EXPAND)      
        self.panel.SetSizer(layout_1)

        #layout2
        self.panel_2_1 = wx.Panel(self.panel_2,wx.ID_ANY,pos=(30,30),size=(467, 255))
        self.panel_2_2 = wx.Panel(self.panel_2,wx.ID_ANY,pos=(30,315),size=(467, 255))
        self.panel_2_3 = wx.Panel(self.panel_2,wx.ID_ANY,pos=(532,30),size=(467-15, 540))
 
        self.panel_2_1.SetBackgroundColour(Color().color1)
        self.panel_2_2.SetBackgroundColour(Color().color1)
        self.panel_2_3.SetBackgroundColour(Color().color1)

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame('GUI')
    app.MainLoop()
