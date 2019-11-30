# -*- coding: utf-8 -*- 

import wx

application = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300,200))

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

element_array = ("element_1", "element_2", "element_4", "element_3", "element_5")
combobox_1 = wx.ComboBox(panel, wx.ID_ANY, u"選択してください", choices=element_array, style=wx.CB_SIMPLE)

layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(combobox_1, flag=wx.GROW)

panel.SetSizer(layout)

frame.Show()
application.MainLoop()
