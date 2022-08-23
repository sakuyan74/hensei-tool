# -*- coding: utf-8 -*-

import wx
import wx.xrc
import wx.grid
from static_data_manager import StaticDataManager
from hensei_data_manager import HenseiDataManager

SUITABLE_SORT_ORDER = {'S': 0, 'A': 1, 'B': 2, 'C': 3}


class UnitSelect(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"武将選択", pos=wx.DefaultPosition, size=wx.Size(931, 346), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer113 = wx.BoxSizer(wx.VERTICAL)

        bSizer116 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText105 = wx.StaticText(self, wx.ID_ANY, u"武将名絞り込み", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText105.Wrap(-1)

        bSizer116.Add(self.m_staticText105, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.LEFT | wx.TOP, 5)

        self.name_filter_text_ctrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer116.Add(self.name_filter_text_ctrl, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        
        self.Bind(wx.EVT_TEXT, self.OnFilterText, self.name_filter_text_ctrl)

        bSizer113.Add(bSizer116, 0, wx.EXPAND, 5)

        bSizer114 = wx.BoxSizer(wx.VERTICAL)

        sbSizer26 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"武将選択（ダブルクリックで選択）"), wx.VERTICAL)

        self.m_staticText109 = wx.StaticText(sbSizer26.GetStaticBox(), wx.ID_ANY, u"※他編成で選択済みの武将は表示されません", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText109.Wrap(-1)

        sbSizer26.Add(self.m_staticText109, 0, wx.ALL, 5)

        self.busyo_table = BusyoTable(sbSizer26.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, style=wx.LC_REPORT | wx.LC_VIRTUAL)
        self.busyo_table.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnDClickList)

        sbSizer26.Add(self.busyo_table, 0, wx.ALL | wx.EXPAND, 5)

        bSizer114.Add(sbSizer26, 1, wx.EXPAND, 5)

        bSizer113.Add(bSizer114, 1, wx.EXPAND, 5)

        bSizer115 = wx.BoxSizer(wx.VERTICAL)

        self.cancel_button = wx.Button(self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer115.Add(self.cancel_button, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        bSizer113.Add(bSizer115, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer113)
        self.Layout()

        self.Centre(wx.BOTH)

    def OnDClickList(self, event):
        busyo_id = self.busyo_table.get_busyo_id(event.GetIndex())
        print(busyo_id)
        self.EndModal(wx.ID_HIGHEST + busyo_id)

    def OnFilterText(self, event):
        key = self.name_filter_text_ctrl.GetValue()
        self.busyo_table.set_filter_key(key)
        return

    def __del__(self):
        pass


class BusyoTable(wx.ListCtrl):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.static_manager = StaticDataManager()
        self.hensei_manager = HenseiDataManager()

        for i, col in enumerate(("武将名", "陣営", "レア", "コスト", "馬", "盾", "弓", "槍", "兵器", "水軍")):
            self.InsertColumn(i, col)

        selected_busyo_list = self.hensei_manager.get_selected_busyo_list()

        data = self.static_manager.get_busyo_list(selected_busyo_list)

        self.items = data
        self.SetItemCount(len(self.items))
        self.Bind(wx.EVT_LIST_COL_CLICK, self.Sort)
        self.prevColumn = None
        self.sortAcend = True
        self.filter_key = ""

    def Sort(self, event):
        col = event.GetColumn()
        if col != self.prevColumn:
            self.sortAcend = True
        else:
            if self.sortAcend:
                self.sortAcend = None
            else:
                self.sortAcend = True
        if self.sortAcend:
            if col > 3:
                self.items.sort(key=lambda x: SUITABLE_SORT_ORDER[x[col]])
            else:
                self.items.sort(key=lambda x: x[col])
        else:
            if col > 3:
                self.items.sort(key=lambda x: SUITABLE_SORT_ORDER[x[col]], reverse=True)
            else:
                self.items.sort(key=lambda x: x[col], reverse=True)
        self.prevColumn = col
        if self.filter_key == "":
            self.DeleteAllItems()
            self.SetItemCount(len(self.items))
            return
        items = list(filter(lambda x: self.filter_key in x[0], self.items))
        self.DeleteAllItems()
        self.SetItemCount(len(items))

    def OnGetItemText(self, line, col):
        if self.filter_key == "":
            return self.items[line][col]
        else:
            items = list(filter(lambda x: self.filter_key in x[0], self.items))
            return items[line][col]

    def get_busyo_id(self, index):
        if self.filter_key == "":
            name = self.items[index][0]
        else:
            items = list(filter(lambda x: self.filter_key in x[0], self.items))
            name = items[index][0]
        return self.static_manager.get_busyo_id_by_name(name)
    
    def set_filter_key(self, key):
        self.filter_key = key
        if self.filter_key == "":
            self.DeleteAllItems()
            self.SetItemCount(len(self.items))
            return
        items = list(filter(lambda x: self.filter_key in x[0], self.items))
        self.DeleteAllItems()
        self.SetItemCount(len(items))
        return
