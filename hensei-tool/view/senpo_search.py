# -*- coding: utf-8 -*-

import wx
import wx.xrc
import wx.grid
import traceback
from static_data_manager import StaticDataManager
from hensei_data_manager import HenseiDataManager


class SenpoSelect(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"戦法選択", pos=wx.DefaultPosition, size=wx.Size(931, 346), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer113 = wx.BoxSizer(wx.VERTICAL)

        bSizer116 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText105 = wx.StaticText(self, wx.ID_ANY, u"戦法名絞り込み", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText105.Wrap(-1)

        bSizer116.Add(self.m_staticText105, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.LEFT | wx.TOP, 5)

        self.name_filter_text_ctrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer116.Add(self.name_filter_text_ctrl, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.Bind(wx.EVT_TEXT, self.OnFilterText, self.name_filter_text_ctrl)

        bSizer113.Add(bSizer116, 0, wx.EXPAND, 5)

        bSizer114 = wx.BoxSizer(wx.VERTICAL)

        sbSizer26 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"戦法選択（ダブルクリックで選択）"), wx.VERTICAL)

        self.senpo_table = SenpoTable(sbSizer26.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, style=wx.LC_REPORT | wx.LC_VIRTUAL)
        for i in range(self.senpo_table.GetColumnCount()):
            self.senpo_table.SetColumnWidth(i, wx.LIST_AUTOSIZE_USEHEADER)
        self.senpo_table.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnDClickList)

        sbSizer26.Add(self.senpo_table, 0, wx.ALL | wx.EXPAND, 5)

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
        index = event.GetIndex()
        if self.senpo_table.check_learned_count(index):
            senpo_id = self.senpo_table.get_senpo_id(index)
            self.EndModal(wx.ID_HIGHEST + senpo_id)
        else:
            box = wx.MessageDialog(None, 'この戦法はこれ以上学習させることができません', '学習上限', wx.OK)
            box.ShowModal()

    def OnFilterText(self, event):
        key = self.name_filter_text_ctrl.GetValue()
        self.senpo_table.set_filter_key(key)
        return

    def __del__(self):
        pass


class SenpoTable(wx.ListCtrl):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        try:
            self.static_manager = StaticDataManager()
            self.hensei_manager = HenseiDataManager()

            for i, col in enumerate(("戦法名", "レア", "タイプ", "馬", "盾", "弓", "槍", "兵器", "効果種別", "発動率", "学習数", "説明（簡易）")):
                self.InsertColumn(i, col)

            # TODO 選択済みの戦法を取得して学習数に反映する処理
            selected_senpo_list = HenseiDataManager.get_selected_senpo_list()
            selected_senpo_data = self.static_manager.get_senpo_name_by_id_list(selected_senpo_list)
            learned_count = self.count_learned_senpo_by_name(selected_senpo_list, selected_senpo_data)

            data = self.static_manager.get_senpo_list()
            
            data = self.set_learned_count(learned_count, data)

            self.items = data
            self.SetItemCount(len(self.items))
            self.Bind(wx.EVT_LIST_COL_CLICK, self.Sort)
            self.prevColumn = None
            self.sortAcend = True
            self.filter_key = ""
        except Exception:
            print(traceback.format_exc())

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
            self.items.sort(key=lambda x: x[col])
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

    def get_senpo_id(self, index):
        if self.filter_key == "":
            name = self.items[index][0]
        else:
            items = list(filter(lambda x: self.filter_key in x[0], self.items))
            name = items[index][0]
        return self.static_manager.get_senpo_id_by_name(name)

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
    
    def count_learned_senpo_by_name(self, selected_list, name_list):
        learned_senpo_dict = {}
        
        for id in selected_list:
            print(name_list)
            senpo_name = name_list[id]
            if senpo_name not in learned_senpo_dict:
                learned_senpo_dict[senpo_name] = 1
            else:
                learned_senpo_dict[senpo_name] = learned_senpo_dict[senpo_name] + 1
        
        return learned_senpo_dict
    
    def set_learned_count(self, learned_count, data):
        for item in data:
            if item[0] not in learned_count:
                item[10] = "0/" + str(item[10])
            else:
                item[10] = str(learned_count[item[0]]) + "/" + str(item[10])
        return data

    def check_learned_count(self, index):
        cap = self.items[index][10]
        cap_list = cap.split("/")
        if cap_list[0] == cap_list[1]:
            return False
        else:
            return True
