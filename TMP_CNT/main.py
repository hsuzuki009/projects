#!/paty/to/python
# -*- coding: utf-8 -*-

import wx
import wx.lib.plot as plot

import math
import time

class Walls(object):
    def __init__(self, x0, y0, x1, y1):
        self.xList = [x0, x1]
        self.yList = [y0, y1]
        self.P_color = wx.Colour(50,50,50)

    def addPoint(self, x, y):
        self.xList.append(x)
        self.yList.append(y)

    def Draw(self,dc):
        dc.SetPen(wx.Pen(self.P_color))
        for i in range(0, len(self.xList)-1):
            dc.DrawLine(self.xList[i], self.yList[i], self.xList[i+1],self.yList[i+1])

class Color():
    def __init__(self):
        self.color1 = '#AFAFAF'

class Mask():
    def __init__(self):
	self.mask_ave  = 0b11110011
	self.mask_mode = 0b11111100
	self.mask_div  = 0b11001111
	self.mask_test = 0b00111111

class frame(wx.Frame):
    def __init__(self,title):
        wx.Frame.__init__(self,None,wx.ID_ANY,title,size=(800,600))
	self.CreateStatusBar()	

	#layout1
	self.panel = wx.Panel(self)
	self.panel.SetBackgroundColour(Color().color1)
	self.panelWIT  = wx.Panel(self.panel,wx.ID_ANY,pos=(0,0),size=(300,100))
        self.panelWIT.SetBackgroundColour(Color().color1)
        self.panelAVE  = wx.Panel(self.panel,wx.ID_ANY,pos=(0,100),size=(150,50))
	self.panelAVE.SetBackgroundColour(Color().color1)
	self.panelMODE = wx.Panel(self.panel,wx.ID_ANY,pos=(0,150),size=(150,50))
	self.panelMODE.SetBackgroundColour(Color().color1)
	self.panelDIV  = wx.Panel(self.panel,wx.ID_ANY,pos=(0,200),size=(150,50))
	self.panelDIV.SetBackgroundColour(Color().color1)
	self.panelTEST = wx.Panel(self.panel,wx.ID_ANY,pos=(0,250),size=(150,50))
        self.panelTEST.SetBackgroundColour(Color().color1)
	self.panelTXT  = wx.Panel(self.panel,wx.ID_ANY,pos=(0,300),size=(150,50))
	self.panelTXT.SetBackgroundColour(Color().color1)
	self.panelTDATA  = wx.Panel(self.panel,wx.ID_ANY,pos=(150,100),size=(150,150))
	self.panelTDATA.SetBackgroundColour(Color().color1)
	self.panelADT7410 = wx.Panel(self.panel,wx.ID_ANY,pos=(150,200),size=(150,150))
        self.panelADT7410.SetBackgroundColour(Color().color1)
	self.panelPLOT = wx.Panel(self.panel,wx.ID_ANY,pos=(300,50),size=(500,500))
	self.panelPLOT.SetBackgroundColour(Color().color1)

	self.plotter = plot.PlotCanvas(self.panelPLOT)
	self.plotter.SetInitialSize(size=(500, 500))
        self.plotter.SetEnableZoom(False)
        self.plotter.SetEnableLegend(True)
	self.plotter.SetEnableGrid(True)
        self.plotter.SetGridColour('gray')
        self.plotter.SetFontSizeLegend(20)

	self.i = 0
        self.data = []
        line = plot.PolyLine(self.data, legend='Dummy', colour='pink', width=2)
        self.gc = plot.PlotGraphics([line], 'Line Graph', 'X Axis', 'Y Axis')
        self.plotter.Draw(self.gc, xAxis=(0,15), yAxis=(0,15))      
        self.plotter.SetFontSizeLegend(point=10.5)

        # OutrBox
        self.Box = Walls(299, 479, 0, 479)
        self.Box.addPoint(1,1)
        self.Box.addPoint(299,1)
        self.Box.addPoint(299,480)

	element_array = ("00", "01", "10", "11")
	self.RegAVE  = wx.ComboBox(self.panelAVE,  wx.ID_ANY, u"選択してください", choices=element_array, style=wx.CB_SIMPLE)
	self.RegMODE = wx.ComboBox(self.panelMODE, wx.ID_ANY, u"選択してください", choices=element_array, style=wx.CB_SIMPLE)
	self.RegDIV  = wx.ComboBox(self.panelDIV, wx.ID_ANY, u"選択してください", choices=element_array, style=wx.CB_SIMPLE)
	self.RegTEST = wx.ComboBox(self.panelTEST, wx.ID_ANY, u"選択してください", choices=element_array, style=wx.CB_SIMPLE)
	self.RegWIT  = wx.Slider(self.panelWIT, style=wx.SL_LABELS)
	self.RegWIT.SetMin(0)
	self.RegWIT.SetMax(255)
	self.RegTDATA= wx.Button(self.panelTDATA, wx.ID_ANY, u"Read TDATA")
	self.RegADT7410= wx.Button(self.panelADT7410, wx.ID_ANY, u"Read ADT7410")

	self.textTDATA = wx.TextCtrl(self.panelTDATA, wx.ID_ANY, u"")
	self.textADT7410 = wx.TextCtrl(self.panelADT7410, wx.ID_ANY, u"")
	self.textReg = wx.TextCtrl(self.panelTXT, wx.ID_ANY, u"")

	self.boxAVE  = wx.StaticBox(self.panelAVE, wx.ID_ANY, "RegAVE")
	self.boxMODE = wx.StaticBox(self.panelMODE, wx.ID_ANY, "RegMODE")
	self.boxDIV  = wx.StaticBox(self.panelDIV, wx.ID_ANY, "RegDIV")
	self.boxWIT  = wx.StaticBox(self.panelWIT, wx.ID_ANY, "RegWIT")
	self.boxTEST = wx.StaticBox(self.panelTEST, wx.ID_ANY, "RegTEST")
	self.boxTDATA  = wx.StaticBox(self.panelTDATA, wx.ID_ANY, "RegTDATA")
	self.boxADT7410  = wx.StaticBox(self.panelADT7410, wx.ID_ANY, "ADT7410")

	self.RegAVE.SetSelection(0)
	self.RegMODE.SetSelection(0)
	self.RegDIV.SetSelection(0)
	self.RegTEST.SetSelection(0)

	self.RegADT7410.Bind(wx.EVT_BUTTON,self.ADT7410_event)
	self.RegTDATA.Bind(wx.EVT_BUTTON,self.RegTDATA_event)
	self.RegAVE.Bind(wx.EVT_COMBOBOX,self.RegAVE_event)
	self.RegMODE.Bind(wx.EVT_COMBOBOX,self.RegMODE_event)
	self.RegDIV.Bind(wx.EVT_COMBOBOX,self.RegDIV_event)
	self.RegTEST.Bind(wx.EVT_COMBOBOX,self.RegTEST_event)
	self.RegWIT.Bind(wx.EVT_SLIDER, self.RegWIT_event)

	layoutTDATA = wx.StaticBoxSizer(self.boxTDATA,wx.VERTICAL)
        layoutTDATA.Add(self.RegTDATA, flag=wx.GROW)
	layoutTDATA.Add(self.textTDATA, flag=wx.GROW)
        self.panelTDATA.SetSizer(layoutTDATA)

	layoutADT7410 = wx.StaticBoxSizer(self.boxADT7410 ,wx.VERTICAL)
        layoutADT7410.Add(self.RegADT7410, flag=wx.GROW)
	layoutADT7410.Add(self.textADT7410, flag=wx.GROW)
        self.panelADT7410.SetSizer(layoutADT7410)

	layoutAVE = wx.StaticBoxSizer(self.boxAVE,wx.VERTICAL)
	layoutAVE.Add(self.RegAVE, flag=wx.GROW)
	self.panelAVE.SetSizer(layoutAVE)

	layoutMODE = wx.StaticBoxSizer(self.boxMODE,wx.VERTICAL)
        layoutMODE.Add(self.RegMODE, flag=wx.GROW)
        self.panelMODE.SetSizer(layoutMODE)

	layoutDIV = wx.StaticBoxSizer(self.boxDIV,wx.VERTICAL)
        layoutDIV.Add(self.RegDIV, flag=wx.GROW)
        self.panelDIV.SetSizer(layoutDIV)

	layoutTEST = wx.StaticBoxSizer(self.boxTEST,wx.VERTICAL)
        layoutTEST.Add(self.RegTEST, flag=wx.GROW)
        self.panelTEST.SetSizer(layoutTEST)

	layoutWIT = wx.StaticBoxSizer(self.boxWIT,wx.VERTICAL)
        layoutWIT.Add(self.RegWIT, flag=wx.GROW)
        self.panelWIT.SetSizer(layoutWIT)

	layoutTXT = wx.BoxSizer(wx.VERTICAL)
	layoutTXT.Add(self.textReg, flag=wx.GROW)
	self.panelTXT.SetSizer(layoutTXT)

	self.Show()

	self.Bind(wx.EVT_CLOSE, self.CloseWindow)

        self.cdc = wx.ClientDC(self.panelPLOT)
        w, h = self.panelPLOT.GetSize()
        self.bmp = wx.EmptyBitmap(w,h)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.timer.Start(1000)

    def i2c_access_box0(self,adr,msk,ofs,selbox):
	rd = p1.I2c_read(device,adr)
	rd_int = int(rd)
	data_led = rd_int & msk
        if selbox == 0:
                wr = (data_led + 0 * ofs)
        elif selbox == 1:
                wr = (data_led + 1 * ofs)
        elif selbox == 2:
                wr = (data_led + 2 * ofs)
        else:
                wr = (data_led + 3 * ofs)
	p1.I2c_write(device,adr,wr)
	rd = p1.I2c_read(device,adr)
	return rd

    def i2c_access_byte(self,adr,wr):
        p1.I2c_write(device,adr,wr)
        rd = p1.I2c_read(device,adr)
        return rd

    def i2c_access_read(self,adr):
        rd = p1.I2c_read(device,adr)
        return rd

    def ADT7410_event(self,event):
	p1.I2c_write(device7410,0x03,0xA0)
	time.sleep(0.5)
        state_lsb = p1.I2c_read(device7410,0x00)
        state_msb = p1.I2c_read(device7410,0x01)
        tdata = float(state_msb * 256 + state_lsb) / 128
        self.textADT7410.SetValue('%f' %tdata)

    def RegTDATA_event(self,event):
	state_lsb = self.i2c_access_read(0x10)
	state_msb = self.i2c_access_read(0x11)
	tdata = float(state_msb * 256 + state_lsb) / 2**16
	self.textTDATA.SetValue('%f' %tdata)
	
    def RegWIT_event(self,event):
        val = self.RegWIT.GetValue()
	state = self.i2c_access_byte(0x00,val)
	state_0x00 = format(state,'08b')
        self.textReg.SetValue("Reg_0x00: " '%s' %state_0x00)

    def RegAVE_event(self,event):
	obj = event.GetEventObject()
	str = obj.GetStringSelection()
	sel = obj.GetSelection()
	state = self.i2c_access_box0(0x01,Mask().mask_ave,4,sel)
	state_0x01 = format(state,'08b')
	self.textReg.SetValue("Reg_0x01: " '%s' %state_0x01)

    def RegMODE_event(self,event):
        obj = event.GetEventObject()
        str = obj.GetStringSelection()
        sel = obj.GetSelection()
        state = self.i2c_access_box0(0x01,Mask().mask_mode,1,sel)
        state_0x01 = format(state,'08b')
        self.textReg.SetValue("Reg_0x01: " '%s' %state_0x01)

    def RegDIV_event(self,event):
        obj = event.GetEventObject()
        str = obj.GetStringSelection()
        sel = obj.GetSelection()
        state = self.i2c_access_box0(0x01,Mask().mask_div,16,sel)
        state_0x01 = format(state,'08b')
        self.textReg.SetValue("Reg_0x01: " '%s' %state_0x01)

    def RegTEST_event(self,event):
        obj = event.GetEventObject()
        str = obj.GetStringSelection()
        sel = obj.GetSelection()
        state = self.i2c_access_box0(0x01,Mask().mask_test,64,sel)
        state_0x01 = format(state,'08b')
        self.textReg.SetValue("Reg_0x01: " '%s' %state_0x01)

    def CloseWindow(self, event):
        self.timer.Stop()
        wx.Exit()

    def OnTimer(self,event):
	self.bdc = wx.BufferedDC(self.cdc, self.bmp)
	self.gcdc = wx.GCDC(self.bdc)
	self.gcdc.Clear()
        state_lsb = self.i2c_access_read(0x10)
        state_msb = self.i2c_access_read(0x11)
        tdata = float(state_msb * 256 + state_lsb) / 2**16
	
	self.data.append((self.i, tdata))
	if len(self.data) >= 60:
            self.data = self.data[-61:]

        line = plot.PolyLine(self.data, legend='Pos Y', colour='red', width = 1)
        self.gc = plot.PlotGraphics([line], 'Line Graph', 'X Axis', 'Y Axis')
        self.plotter.Draw(self.gc, xAxis=(max(0,self.i-60), self.i), yAxis=(0, 2))
        self.i += 1


from I2C import I2ctask
if __name__ == '__main__' :
	device = 0x05
	device7410 = 0x48
	p1 = I2ctask()
	p1.I2c_write(device,0x01,0x00) 
	rd = p1.I2c_read(device,0x01)
	print "%x" %rd
	p1.I2c_write(device7410,0x03,0xA0)

	#GUI
	app = wx.App()
	frame('GUI')
	app.MainLoop()

