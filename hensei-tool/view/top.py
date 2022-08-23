# -*- coding: utf-8 -*-
import wx
import wx.xrc
from view.busyo_search import UnitSelect
from view.senpo_search import SenpoSelect
from hensei_data_manager import HenseiDataManager
from static_data_manager import StaticDataManager
from status_manager import StatusManager

###########################################################################
# Class TopFrame
###########################################################################

ARMY_KIND = ["馬", "盾", "弓", "槍"]
LABEL_CHOICE = "選択"
LABEL_NOTHING = "―"
LABEL_ZERO = "0"

ID_SELECT_MAIN = wx.ID_HIGHEST + 1
ID_SELECT_SUB_1 = wx.ID_HIGHEST + 2
ID_SELECT_SUB_2 = wx.ID_HIGHEST + 3
ID_SELECT_MAIN_SENPO_2 = wx.ID_HIGHEST + 4
ID_SELECT_MAIN_SENPO_3 = wx.ID_HIGHEST + 5
ID_SELECT_SUB_1_SENPO_2 = wx.ID_HIGHEST + 6
ID_SELECT_SUB_1_SENPO_3 = wx.ID_HIGHEST + 7
ID_SELECT_SUB_2_SENPO_2 = wx.ID_HIGHEST + 8
ID_SELECT_SUB_2_SENPO_3 = wx.ID_HIGHEST + 9
ID_SELECT_MAIN_HEIHO_1 = wx.ID_HIGHEST + 10
ID_SELECT_MAIN_HEIHO_2 = wx.ID_HIGHEST + 11
ID_SELECT_MAIN_HEIHO_3 = wx.ID_HIGHEST + 12
ID_SELECT_SUB_1_HEIHO_1 = wx.ID_HIGHEST + 13
ID_SELECT_SUB_1_HEIHO_2 = wx.ID_HIGHEST + 14
ID_SELECT_SUB_1_HEIHO_3 = wx.ID_HIGHEST + 15
ID_SELECT_SUB_2_HEIHO_1 = wx.ID_HIGHEST + 16
ID_SELECT_SUB_2_HEIHO_2 = wx.ID_HIGHEST + 17
ID_SELECT_SUB_2_HEIHO_3 = wx.ID_HIGHEST + 18
ID_SELECT_CLEAR_MAIN = wx.ID_HIGHEST + 19
ID_SELECT_CLEAR_SUB_1 = wx.ID_HIGHEST + 20
ID_SELECT_CLEAR_SUB_2 = wx.ID_HIGHEST + 21
ID_CHANGE_HENSEI_1 = wx.ID_HIGHEST + 22
ID_CHANGE_HENSEI_2 = wx.ID_HIGHEST + 23
ID_CHANGE_HENSEI_3 = wx.ID_HIGHEST + 24
ID_CHANGE_HENSEI_4 = wx.ID_HIGHEST + 25
ID_CHANGE_HENSEI_5 = wx.ID_HIGHEST + 26
ID_CHANGE_HENSEI_6 = wx.ID_HIGHEST + 27
ID_CHANGE_HENSEI_7 = wx.ID_HIGHEST + 28
ID_CHANGE_HENSEI_8 = wx.ID_HIGHEST + 29
ID_CHANGE_HENSEI_9 = wx.ID_HIGHEST + 30
ID_CHANGE_HENSEI_10 = wx.ID_HIGHEST + 31


class TopFrame (wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"編成ツール", pos=wx.DefaultPosition, size=wx.Size(1280, 850), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

        sbSizer7 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel4, wx.ID_ANY, u"操作"), wx.VERTICAL)

        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        self.output_button = wx.Button(sbSizer7.GetStaticBox(), wx.ID_ANY, u"編成セット出力", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer14.Add(self.output_button, 0, wx.ALL, 5)
        self.output_button.Disable()

        self.input_button = wx.Button(sbSizer7.GetStaticBox(), wx.ID_ANY, u"編成セット読込", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer14.Add(self.input_button, 0, wx.ALL, 5)
        self.input_button.Disable()

        self.output_discord_button = wx.Button(sbSizer7.GetStaticBox(), wx.ID_ANY, u"編成出力(Discord用)", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer14.Add(self.output_discord_button, 0, wx.ALL, 5)

        sbSizer7.Add(bSizer14, 1, wx.EXPAND, 5)

        self.m_panel4.SetSizer(sbSizer7)
        self.m_panel4.Layout()
        sbSizer7.Fit(self.m_panel4)
        bSizer5.Add(self.m_panel4, 0, wx.EXPAND | wx.ALL, 5)

        self.m_panel6 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer89 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel1 = wx.Panel(self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel1, wx.ID_ANY, u"編成選択"), wx.VERTICAL)

        self.h_select_1_button = wx.Button(sbSizer3.GetStaticBox(), ID_CHANGE_HENSEI_1, u"編成1", wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer3.Add(self.h_select_1_button, 1, wx.ALL, 5)

        self.h_select_2_button = wx.Button(sbSizer3.GetStaticBox(), ID_CHANGE_HENSEI_2, u"編成2", wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer3.Add(self.h_select_2_button, 1, wx.ALL, 5)

        self.h_select_3_button = wx.Button(sbSizer3.GetStaticBox(), ID_CHANGE_HENSEI_3, u"編成3", wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer3.Add(self.h_select_3_button, 1, wx.ALL, 5)

        self.h_select_4_button = wx.Button(sbSizer3.GetStaticBox(), ID_CHANGE_HENSEI_4, u"編成4", wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer3.Add(self.h_select_4_button, 1, wx.ALL, 5)

        self.h_select_5_button = wx.Button(sbSizer3.GetStaticBox(), ID_CHANGE_HENSEI_5, u"編成5", wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer3.Add(self.h_select_5_button, 1, wx.ALL, 5)

        self.h_select_6_button = wx.Button(sbSizer3.GetStaticBox(), ID_CHANGE_HENSEI_6, u"編成6", wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer3.Add(self.h_select_6_button, 1, wx.ALL, 5)

        self.h_select_7_button = wx.Button(sbSizer3.GetStaticBox(), ID_CHANGE_HENSEI_7, u"編成7", wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer3.Add(self.h_select_7_button, 1, wx.ALL, 5)

        self.h_select_8_button = wx.Button(sbSizer3.GetStaticBox(), ID_CHANGE_HENSEI_8, u"編成8", wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer3.Add(self.h_select_8_button, 1, wx.ALL, 5)

        self.h_select_9_button = wx.Button(sbSizer3.GetStaticBox(), ID_CHANGE_HENSEI_9, u"編成9", wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer3.Add(self.h_select_9_button, 1, wx.ALL, 5)

        self.h_select_10_button = wx.Button(sbSizer3.GetStaticBox(), ID_CHANGE_HENSEI_10, u"編成10", wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer3.Add(self.h_select_10_button, 1, wx.ALL, 5)
        
        self.Bind(wx.EVT_BUTTON, self.change_hensei, self.h_select_1_button)
        self.Bind(wx.EVT_BUTTON, self.change_hensei, self.h_select_2_button)
        self.Bind(wx.EVT_BUTTON, self.change_hensei, self.h_select_3_button)
        self.Bind(wx.EVT_BUTTON, self.change_hensei, self.h_select_4_button)
        self.Bind(wx.EVT_BUTTON, self.change_hensei, self.h_select_5_button)
        self.Bind(wx.EVT_BUTTON, self.change_hensei, self.h_select_6_button)
        self.Bind(wx.EVT_BUTTON, self.change_hensei, self.h_select_7_button)
        self.Bind(wx.EVT_BUTTON, self.change_hensei, self.h_select_8_button)
        self.Bind(wx.EVT_BUTTON, self.change_hensei, self.h_select_9_button)
        self.Bind(wx.EVT_BUTTON, self.change_hensei, self.h_select_10_button)

        self.m_panel1.SetSizer(sbSizer3)
        self.m_panel1.Layout()
        sbSizer3.Fit(self.m_panel1)
        bSizer89.Add(self.m_panel1, 0, wx.EXPAND | wx.ALL, 5)

        self.m_panel7 = wx.Panel(self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer91 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel2 = wx.Panel(self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer119 = wx.BoxSizer(wx.HORIZONTAL)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel2, wx.ID_ANY, u"兵種"), wx.VERTICAL)

        select_kind_choiceChoices = ["馬", "盾", "弓", "槍", "兵器", "水軍"]
        self.select_kind_choice = wx.Choice(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, select_kind_choiceChoices, 0)
        self.select_kind_choice.SetSelection(0)
        self.Bind(wx.EVT_CHOICE, self.update_kind, self.select_kind_choice)
        sbSizer2.Add(self.select_kind_choice, 0, wx.ALL, 5)

        bSizer119.Add(sbSizer2, 1, wx.EXPAND, 5)

        sbSizer21 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel2, wx.ID_ANY, u"レベル"), wx.VERTICAL)

        self.level_text_ctrl = wx.TextCtrl(sbSizer21.GetStaticBox(), wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.level_text_ctrl.SetMaxLength(2)
        sbSizer21.Add(self.level_text_ctrl, 0, wx.ALL, 5)

        bSizer119.Add(sbSizer21, 1, wx.EXPAND, 5)

        sbSizer211 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel2, wx.ID_ANY, u"兵戦レベル"), wx.VERTICAL)

        select_heisen_level_choiceChoices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.select_heisen_level_choice = wx.Choice(sbSizer211.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, select_heisen_level_choiceChoices, 0)
        self.select_heisen_level_choice.SetSelection(0)
        sbSizer211.Add(self.select_heisen_level_choice, 0, wx.ALL, 5)

        bSizer119.Add(sbSizer211, 1, wx.EXPAND, 5)

        sbSizer212 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel2, wx.ID_ANY, u"協力レベル"), wx.VERTICAL)
        select_kyoryoku_level_choiceChoices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.select_kyoryoku_level_choice = wx.Choice(sbSizer212.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, select_kyoryoku_level_choiceChoices, 0)
        self.select_kyoryoku_level_choice.SetSelection(0)
        sbSizer212.Add(self.select_kyoryoku_level_choice, 0, wx.ALL, 5)

        bSizer119.Add(sbSizer212, 1, wx.EXPAND, 5)

        sbSizer25 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel2, wx.ID_ANY, u"絆効果"), wx.VERTICAL)

        self.kizuna_label = wx.StaticText(sbSizer25.GetStaticBox(), wx.ID_ANY, u"なし（効果なし）", wx.DefaultPosition, wx.DefaultSize, 0)
        self.kizuna_label.Wrap(-1)

        sbSizer25.Add(self.kizuna_label, 0, wx.ALL, 5)

        bSizer119.Add(sbSizer25, 1, wx.EXPAND, 5)

        self.m_panel2.SetSizer(bSizer119)
        self.m_panel2.Layout()
        bSizer119.Fit(self.m_panel2)
        bSizer91.Add(self.m_panel2, 0, wx.ALL, 5)

        self.m_panel3 = wx.Panel(self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sbSizer6 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel3, wx.ID_ANY, u"編成"), wx.VERTICAL)

        bSizer19 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer19.SetMinSize(wx.Size(-1, 150))
        self.m_panel12 = wx.Panel(sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_THEME | wx.TAB_TRAVERSAL)
        bSizer271 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText431 = wx.StaticText(self.m_panel12, wx.ID_ANY, u"選択", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText431.Wrap(-1)

        bSizer271.Add(self.m_staticText431, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer3111 = wx.BoxSizer(wx.HORIZONTAL)

        self.main_unit_drop_button = wx.Button(self.m_panel12, ID_SELECT_CLEAR_MAIN, u"外す", wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_unit_drop_button.SetMaxSize(wx.Size(35, -1))
        self.Bind(wx.EVT_BUTTON, self.drop_unit, self.main_unit_drop_button)

        bSizer3111.Add(self.main_unit_drop_button, 0, wx.ALL | wx.EXPAND, 5)

        bSizer271.Add(bSizer3111, 1, wx.EXPAND, 5)

        bSizer3121 = wx.BoxSizer(wx.HORIZONTAL)

        self.sub_1_unit_drop_button = wx.Button(self.m_panel12, ID_SELECT_CLEAR_SUB_1, u"外す", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_1_unit_drop_button.SetMaxSize(wx.Size(35, -1))
        self.Bind(wx.EVT_BUTTON, self.drop_unit, self.sub_1_unit_drop_button)

        bSizer3121.Add(self.sub_1_unit_drop_button, 0, wx.ALL | wx.EXPAND, 5)

        bSizer271.Add(bSizer3121, 1, wx.EXPAND, 5)

        bSizer3131 = wx.BoxSizer(wx.HORIZONTAL)

        self.sub_2_unit_drop_button = wx.Button(self.m_panel12, ID_SELECT_CLEAR_SUB_2, u"外す", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_2_unit_drop_button.SetMaxSize(wx.Size(35, -1))
        self.Bind(wx.EVT_BUTTON, self.drop_unit, self.sub_2_unit_drop_button)

        bSizer3131.Add(self.sub_2_unit_drop_button, 0, wx.ALL | wx.EXPAND, 5)

        bSizer271.Add(bSizer3131, 1, wx.EXPAND, 5)

        self.m_panel12.SetSizer(bSizer271)
        self.m_panel12.Layout()
        bSizer271.Fit(self.m_panel12)
        bSizer19.Add(self.m_panel12, 0, wx.EXPAND | wx.ALL, 5)

        bSizer27 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText43 = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"武将名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText43.Wrap(-1)

        bSizer27.Add(self.m_staticText43, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer311 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText351 = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"主将", wx.DefaultPosition, wx.Size(50, -1), wx.ALIGN_LEFT)
        self.m_staticText351.Wrap(-1)

        bSizer311.Add(self.m_staticText351, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.main_unit_select_button = wx.Button(sbSizer6.GetStaticBox(), ID_SELECT_MAIN, u"選択", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer311.Add(self.main_unit_select_button, 0, wx.ALL | wx.EXPAND, 5)
        self.Bind(wx.EVT_BUTTON, self.show_unit_select, self.main_unit_select_button)

        bSizer27.Add(bSizer311, 1, wx.EXPAND, 5)

        bSizer312 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText352 = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"副将１", wx.DefaultPosition, wx.Size(50, -1), wx.ALIGN_LEFT)
        self.m_staticText352.Wrap(-1)

        bSizer312.Add(self.m_staticText352, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_1_unit_select_button = wx.Button(sbSizer6.GetStaticBox(), ID_SELECT_SUB_1, u"選択", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer312.Add(self.sub_1_unit_select_button, 0, wx.ALL | wx.EXPAND, 5)
        self.Bind(wx.EVT_BUTTON, self.show_unit_select, self.sub_1_unit_select_button)

        bSizer27.Add(bSizer312, 1, wx.EXPAND, 5)

        bSizer313 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText353 = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"副将２", wx.DefaultPosition, wx.Size(50, -1), wx.ALIGN_LEFT)
        self.m_staticText353.Wrap(-1)

        bSizer313.Add(self.m_staticText353, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_2_unit_select_button = wx.Button(sbSizer6.GetStaticBox(), ID_SELECT_SUB_2, u"選択", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer313.Add(self.sub_2_unit_select_button, 0, wx.ALL | wx.EXPAND, 5)
        self.Bind(wx.EVT_BUTTON, self.show_unit_select, self.sub_2_unit_select_button)

        bSizer27.Add(bSizer313, 1, wx.EXPAND, 5)

        bSizer19.Add(bSizer27, 1, wx.EXPAND, 5)

        bSizer2011 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1611 = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"陣営", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1611.Wrap(-1)

        bSizer2011.Add(self.m_staticText1611, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer4411 = wx.BoxSizer(wx.HORIZONTAL)

        self.main_country_label = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"魏", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.main_country_label.Wrap(-1)

        self.main_country_label.SetMaxSize(wx.Size(20, -1))

        bSizer4411.Add(self.main_country_label, 1, wx.ALIGN_CENTER | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer2011.Add(bSizer4411, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer4511 = wx.BoxSizer(wx.HORIZONTAL)

        self.sub_1_country_label = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"魏", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.sub_1_country_label.Wrap(-1)

        self.sub_1_country_label.SetMaxSize(wx.Size(20, -1))

        bSizer4511.Add(self.sub_1_country_label, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer2011.Add(bSizer4511, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer4611 = wx.BoxSizer(wx.HORIZONTAL)

        self.sub_2_country_label = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"魏", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.sub_2_country_label.Wrap(-1)

        self.sub_2_country_label.SetMaxSize(wx.Size(20, -1))

        bSizer4611.Add(self.sub_2_country_label, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer2011.Add(bSizer4611, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer19.Add(bSizer2011, 0, wx.EXPAND, 5)

        bSizer201 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText161 = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"適正", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText161.Wrap(-1)

        bSizer201.Add(self.m_staticText161, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer441 = wx.BoxSizer(wx.HORIZONTAL)

        self.main_suitable_label = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"S", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.main_suitable_label.Wrap(-1)

        self.main_suitable_label.SetMaxSize(wx.Size(20, -1))

        bSizer441.Add(self.main_suitable_label, 1, wx.ALIGN_CENTER | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer201.Add(bSizer441, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer451 = wx.BoxSizer(wx.HORIZONTAL)

        self.sub_1_suitable_label = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"S", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.sub_1_suitable_label.Wrap(-1)

        self.sub_1_suitable_label.SetMaxSize(wx.Size(20, -1))

        bSizer451.Add(self.sub_1_suitable_label, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer201.Add(bSizer451, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer461 = wx.BoxSizer(wx.HORIZONTAL)

        self.sub_2_suitable_label = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"S", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.sub_2_suitable_label.Wrap(-1)

        self.sub_2_suitable_label.SetMaxSize(wx.Size(20, -1))

        bSizer461.Add(self.sub_2_suitable_label, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer201.Add(bSizer461, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer19.Add(bSizer201, 0, wx.EXPAND, 5)

        bSizer20 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText16 = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"固有戦法", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)

        bSizer20.Add(self.m_staticText16, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer44 = wx.BoxSizer(wx.HORIZONTAL)

        self.main_unique_senpo_label = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"固有戦法1", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.main_unique_senpo_label.Wrap(-1)

        bSizer44.Add(self.main_unique_senpo_label, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer20.Add(bSizer44, 1, wx.EXPAND, 5)

        bSizer45 = wx.BoxSizer(wx.HORIZONTAL)

        self.sub_1_unique_senpo_label = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"固有戦法2", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.sub_1_unique_senpo_label.Wrap(-1)

        bSizer45.Add(self.sub_1_unique_senpo_label, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer20.Add(bSizer45, 1, wx.EXPAND, 5)

        bSizer46 = wx.BoxSizer(wx.HORIZONTAL)

        self.sub_2_unique_senpo_label = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"固有戦法3", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.sub_2_unique_senpo_label.Wrap(-1)

        bSizer46.Add(self.sub_2_unique_senpo_label, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer20.Add(bSizer46, 1, wx.EXPAND, 5)

        bSizer19.Add(bSizer20, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        bSizer21 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText22 = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"戦法２", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)

        bSizer21.Add(self.m_staticText22, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer47 = wx.BoxSizer(wx.HORIZONTAL)
        self.main_senpo2_select_button = wx.Button(sbSizer6.GetStaticBox(), ID_SELECT_MAIN_SENPO_2, u"選択", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer47.Add(self.main_senpo2_select_button, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.Bind(wx.EVT_BUTTON, self.show_senpo_select, self.main_senpo2_select_button)
        bSizer21.Add(bSizer47, 1, wx.EXPAND, 5)

        bSizer49 = wx.BoxSizer(wx.HORIZONTAL)
        self.sub_1_senpo2_select_button = wx.Button(sbSizer6.GetStaticBox(), ID_SELECT_SUB_1_SENPO_2, u"選択", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer49.Add(self.sub_1_senpo2_select_button, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.Bind(wx.EVT_BUTTON, self.show_senpo_select, self.sub_1_senpo2_select_button)
        bSizer21.Add(bSizer49, 1, wx.EXPAND, 5)

        bSizer50 = wx.BoxSizer(wx.HORIZONTAL)
        self.sub_2_senpo2_select_button = wx.Button(sbSizer6.GetStaticBox(), ID_SELECT_SUB_2_SENPO_2, u"選択", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer50.Add(self.sub_2_senpo2_select_button, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.Bind(wx.EVT_BUTTON, self.show_senpo_select, self.sub_2_senpo2_select_button)
        bSizer21.Add(bSizer50, 1, wx.EXPAND, 5)
        
        bSizer19.Add(bSizer21, 1, wx.EXPAND, 5)

        bSizer22 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText26 = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"戦法３", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText26.Wrap(-1)

        bSizer22.Add(self.m_staticText26, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer51 = wx.BoxSizer(wx.HORIZONTAL)
        self.main_senpo3_select_button = wx.Button(sbSizer6.GetStaticBox(), ID_SELECT_MAIN_SENPO_3, u"選択", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer51.Add(self.main_senpo3_select_button, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.Bind(wx.EVT_BUTTON, self.show_senpo_select, self.main_senpo3_select_button)
        bSizer22.Add(bSizer51, 1, wx.EXPAND, 5)

        bSizer52 = wx.BoxSizer(wx.HORIZONTAL)
        self.sub_1_senpo3_select_button = wx.Button(sbSizer6.GetStaticBox(), ID_SELECT_SUB_1_SENPO_3, u"選択", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer52.Add(self.sub_1_senpo3_select_button, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.Bind(wx.EVT_BUTTON, self.show_senpo_select, self.sub_1_senpo3_select_button)
        bSizer22.Add(bSizer52, 1, wx.EXPAND, 5)

        bSizer53 = wx.BoxSizer(wx.HORIZONTAL)
        self.sub_2_senpo3_select_button = wx.Button(sbSizer6.GetStaticBox(), ID_SELECT_SUB_2_SENPO_3, u"選択", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer53.Add(self.sub_2_senpo3_select_button, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.Bind(wx.EVT_BUTTON, self.show_senpo_select, self.sub_2_senpo3_select_button)
        bSizer22.Add(bSizer53, 1, wx.EXPAND, 5)

        bSizer19.Add(bSizer22, 1, wx.EXPAND, 5)

        bSizer23 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText27 = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"兵法書", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText27.Wrap(-1)

        bSizer23.Add(self.m_staticText27, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer54 = wx.BoxSizer(wx.HORIZONTAL)

        main_heihousyo_choiceChoices = []
        self.main_heihousyo_choice = wx.Choice(sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, main_heihousyo_choiceChoices, 0)
        self.main_heihousyo_choice.Bind(wx.EVT_CHOICE, self.on_select_main_heihosyo_choice)
        bSizer54.Add(self.main_heihousyo_choice, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer23.Add(bSizer54, 1, wx.EXPAND, 5)

        bSizer55 = wx.BoxSizer(wx.HORIZONTAL)

        sub_1_heihousyo_choiceChoices = []
        self.sub_1_heihousyo_choice = wx.Choice(sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sub_1_heihousyo_choiceChoices, 0)
        self.sub_1_heihousyo_choice.Bind(wx.EVT_CHOICE, self.on_select_sub_1_heihosyo_choice)
        bSizer55.Add(self.sub_1_heihousyo_choice, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer23.Add(bSizer55, 1, wx.EXPAND, 5)

        bSizer56 = wx.BoxSizer(wx.HORIZONTAL)

        sub_2_heihousyo_choiceChoices = []
        self.sub_2_heihousyo_choice = wx.Choice(sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sub_2_heihousyo_choiceChoices, 0)
        self.sub_2_heihousyo_choice.Bind(wx.EVT_CHOICE, self.on_select_sub_2_heihosyo_choice)
        bSizer56.Add(self.sub_2_heihousyo_choice, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer23.Add(bSizer56, 1, wx.EXPAND, 5)

        bSizer19.Add(bSizer23, 1, wx.EXPAND, 5)

        bSizer231 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText271 = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"兵法１", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText271.Wrap(-1)

        bSizer231.Add(self.m_staticText271, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer541 = wx.BoxSizer(wx.HORIZONTAL)

        main_heihou1_choiceChoices = []
        self.main_heihou1_choice = wx.Choice(sbSizer6.GetStaticBox(), ID_SELECT_MAIN_HEIHO_1, wx.DefaultPosition, wx.DefaultSize, main_heihou1_choiceChoices, 0)
        self.main_heihou1_choice.SetSelection(0)
        self.main_heihou1_choice.Bind(wx.EVT_CHOICE, self.on_select_heiho_1_choice)
        bSizer541.Add(self.main_heihou1_choice, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer231.Add(bSizer541, 1, wx.EXPAND, 5)

        bSizer551 = wx.BoxSizer(wx.HORIZONTAL)

        sub_1_heihou1_choiceChoices = []
        self.sub_1_heihou1_choice = wx.Choice(sbSizer6.GetStaticBox(), ID_SELECT_SUB_1_HEIHO_1, wx.DefaultPosition, wx.DefaultSize, sub_1_heihou1_choiceChoices, 0)
        self.sub_1_heihou1_choice.SetSelection(0)
        self.sub_1_heihou1_choice.Bind(wx.EVT_CHOICE, self.on_select_heiho_1_choice)
        bSizer551.Add(self.sub_1_heihou1_choice, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer231.Add(bSizer551, 1, wx.EXPAND, 5)

        bSizer561 = wx.BoxSizer(wx.HORIZONTAL)

        sub_2_heihou1_choiceChoices = []
        self.sub_2_heihou1_choice = wx.Choice(sbSizer6.GetStaticBox(), ID_SELECT_SUB_2_HEIHO_1, wx.DefaultPosition, wx.DefaultSize, sub_2_heihou1_choiceChoices, 0)
        self.sub_2_heihou1_choice.SetSelection(0)
        self.sub_2_heihou1_choice.Bind(wx.EVT_CHOICE, self.on_select_heiho_1_choice)
        bSizer561.Add(self.sub_2_heihou1_choice, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer231.Add(bSizer561, 1, wx.EXPAND, 5)

        bSizer19.Add(bSizer231, 1, wx.EXPAND, 5)

        bSizer232 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText272 = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"兵法２", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText272.Wrap(-1)

        bSizer232.Add(self.m_staticText272, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer542 = wx.BoxSizer(wx.HORIZONTAL)

        main_heihou2_choiceChoices = []
        self.main_heihou2_choice = wx.Choice(sbSizer6.GetStaticBox(), ID_SELECT_MAIN_HEIHO_2, wx.DefaultPosition, wx.DefaultSize, main_heihou2_choiceChoices, 0)
        self.main_heihou2_choice.SetSelection(0)
        self.main_heihou2_choice.Bind(wx.EVT_CHOICE, self.on_select_heiho_2_3_choice)
        bSizer542.Add(self.main_heihou2_choice, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer232.Add(bSizer542, 1, wx.EXPAND, 5)

        bSizer552 = wx.BoxSizer(wx.HORIZONTAL)

        sub_1_heihou2_choiceChoices = []
        self.sub_1_heihou2_choice = wx.Choice(sbSizer6.GetStaticBox(), ID_SELECT_SUB_1_HEIHO_2, wx.DefaultPosition, wx.DefaultSize, sub_1_heihou2_choiceChoices, 0)
        self.sub_1_heihou2_choice.SetSelection(0)
        self.sub_1_heihou2_choice.Bind(wx.EVT_CHOICE, self.on_select_heiho_2_3_choice)
        bSizer552.Add(self.sub_1_heihou2_choice, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer232.Add(bSizer552, 1, wx.EXPAND, 5)

        bSizer562 = wx.BoxSizer(wx.HORIZONTAL)

        sub_2_heihou2_choiceChoices = []
        self.sub_2_heihou2_choice = wx.Choice(sbSizer6.GetStaticBox(), ID_SELECT_SUB_2_HEIHO_2, wx.DefaultPosition, wx.DefaultSize, sub_2_heihou2_choiceChoices, 0)
        self.sub_2_heihou2_choice.SetSelection(0)
        self.sub_2_heihou2_choice.Bind(wx.EVT_CHOICE, self.on_select_heiho_2_3_choice)
        bSizer562.Add(self.sub_2_heihou2_choice, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer232.Add(bSizer562, 1, wx.EXPAND, 5)

        bSizer19.Add(bSizer232, 1, wx.EXPAND, 5)

        bSizer2321 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2721 = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"兵法３", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2721.Wrap(-1)

        bSizer2321.Add(self.m_staticText2721, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer5421 = wx.BoxSizer(wx.HORIZONTAL)

        main_heihou3_choiceChoices = []
        self.main_heihou3_choice = wx.Choice(sbSizer6.GetStaticBox(), ID_SELECT_MAIN_HEIHO_3, wx.DefaultPosition, wx.DefaultSize, main_heihou3_choiceChoices, 0)
        self.main_heihou3_choice.SetSelection(0)
        self.main_heihou3_choice.Bind(wx.EVT_CHOICE, self.on_select_heiho_2_3_choice)
        bSizer5421.Add(self.main_heihou3_choice, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer2321.Add(bSizer5421, 1, wx.EXPAND, 5)

        bSizer5521 = wx.BoxSizer(wx.HORIZONTAL)

        sub_1_heihou3_choiceChoices = []
        self.sub_1_heihou3_choice = wx.Choice(sbSizer6.GetStaticBox(), ID_SELECT_SUB_1_HEIHO_3, wx.DefaultPosition, wx.DefaultSize, sub_1_heihou3_choiceChoices, 0)
        self.sub_1_heihou3_choice.SetSelection(0)
        self.sub_1_heihou3_choice.Bind(wx.EVT_CHOICE, self.on_select_heiho_2_3_choice)
        bSizer5521.Add(self.sub_1_heihou3_choice, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer2321.Add(bSizer5521, 1, wx.EXPAND, 5)

        bSizer5621 = wx.BoxSizer(wx.HORIZONTAL)

        sub_2_heihou3_choiceChoices = []
        self.sub_2_heihou3_choice = wx.Choice(sbSizer6.GetStaticBox(), ID_SELECT_SUB_2_HEIHO_3, wx.DefaultPosition, wx.DefaultSize, sub_2_heihou3_choiceChoices, 0)
        self.sub_2_heihou3_choice.SetSelection(0)
        self.sub_2_heihou3_choice.Bind(wx.EVT_CHOICE, self.on_select_heiho_2_3_choice)
        bSizer5621.Add(self.sub_2_heihou3_choice, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer2321.Add(bSizer5621, 1, wx.EXPAND, 5)

        bSizer19.Add(bSizer2321, 1, wx.EXPAND, 5)

        sbSizer6.Add(bSizer19, 1, wx.EXPAND, 5)

        self.m_panel3.SetSizer(sbSizer6)
        self.m_panel3.Layout()
        sbSizer6.Fit(self.m_panel3)
        bSizer91.Add(self.m_panel3, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel8 = wx.Panel(self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sbSizer9 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel8, wx.ID_ANY, u"ステータス配分（シミュレータ用）"), wx.HORIZONTAL)

        bSizer100 = wx.BoxSizer(wx.HORIZONTAL)

        sbSizer20 = wx.StaticBoxSizer(wx.StaticBox(sbSizer9.GetStaticBox(), wx.ID_ANY, u"主将"), wx.VERTICAL)

        bSizer129 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer121 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText58 = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, u"ランクアップ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText58.Wrap(-1)

        bSizer121.Add(self.m_staticText58, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        main_rankup_choiceChoices = [u"0回", u"1回", u"2回", u"3回", u"4回", u"5回"]
        self.main_rankup_choice = wx.Choice(sbSizer20.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, main_rankup_choiceChoices, 0)
        self.main_rankup_choice.SetSelection(0)
        bSizer121.Add(self.main_rankup_choice, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer129.Add(bSizer121, 0, wx.EXPAND, 5)

        bSizer1211 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText581 = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, u"秘蔵", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText581.Wrap(-1)

        bSizer1211.Add(self.m_staticText581, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.main_hizo_checkbox = wx.CheckBox(sbSizer20.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1211.Add(self.main_hizo_checkbox, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer129.Add(bSizer1211, 0, wx.EXPAND, 5)

        bSizer12111 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText5811 = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, u"アニメ解放", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5811.Wrap(-1)

        bSizer12111.Add(self.m_staticText5811, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.main_anime_checkbox = wx.CheckBox(sbSizer20.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12111.Add(self.main_anime_checkbox, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer129.Add(bSizer12111, 1, wx.EXPAND, 5)

        sbSizer20.Add(bSizer129, 1, wx.EXPAND, 5)

        bSizer130 = wx.BoxSizer(wx.VERTICAL)

        bSizer131 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText64 = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, u"残り配分ポイント：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText64.Wrap(-1)

        bSizer131.Add(self.m_staticText64, 0, wx.ALL, 5)

        self.main_remained_point_label = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, u"60", wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_remained_point_label.Wrap(-1)

        bSizer131.Add(self.main_remained_point_label, 0, wx.ALL, 5)

        bSizer130.Add(bSizer131, 0, wx.EXPAND, 5)

        bSizer132 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer133 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText65 = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, u"武力", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText65.Wrap(-1)

        bSizer133.Add(self.m_staticText65, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.main_str_point_text_ctrl = wx.TextCtrl(sbSizer20.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_str_point_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer133.Add(self.main_str_point_text_ctrl, 0, wx.ALL, 5)

        bSizer132.Add(bSizer133, 0, wx.EXPAND, 5)

        bSizer1331 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText651 = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, u"統率", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText651.Wrap(-1)

        bSizer1331.Add(self.m_staticText651, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.main_def_point_text_ctrl = wx.TextCtrl(sbSizer20.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_def_point_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer1331.Add(self.main_def_point_text_ctrl, 0, wx.ALL, 5)

        bSizer132.Add(bSizer1331, 0, wx.EXPAND, 5)

        bSizer1332 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText652 = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, u"知力", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText652.Wrap(-1)

        bSizer1332.Add(self.m_staticText652, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.main_int_point_text_ctrl = wx.TextCtrl(sbSizer20.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_int_point_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer1332.Add(self.main_int_point_text_ctrl, 0, wx.ALL, 5)

        bSizer132.Add(bSizer1332, 0, wx.EXPAND, 5)

        bSizer13321 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText6521 = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, u"速度", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6521.Wrap(-1)

        bSizer13321.Add(self.m_staticText6521, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.main_spd_point_text_ctrl = wx.TextCtrl(sbSizer20.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_spd_point_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer13321.Add(self.main_spd_point_text_ctrl, 0, wx.ALL, 5)

        bSizer132.Add(bSizer13321, 0, wx.EXPAND, 5)

        bSizer130.Add(bSizer132, 0, wx.EXPAND, 5)

        sbSizer20.Add(bSizer130, 1, wx.EXPAND, 5)

        sbSizer26 = wx.StaticBoxSizer(wx.StaticBox(sbSizer20.GetStaticBox(), wx.ID_ANY, u"装備補正"), wx.VERTICAL)

        bSizer1323 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1335 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText655 = wx.StaticText(sbSizer26.GetStaticBox(), wx.ID_ANY, u"武力", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText655.Wrap(-1)

        bSizer1335.Add(self.m_staticText655, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.main_str_point_eq_text_ctrl = wx.TextCtrl(sbSizer26.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_str_point_eq_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer1335.Add(self.main_str_point_eq_text_ctrl, 0, wx.ALL, 5)

        bSizer1323.Add(bSizer1335, 0, wx.EXPAND, 5)

        bSizer13313 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText6513 = wx.StaticText(sbSizer26.GetStaticBox(), wx.ID_ANY, u"統率", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6513.Wrap(-1)

        bSizer13313.Add(self.m_staticText6513, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.main_def_point_eq_text_ctrl = wx.TextCtrl(sbSizer26.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_def_point_eq_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer13313.Add(self.main_def_point_eq_text_ctrl, 0, wx.ALL, 5)

        bSizer1323.Add(bSizer13313, 0, wx.EXPAND, 5)

        bSizer13324 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText6524 = wx.StaticText(sbSizer26.GetStaticBox(), wx.ID_ANY, u"知力", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6524.Wrap(-1)

        bSizer13324.Add(self.m_staticText6524, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.main_int_point_eq_text_ctrl = wx.TextCtrl(sbSizer26.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_int_point_eq_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer13324.Add(self.main_int_point_eq_text_ctrl, 0, wx.ALL, 5)

        bSizer1323.Add(bSizer13324, 0, wx.EXPAND, 5)

        bSizer133213 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText65213 = wx.StaticText(sbSizer26.GetStaticBox(), wx.ID_ANY, u"速度", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText65213.Wrap(-1)

        bSizer133213.Add(self.m_staticText65213, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.main_spd_point_eq_text_ctrl = wx.TextCtrl(sbSizer26.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_spd_point_eq_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer133213.Add(self.main_spd_point_eq_text_ctrl, 0, wx.ALL, 5)

        bSizer1323.Add(bSizer133213, 0, wx.EXPAND, 5)

        sbSizer26.Add(bSizer1323, 1, wx.EXPAND, 5)

        sbSizer20.Add(sbSizer26, 1, wx.EXPAND, 5)

        self.m_panel9 = wx.Panel(sbSizer20.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_STATIC | wx.TAB_TRAVERSAL)
        bSizer220 = wx.BoxSizer(wx.VERTICAL)

        bSizer221 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText134 = wx.StaticText(self.m_panel9, wx.ID_ANY, u"装備スキル設定", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText134.Wrap(-1)

        bSizer221.Add(self.m_staticText134, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.main_eq_skill_select_button = wx.Button(self.m_panel9, wx.ID_ANY, u"設定", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer221.Add(self.main_eq_skill_select_button, 0, wx.ALL, 5)

        bSizer220.Add(bSizer221, 0, wx.EXPAND, 5)

        bSizer222 = wx.BoxSizer(wx.HORIZONTAL)

        self.main_eq_skill_label = wx.StaticText(self.m_panel9, wx.ID_ANY, u"明朗", wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_eq_skill_label.Wrap(-1)

        bSizer222.Add(self.main_eq_skill_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer220.Add(bSizer222, 1, wx.EXPAND, 5)

        self.m_panel9.SetSizer(bSizer220)
        self.m_panel9.Layout()
        bSizer220.Fit(self.m_panel9)
        sbSizer20.Add(self.m_panel9, 0, wx.EXPAND | wx.ALL, 5)

        bSizer100.Add(sbSizer20, 1, wx.ALL | wx.EXPAND, 5)

        sbSizer201 = wx.StaticBoxSizer(wx.StaticBox(sbSizer9.GetStaticBox(), wx.ID_ANY, u"副将1"), wx.VERTICAL)

        bSizer1291 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1212 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText582 = wx.StaticText(sbSizer201.GetStaticBox(), wx.ID_ANY, u"ランクアップ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText582.Wrap(-1)

        bSizer1212.Add(self.m_staticText582, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        sub_1_rankup_choiceChoices = [u"0回", u"1回", u"2回", u"3回", u"4回", u"5回"]
        self.sub_1_rankup_choice = wx.Choice(sbSizer201.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sub_1_rankup_choiceChoices, 0)
        self.sub_1_rankup_choice.SetSelection(0)
        bSizer1212.Add(self.sub_1_rankup_choice, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer1291.Add(bSizer1212, 0, wx.EXPAND, 5)

        bSizer12112 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText5812 = wx.StaticText(sbSizer201.GetStaticBox(), wx.ID_ANY, u"秘蔵", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5812.Wrap(-1)

        bSizer12112.Add(self.m_staticText5812, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_1_hizo_checkbox = wx.CheckBox(sbSizer201.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12112.Add(self.sub_1_hizo_checkbox, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer1291.Add(bSizer12112, 0, wx.EXPAND, 5)

        bSizer121111 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText58111 = wx.StaticText(sbSizer201.GetStaticBox(), wx.ID_ANY, u"アニメ解放", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText58111.Wrap(-1)

        bSizer121111.Add(self.m_staticText58111, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_1_anime_checkbox = wx.CheckBox(sbSizer201.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer121111.Add(self.sub_1_anime_checkbox, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer1291.Add(bSizer121111, 1, wx.EXPAND, 5)

        sbSizer201.Add(bSizer1291, 1, wx.EXPAND, 5)

        bSizer1301 = wx.BoxSizer(wx.VERTICAL)

        bSizer1311 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText641 = wx.StaticText(sbSizer201.GetStaticBox(), wx.ID_ANY, u"残り配分ポイント：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText641.Wrap(-1)

        bSizer1311.Add(self.m_staticText641, 0, wx.ALL, 5)

        self.sub_1_remained_point_label = wx.StaticText(sbSizer201.GetStaticBox(), wx.ID_ANY, u"60", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_1_remained_point_label.Wrap(-1)

        bSizer1311.Add(self.sub_1_remained_point_label, 0, wx.ALL, 5)

        bSizer1301.Add(bSizer1311, 0, wx.EXPAND, 5)

        bSizer1321 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1333 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText653 = wx.StaticText(sbSizer201.GetStaticBox(), wx.ID_ANY, u"武力", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText653.Wrap(-1)

        bSizer1333.Add(self.m_staticText653, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_1_str_point_text_ctrl = wx.TextCtrl(sbSizer201.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_1_str_point_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer1333.Add(self.sub_1_str_point_text_ctrl, 0, wx.ALL, 5)

        bSizer1321.Add(bSizer1333, 0, wx.EXPAND, 5)

        bSizer13311 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText6511 = wx.StaticText(sbSizer201.GetStaticBox(), wx.ID_ANY, u"統率", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6511.Wrap(-1)

        bSizer13311.Add(self.m_staticText6511, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_1_def_point_text_ctrl = wx.TextCtrl(sbSizer201.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_1_def_point_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer13311.Add(self.sub_1_def_point_text_ctrl, 0, wx.ALL, 5)

        bSizer1321.Add(bSizer13311, 0, wx.EXPAND, 5)

        bSizer13322 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText6522 = wx.StaticText(sbSizer201.GetStaticBox(), wx.ID_ANY, u"知力", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6522.Wrap(-1)

        bSizer13322.Add(self.m_staticText6522, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_1_int_point_text_ctrl = wx.TextCtrl(sbSizer201.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_1_int_point_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer13322.Add(self.sub_1_int_point_text_ctrl, 0, wx.ALL, 5)

        bSizer1321.Add(bSizer13322, 0, wx.EXPAND, 5)

        bSizer133211 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText65211 = wx.StaticText(sbSizer201.GetStaticBox(), wx.ID_ANY, u"速度", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText65211.Wrap(-1)

        bSizer133211.Add(self.m_staticText65211, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_1_spd_point_text_ctrl = wx.TextCtrl(sbSizer201.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_1_spd_point_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer133211.Add(self.sub_1_spd_point_text_ctrl, 0, wx.ALL, 5)

        bSizer1321.Add(bSizer133211, 0, wx.EXPAND, 5)

        bSizer1301.Add(bSizer1321, 0, wx.EXPAND, 5)

        sbSizer201.Add(bSizer1301, 1, wx.EXPAND, 5)

        sbSizer261 = wx.StaticBoxSizer(wx.StaticBox(sbSizer201.GetStaticBox(), wx.ID_ANY, u"装備補正"), wx.VERTICAL)

        bSizer13231 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer13351 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText6551 = wx.StaticText(sbSizer261.GetStaticBox(), wx.ID_ANY, u"武力", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6551.Wrap(-1)

        bSizer13351.Add(self.m_staticText6551, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_1_str_point_eq_text_ctrl = wx.TextCtrl(sbSizer261.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_1_str_point_eq_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer13351.Add(self.sub_1_str_point_eq_text_ctrl, 0, wx.ALL, 5)

        bSizer13231.Add(bSizer13351, 0, wx.EXPAND, 5)

        bSizer133131 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText65131 = wx.StaticText(sbSizer261.GetStaticBox(), wx.ID_ANY, u"統率", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText65131.Wrap(-1)

        bSizer133131.Add(self.m_staticText65131, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_1_def_point_eq_text_ctrl = wx.TextCtrl(sbSizer261.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_1_def_point_eq_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer133131.Add(self.sub_1_def_point_eq_text_ctrl, 0, wx.ALL, 5)

        bSizer13231.Add(bSizer133131, 0, wx.EXPAND, 5)

        bSizer133241 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText65241 = wx.StaticText(sbSizer261.GetStaticBox(), wx.ID_ANY, u"知力", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText65241.Wrap(-1)

        bSizer133241.Add(self.m_staticText65241, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_1_int_point_eq_text_ctrl = wx.TextCtrl(sbSizer261.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_1_int_point_eq_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer133241.Add(self.sub_1_int_point_eq_text_ctrl, 0, wx.ALL, 5)

        bSizer13231.Add(bSizer133241, 0, wx.EXPAND, 5)

        bSizer1332131 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText652131 = wx.StaticText(sbSizer261.GetStaticBox(), wx.ID_ANY, u"速度", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText652131.Wrap(-1)

        bSizer1332131.Add(self.m_staticText652131, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_1_spd_point_eq_text_ctrl = wx.TextCtrl(sbSizer261.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_1_spd_point_eq_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer1332131.Add(self.sub_1_spd_point_eq_text_ctrl, 0, wx.ALL, 5)

        bSizer13231.Add(bSizer1332131, 0, wx.EXPAND, 5)

        sbSizer261.Add(bSizer13231, 1, wx.EXPAND, 5)

        sbSizer201.Add(sbSizer261, 1, wx.EXPAND, 5)

        self.m_panel91 = wx.Panel(sbSizer201.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_STATIC | wx.TAB_TRAVERSAL)
        bSizer2201 = wx.BoxSizer(wx.VERTICAL)

        bSizer2211 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1341 = wx.StaticText(self.m_panel91, wx.ID_ANY, u"装備スキル設定", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1341.Wrap(-1)

        bSizer2211.Add(self.m_staticText1341, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_1_eq_skill_select_button = wx.Button(self.m_panel91, wx.ID_ANY, u"設定", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2211.Add(self.sub_1_eq_skill_select_button, 0, wx.ALL, 5)

        bSizer2201.Add(bSizer2211, 0, wx.EXPAND, 5)

        bSizer2221 = wx.BoxSizer(wx.HORIZONTAL)

        self.sub_1_eq_skill_label = wx.StaticText(self.m_panel91, wx.ID_ANY, u"明朗", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_1_eq_skill_label.Wrap(-1)

        bSizer2221.Add(self.sub_1_eq_skill_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer2201.Add(bSizer2221, 1, wx.EXPAND, 5)

        self.m_panel91.SetSizer(bSizer2201)
        self.m_panel91.Layout()
        bSizer2201.Fit(self.m_panel91)
        sbSizer201.Add(self.m_panel91, 0, wx.EXPAND | wx.ALL, 5)

        bSizer100.Add(sbSizer201, 1, wx.ALL | wx.EXPAND, 5)

        sbSizer202 = wx.StaticBoxSizer(wx.StaticBox(sbSizer9.GetStaticBox(), wx.ID_ANY, u"副将2"), wx.VERTICAL)

        bSizer1292 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1213 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText583 = wx.StaticText(sbSizer202.GetStaticBox(), wx.ID_ANY, u"ランクアップ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText583.Wrap(-1)

        bSizer1213.Add(self.m_staticText583, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        sub_2_rankup_choiceChoices = [u"0回", u"1回", u"2回", u"3回", u"4回", u"5回"]
        self.sub_2_rankup_choice = wx.Choice(sbSizer202.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sub_2_rankup_choiceChoices, 0)
        self.sub_2_rankup_choice.SetSelection(0)
        bSizer1213.Add(self.sub_2_rankup_choice, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer1292.Add(bSizer1213, 0, wx.EXPAND, 5)

        bSizer12113 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText5813 = wx.StaticText(sbSizer202.GetStaticBox(), wx.ID_ANY, u"秘蔵", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5813.Wrap(-1)

        bSizer12113.Add(self.m_staticText5813, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_2_hizo_checkbox = wx.CheckBox(sbSizer202.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12113.Add(self.sub_2_hizo_checkbox, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer1292.Add(bSizer12113, 0, wx.EXPAND, 5)

        bSizer121112 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText58112 = wx.StaticText(sbSizer202.GetStaticBox(), wx.ID_ANY, u"アニメ解放", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText58112.Wrap(-1)

        bSizer121112.Add(self.m_staticText58112, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_2_anime_checkbox = wx.CheckBox(sbSizer202.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer121112.Add(self.sub_2_anime_checkbox, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer1292.Add(bSizer121112, 1, wx.EXPAND, 5)

        sbSizer202.Add(bSizer1292, 1, wx.EXPAND, 5)

        bSizer1302 = wx.BoxSizer(wx.VERTICAL)

        bSizer1312 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText642 = wx.StaticText(sbSizer202.GetStaticBox(), wx.ID_ANY, u"残り配分ポイント：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText642.Wrap(-1)

        bSizer1312.Add(self.m_staticText642, 0, wx.ALL, 5)

        self.sub_2_remained_point_label = wx.StaticText(sbSizer202.GetStaticBox(), wx.ID_ANY, u"60", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_2_remained_point_label.Wrap(-1)

        bSizer1312.Add(self.sub_2_remained_point_label, 0, wx.ALL, 5)

        bSizer1302.Add(bSizer1312, 0, wx.EXPAND, 5)

        bSizer1322 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1334 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText654 = wx.StaticText(sbSizer202.GetStaticBox(), wx.ID_ANY, u"武力", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText654.Wrap(-1)

        bSizer1334.Add(self.m_staticText654, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_2_str_point_text_ctrl = wx.TextCtrl(sbSizer202.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_2_str_point_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer1334.Add(self.sub_2_str_point_text_ctrl, 0, wx.ALL, 5)

        bSizer1322.Add(bSizer1334, 0, wx.EXPAND, 5)

        bSizer13312 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText6512 = wx.StaticText(sbSizer202.GetStaticBox(), wx.ID_ANY, u"統率", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6512.Wrap(-1)

        bSizer13312.Add(self.m_staticText6512, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_2_def_point_text_ctrl = wx.TextCtrl(sbSizer202.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_2_def_point_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer13312.Add(self.sub_2_def_point_text_ctrl, 0, wx.ALL, 5)

        bSizer1322.Add(bSizer13312, 0, wx.EXPAND, 5)

        bSizer13323 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText6523 = wx.StaticText(sbSizer202.GetStaticBox(), wx.ID_ANY, u"知力", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6523.Wrap(-1)

        bSizer13323.Add(self.m_staticText6523, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_2_int_point_text_ctrl = wx.TextCtrl(sbSizer202.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_2_int_point_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer13323.Add(self.sub_2_int_point_text_ctrl, 0, wx.ALL, 5)

        bSizer1322.Add(bSizer13323, 0, wx.EXPAND, 5)

        bSizer133212 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText65212 = wx.StaticText(sbSizer202.GetStaticBox(), wx.ID_ANY, u"速度", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText65212.Wrap(-1)

        bSizer133212.Add(self.m_staticText65212, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_2_spd_point_text_ctrl = wx.TextCtrl(sbSizer202.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_2_spd_point_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer133212.Add(self.sub_2_spd_point_text_ctrl, 0, wx.ALL, 5)

        bSizer1322.Add(bSizer133212, 0, wx.EXPAND, 5)

        bSizer1302.Add(bSizer1322, 0, wx.EXPAND, 5)

        sbSizer202.Add(bSizer1302, 1, wx.EXPAND, 5)

        sbSizer262 = wx.StaticBoxSizer(wx.StaticBox(sbSizer202.GetStaticBox(), wx.ID_ANY, u"装備補正"), wx.VERTICAL)

        bSizer13232 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer13352 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText6552 = wx.StaticText(sbSizer262.GetStaticBox(), wx.ID_ANY, u"武力", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6552.Wrap(-1)

        bSizer13352.Add(self.m_staticText6552, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_2_str_point_eq_text_ctrl = wx.TextCtrl(sbSizer262.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_2_str_point_eq_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer13352.Add(self.sub_2_str_point_eq_text_ctrl, 0, wx.ALL, 5)

        bSizer13232.Add(bSizer13352, 0, wx.EXPAND, 5)

        bSizer133132 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText65132 = wx.StaticText(sbSizer262.GetStaticBox(), wx.ID_ANY, u"統率", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText65132.Wrap(-1)

        bSizer133132.Add(self.m_staticText65132, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_2_def_point_eq_text_ctrl = wx.TextCtrl(sbSizer262.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_2_def_point_eq_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer133132.Add(self.sub_2_def_point_eq_text_ctrl, 0, wx.ALL, 5)

        bSizer13232.Add(bSizer133132, 0, wx.EXPAND, 5)

        bSizer133242 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText65242 = wx.StaticText(sbSizer262.GetStaticBox(), wx.ID_ANY, u"知力", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText65242.Wrap(-1)

        bSizer133242.Add(self.m_staticText65242, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_2_int_point_eq_text_ctrl = wx.TextCtrl(sbSizer262.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_2_int_point_eq_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer133242.Add(self.sub_2_int_point_eq_text_ctrl, 0, wx.ALL, 5)

        bSizer13232.Add(bSizer133242, 0, wx.EXPAND, 5)

        bSizer1332132 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText652132 = wx.StaticText(sbSizer262.GetStaticBox(), wx.ID_ANY, u"速度", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText652132.Wrap(-1)

        bSizer1332132.Add(self.m_staticText652132, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_2_spd_point_eq_text_ctrl = wx.TextCtrl(sbSizer262.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_2_spd_point_eq_text_ctrl.SetMaxSize(wx.Size(30, -1))

        bSizer1332132.Add(self.sub_2_spd_point_eq_text_ctrl, 0, wx.ALL, 5)

        bSizer13232.Add(bSizer1332132, 0, wx.EXPAND, 5)

        sbSizer262.Add(bSizer13232, 1, wx.EXPAND, 5)

        sbSizer202.Add(sbSizer262, 1, wx.EXPAND, 5)

        self.m_panel92 = wx.Panel(sbSizer202.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_STATIC | wx.TAB_TRAVERSAL)
        bSizer2202 = wx.BoxSizer(wx.VERTICAL)

        bSizer2212 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1342 = wx.StaticText(self.m_panel92, wx.ID_ANY, u"装備スキル設定", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1342.Wrap(-1)

        bSizer2212.Add(self.m_staticText1342, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.sub_2_eq_skill_select_button = wx.Button(self.m_panel92, wx.ID_ANY, u"設定", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2212.Add(self.sub_2_eq_skill_select_button, 0, wx.ALL, 5)

        bSizer2202.Add(bSizer2212, 0, wx.EXPAND, 5)

        bSizer2222 = wx.BoxSizer(wx.HORIZONTAL)

        self.sub_2_eq_skill_label = wx.StaticText(self.m_panel92, wx.ID_ANY, u"明朗", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_2_eq_skill_label.Wrap(-1)

        bSizer2222.Add(self.sub_2_eq_skill_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer2202.Add(bSizer2222, 1, wx.EXPAND, 5)

        self.m_panel92.SetSizer(bSizer2202)
        self.m_panel92.Layout()
        bSizer2202.Fit(self.m_panel92)
        sbSizer202.Add(self.m_panel92, 0, wx.EXPAND | wx.ALL, 5)

        bSizer100.Add(sbSizer202, 1, wx.ALL | wx.EXPAND, 5)

        sbSizer9.Add(bSizer100, 1, 0, 5)

        self.m_panel8.SetSizer(sbSizer9)
        self.m_panel8.Layout()
        sbSizer9.Fit(self.m_panel8)
        bSizer91.Add(self.m_panel8, 0, wx.EXPAND | wx.ALL, 5)

        sbSizer32 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel7, wx.ID_ANY, u"ステータス"), wx.HORIZONTAL)

        sbSizer33 = wx.StaticBoxSizer(wx.StaticBox(sbSizer32.GetStaticBox(), wx.ID_ANY, u"主将"), wx.VERTICAL)

        sbSizer34 = wx.StaticBoxSizer(wx.StaticBox(sbSizer33.GetStaticBox(), wx.ID_ANY, u"通常"), wx.HORIZONTAL)

        self.main_normal_str_label = wx.StaticText(sbSizer34.GetStaticBox(), wx.ID_ANY, u"武力：100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_normal_str_label.Wrap(-1)

        sbSizer34.Add(self.main_normal_str_label, 0, wx.ALL, 5)

        self.main_normal_def_label = wx.StaticText(sbSizer34.GetStaticBox(), wx.ID_ANY, u"統率:100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_normal_def_label.Wrap(-1)

        sbSizer34.Add(self.main_normal_def_label, 0, wx.ALL, 5)

        self.main_normal_int_label = wx.StaticText(sbSizer34.GetStaticBox(), wx.ID_ANY, u"知力:100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_normal_int_label.Wrap(-1)

        sbSizer34.Add(self.main_normal_int_label, 0, wx.ALL, 5)

        self.main_normal_spd_label = wx.StaticText(sbSizer34.GetStaticBox(), wx.ID_ANY, u"速度:100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_normal_spd_label.Wrap(-1)

        sbSizer34.Add(self.main_normal_spd_label, 0, wx.ALL, 5)

        sbSizer33.Add(sbSizer34, 0, wx.EXPAND, 5)

        sbSizer35 = wx.StaticBoxSizer(wx.StaticBox(sbSizer33.GetStaticBox(), wx.ID_ANY, u"戦闘開始時"), wx.HORIZONTAL)

        self.main_battle_str_label = wx.StaticText(sbSizer35.GetStaticBox(), wx.ID_ANY, u"武力：100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_battle_str_label.Wrap(-1)

        sbSizer35.Add(self.main_battle_str_label, 0, wx.ALL, 5)

        self.main_battle_def_label = wx.StaticText(sbSizer35.GetStaticBox(), wx.ID_ANY, u"統率:100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_battle_def_label.Wrap(-1)

        sbSizer35.Add(self.main_battle_def_label, 0, wx.ALL, 5)

        self.main_battle_int_label = wx.StaticText(sbSizer35.GetStaticBox(), wx.ID_ANY, u"知力:100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_battle_int_label.Wrap(-1)

        sbSizer35.Add(self.main_battle_int_label, 0, wx.ALL, 5)

        self.main_battle_spd_label = wx.StaticText(sbSizer35.GetStaticBox(), wx.ID_ANY, u"速度:100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_battle_spd_label.Wrap(-1)

        sbSizer35.Add(self.main_battle_spd_label, 0, wx.ALL, 5)

        sbSizer33.Add(sbSizer35, 0, wx.EXPAND, 5)

        sbSizer32.Add(sbSizer33, 1, wx.EXPAND, 5)

        sbSizer331 = wx.StaticBoxSizer(wx.StaticBox(sbSizer32.GetStaticBox(), wx.ID_ANY, u"副将1"), wx.VERTICAL)

        sbSizer341 = wx.StaticBoxSizer(wx.StaticBox(sbSizer331.GetStaticBox(), wx.ID_ANY, u"通常"), wx.HORIZONTAL)

        self.sub_1_normal_str_label = wx.StaticText(sbSizer341.GetStaticBox(), wx.ID_ANY, u"武力：100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_1_normal_str_label.Wrap(-1)

        sbSizer341.Add(self.sub_1_normal_str_label, 0, wx.ALL, 5)

        self.sub_1_normal_def_label = wx.StaticText(sbSizer341.GetStaticBox(), wx.ID_ANY, u"統率:100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_1_normal_def_label.Wrap(-1)

        sbSizer341.Add(self.sub_1_normal_def_label, 0, wx.ALL, 5)

        self.sub_1_normal_int_label = wx.StaticText(sbSizer341.GetStaticBox(), wx.ID_ANY, u"知力:100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_1_normal_int_label.Wrap(-1)

        sbSizer341.Add(self.sub_1_normal_int_label, 0, wx.ALL, 5)

        self.sub_1_normal_spd_label = wx.StaticText(sbSizer341.GetStaticBox(), wx.ID_ANY, u"速度:100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_1_normal_spd_label.Wrap(-1)

        sbSizer341.Add(self.sub_1_normal_spd_label, 0, wx.ALL, 5)

        sbSizer331.Add(sbSizer341, 0, wx.EXPAND, 5)

        sbSizer351 = wx.StaticBoxSizer(wx.StaticBox(sbSizer331.GetStaticBox(), wx.ID_ANY, u"戦闘開始時"), wx.HORIZONTAL)

        self.sub_1_battle_str_label = wx.StaticText(sbSizer351.GetStaticBox(), wx.ID_ANY, u"武力：100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_1_battle_str_label.Wrap(-1)

        sbSizer351.Add(self.sub_1_battle_str_label, 0, wx.ALL, 5)

        self.sub_1_battle_def_label = wx.StaticText(sbSizer351.GetStaticBox(), wx.ID_ANY, u"統率:100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_1_battle_def_label.Wrap(-1)

        sbSizer351.Add(self.sub_1_battle_def_label, 0, wx.ALL, 5)

        self.sub_1_battle_int_label = wx.StaticText(sbSizer351.GetStaticBox(), wx.ID_ANY, u"知力:100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_1_battle_int_label.Wrap(-1)

        sbSizer351.Add(self.sub_1_battle_int_label, 0, wx.ALL, 5)

        self.sub_1_battle_spd_label = wx.StaticText(sbSizer351.GetStaticBox(), wx.ID_ANY, u"速度:100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_1_battle_spd_label.Wrap(-1)

        sbSizer351.Add(self.sub_1_battle_spd_label, 0, wx.ALL, 5)

        sbSizer331.Add(sbSizer351, 0, wx.EXPAND, 5)

        sbSizer32.Add(sbSizer331, 1, wx.EXPAND, 5)

        sbSizer332 = wx.StaticBoxSizer(wx.StaticBox(sbSizer32.GetStaticBox(), wx.ID_ANY, u"副将2"), wx.VERTICAL)

        sbSizer342 = wx.StaticBoxSizer(wx.StaticBox(sbSizer332.GetStaticBox(), wx.ID_ANY, u"通常"), wx.HORIZONTAL)

        self.sub_2_normal_str_label = wx.StaticText(sbSizer342.GetStaticBox(), wx.ID_ANY, u"武力：100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_2_normal_str_label.Wrap(-1)

        sbSizer342.Add(self.sub_2_normal_str_label, 0, wx.ALL, 5)

        self.sub_2_normal_def_label = wx.StaticText(sbSizer342.GetStaticBox(), wx.ID_ANY, u"統率:100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_2_normal_def_label.Wrap(-1)

        sbSizer342.Add(self.sub_2_normal_def_label, 0, wx.ALL, 5)

        self.sub_2_normal_int_label = wx.StaticText(sbSizer342.GetStaticBox(), wx.ID_ANY, u"知力:100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_2_normal_int_label.Wrap(-1)

        sbSizer342.Add(self.sub_2_normal_int_label, 0, wx.ALL, 5)

        self.sub_2_normal_spd_label = wx.StaticText(sbSizer342.GetStaticBox(), wx.ID_ANY, u"速度:100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_2_normal_spd_label.Wrap(-1)

        sbSizer342.Add(self.sub_2_normal_spd_label, 0, wx.ALL, 5)

        sbSizer332.Add(sbSizer342, 0, wx.EXPAND, 5)

        sbSizer352 = wx.StaticBoxSizer(wx.StaticBox(sbSizer332.GetStaticBox(), wx.ID_ANY, u"戦闘開始時"), wx.HORIZONTAL)

        self.sub_2_battle_str_label = wx.StaticText(sbSizer352.GetStaticBox(), wx.ID_ANY, u"武力：100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_2_battle_str_label.Wrap(-1)

        sbSizer352.Add(self.sub_2_battle_str_label, 0, wx.ALL, 5)

        self.sub_2_battle_def_label = wx.StaticText(sbSizer352.GetStaticBox(), wx.ID_ANY, u"統率:100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_2_battle_def_label.Wrap(-1)

        sbSizer352.Add(self.sub_2_battle_def_label, 0, wx.ALL, 5)

        self.sub_2_battle_int_label = wx.StaticText(sbSizer352.GetStaticBox(), wx.ID_ANY, u"知力:100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_2_battle_int_label.Wrap(-1)

        sbSizer352.Add(self.sub_2_battle_int_label, 0, wx.ALL, 5)

        self.sub_2_battle_spd_label = wx.StaticText(sbSizer352.GetStaticBox(), wx.ID_ANY, u"速度:100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sub_2_battle_spd_label.Wrap(-1)

        sbSizer352.Add(self.sub_2_battle_spd_label, 0, wx.ALL, 5)

        sbSizer332.Add(sbSizer352, 0, wx.EXPAND, 5)

        sbSizer32.Add(sbSizer332, 1, wx.EXPAND, 5)

        bSizer91.Add(sbSizer32, 0, wx.EXPAND, 5)

        self.m_panel7.SetSizer(bSizer91)
        self.m_panel7.Layout()
        bSizer91.Fit(self.m_panel7)
        bSizer89.Add(self.m_panel7, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel6.SetSizer(bSizer89)
        self.m_panel6.Layout()
        bSizer89.Fit(self.m_panel6)
        bSizer5.Add(self.m_panel6, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer5)
        self.Layout()

        self.Centre(wx.BOTH)

        self.initialize_parameter()

        return
    
    def update_kind(self, event):
        choice = event.GetEventObject()
        n = choice.GetSelection()
        HenseiDataManager().update_kind(n, StatusManager().selected_hensei)
        
        hensei_data = self.get_selected_hensei_data()
        self.update_parameter(hensei_data, 0)
        self.update_parameter(hensei_data, 1)
        self.update_parameter(hensei_data, 2)
        return

    def on_select_heiho_1_choice(self, event):
        choice = event.GetEventObject()
        n = choice.GetSelection()
        selected_heiho_id = choice.GetClientData(n)
        hensei_data = self.get_selected_hensei_data()
        hensei_id = StatusManager().selected_hensei
        if event.GetId() == ID_SELECT_MAIN_HEIHO_1:
            org_heiho_id = hensei_data["main_unit"]["heihou_1"]
            unit_id = 0
        elif event.GetId() == ID_SELECT_SUB_1_HEIHO_1:
            org_heiho_id = hensei_data["sub_1_unit"]["heihou_1"]
            unit_id = 1
        elif event.GetId() == ID_SELECT_SUB_2_HEIHO_1:
            org_heiho_id = hensei_data["sub_2_unit"]["heihou_1"]
            unit_id = 2
        else:
            raise(Exception("Heiho_1 choice Error"))
        
        if selected_heiho_id == org_heiho_id:
            return

        HenseiDataManager().set_heiho(selected_heiho_id, unit_id, 1, hensei_id)

        return

    def on_select_heiho_2_3_choice(self, event):
        choice = event.GetEventObject()
        n = choice.GetSelection()
        selected_heiho_id = choice.GetClientData(n)
        hensei_data = self.get_selected_hensei_data()
        hensei_id = StatusManager().selected_hensei
        index = None
        if event.GetId() == ID_SELECT_MAIN_HEIHO_2:
            org_heiho_id = hensei_data["main_unit"]["heihou_2"]
            unit_id = 0
            index = 2
        elif event.GetId() == ID_SELECT_MAIN_HEIHO_3:
            org_heiho_id = hensei_data["main_unit"]["heihou_3"]
            unit_id = 0
            index = 3
        elif event.GetId() == ID_SELECT_SUB_1_HEIHO_2:
            org_heiho_id = hensei_data["sub_1_unit"]["heihou_2"]
            unit_id = 1
            index = 2
        elif event.GetId() == ID_SELECT_SUB_1_HEIHO_3:
            org_heiho_id = hensei_data["sub_1_unit"]["heihou_3"]
            unit_id = 1
            index = 3
        elif event.GetId() == ID_SELECT_SUB_2_HEIHO_2:
            org_heiho_id = hensei_data["sub_2_unit"]["heihou_2"]
            unit_id = 2
            index = 2
        elif event.GetId() == ID_SELECT_SUB_2_HEIHO_3:
            org_heiho_id = hensei_data["sub_2_unit"]["heihou_3"]
            unit_id = 2
            index = 3
        else:
            raise(Exception("Heiho_2_3 choice Error"))

        if selected_heiho_id == org_heiho_id:
            return

        HenseiDataManager().set_heiho(selected_heiho_id, unit_id, index, hensei_id)
        self.update_heihou_choice(selected_heiho_id, unit_id, index)
        return

    def on_select_main_heihosyo_choice(self, event):
        hensei_data = self.get_selected_hensei_data()
        busyo_data = StaticDataManager().get_busyo_by_id(hensei_data["main_unit"]["busyo"])

        selected_heihousyo = event.GetEventObject().GetSelection() + 1
        if selected_heihousyo + 1 == hensei_data["main_unit"]["heihousyo"]:
            return

        heihou_tuple = self.initialize_heihou(selected_heihousyo, busyo_data)
        StatusManager().main_heiho_2_3_tuple_list = heihou_tuple[1]

        self.main_heihou1_choice.Clear()
        self.main_heihou2_choice.Clear()
        self.main_heihou3_choice.Clear()

        for item in heihou_tuple[0]:
            self.main_heihou1_choice.Append(item[0], item[1])

        for item in heihou_tuple[1]:
            self.main_heihou2_choice.Append(item[0], item[1])
            self.main_heihou3_choice.Append(item[0], item[1])

        self.main_heihou1_choice.SetSelection(0)
        self.main_heihou2_choice.SetSelection(0)
        self.main_heihou3_choice.SetSelection(0)
        
        HenseiDataManager().set_heiho(selected_heihousyo, 0, 0, hensei_data["hensei"]["hensei_id"])
        HenseiDataManager().set_heiho(-1, 0, 1, hensei_data["hensei"]["hensei_id"])
        HenseiDataManager().set_heiho(-1, 0, 2, hensei_data["hensei"]["hensei_id"])
        HenseiDataManager().set_heiho(-1, 0, 3, hensei_data["hensei"]["hensei_id"])

        return

    def on_select_sub_1_heihosyo_choice(self, event):
        hensei_data = self.get_selected_hensei_data()
        busyo_data = StaticDataManager().get_busyo_by_id(hensei_data["sub_1_unit"]["busyo"])

        selected_heihousyo = event.GetEventObject().GetSelection() + 1

        if selected_heihousyo + 1 == hensei_data["sub_1_unit"]["heihousyo"]:
            return

        heihou_tuple = self.initialize_heihou(selected_heihousyo, busyo_data)
        StatusManager().sub_1_heiho_2_3_tuple_list = heihou_tuple[1]

        self.sub_1_heihou1_choice.Clear()
        self.sub_1_heihou2_choice.Clear()
        self.sub_1_heihou3_choice.Clear()

        for item in heihou_tuple[0]:
            self.sub_1_heihou1_choice.Append(item[0], item[1])

        for item in heihou_tuple[1]:
            self.sub_1_heihou2_choice.Append(item[0], item[1])
            self.sub_1_heihou3_choice.Append(item[0], item[1])

        self.sub_1_heihou1_choice.SetSelection(0)
        self.sub_1_heihou2_choice.SetSelection(0)
        self.sub_1_heihou3_choice.SetSelection(0)

        HenseiDataManager().set_heiho(selected_heihousyo, 1, 0, hensei_data["hensei"]["hensei_id"])
        HenseiDataManager().set_heiho(-1, 1, 1, hensei_data["hensei"]["hensei_id"])
        HenseiDataManager().set_heiho(-1, 1, 2, hensei_data["hensei"]["hensei_id"])
        HenseiDataManager().set_heiho(-1, 1, 3, hensei_data["hensei"]["hensei_id"])
        return

    def on_select_sub_2_heihosyo_choice(self, event):
        hensei_data = self.get_selected_hensei_data()
        busyo_data = StaticDataManager().get_busyo_by_id(hensei_data["sub_2_unit"]["busyo"])
        
        selected_heihousyo = event.GetEventObject().GetSelection() + 1
        
        heihou_tuple = self.initialize_heihou(selected_heihousyo, busyo_data)
        StatusManager().sub_2_heiho_2_3_tuple_list = heihou_tuple[1]
        
        if selected_heihousyo + 1 == hensei_data["sub_2_unit"]["heihousyo"]:
            return
        
        self.sub_2_heihou1_choice.Clear()
        self.sub_2_heihou2_choice.Clear()
        self.sub_2_heihou3_choice.Clear()
        
        for item in heihou_tuple[0]:
            self.sub_2_heihou1_choice.Append(item[0], item[1])
            
        for item in heihou_tuple[1]:
            self.sub_2_heihou2_choice.Append(item[0], item[1])
            self.sub_2_heihou3_choice.Append(item[0], item[1])

        self.sub_2_heihou1_choice.SetSelection(0)
        self.sub_2_heihou2_choice.SetSelection(0)
        self.sub_2_heihou3_choice.SetSelection(0)
        
        HenseiDataManager().set_heiho(selected_heihousyo, 2, 0, hensei_data["hensei"]["hensei_id"])
        HenseiDataManager().set_heiho(-1, 2, 1, hensei_data["hensei"]["hensei_id"])
        HenseiDataManager().set_heiho(-1, 2, 2, hensei_data["hensei"]["hensei_id"])
        HenseiDataManager().set_heiho(-1, 2, 3, hensei_data["hensei"]["hensei_id"])
        return
    
    def update_heihou_choice(self, heiho_id, unit_id, index):
        hensei_data = HenseiDataManager.get_hensei_data(StatusManager().selected_hensei)
        if unit_id == 0:
            if index == 2:
                another_heiho_id = hensei_data["main_unit"]["heihou_3"]
                heiho_name_list = StaticDataManager.get_heiho_name_by_id_list([heiho_id, another_heiho_id])
                self.main_heihou3_choice.Clear()
                heihou_tuple = StatusManager().main_heiho_2_3_tuple_list
                for item in heihou_tuple:
                    self.main_heihou3_choice.Append(item[0], item[1])
                if heiho_id != -1:
                    self.main_heihou3_choice.Delete(self.main_heihou3_choice.FindString(heiho_name_list[0]))
                if another_heiho_id != -1:
                    self.main_heihou3_choice.SetSelection(self.main_heihou3_choice.FindString(heiho_name_list[1]))
                else:
                    self.main_heihou3_choice.SetSelection(0)
            else:
                another_heiho_id = hensei_data["main_unit"]["heihou_2"]
                heiho_name_list = StaticDataManager.get_heiho_name_by_id_list([heiho_id, another_heiho_id])
                self.main_heihou2_choice.Clear()
                heihou_tuple = StatusManager().main_heiho_2_3_tuple_list
                for item in heihou_tuple:
                    self.main_heihou2_choice.Append(item[0], item[1])
                if heiho_id != -1:
                    self.main_heihou2_choice.Delete(self.main_heihou2_choice.FindString(heiho_name_list[0]))
                if another_heiho_id != -1:
                    self.main_heihou2_choice.SetSelection(self.main_heihou2_choice.FindString(heiho_name_list[1]))
                else:
                    self.main_heihou2_choice.SetSelection(0)
        if unit_id == 1:
            if index == 2:
                another_heiho_id = hensei_data["sub_1_unit"]["heihou_3"]
                heiho_name_list = StaticDataManager.get_heiho_name_by_id_list([heiho_id, another_heiho_id])
                self.sub_1_heihou3_choice.Clear()
                heihou_tuple = StatusManager().sub_1_heiho_2_3_tuple_list
                for item in heihou_tuple:
                    self.sub_1_heihou3_choice.Append(item[0], item[1])
                if heiho_id != -1:
                    self.sub_1_heihou3_choice.Delete(self.sub_1_heihou3_choice.FindString(heiho_name_list[0]))
                if another_heiho_id != -1:
                    self.sub_1_heihou3_choice.SetSelection(self.sub_1_heihou3_choice.FindString(heiho_name_list[1]))
                else:
                    self.sub_1_heihou3_choice.SetSelection(0)
            else:
                another_heiho_id = hensei_data["sub_1_unit"]["heihou_2"]
                heiho_name_list = StaticDataManager.get_heiho_name_by_id_list([heiho_id, another_heiho_id])
                self.sub_1_heihou2_choice.Clear()
                heihou_tuple = StatusManager().sub_1_heiho_2_3_tuple_list
                for item in heihou_tuple:
                    self.sub_1_heihou2_choice.Append(item[0], item[1])
                if heiho_id != -1:
                    self.sub_1_heihou2_choice.Delete(self.sub_1_heihou2_choice.FindString(heiho_name_list[0]))
                if another_heiho_id != -1:
                    self.sub_1_heihou2_choice.SetSelection(self.sub_1_heihou2_choice.FindString(heiho_name_list[1]))
                else:
                    self.sub_1_heihou2_choice.SetSelection(0)
        if unit_id == 2:
            if index == 2:
                another_heiho_id = hensei_data["sub_2_unit"]["heihou_3"]
                heiho_name_list = StaticDataManager.get_heiho_name_by_id_list([heiho_id, another_heiho_id])
                self.sub_2_heihou3_choice.Clear()
                heihou_tuple = StatusManager().sub_2_heiho_2_3_tuple_list
                for item in heihou_tuple:
                    self.sub_2_heihou3_choice.Append(item[0], item[1])
                print(self.sub_2_heihou3_choice.GetStrings())
                print(heiho_id)
                print(heiho_name_list[0])
                if heiho_id != -1:
                    
                    print(self.sub_2_heihou3_choice.FindString(heiho_name_list[0]))
                    self.sub_2_heihou3_choice.Delete(self.sub_2_heihou3_choice.FindString(heiho_name_list[0]))
                if another_heiho_id != -1:
                    self.sub_2_heihou3_choice.SetSelection(self.sub_2_heihou3_choice.FindString(heiho_name_list[1]))
                else:
                    self.sub_2_heihou3_choice.SetSelection(0)
            else:
                another_heiho_id = hensei_data["sub_2_unit"]["heihou_2"]
                heiho_name_list = StaticDataManager.get_heiho_name_by_id_list([heiho_id, another_heiho_id])
                self.sub_2_heihou2_choice.Clear()
                heihou_tuple = StatusManager().sub_2_heiho_2_3_tuple_list
                for item in heihou_tuple:
                    self.sub_2_heihou2_choice.Append(item[0], item[1])
                if heiho_id != -1:
                    self.sub_2_heihou2_choice.Delete(self.sub_2_heihou2_choice.FindString(heiho_name_list[0]))
                if another_heiho_id != -1:
                    self.sub_2_heihou2_choice.SetSelection(self.sub_2_heihou2_choice.FindString(heiho_name_list[1]))
                else:
                    self.sub_2_heihou2_choice.SetSelection(0)

        return

    def initialize_heihou(self, heihousyo, busyo_data):
        condition_1 = {"heiho_" + str(heihousyo) + "_2_1", "heiho_" + str(heihousyo) + "_2_2", "heiho_" + str(heihousyo) + "_2_3"}
        condition_2 = {"heiho_" + str(heihousyo) + "_3_1",
                       "heiho_" + str(heihousyo) + "_3_2",
                       "heiho_" + str(heihousyo) + "_3_3",
                       "heiho_" + str(heihousyo) + "_3_4",
                       "heiho_" + str(heihousyo) + "_3_5"}
        heiho_1_id = []
        heiho_2_id = []
        for key, value in busyo_data.items():
            if key in condition_1:
                heiho_1_id.append(value)
            if key in condition_2:
                heiho_2_id.append(value)

        heiho_1_name = StaticDataManager().get_heiho_name_by_id_list(heiho_1_id)
        heiho_2_name = StaticDataManager().get_heiho_name_by_id_list(heiho_2_id)

        heiho_1 = list(zip(heiho_1_name, heiho_1_id))
        heiho_2 = list(zip(heiho_2_name, heiho_2_id))
        heiho_2.insert(0, ("", -1))

        return (heiho_1, heiho_2)

    def update_common_parameter(self, hensei_data):
        self.select_kind_choice.SetSelection(hensei_data["hensei"]["kind"])
        self.level_text_ctrl.SetValue(str(hensei_data["hensei"]["level"]))
        self.select_heisen_level_choice.SetSelection(hensei_data["hensei"]["heisen_level"])
        self.select_kyoryoku_level_choice.SetSelection(hensei_data["hensei"]["kyoryoku_level"])
        return

    def update_parameter(self, hensei_data, unit_id):
        if unit_id == 0:
            self.update_main_parameter(hensei_data)
        elif unit_id == 1:
            self.update_sub_1_parameter(hensei_data)
        elif unit_id == 2:
            self.update_sub_2_parameter(hensei_data)
        else:
            return

    def update_main_parameter(self, hensei_data):
        if hensei_data["hensei"]["main_unit"] is None:
            self.clear_main_unit()
            return

        busyo_data = StaticDataManager().get_busyo_by_id(hensei_data["main_unit"]["busyo"])

        self.main_unit_drop_button.Enable()
        self.main_unit_select_button.SetLabel(busyo_data["name"])
        self.main_country_label.SetLabel(busyo_data["country"])
        kind = hensei_data["hensei"]["kind"]
        if kind == 0:
            self.main_suitable_label.SetLabel(busyo_data["horse"])
        elif kind == 1:
            self.main_suitable_label.SetLabel(busyo_data["shield"])
        elif kind == 2:
            self.main_suitable_label.SetLabel(busyo_data["bow"])
        elif kind == 3:
            self.main_suitable_label.SetLabel(busyo_data["rance"])
        elif kind == 4:
            self.main_suitable_label.SetLabel(busyo_data["weapon"])
        elif kind == 5:
            self.main_suitable_label.SetLabel(busyo_data["water"])
        else:
            pass

        unique_senpo = StaticDataManager().get_senpo_by_id(busyo_data["org_skill"])
        self.main_unique_senpo_label.SetLabel(unique_senpo["name"])

        self.main_senpo2_select_button.Enable()
        if hensei_data["main_unit"]["skill_2"] == -1:
            self.main_senpo2_select_button.SetLabel(LABEL_CHOICE)
            self.main_senpo2_select_button.SetForegroundColour(wx.BLACK)
        else:
            senpo_2 = StaticDataManager().get_senpo_by_id(hensei_data["main_unit"]["skill_2"])
            suitable_list = StaticDataManager().get_suitable_by_id(hensei_data["main_unit"]["skill_2"])
            
            if kind != 5 and suitable_list[kind] is not True:
                self.main_senpo2_select_button.SetForegroundColour(wx.RED)
            else:
                self.main_senpo2_select_button.SetForegroundColour(wx.BLACK)
            self.main_senpo2_select_button.SetLabel(senpo_2["name"])

        self.main_senpo3_select_button.Enable()
        if hensei_data["main_unit"]["skill_3"] == -1:
            self.main_senpo3_select_button.SetLabel(LABEL_CHOICE)
            self.main_senpo3_select_button.SetForegroundColour(wx.BLACK)
        else:
            senpo_3 = StaticDataManager().get_senpo_by_id(hensei_data["main_unit"]["skill_3"])
            suitable_list = StaticDataManager().get_suitable_by_id(hensei_data["main_unit"]["skill_3"])

            if kind != 5 and suitable_list[kind] is not True:
                self.main_senpo3_select_button.SetForegroundColour(wx.RED)
            else:
                self.main_senpo3_select_button.SetForegroundColour(wx.BLACK)
            self.main_senpo3_select_button.SetLabel(senpo_3["name"])

        self.main_heihousyo_choice.Clear()
        self.main_heihou1_choice.Clear()
        self.main_heihou2_choice.Clear()
        self.main_heihou3_choice.Clear()

        self.main_heihousyo_choice.AppendItems(["作戦", "虚実", "軍形", "九変"])

        main_heihousyo = hensei_data["main_unit"]["heihousyo"]
        
        self.main_heihousyo_choice.SetSelection(main_heihousyo - 1)
        heihou_tuple = self.initialize_heihou(main_heihousyo, busyo_data)
        StatusManager().main_heiho_2_3_tuple_list = heihou_tuple[1]
        
        for item in heihou_tuple[0]:
            self.main_heihou1_choice.Append(item[0], item[1])
            
        for item in heihou_tuple[1]:
            self.main_heihou2_choice.Append(item[0], item[1])
            self.main_heihou3_choice.Append(item[0], item[1])

        if hensei_data["main_unit"]["heihou_1"] == -1:
            self.main_heihou1_choice.SetSelection(0)
        else:
            self.main_heihou1_choice.SetSelection(self.main_heihou1_choice.FindString(StaticDataManager.get_heiho_name_by_id_list([hensei_data["main_unit"]["heihou_1"]])[0]))

        self.update_heihou_choice(hensei_data["main_unit"]["heihou_2"], 0, 2)
        self.update_heihou_choice(hensei_data["main_unit"]["heihou_3"], 0, 3)
        
        self.main_rankup_choice.SetSelection(hensei_data["main_unit"]["rankup"])
        if hensei_data["main_unit"]["hizo"] == 0:
            self.main_hizo_checkbox.SetValue(False)
        else:
            self.main_hizo_checkbox.SetValue(True)
        if hensei_data["main_unit"]["anime"] == 0:
            self.main_anime_checkbox.SetValue(False)
        else:
            self.main_anime_checkbox.SetValue(True)
        # TODO 残ポイント実装
        self.main_remained_point_label.SetLabel(LABEL_ZERO)
        self.main_str_point_text_ctrl.SetValue(str(hensei_data["main_unit"]["buf_str"]))
        self.main_def_point_text_ctrl.SetValue(str(hensei_data["main_unit"]["buf_def"]))
        self.main_int_point_text_ctrl.SetValue(str(hensei_data["main_unit"]["buf_int"]))
        self.main_spd_point_text_ctrl.SetValue(str(hensei_data["main_unit"]["buf_spd"]))
        self.main_str_point_eq_text_ctrl.SetValue(str(hensei_data["main_unit"]["buf_eq_str"]))
        self.main_def_point_eq_text_ctrl.SetValue(str(hensei_data["main_unit"]["buf_eq_def"]))
        self.main_int_point_eq_text_ctrl.SetValue(str(hensei_data["main_unit"]["buf_eq_int"]))
        self.main_spd_point_eq_text_ctrl.SetValue(str(hensei_data["main_unit"]["buf_eq_spd"]))
        # TODO 装備スキルリスト実装
        self.main_eq_skill_label.SetLabel(LABEL_NOTHING)
        # TODO パラメータ表示実装
        self.main_normal_str_label.SetLabel("武力:" + LABEL_NOTHING)
        self.main_normal_def_label.SetLabel("統率:" + LABEL_NOTHING)
        self.main_normal_int_label.SetLabel("知力:" + LABEL_NOTHING)
        self.main_normal_spd_label.SetLabel("速度:" + LABEL_NOTHING)
        self.main_battle_str_label.SetLabel("武力:" + LABEL_NOTHING)
        self.main_battle_def_label.SetLabel("統率:" + LABEL_NOTHING)
        self.main_battle_int_label.SetLabel("知力:" + LABEL_NOTHING)
        self.main_battle_spd_label.SetLabel("速度:" + LABEL_NOTHING)
        
        self.main_heihousyo_choice.Enable()
        self.main_heihou1_choice.Enable()
        self.main_heihou2_choice.Enable()
        self.main_heihou3_choice.Enable()
        self.main_rankup_choice.Enable()
        self.main_hizo_checkbox.Enable()
        self.main_anime_checkbox.Enable()
        self.main_eq_skill_select_button.Enable()
        return

    def update_sub_1_parameter(self, hensei_data):
        if hensei_data["hensei"]["sub_1_unit"] is None:
            self.clear_sub_1_unit()
            return

        busyo_data = StaticDataManager().get_busyo_by_id(hensei_data["sub_1_unit"]["busyo"])

        self.sub_1_unit_drop_button.Enable()
        self.sub_1_unit_select_button.SetLabel(busyo_data["name"])
        self.sub_1_country_label.SetLabel(busyo_data["country"])
        kind = hensei_data["hensei"]["kind"]
        if kind == 0:
            self.sub_1_suitable_label.SetLabel(busyo_data["horse"])
        elif kind == 1:
            self.sub_1_suitable_label.SetLabel(busyo_data["shield"])
        elif kind == 2:
            self.sub_1_suitable_label.SetLabel(busyo_data["bow"])
        elif kind == 3:
            self.sub_1_suitable_label.SetLabel(busyo_data["rance"])
        elif kind == 4:
            self.sub_1_suitable_label.SetLabel(busyo_data["weapon"])
        elif kind == 5:
            self.sub_1_suitable_label.SetLabel(busyo_data["water"])

        unique_senpo = StaticDataManager().get_senpo_by_id(busyo_data["org_skill"])
        self.sub_1_unique_senpo_label.SetLabel(unique_senpo["name"])

        self.sub_1_senpo2_select_button.Enable()
        if hensei_data["sub_1_unit"]["skill_2"] == -1:
            self.sub_1_senpo2_select_button.SetLabel(LABEL_CHOICE)
            self.sub_1_senpo2_select_button.SetForegroundColour(wx.BLACK)
        else:
            senpo_2 = StaticDataManager().get_senpo_by_id(hensei_data["sub_1_unit"]["skill_2"])
            suitable_list = StaticDataManager().get_suitable_by_id(hensei_data["sub_1_unit"]["skill_2"])

            if kind != 5 and suitable_list[kind] is not True:
                self.sub_1_senpo2_select_button.SetForegroundColour(wx.RED)
            else:
                self.sub_1_senpo2_select_button.SetForegroundColour(wx.BLACK)
            self.sub_1_senpo2_select_button.SetLabel(senpo_2["name"])

        self.sub_1_senpo3_select_button.Enable()
        if hensei_data["sub_1_unit"]["skill_3"] == -1:
            self.sub_1_senpo3_select_button.SetLabel(LABEL_CHOICE)
            self.sub_1_senpo3_select_button.SetForegroundColour(wx.BLACK)
        else:
            senpo_3 = StaticDataManager().get_senpo_by_id(hensei_data["sub_1_unit"]["skill_3"])
            suitable_list = StaticDataManager().get_suitable_by_id(hensei_data["sub_1_unit"]["skill_3"])

            if kind != 5 and suitable_list[kind] is not True:
                self.sub_1_senpo3_select_button.SetForegroundColour(wx.RED)
            else:
                self.sub_1_senpo3_select_button.SetForegroundColour(wx.BLACK)
            self.sub_1_senpo3_select_button.SetLabel(senpo_3["name"])
        
        self.sub_1_heihousyo_choice.Clear()
        self.sub_1_heihou1_choice.Clear()
        self.sub_1_heihou2_choice.Clear()
        self.sub_1_heihou3_choice.Clear()

        self.sub_1_heihousyo_choice.AppendItems(["作戦", "虚実", "軍形", "九変"])
        sub_1_heihousyo = hensei_data["sub_1_unit"]["heihousyo"]
        
        self.sub_1_heihousyo_choice.SetSelection(sub_1_heihousyo - 1)
        heihou_tuple = self.initialize_heihou(sub_1_heihousyo, busyo_data)
        StatusManager().sub_1_heiho_2_3_tuple_list = heihou_tuple[1]
        
        for item in heihou_tuple[0]:
            self.sub_1_heihou1_choice.Append(item[0], item[1])
            
        for item in heihou_tuple[1]:
            self.sub_1_heihou2_choice.Append(item[0], item[1])
            self.sub_1_heihou3_choice.Append(item[0], item[1])
        
        if hensei_data["sub_1_unit"]["heihou_1"] == -1:
            self.sub_1_heihou1_choice.SetSelection(0)
        else:
            self.sub_1_heihou1_choice.SetSelection(self.sub_1_heihou1_choice.FindString(StaticDataManager.get_heiho_name_by_id_list([hensei_data["sub_1_unit"]["heihou_1"]])[0]))
        self.update_heihou_choice(hensei_data["sub_1_unit"]["heihou_2"], 1, 2)
        self.update_heihou_choice(hensei_data["sub_1_unit"]["heihou_3"], 1, 3)

        self.sub_1_rankup_choice.SetSelection(hensei_data["sub_1_unit"]["rankup"])
        if hensei_data["sub_1_unit"]["hizo"] == 0:
            self.sub_1_hizo_checkbox.SetValue(False)
        else:
            self.sub_1_hizo_checkbox.SetValue(True)
        if hensei_data["sub_1_unit"]["anime"] == 0:
            self.sub_1_anime_checkbox.SetValue(False)
        else:
            self.sub_1_anime_checkbox.SetValue(True)
        # TODO 残ポイント実装
        self.sub_1_remained_point_label.SetLabel(LABEL_ZERO)
        self.sub_1_str_point_text_ctrl.SetValue(str(hensei_data["sub_1_unit"]["buf_str"]))
        self.sub_1_def_point_text_ctrl.SetValue(str(hensei_data["sub_1_unit"]["buf_def"]))
        self.sub_1_int_point_text_ctrl.SetValue(str(hensei_data["sub_1_unit"]["buf_int"]))
        self.sub_1_spd_point_text_ctrl.SetValue(str(hensei_data["sub_1_unit"]["buf_spd"]))
        self.sub_1_str_point_eq_text_ctrl.SetValue(str(hensei_data["sub_1_unit"]["buf_eq_str"]))
        self.sub_1_def_point_eq_text_ctrl.SetValue(str(hensei_data["sub_1_unit"]["buf_eq_def"]))
        self.sub_1_int_point_eq_text_ctrl.SetValue(str(hensei_data["sub_1_unit"]["buf_eq_int"]))
        self.sub_1_spd_point_eq_text_ctrl.SetValue(str(hensei_data["sub_1_unit"]["buf_eq_spd"]))
        # TODO 装備スキルリスト実装
        self.sub_1_eq_skill_label.SetLabel(LABEL_NOTHING)
        # TODO パラメータ表示実装
        self.sub_1_normal_str_label.SetLabel("武力:" + LABEL_NOTHING)
        self.sub_1_normal_def_label.SetLabel("統率:" + LABEL_NOTHING)
        self.sub_1_normal_int_label.SetLabel("知力:" + LABEL_NOTHING)
        self.sub_1_normal_spd_label.SetLabel("速度:" + LABEL_NOTHING)
        self.sub_1_battle_str_label.SetLabel("武力:" + LABEL_NOTHING)
        self.sub_1_battle_def_label.SetLabel("統率:" + LABEL_NOTHING)
        self.sub_1_battle_int_label.SetLabel("知力:" + LABEL_NOTHING)
        self.sub_1_battle_spd_label.SetLabel("速度:" + LABEL_NOTHING)
        
        self.sub_1_heihousyo_choice.Enable()
        self.sub_1_heihou1_choice.Enable()
        self.sub_1_heihou2_choice.Enable()
        self.sub_1_heihou3_choice.Enable()
        self.sub_1_rankup_choice.Enable()
        self.sub_1_hizo_checkbox.Enable()
        self.sub_1_anime_checkbox.Enable()
        self.sub_1_eq_skill_select_button.Enable()
        return

    def update_sub_2_parameter(self, hensei_data):
        if hensei_data["hensei"]["sub_2_unit"] is None:
            self.clear_sub_2_unit()
            return
        
        busyo_data = StaticDataManager().get_busyo_by_id(hensei_data["sub_2_unit"]["busyo"])

        self.sub_2_unit_drop_button.Enable()
        self.sub_2_unit_select_button.SetLabel(busyo_data["name"])
        self.sub_2_country_label.SetLabel(busyo_data["country"])
        kind = hensei_data["hensei"]["kind"]
        if kind == 0:
            self.sub_2_suitable_label.SetLabel(busyo_data["horse"])
        elif kind == 1:
            self.sub_2_suitable_label.SetLabel(busyo_data["shield"])
        elif kind == 2:
            self.sub_2_suitable_label.SetLabel(busyo_data["bow"])
        elif kind == 3:
            self.sub_2_suitable_label.SetLabel(busyo_data["rance"])
        elif kind == 4:
            self.sub_2_suitable_label.SetLabel(busyo_data["weapon"])
        elif kind == 5:
            self.sub_2_suitable_label.SetLabel(busyo_data["water"])
        
        unique_senpo = StaticDataManager().get_senpo_by_id(busyo_data["org_skill"])
        self.sub_2_unique_senpo_label.SetLabel(unique_senpo["name"])
        self.sub_2_senpo2_select_button.Enable()
        if hensei_data["sub_2_unit"]["skill_2"] == -1:
            self.sub_2_senpo2_select_button.SetLabel(LABEL_CHOICE)
            self.sub_2_senpo2_select_button.SetForegroundColour(wx.BLACK)
        else:
            senpo_2 = StaticDataManager().get_senpo_by_id(hensei_data["sub_2_unit"]["skill_2"])
            suitable_list = StaticDataManager().get_suitable_by_id(hensei_data["sub_2_unit"]["skill_2"])

            if kind != 5 and suitable_list[kind] is not True:
                self.sub_2_senpo2_select_button.SetForegroundColour(wx.RED)
            else:
                self.sub_2_senpo2_select_button.SetForegroundColour(wx.BLACK)
            self.sub_2_senpo2_select_button.SetLabel(senpo_2["name"])

        self.sub_2_senpo3_select_button.Enable()
        if hensei_data["sub_2_unit"]["skill_3"] == -1:
            self.sub_2_senpo3_select_button.SetLabel(LABEL_CHOICE)
            self.sub_2_senpo3_select_button.SetForegroundColour(wx.BLACK)
        else:
            senpo_3 = StaticDataManager().get_senpo_by_id(hensei_data["sub_2_unit"]["skill_3"])
            suitable_list = StaticDataManager().get_suitable_by_id(hensei_data["sub_2_unit"]["skill_3"])

            if kind != 5 and suitable_list[kind] is not True:
                self.sub_2_senpo3_select_button.SetForegroundColour(wx.RED)
            else:
                self.sub_2_senpo3_select_button.SetForegroundColour(wx.BLACK)
            self.sub_2_senpo3_select_button.SetLabel(senpo_3["name"])
        
        self.sub_2_heihousyo_choice.Clear()
        self.sub_2_heihou1_choice.Clear()
        self.sub_2_heihou2_choice.Clear()
        self.sub_2_heihou3_choice.Clear()

        self.sub_2_heihousyo_choice.AppendItems(["作戦", "虚実", "軍形", "九変"])
        sub_2_heihousyo = hensei_data["sub_2_unit"]["heihousyo"]
        
        self.sub_2_heihousyo_choice.SetSelection(sub_2_heihousyo - 1)
        heihou_tuple = self.initialize_heihou(sub_2_heihousyo, busyo_data)
        print(heihou_tuple[1])
        StatusManager().sub_2_heiho_2_3_tuple_list = heihou_tuple[1]
        
        for item in heihou_tuple[0]:
            self.sub_2_heihou1_choice.Append(item[0], item[1])
            
        for item in heihou_tuple[1]:
            self.sub_2_heihou2_choice.Append(item[0], item[1])
            self.sub_2_heihou3_choice.Append(item[0], item[1])
        
        if hensei_data["sub_2_unit"]["heihou_1"] == -1:
            self.sub_2_heihou1_choice.SetSelection(0)

        else:
            self.sub_2_heihou1_choice.SetSelection(self.sub_2_heihou1_choice.FindString(StaticDataManager.get_heiho_name_by_id_list([hensei_data["sub_2_unit"]["heihou_1"]])[0]))
        self.update_heihou_choice(hensei_data["sub_2_unit"]["heihou_2"], 2, 2)
        self.update_heihou_choice(hensei_data["sub_2_unit"]["heihou_3"], 2, 3)
        
        self.sub_2_rankup_choice.SetSelection(hensei_data["sub_1_unit"]["rankup"])
        if hensei_data["sub_2_unit"]["hizo"] == 0:
            self.sub_2_hizo_checkbox.SetValue(False)
        else:
            self.sub_2_hizo_checkbox.SetValue(True)
        if hensei_data["sub_2_unit"]["anime"] == 0:
            self.sub_2_anime_checkbox.SetValue(False)
        else:
            self.sub_2_anime_checkbox.SetValue(True)
        # TODO 残ポイント実装
        self.sub_2_remained_point_label.SetLabel(LABEL_ZERO)
        self.sub_2_str_point_text_ctrl.SetValue(str(hensei_data["sub_2_unit"]["buf_str"]))
        self.sub_2_def_point_text_ctrl.SetValue(str(hensei_data["sub_2_unit"]["buf_def"]))
        self.sub_2_int_point_text_ctrl.SetValue(str(hensei_data["sub_2_unit"]["buf_int"]))
        self.sub_2_spd_point_text_ctrl.SetValue(str(hensei_data["sub_2_unit"]["buf_spd"]))
        self.sub_2_str_point_eq_text_ctrl.SetValue(str(hensei_data["sub_2_unit"]["buf_eq_str"]))
        self.sub_2_def_point_eq_text_ctrl.SetValue(str(hensei_data["sub_2_unit"]["buf_eq_def"]))
        self.sub_2_int_point_eq_text_ctrl.SetValue(str(hensei_data["sub_2_unit"]["buf_eq_int"]))
        self.sub_2_spd_point_eq_text_ctrl.SetValue(str(hensei_data["sub_2_unit"]["buf_eq_spd"]))
        # TODO 装備スキルリスト実装
        self.sub_2_eq_skill_label.SetLabel(LABEL_NOTHING)
        # TODO パラメータ表示実装
        self.sub_2_normal_str_label.SetLabel("武力:" + LABEL_NOTHING)
        self.sub_2_normal_def_label.SetLabel("統率:" + LABEL_NOTHING)
        self.sub_2_normal_int_label.SetLabel("知力:" + LABEL_NOTHING)
        self.sub_2_normal_spd_label.SetLabel("速度:" + LABEL_NOTHING)
        self.sub_2_battle_str_label.SetLabel("武力:" + LABEL_NOTHING)
        self.sub_2_battle_def_label.SetLabel("統率:" + LABEL_NOTHING)
        self.sub_2_battle_int_label.SetLabel("知力:" + LABEL_NOTHING)
        self.sub_2_battle_spd_label.SetLabel("速度:" + LABEL_NOTHING)
        
        self.sub_2_heihousyo_choice.Enable()
        self.sub_2_heihou1_choice.Enable()
        self.sub_2_heihou2_choice.Enable()
        self.sub_2_heihou3_choice.Enable()
        self.sub_2_rankup_choice.Enable()
        self.sub_2_hizo_checkbox.Enable()
        self.sub_2_anime_checkbox.Enable()
        self.sub_2_eq_skill_select_button.Enable()
        return

    def change_hensei(self, event):
        event_id = event.GetId()
        hensei_id = 1
        if event_id == ID_CHANGE_HENSEI_1:
            hensei_id = 1
        elif event_id == ID_CHANGE_HENSEI_2:
            hensei_id = 2
        elif event_id == ID_CHANGE_HENSEI_3:
            hensei_id = 3
        elif event_id == ID_CHANGE_HENSEI_4:
            hensei_id = 4
        elif event_id == ID_CHANGE_HENSEI_5:
            hensei_id = 5
        elif event_id == ID_CHANGE_HENSEI_6:
            hensei_id = 6
        elif event_id == ID_CHANGE_HENSEI_7:
            hensei_id = 7
        elif event_id == ID_CHANGE_HENSEI_8:
            hensei_id = 8
        elif event_id == ID_CHANGE_HENSEI_9:
            hensei_id = 9
        elif event_id == ID_CHANGE_HENSEI_10:
            hensei_id = 10

        StatusManager().selected_hensei = hensei_id
        self.initialize_parameter()
        return

    def initialize_parameter(self):
        status_manager = StatusManager()
        selected_hensei_id = status_manager.selected_hensei
        hensei_manager = HenseiDataManager()
        hensei_data = hensei_manager.get_hensei_data(selected_hensei_id)
        self.update_selected_hensei_button(selected_hensei_id)

        self.update_common_parameter(hensei_data)

        # TODO 絆ラベルの表示処理実装

        self.update_parameter(hensei_data, 0)
        self.update_parameter(hensei_data, 1)
        self.update_parameter(hensei_data, 2)

    def clear_main_unit(self):
        self.main_unit_drop_button.Disable()
        self.main_unit_select_button.SetLabel(LABEL_CHOICE)
        self.main_country_label.SetLabel(LABEL_NOTHING)
        self.main_suitable_label.SetLabel(LABEL_NOTHING)
        self.main_unique_senpo_label.SetLabel(LABEL_NOTHING)
        self.main_senpo2_select_button.Disable()
        self.main_senpo3_select_button.Disable()
        self.main_senpo2_select_button.SetLabel(LABEL_CHOICE)
        self.main_senpo3_select_button.SetLabel(LABEL_CHOICE)
        for i in range(self.main_heihousyo_choice.GetCount()):
            self.main_heihousyo_choice.Delete(0)
        for i in range(self.main_heihou1_choice.GetCount()):
            self.main_heihou1_choice.Delete(0)
        for i in range(self.main_heihou2_choice.GetCount()):
            self.main_heihou2_choice.Delete(0)
        for i in range(self.main_heihou3_choice.GetCount()):
            self.main_heihou3_choice.Delete(0)
        self.main_heihousyo_choice.SetSelection(0)
        self.main_heihou1_choice.SetSelection(0)
        self.main_heihou2_choice.SetSelection(0)
        self.main_heihou3_choice.SetSelection(0)
        self.main_rankup_choice.SetSelection(0)
        self.main_hizo_checkbox.SetValue(False)
        self.main_anime_checkbox.SetValue(False)
        self.main_remained_point_label.SetLabel(LABEL_ZERO)
        self.main_heihousyo_choice.Disable()
        self.main_heihou1_choice.Disable()
        self.main_heihou2_choice.Disable()
        self.main_heihou3_choice.Disable()
        self.main_rankup_choice.Disable()
        self.main_hizo_checkbox.Disable()
        self.main_anime_checkbox.Disable()
        self.main_str_point_text_ctrl.Clear()
        self.main_def_point_text_ctrl.Clear()
        self.main_int_point_text_ctrl.Clear()
        self.main_spd_point_text_ctrl.Clear()
        self.main_str_point_eq_text_ctrl.Clear()
        self.main_def_point_eq_text_ctrl.Clear()
        self.main_int_point_eq_text_ctrl.Clear()
        self.main_spd_point_eq_text_ctrl.Clear()
        self.main_eq_skill_select_button.Disable()
        self.main_eq_skill_label.SetLabel(LABEL_NOTHING)
        self.main_normal_str_label.SetLabel("武力:" + LABEL_NOTHING)
        self.main_normal_def_label.SetLabel("統率:" + LABEL_NOTHING)
        self.main_normal_int_label.SetLabel("知力:" + LABEL_NOTHING)
        self.main_normal_spd_label.SetLabel("速度:" + LABEL_NOTHING)
        self.main_battle_str_label.SetLabel("武力:" + LABEL_NOTHING)
        self.main_battle_def_label.SetLabel("統率:" + LABEL_NOTHING)
        self.main_battle_int_label.SetLabel("知力:" + LABEL_NOTHING)
        self.main_battle_spd_label.SetLabel("速度:" + LABEL_NOTHING)

    def clear_sub_1_unit(self):
        self.sub_1_unit_drop_button.Disable()
        self.sub_1_unit_select_button.SetLabel(LABEL_CHOICE)
        self.sub_1_country_label.SetLabel(LABEL_NOTHING)
        self.sub_1_suitable_label.SetLabel(LABEL_NOTHING)
        self.sub_1_unique_senpo_label.SetLabel(LABEL_NOTHING)
        self.sub_1_senpo2_select_button.Disable()
        self.sub_1_senpo3_select_button.Disable()
        self.sub_1_senpo2_select_button.SetLabel(LABEL_CHOICE)
        self.sub_1_senpo3_select_button.SetLabel(LABEL_CHOICE)
        for i in range(self.sub_1_heihousyo_choice.GetCount()):
            self.sub_1_heihousyo_choice.Delete(0)
        for i in range(self.sub_1_heihou1_choice.GetCount()):
            self.sub_1_heihou1_choice.Delete(0)
        for i in range(self.sub_1_heihou2_choice.GetCount()):
            self.sub_1_heihou2_choice.Delete(0)
        for i in range(self.sub_1_heihou3_choice.GetCount()):
            self.sub_1_heihou3_choice.Delete(0)
        self.sub_1_heihousyo_choice.SetSelection(0)
        self.sub_1_heihou1_choice.SetSelection(0)
        self.sub_1_heihou2_choice.SetSelection(0)
        self.sub_1_heihou3_choice.SetSelection(0)
        self.sub_1_rankup_choice.SetSelection(0)
        self.sub_1_hizo_checkbox.SetValue(False)
        self.sub_1_anime_checkbox.SetValue(False)
        self.sub_1_remained_point_label.SetLabel(LABEL_ZERO)
        self.sub_1_heihousyo_choice.Disable()
        self.sub_1_heihou1_choice.Disable()
        self.sub_1_heihou2_choice.Disable()
        self.sub_1_heihou3_choice.Disable()
        self.sub_1_rankup_choice.Disable()
        self.sub_1_hizo_checkbox.Disable()
        self.sub_1_anime_checkbox.Disable()
        self.sub_1_str_point_text_ctrl.Clear()
        self.sub_1_def_point_text_ctrl.Clear()
        self.sub_1_int_point_text_ctrl.Clear()
        self.sub_1_spd_point_text_ctrl.Clear()
        self.sub_1_str_point_eq_text_ctrl.Clear()
        self.sub_1_def_point_eq_text_ctrl.Clear()
        self.sub_1_int_point_eq_text_ctrl.Clear()
        self.sub_1_spd_point_eq_text_ctrl.Clear()
        self.sub_1_eq_skill_select_button.Disable()
        self.sub_1_eq_skill_label.SetLabel(LABEL_NOTHING)
        self.sub_1_normal_str_label.SetLabel("武力:" + LABEL_NOTHING)
        self.sub_1_normal_def_label.SetLabel("統率:" + LABEL_NOTHING)
        self.sub_1_normal_int_label.SetLabel("知力:" + LABEL_NOTHING)
        self.sub_1_normal_spd_label.SetLabel("速度:" + LABEL_NOTHING)
        self.sub_1_battle_str_label.SetLabel("武力:" + LABEL_NOTHING)
        self.sub_1_battle_def_label.SetLabel("統率:" + LABEL_NOTHING)
        self.sub_1_battle_int_label.SetLabel("知力:" + LABEL_NOTHING)
        self.sub_1_battle_spd_label.SetLabel("速度:" + LABEL_NOTHING)
    
    def clear_sub_2_unit(self):
        self.sub_2_unit_drop_button.Disable()
        self.sub_2_unit_select_button.SetLabel(LABEL_CHOICE)
        self.sub_2_country_label.SetLabel(LABEL_NOTHING)
        self.sub_2_suitable_label.SetLabel(LABEL_NOTHING)
        self.sub_2_unique_senpo_label.SetLabel(LABEL_NOTHING)
        self.sub_2_senpo2_select_button.Disable()
        self.sub_2_senpo3_select_button.Disable()
        self.sub_2_senpo2_select_button.SetLabel(LABEL_CHOICE)
        self.sub_2_senpo3_select_button.SetLabel(LABEL_CHOICE)
        for i in range(self.sub_2_heihousyo_choice.GetCount()):
            self.sub_2_heihousyo_choice.Delete(0)
        for i in range(self.sub_2_heihou1_choice.GetCount()):
            self.sub_2_heihou1_choice.Delete(0)
        for i in range(self.sub_2_heihou2_choice.GetCount()):
            self.sub_2_heihou2_choice.Delete(0)
        for i in range(self.sub_2_heihou3_choice.GetCount()):
            self.sub_2_heihou3_choice.Delete(0)
        self.sub_2_heihousyo_choice.SetSelection(0)
        self.sub_2_heihousyo_choice.Disable()
        self.sub_2_heihou1_choice.SetSelection(0)
        self.sub_2_heihou2_choice.SetSelection(0)
        self.sub_2_heihou3_choice.SetSelection(0)
        self.sub_2_heihou1_choice.Disable()
        self.sub_2_heihou2_choice.Disable()
        self.sub_2_heihou3_choice.Disable()
        self.sub_2_rankup_choice.SetSelection(0)
        self.sub_2_hizo_checkbox.SetValue(False)
        self.sub_2_anime_checkbox.SetValue(False)
        self.sub_2_rankup_choice.Disable()
        self.sub_2_hizo_checkbox.Disable()
        self.sub_2_anime_checkbox.Disable()
        self.sub_2_remained_point_label.SetLabel(LABEL_ZERO)
        self.sub_2_str_point_text_ctrl.Clear()
        self.sub_2_def_point_text_ctrl.Clear()
        self.sub_2_int_point_text_ctrl.Clear()
        self.sub_2_spd_point_text_ctrl.Clear()
        self.sub_2_str_point_eq_text_ctrl.Clear()
        self.sub_2_def_point_eq_text_ctrl.Clear()
        self.sub_2_int_point_eq_text_ctrl.Clear()
        self.sub_2_spd_point_eq_text_ctrl.Clear()
        self.sub_2_eq_skill_select_button.Disable()
        self.sub_2_eq_skill_label.SetLabel(LABEL_NOTHING)
        self.sub_2_normal_str_label.SetLabel("武力:" + LABEL_NOTHING)
        self.sub_2_normal_def_label.SetLabel("統率:" + LABEL_NOTHING)
        self.sub_2_normal_int_label.SetLabel("知力:" + LABEL_NOTHING)
        self.sub_2_normal_spd_label.SetLabel("速度:" + LABEL_NOTHING)
        self.sub_2_battle_str_label.SetLabel("武力:" + LABEL_NOTHING)
        self.sub_2_battle_def_label.SetLabel("統率:" + LABEL_NOTHING)
        self.sub_2_battle_int_label.SetLabel("知力:" + LABEL_NOTHING)
        self.sub_2_battle_spd_label.SetLabel("速度:" + LABEL_NOTHING)

    def update_selected_hensei_button(self, hensei_id):
        button_list = [
            self.h_select_1_button,
            self.h_select_2_button,
            self.h_select_3_button,
            self.h_select_4_button,
            self.h_select_5_button,
            self.h_select_6_button,
            self.h_select_7_button,
            self.h_select_8_button,
            self.h_select_9_button,
            self.h_select_10_button
        ]

        for i, button in enumerate(button_list):
            if i + 1 == hensei_id:
                button.SetBackgroundColour(wx.Colour("SPRING GREEN"))
                button.Disable()
            else:
                button.SetBackgroundColour(wx.Colour(-1))
                button.Enable()
        return

    def show_unit_select(self, event):
        try:
            select_window = UnitSelect(self)
            result = select_window.ShowModal()
        except Exception as e:
            print(e)
        if result == wx.ID_CANCEL:
            print("canceled")
        else:
            busyo_id = result - wx.ID_HIGHEST
            unit_id = 0
            if event.GetId() == ID_SELECT_MAIN:
                unit_id = 0
            elif event.GetId() == ID_SELECT_SUB_1:
                unit_id = 1
            elif event.GetId() == ID_SELECT_SUB_2:
                unit_id = 2
            else:
                pass

            hensei_manager = HenseiDataManager()
            selected_hensei = StatusManager().selected_hensei

            hensei_manager.delete_busyo(unit_id, selected_hensei)
            hensei_manager.set_busyo(busyo_id, unit_id, selected_hensei)
            hensei_data = hensei_manager.get_hensei_data(selected_hensei)

            self.update_parameter(hensei_data, unit_id)

        select_window.Destroy()

    def show_senpo_select(self, event):
        try:
            select_window = SenpoSelect(self)
            result = select_window.ShowModal()
        except Exception as e:
            print(e)
        if result == wx.ID_CANCEL:
            print("canceled")
        else:
            senpo_id = result - wx.ID_HIGHEST

            unit_id = 0
            button_id = 0

            if event.GetId() == ID_SELECT_MAIN_SENPO_2:
                unit_id = 0
                button_id = 0
            elif event.GetId() == ID_SELECT_MAIN_SENPO_3:
                unit_id = 0
                button_id = 1
            elif event.GetId() == ID_SELECT_SUB_1_SENPO_2:
                unit_id = 1
                button_id = 0
            elif event.GetId() == ID_SELECT_SUB_1_SENPO_3:
                unit_id = 1
                button_id = 1
            elif event.GetId() == ID_SELECT_SUB_2_SENPO_2:
                unit_id = 2
                button_id = 0
            elif event.GetId() == ID_SELECT_SUB_2_SENPO_3:
                unit_id = 2
                button_id = 1
            else:
                pass
            
            print(unit_id)
            print(button_id)

            hensei_manager = HenseiDataManager()
            selected_hensei = StatusManager().selected_hensei

            hensei_manager.set_senpo(senpo_id, unit_id, button_id, selected_hensei)
            hensei_data = hensei_manager.get_hensei_data(selected_hensei)

            self.update_parameter(hensei_data, unit_id)

        select_window.Destroy()

    def get_selected_hensei_data(self):
        hensei_manager = HenseiDataManager()
        selected_hensei = StatusManager().selected_hensei
        hensei_data = hensei_manager.get_hensei_data(selected_hensei)
        return hensei_data
    
    def drop_unit(self, event):
        hensei_id = StatusManager().selected_hensei
        if event.GetId() == ID_SELECT_CLEAR_MAIN:
            HenseiDataManager().delete_busyo(0, hensei_id)
            self.clear_main_unit()
            StatusManager.main_heiho_2_3_tuple_list = []
        elif event.GetId() == ID_SELECT_CLEAR_SUB_1:
            HenseiDataManager().delete_busyo(1, hensei_id)
            self.clear_sub_1_unit()
            StatusManager.sub_1_heiho_2_3_tuple_list = []
        elif event.GetId() == ID_SELECT_CLEAR_SUB_2:
            HenseiDataManager().delete_busyo(2, hensei_id)
            self.clear_sub_2_unit()
            StatusManager.sub_2_heiho_2_3_tuple_list = []
        

    def __del__(self):
        pass
