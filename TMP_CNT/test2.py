
import wx
import logging
import wx.lib.plot as plot

class PlotCanvasExample(plot.PlotCanvas):
    def __init__(self, parent, id, size):
        ''' Initialization routine for the this panel.'''
        plot.PlotCanvas.__init__(self, parent, id, style=wx.BORDER_NONE, size=desiredSize)
        self.data = [(1,2), (2,3), (3,5), (4,6), (5,8), (6,8), (10,10)]
        line = plot.PolyLine(self.data, legend='', colour='pink', width=2)
        gc = plot.PlotGraphics([line], 'Line Graph', 'X Axis', 'Y Axis')
        self.Draw(gc, xAxis=(0,15), yAxis=(0,15))

class MyFrame(wx.Frame):
    def __init__(self, parent, id ,size):
        wx.Frame.__init__(self, parent, id, size=desiredSize)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.canvas = PlotCanvasExample(self, 0, size)
        sizer.Add(self.canvas, 1, wx.EXPAND, 0)
        self.SetSizer(sizer)
        self.Layout()

if __name__ == '__main__':
    ''' Simple main program to display this panel. '''
    # Create a simple wxFrame to insert the panel into
    desiredSize = wx.Size(300,200)
    app = wx.PySimpleApp()
    frame = MyFrame(None, -1,  size=desiredSize)    
    frame.Show()
    app.MainLoop()
