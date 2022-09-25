# -*- coding: utf-8 -*-

import wx
import wx.xrc

###########################################################################
# Class ShowList
###########################################################################


class ShowList(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"編成一覧", pos=wx.DefaultPosition, size=wx.Size(733, 362), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        base_box = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow1 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow1.SetScrollRate(5, 5)
        sbSizer37 = wx.StaticBoxSizer(wx.StaticBox(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        sbSizer38 = wx.StaticBoxSizer(wx.StaticBox(sbSizer37.GetStaticBox(), wx.ID_ANY, u"編成1"), wx.VERTICAL)

        bSizer150 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText136 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText136.Wrap(-1)

        bSizer150.Add(self.m_staticText136, 0, wx.ALL, 5)

        bSizer132 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer133 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText103 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText103.Wrap(-1)

        bSizer133.Add(self.m_staticText103, 0, wx.ALL, 5)

        self.m_staticText104 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText104.Wrap(-1)

        bSizer133.Add(self.m_staticText104, 0, wx.ALL, 5)

        self.m_staticText105 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText105.Wrap(-1)

        bSizer133.Add(self.m_staticText105, 0, wx.ALL, 5)

        bSizer132.Add(bSizer133, 1, wx.EXPAND, 5)

        bSizer134 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText106 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText106.Wrap(-1)

        bSizer134.Add(self.m_staticText106, 0, wx.ALL, 5)

        self.m_staticText107 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText107.Wrap(-1)

        bSizer134.Add(self.m_staticText107, 0, wx.ALL, 5)

        self.m_staticText108 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText108.Wrap(-1)

        bSizer134.Add(self.m_staticText108, 0, wx.ALL, 5)

        bSizer132.Add(bSizer134, 1, wx.EXPAND, 5)

        bSizer135 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText109 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText109.Wrap(-1)

        bSizer135.Add(self.m_staticText109, 0, wx.ALL, 5)

        self.m_staticText110 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText110.Wrap(-1)

        bSizer135.Add(self.m_staticText110, 0, wx.ALL, 5)

        self.m_staticText111 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText111.Wrap(-1)

        bSizer135.Add(self.m_staticText111, 0, wx.ALL, 5)

        bSizer132.Add(bSizer135, 1, wx.EXPAND, 5)

        bSizer1352 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1092 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1092.Wrap(-1)

        bSizer1352.Add(self.m_staticText1092, 0, wx.ALL, 5)

        self.m_staticText1102 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1102.Wrap(-1)

        bSizer1352.Add(self.m_staticText1102, 0, wx.ALL, 5)

        self.m_staticText1112 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1112.Wrap(-1)

        bSizer1352.Add(self.m_staticText1112, 0, wx.ALL, 5)

        bSizer132.Add(bSizer1352, 1, wx.EXPAND, 5)

        bSizer1353 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1093 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1093.Wrap(-1)

        bSizer1353.Add(self.m_staticText1093, 0, wx.ALL, 5)

        self.m_staticText1103 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1103.Wrap(-1)

        bSizer1353.Add(self.m_staticText1103, 0, wx.ALL, 5)

        self.m_staticText1113 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1113.Wrap(-1)

        bSizer1353.Add(self.m_staticText1113, 0, wx.ALL, 5)

        bSizer132.Add(bSizer1353, 1, wx.EXPAND, 5)

        bSizer1354 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1094 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1094.Wrap(-1)

        bSizer1354.Add(self.m_staticText1094, 0, wx.ALL, 5)

        self.m_staticText1104 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1104.Wrap(-1)

        bSizer1354.Add(self.m_staticText1104, 0, wx.ALL, 5)

        self.m_staticText1114 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1114.Wrap(-1)

        bSizer1354.Add(self.m_staticText1114, 0, wx.ALL, 5)

        bSizer132.Add(bSizer1354, 1, wx.EXPAND, 5)

        bSizer1355 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1095 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1095.Wrap(-1)

        bSizer1355.Add(self.m_staticText1095, 0, wx.ALL, 5)

        self.m_staticText1105 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1105.Wrap(-1)

        bSizer1355.Add(self.m_staticText1105, 0, wx.ALL, 5)

        self.m_staticText1115 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1115.Wrap(-1)

        bSizer1355.Add(self.m_staticText1115, 0, wx.ALL, 5)

        bSizer132.Add(bSizer1355, 1, wx.EXPAND, 5)

        bSizer1331 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1031 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1031.Wrap(-1)

        bSizer1331.Add(self.m_staticText1031, 0, wx.ALL, 5)

        self.m_staticText1041 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1041.Wrap(-1)

        bSizer1331.Add(self.m_staticText1041, 0, wx.ALL, 5)

        self.m_staticText1051 = wx.StaticText(sbSizer38.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1051.Wrap(-1)

        bSizer1331.Add(self.m_staticText1051, 0, wx.ALL, 5)

        bSizer132.Add(bSizer1331, 1, wx.EXPAND, 5)

        bSizer150.Add(bSizer132, 1, wx.EXPAND, 5)

        sbSizer38.Add(bSizer150, 1, wx.EXPAND, 5)

        sbSizer37.Add(sbSizer38, 1, wx.EXPAND, 5)

        sbSizer40 = wx.StaticBoxSizer(wx.StaticBox(sbSizer37.GetStaticBox(), wx.ID_ANY, u"編成2"), wx.VERTICAL)

        bSizer1501 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1361 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1361.Wrap(-1)

        bSizer1501.Add(self.m_staticText1361, 0, wx.ALL, 5)

        bSizer1321 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1332 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1032 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1032.Wrap(-1)

        bSizer1332.Add(self.m_staticText1032, 0, wx.ALL, 5)

        self.m_staticText1042 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1042.Wrap(-1)

        bSizer1332.Add(self.m_staticText1042, 0, wx.ALL, 5)

        self.m_staticText1052 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1052.Wrap(-1)

        bSizer1332.Add(self.m_staticText1052, 0, wx.ALL, 5)

        bSizer1321.Add(bSizer1332, 1, wx.EXPAND, 5)

        bSizer1341 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1061 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1061.Wrap(-1)

        bSizer1341.Add(self.m_staticText1061, 0, wx.ALL, 5)

        self.m_staticText1071 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1071.Wrap(-1)

        bSizer1341.Add(self.m_staticText1071, 0, wx.ALL, 5)

        self.m_staticText1081 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1081.Wrap(-1)

        bSizer1341.Add(self.m_staticText1081, 0, wx.ALL, 5)

        bSizer1321.Add(bSizer1341, 1, wx.EXPAND, 5)

        bSizer1351 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1091 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1091.Wrap(-1)

        bSizer1351.Add(self.m_staticText1091, 0, wx.ALL, 5)

        self.m_staticText1101 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1101.Wrap(-1)

        bSizer1351.Add(self.m_staticText1101, 0, wx.ALL, 5)

        self.m_staticText1111 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1111.Wrap(-1)

        bSizer1351.Add(self.m_staticText1111, 0, wx.ALL, 5)

        bSizer1321.Add(bSizer1351, 1, wx.EXPAND, 5)

        bSizer13521 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10921 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10921.Wrap(-1)

        bSizer13521.Add(self.m_staticText10921, 0, wx.ALL, 5)

        self.m_staticText11021 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11021.Wrap(-1)

        bSizer13521.Add(self.m_staticText11021, 0, wx.ALL, 5)

        self.m_staticText11121 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11121.Wrap(-1)

        bSizer13521.Add(self.m_staticText11121, 0, wx.ALL, 5)

        bSizer1321.Add(bSizer13521, 1, wx.EXPAND, 5)

        bSizer13531 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10931 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10931.Wrap(-1)

        bSizer13531.Add(self.m_staticText10931, 0, wx.ALL, 5)

        self.m_staticText11031 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11031.Wrap(-1)

        bSizer13531.Add(self.m_staticText11031, 0, wx.ALL, 5)

        self.m_staticText11131 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11131.Wrap(-1)

        bSizer13531.Add(self.m_staticText11131, 0, wx.ALL, 5)

        bSizer1321.Add(bSizer13531, 1, wx.EXPAND, 5)

        bSizer13541 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10941 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10941.Wrap(-1)

        bSizer13541.Add(self.m_staticText10941, 0, wx.ALL, 5)

        self.m_staticText11041 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11041.Wrap(-1)

        bSizer13541.Add(self.m_staticText11041, 0, wx.ALL, 5)

        self.m_staticText11141 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11141.Wrap(-1)

        bSizer13541.Add(self.m_staticText11141, 0, wx.ALL, 5)

        bSizer1321.Add(bSizer13541, 1, wx.EXPAND, 5)

        bSizer13551 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10951 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10951.Wrap(-1)

        bSizer13551.Add(self.m_staticText10951, 0, wx.ALL, 5)

        self.m_staticText11051 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11051.Wrap(-1)

        bSizer13551.Add(self.m_staticText11051, 0, wx.ALL, 5)

        self.m_staticText11151 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11151.Wrap(-1)

        bSizer13551.Add(self.m_staticText11151, 0, wx.ALL, 5)

        bSizer1321.Add(bSizer13551, 1, wx.EXPAND, 5)

        bSizer13311 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10311 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10311.Wrap(-1)

        bSizer13311.Add(self.m_staticText10311, 0, wx.ALL, 5)

        self.m_staticText10411 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10411.Wrap(-1)

        bSizer13311.Add(self.m_staticText10411, 0, wx.ALL, 5)

        self.m_staticText10511 = wx.StaticText(sbSizer40.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10511.Wrap(-1)

        bSizer13311.Add(self.m_staticText10511, 0, wx.ALL, 5)

        bSizer1321.Add(bSizer13311, 1, wx.EXPAND, 5)

        bSizer1501.Add(bSizer1321, 1, wx.EXPAND, 5)

        sbSizer40.Add(bSizer1501, 1, wx.EXPAND, 5)

        sbSizer37.Add(sbSizer40, 1, wx.EXPAND, 5)

        sbSizer42 = wx.StaticBoxSizer(wx.StaticBox(sbSizer37.GetStaticBox(), wx.ID_ANY, u"編成3"), wx.VERTICAL)

        bSizer1502 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1362 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1362.Wrap(-1)

        bSizer1502.Add(self.m_staticText1362, 0, wx.ALL, 5)

        bSizer1322 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1333 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1033 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1033.Wrap(-1)

        bSizer1333.Add(self.m_staticText1033, 0, wx.ALL, 5)

        self.m_staticText1043 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1043.Wrap(-1)

        bSizer1333.Add(self.m_staticText1043, 0, wx.ALL, 5)

        self.m_staticText1053 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1053.Wrap(-1)

        bSizer1333.Add(self.m_staticText1053, 0, wx.ALL, 5)

        bSizer1322.Add(bSizer1333, 1, wx.EXPAND, 5)

        bSizer1342 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1062 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1062.Wrap(-1)

        bSizer1342.Add(self.m_staticText1062, 0, wx.ALL, 5)

        self.m_staticText1072 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1072.Wrap(-1)

        bSizer1342.Add(self.m_staticText1072, 0, wx.ALL, 5)

        self.m_staticText1082 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1082.Wrap(-1)

        bSizer1342.Add(self.m_staticText1082, 0, wx.ALL, 5)

        bSizer1322.Add(bSizer1342, 1, wx.EXPAND, 5)

        bSizer1356 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1096 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1096.Wrap(-1)

        bSizer1356.Add(self.m_staticText1096, 0, wx.ALL, 5)

        self.m_staticText1106 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1106.Wrap(-1)

        bSizer1356.Add(self.m_staticText1106, 0, wx.ALL, 5)

        self.m_staticText1116 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1116.Wrap(-1)

        bSizer1356.Add(self.m_staticText1116, 0, wx.ALL, 5)

        bSizer1322.Add(bSizer1356, 1, wx.EXPAND, 5)

        bSizer13522 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10922 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10922.Wrap(-1)

        bSizer13522.Add(self.m_staticText10922, 0, wx.ALL, 5)

        self.m_staticText11022 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11022.Wrap(-1)

        bSizer13522.Add(self.m_staticText11022, 0, wx.ALL, 5)

        self.m_staticText11122 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11122.Wrap(-1)

        bSizer13522.Add(self.m_staticText11122, 0, wx.ALL, 5)

        bSizer1322.Add(bSizer13522, 1, wx.EXPAND, 5)

        bSizer13532 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10932 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10932.Wrap(-1)

        bSizer13532.Add(self.m_staticText10932, 0, wx.ALL, 5)

        self.m_staticText11032 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11032.Wrap(-1)

        bSizer13532.Add(self.m_staticText11032, 0, wx.ALL, 5)

        self.m_staticText11132 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11132.Wrap(-1)

        bSizer13532.Add(self.m_staticText11132, 0, wx.ALL, 5)

        bSizer1322.Add(bSizer13532, 1, wx.EXPAND, 5)

        bSizer13542 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10942 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10942.Wrap(-1)

        bSizer13542.Add(self.m_staticText10942, 0, wx.ALL, 5)

        self.m_staticText11042 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11042.Wrap(-1)

        bSizer13542.Add(self.m_staticText11042, 0, wx.ALL, 5)

        self.m_staticText11142 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11142.Wrap(-1)

        bSizer13542.Add(self.m_staticText11142, 0, wx.ALL, 5)

        bSizer1322.Add(bSizer13542, 1, wx.EXPAND, 5)

        bSizer13552 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10952 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10952.Wrap(-1)

        bSizer13552.Add(self.m_staticText10952, 0, wx.ALL, 5)

        self.m_staticText11052 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11052.Wrap(-1)

        bSizer13552.Add(self.m_staticText11052, 0, wx.ALL, 5)

        self.m_staticText11152 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11152.Wrap(-1)

        bSizer13552.Add(self.m_staticText11152, 0, wx.ALL, 5)

        bSizer1322.Add(bSizer13552, 1, wx.EXPAND, 5)

        bSizer13312 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10312 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10312.Wrap(-1)

        bSizer13312.Add(self.m_staticText10312, 0, wx.ALL, 5)

        self.m_staticText10412 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10412.Wrap(-1)

        bSizer13312.Add(self.m_staticText10412, 0, wx.ALL, 5)

        self.m_staticText10512 = wx.StaticText(sbSizer42.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10512.Wrap(-1)

        bSizer13312.Add(self.m_staticText10512, 0, wx.ALL, 5)

        bSizer1322.Add(bSizer13312, 1, wx.EXPAND, 5)

        bSizer1502.Add(bSizer1322, 1, wx.EXPAND, 5)

        sbSizer42.Add(bSizer1502, 1, wx.EXPAND, 5)

        sbSizer37.Add(sbSizer42, 1, wx.EXPAND, 5)

        sbSizer43 = wx.StaticBoxSizer(wx.StaticBox(sbSizer37.GetStaticBox(), wx.ID_ANY, u"編成4"), wx.VERTICAL)

        bSizer1503 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1363 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1363.Wrap(-1)

        bSizer1503.Add(self.m_staticText1363, 0, wx.ALL, 5)

        bSizer1323 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1334 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1034 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1034.Wrap(-1)

        bSizer1334.Add(self.m_staticText1034, 0, wx.ALL, 5)

        self.m_staticText1044 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1044.Wrap(-1)

        bSizer1334.Add(self.m_staticText1044, 0, wx.ALL, 5)

        self.m_staticText1054 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1054.Wrap(-1)

        bSizer1334.Add(self.m_staticText1054, 0, wx.ALL, 5)

        bSizer1323.Add(bSizer1334, 1, wx.EXPAND, 5)

        bSizer1343 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1063 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1063.Wrap(-1)

        bSizer1343.Add(self.m_staticText1063, 0, wx.ALL, 5)

        self.m_staticText1073 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1073.Wrap(-1)

        bSizer1343.Add(self.m_staticText1073, 0, wx.ALL, 5)

        self.m_staticText1083 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1083.Wrap(-1)

        bSizer1343.Add(self.m_staticText1083, 0, wx.ALL, 5)

        bSizer1323.Add(bSizer1343, 1, wx.EXPAND, 5)

        bSizer1357 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1097 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1097.Wrap(-1)

        bSizer1357.Add(self.m_staticText1097, 0, wx.ALL, 5)

        self.m_staticText1107 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1107.Wrap(-1)

        bSizer1357.Add(self.m_staticText1107, 0, wx.ALL, 5)

        self.m_staticText1117 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1117.Wrap(-1)

        bSizer1357.Add(self.m_staticText1117, 0, wx.ALL, 5)

        bSizer1323.Add(bSizer1357, 1, wx.EXPAND, 5)

        bSizer13523 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10923 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10923.Wrap(-1)

        bSizer13523.Add(self.m_staticText10923, 0, wx.ALL, 5)

        self.m_staticText11023 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11023.Wrap(-1)

        bSizer13523.Add(self.m_staticText11023, 0, wx.ALL, 5)

        self.m_staticText11123 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11123.Wrap(-1)

        bSizer13523.Add(self.m_staticText11123, 0, wx.ALL, 5)

        bSizer1323.Add(bSizer13523, 1, wx.EXPAND, 5)

        bSizer13533 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10933 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10933.Wrap(-1)

        bSizer13533.Add(self.m_staticText10933, 0, wx.ALL, 5)

        self.m_staticText11033 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11033.Wrap(-1)

        bSizer13533.Add(self.m_staticText11033, 0, wx.ALL, 5)

        self.m_staticText11133 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11133.Wrap(-1)

        bSizer13533.Add(self.m_staticText11133, 0, wx.ALL, 5)

        bSizer1323.Add(bSizer13533, 1, wx.EXPAND, 5)

        bSizer13543 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10943 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10943.Wrap(-1)

        bSizer13543.Add(self.m_staticText10943, 0, wx.ALL, 5)

        self.m_staticText11043 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11043.Wrap(-1)

        bSizer13543.Add(self.m_staticText11043, 0, wx.ALL, 5)

        self.m_staticText11143 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11143.Wrap(-1)

        bSizer13543.Add(self.m_staticText11143, 0, wx.ALL, 5)

        bSizer1323.Add(bSizer13543, 1, wx.EXPAND, 5)

        bSizer13553 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10953 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10953.Wrap(-1)

        bSizer13553.Add(self.m_staticText10953, 0, wx.ALL, 5)

        self.m_staticText11053 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11053.Wrap(-1)

        bSizer13553.Add(self.m_staticText11053, 0, wx.ALL, 5)

        self.m_staticText11153 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11153.Wrap(-1)

        bSizer13553.Add(self.m_staticText11153, 0, wx.ALL, 5)

        bSizer1323.Add(bSizer13553, 1, wx.EXPAND, 5)

        bSizer13313 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10313 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10313.Wrap(-1)

        bSizer13313.Add(self.m_staticText10313, 0, wx.ALL, 5)

        self.m_staticText10413 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10413.Wrap(-1)

        bSizer13313.Add(self.m_staticText10413, 0, wx.ALL, 5)

        self.m_staticText10513 = wx.StaticText(sbSizer43.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10513.Wrap(-1)

        bSizer13313.Add(self.m_staticText10513, 0, wx.ALL, 5)

        bSizer1323.Add(bSizer13313, 1, wx.EXPAND, 5)

        bSizer1503.Add(bSizer1323, 1, wx.EXPAND, 5)

        sbSizer43.Add(bSizer1503, 1, wx.EXPAND, 5)

        sbSizer37.Add(sbSizer43, 1, wx.EXPAND, 5)

        sbSizer44 = wx.StaticBoxSizer(wx.StaticBox(sbSizer37.GetStaticBox(), wx.ID_ANY, u"編成5"), wx.VERTICAL)

        bSizer1504 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1364 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1364.Wrap(-1)

        bSizer1504.Add(self.m_staticText1364, 0, wx.ALL, 5)

        bSizer1324 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1335 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1035 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1035.Wrap(-1)

        bSizer1335.Add(self.m_staticText1035, 0, wx.ALL, 5)

        self.m_staticText1045 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1045.Wrap(-1)

        bSizer1335.Add(self.m_staticText1045, 0, wx.ALL, 5)

        self.m_staticText1055 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1055.Wrap(-1)

        bSizer1335.Add(self.m_staticText1055, 0, wx.ALL, 5)

        bSizer1324.Add(bSizer1335, 1, wx.EXPAND, 5)

        bSizer1344 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1064 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1064.Wrap(-1)

        bSizer1344.Add(self.m_staticText1064, 0, wx.ALL, 5)

        self.m_staticText1074 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1074.Wrap(-1)

        bSizer1344.Add(self.m_staticText1074, 0, wx.ALL, 5)

        self.m_staticText1084 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1084.Wrap(-1)

        bSizer1344.Add(self.m_staticText1084, 0, wx.ALL, 5)

        bSizer1324.Add(bSizer1344, 1, wx.EXPAND, 5)

        bSizer1358 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1098 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1098.Wrap(-1)

        bSizer1358.Add(self.m_staticText1098, 0, wx.ALL, 5)

        self.m_staticText1108 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1108.Wrap(-1)

        bSizer1358.Add(self.m_staticText1108, 0, wx.ALL, 5)

        self.m_staticText1118 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1118.Wrap(-1)

        bSizer1358.Add(self.m_staticText1118, 0, wx.ALL, 5)

        bSizer1324.Add(bSizer1358, 1, wx.EXPAND, 5)

        bSizer13524 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10924 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10924.Wrap(-1)

        bSizer13524.Add(self.m_staticText10924, 0, wx.ALL, 5)

        self.m_staticText11024 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11024.Wrap(-1)

        bSizer13524.Add(self.m_staticText11024, 0, wx.ALL, 5)

        self.m_staticText11124 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11124.Wrap(-1)

        bSizer13524.Add(self.m_staticText11124, 0, wx.ALL, 5)

        bSizer1324.Add(bSizer13524, 1, wx.EXPAND, 5)

        bSizer13534 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10934 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10934.Wrap(-1)

        bSizer13534.Add(self.m_staticText10934, 0, wx.ALL, 5)

        self.m_staticText11034 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11034.Wrap(-1)

        bSizer13534.Add(self.m_staticText11034, 0, wx.ALL, 5)

        self.m_staticText11134 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11134.Wrap(-1)

        bSizer13534.Add(self.m_staticText11134, 0, wx.ALL, 5)

        bSizer1324.Add(bSizer13534, 1, wx.EXPAND, 5)

        bSizer13544 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10944 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10944.Wrap(-1)

        bSizer13544.Add(self.m_staticText10944, 0, wx.ALL, 5)

        self.m_staticText11044 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11044.Wrap(-1)

        bSizer13544.Add(self.m_staticText11044, 0, wx.ALL, 5)

        self.m_staticText11144 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11144.Wrap(-1)

        bSizer13544.Add(self.m_staticText11144, 0, wx.ALL, 5)

        bSizer1324.Add(bSizer13544, 1, wx.EXPAND, 5)

        bSizer13554 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10954 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10954.Wrap(-1)

        bSizer13554.Add(self.m_staticText10954, 0, wx.ALL, 5)

        self.m_staticText11054 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11054.Wrap(-1)

        bSizer13554.Add(self.m_staticText11054, 0, wx.ALL, 5)

        self.m_staticText11154 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11154.Wrap(-1)

        bSizer13554.Add(self.m_staticText11154, 0, wx.ALL, 5)

        bSizer1324.Add(bSizer13554, 1, wx.EXPAND, 5)

        bSizer13314 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10314 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10314.Wrap(-1)

        bSizer13314.Add(self.m_staticText10314, 0, wx.ALL, 5)

        self.m_staticText10414 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10414.Wrap(-1)

        bSizer13314.Add(self.m_staticText10414, 0, wx.ALL, 5)

        self.m_staticText10514 = wx.StaticText(sbSizer44.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10514.Wrap(-1)

        bSizer13314.Add(self.m_staticText10514, 0, wx.ALL, 5)

        bSizer1324.Add(bSizer13314, 1, wx.EXPAND, 5)

        bSizer1504.Add(bSizer1324, 1, wx.EXPAND, 5)

        sbSizer44.Add(bSizer1504, 1, wx.EXPAND, 5)

        sbSizer37.Add(sbSizer44, 1, wx.EXPAND, 5)

        sbSizer47 = wx.StaticBoxSizer(wx.StaticBox(sbSizer37.GetStaticBox(), wx.ID_ANY, u"編成6"), wx.VERTICAL)

        bSizer1505 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1365 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1365.Wrap(-1)

        bSizer1505.Add(self.m_staticText1365, 0, wx.ALL, 5)

        bSizer1325 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1336 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1036 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1036.Wrap(-1)

        bSizer1336.Add(self.m_staticText1036, 0, wx.ALL, 5)

        self.m_staticText1046 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1046.Wrap(-1)

        bSizer1336.Add(self.m_staticText1046, 0, wx.ALL, 5)

        self.m_staticText1056 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1056.Wrap(-1)

        bSizer1336.Add(self.m_staticText1056, 0, wx.ALL, 5)

        bSizer1325.Add(bSizer1336, 1, wx.EXPAND, 5)

        bSizer1345 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1065 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1065.Wrap(-1)

        bSizer1345.Add(self.m_staticText1065, 0, wx.ALL, 5)

        self.m_staticText1075 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1075.Wrap(-1)

        bSizer1345.Add(self.m_staticText1075, 0, wx.ALL, 5)

        self.m_staticText1085 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1085.Wrap(-1)

        bSizer1345.Add(self.m_staticText1085, 0, wx.ALL, 5)

        bSizer1325.Add(bSizer1345, 1, wx.EXPAND, 5)

        bSizer1359 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1099 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1099.Wrap(-1)

        bSizer1359.Add(self.m_staticText1099, 0, wx.ALL, 5)

        self.m_staticText1109 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1109.Wrap(-1)

        bSizer1359.Add(self.m_staticText1109, 0, wx.ALL, 5)

        self.m_staticText1119 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1119.Wrap(-1)

        bSizer1359.Add(self.m_staticText1119, 0, wx.ALL, 5)

        bSizer1325.Add(bSizer1359, 1, wx.EXPAND, 5)

        bSizer13525 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10925 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10925.Wrap(-1)

        bSizer13525.Add(self.m_staticText10925, 0, wx.ALL, 5)

        self.m_staticText11025 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11025.Wrap(-1)

        bSizer13525.Add(self.m_staticText11025, 0, wx.ALL, 5)

        self.m_staticText11125 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11125.Wrap(-1)

        bSizer13525.Add(self.m_staticText11125, 0, wx.ALL, 5)

        bSizer1325.Add(bSizer13525, 1, wx.EXPAND, 5)

        bSizer13535 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10935 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10935.Wrap(-1)

        bSizer13535.Add(self.m_staticText10935, 0, wx.ALL, 5)

        self.m_staticText11035 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11035.Wrap(-1)

        bSizer13535.Add(self.m_staticText11035, 0, wx.ALL, 5)

        self.m_staticText11135 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11135.Wrap(-1)

        bSizer13535.Add(self.m_staticText11135, 0, wx.ALL, 5)

        bSizer1325.Add(bSizer13535, 1, wx.EXPAND, 5)

        bSizer13545 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10945 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10945.Wrap(-1)

        bSizer13545.Add(self.m_staticText10945, 0, wx.ALL, 5)

        self.m_staticText11045 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11045.Wrap(-1)

        bSizer13545.Add(self.m_staticText11045, 0, wx.ALL, 5)

        self.m_staticText11145 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11145.Wrap(-1)

        bSizer13545.Add(self.m_staticText11145, 0, wx.ALL, 5)

        bSizer1325.Add(bSizer13545, 1, wx.EXPAND, 5)

        bSizer13555 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10955 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10955.Wrap(-1)

        bSizer13555.Add(self.m_staticText10955, 0, wx.ALL, 5)

        self.m_staticText11055 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11055.Wrap(-1)

        bSizer13555.Add(self.m_staticText11055, 0, wx.ALL, 5)

        self.m_staticText11155 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11155.Wrap(-1)

        bSizer13555.Add(self.m_staticText11155, 0, wx.ALL, 5)

        bSizer1325.Add(bSizer13555, 1, wx.EXPAND, 5)

        bSizer13315 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10315 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10315.Wrap(-1)

        bSizer13315.Add(self.m_staticText10315, 0, wx.ALL, 5)

        self.m_staticText10415 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10415.Wrap(-1)

        bSizer13315.Add(self.m_staticText10415, 0, wx.ALL, 5)

        self.m_staticText10515 = wx.StaticText(sbSizer47.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10515.Wrap(-1)

        bSizer13315.Add(self.m_staticText10515, 0, wx.ALL, 5)

        bSizer1325.Add(bSizer13315, 1, wx.EXPAND, 5)

        bSizer1505.Add(bSizer1325, 1, wx.EXPAND, 5)

        sbSizer47.Add(bSizer1505, 1, wx.EXPAND, 5)

        sbSizer37.Add(sbSizer47, 1, wx.EXPAND, 5)

        sbSizer48 = wx.StaticBoxSizer(wx.StaticBox(sbSizer37.GetStaticBox(), wx.ID_ANY, u"編成7"), wx.VERTICAL)

        bSizer1506 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1366 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1366.Wrap(-1)

        bSizer1506.Add(self.m_staticText1366, 0, wx.ALL, 5)

        bSizer1326 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1337 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1037 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1037.Wrap(-1)

        bSizer1337.Add(self.m_staticText1037, 0, wx.ALL, 5)

        self.m_staticText1047 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1047.Wrap(-1)

        bSizer1337.Add(self.m_staticText1047, 0, wx.ALL, 5)

        self.m_staticText1057 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1057.Wrap(-1)

        bSizer1337.Add(self.m_staticText1057, 0, wx.ALL, 5)

        bSizer1326.Add(bSizer1337, 1, wx.EXPAND, 5)

        bSizer1346 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1066 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1066.Wrap(-1)

        bSizer1346.Add(self.m_staticText1066, 0, wx.ALL, 5)

        self.m_staticText1076 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1076.Wrap(-1)

        bSizer1346.Add(self.m_staticText1076, 0, wx.ALL, 5)

        self.m_staticText1086 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1086.Wrap(-1)

        bSizer1346.Add(self.m_staticText1086, 0, wx.ALL, 5)

        bSizer1326.Add(bSizer1346, 1, wx.EXPAND, 5)

        bSizer13510 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10910 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10910.Wrap(-1)

        bSizer13510.Add(self.m_staticText10910, 0, wx.ALL, 5)

        self.m_staticText11010 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11010.Wrap(-1)

        bSizer13510.Add(self.m_staticText11010, 0, wx.ALL, 5)

        self.m_staticText11110 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11110.Wrap(-1)

        bSizer13510.Add(self.m_staticText11110, 0, wx.ALL, 5)

        bSizer1326.Add(bSizer13510, 1, wx.EXPAND, 5)

        bSizer13526 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10926 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10926.Wrap(-1)

        bSizer13526.Add(self.m_staticText10926, 0, wx.ALL, 5)

        self.m_staticText11026 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11026.Wrap(-1)

        bSizer13526.Add(self.m_staticText11026, 0, wx.ALL, 5)

        self.m_staticText11126 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11126.Wrap(-1)

        bSizer13526.Add(self.m_staticText11126, 0, wx.ALL, 5)

        bSizer1326.Add(bSizer13526, 1, wx.EXPAND, 5)

        bSizer13536 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10936 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10936.Wrap(-1)

        bSizer13536.Add(self.m_staticText10936, 0, wx.ALL, 5)

        self.m_staticText11036 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11036.Wrap(-1)

        bSizer13536.Add(self.m_staticText11036, 0, wx.ALL, 5)

        self.m_staticText11136 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11136.Wrap(-1)

        bSizer13536.Add(self.m_staticText11136, 0, wx.ALL, 5)

        bSizer1326.Add(bSizer13536, 1, wx.EXPAND, 5)

        bSizer13546 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10946 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10946.Wrap(-1)

        bSizer13546.Add(self.m_staticText10946, 0, wx.ALL, 5)

        self.m_staticText11046 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11046.Wrap(-1)

        bSizer13546.Add(self.m_staticText11046, 0, wx.ALL, 5)

        self.m_staticText11146 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11146.Wrap(-1)

        bSizer13546.Add(self.m_staticText11146, 0, wx.ALL, 5)

        bSizer1326.Add(bSizer13546, 1, wx.EXPAND, 5)

        bSizer13556 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10956 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10956.Wrap(-1)

        bSizer13556.Add(self.m_staticText10956, 0, wx.ALL, 5)

        self.m_staticText11056 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11056.Wrap(-1)

        bSizer13556.Add(self.m_staticText11056, 0, wx.ALL, 5)

        self.m_staticText11156 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11156.Wrap(-1)

        bSizer13556.Add(self.m_staticText11156, 0, wx.ALL, 5)

        bSizer1326.Add(bSizer13556, 1, wx.EXPAND, 5)

        bSizer13316 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10316 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10316.Wrap(-1)

        bSizer13316.Add(self.m_staticText10316, 0, wx.ALL, 5)

        self.m_staticText10416 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10416.Wrap(-1)

        bSizer13316.Add(self.m_staticText10416, 0, wx.ALL, 5)

        self.m_staticText10516 = wx.StaticText(sbSizer48.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10516.Wrap(-1)

        bSizer13316.Add(self.m_staticText10516, 0, wx.ALL, 5)

        bSizer1326.Add(bSizer13316, 1, wx.EXPAND, 5)

        bSizer1506.Add(bSizer1326, 1, wx.EXPAND, 5)

        sbSizer48.Add(bSizer1506, 1, wx.EXPAND, 5)

        sbSizer37.Add(sbSizer48, 1, wx.EXPAND, 5)

        sbSizer46 = wx.StaticBoxSizer(wx.StaticBox(sbSizer37.GetStaticBox(), wx.ID_ANY, u"編成8"), wx.VERTICAL)

        bSizer1507 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1367 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1367.Wrap(-1)

        bSizer1507.Add(self.m_staticText1367, 0, wx.ALL, 5)

        bSizer1327 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1338 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1038 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1038.Wrap(-1)

        bSizer1338.Add(self.m_staticText1038, 0, wx.ALL, 5)

        self.m_staticText1048 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1048.Wrap(-1)

        bSizer1338.Add(self.m_staticText1048, 0, wx.ALL, 5)

        self.m_staticText1058 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1058.Wrap(-1)

        bSizer1338.Add(self.m_staticText1058, 0, wx.ALL, 5)

        bSizer1327.Add(bSizer1338, 1, wx.EXPAND, 5)

        bSizer1347 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1067 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1067.Wrap(-1)

        bSizer1347.Add(self.m_staticText1067, 0, wx.ALL, 5)

        self.m_staticText1077 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1077.Wrap(-1)

        bSizer1347.Add(self.m_staticText1077, 0, wx.ALL, 5)

        self.m_staticText1087 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1087.Wrap(-1)

        bSizer1347.Add(self.m_staticText1087, 0, wx.ALL, 5)

        bSizer1327.Add(bSizer1347, 1, wx.EXPAND, 5)

        bSizer13511 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10911 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10911.Wrap(-1)

        bSizer13511.Add(self.m_staticText10911, 0, wx.ALL, 5)

        self.m_staticText11011 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11011.Wrap(-1)

        bSizer13511.Add(self.m_staticText11011, 0, wx.ALL, 5)

        self.m_staticText11111 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11111.Wrap(-1)

        bSizer13511.Add(self.m_staticText11111, 0, wx.ALL, 5)

        bSizer1327.Add(bSizer13511, 1, wx.EXPAND, 5)

        bSizer13527 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10927 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10927.Wrap(-1)

        bSizer13527.Add(self.m_staticText10927, 0, wx.ALL, 5)

        self.m_staticText11027 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11027.Wrap(-1)

        bSizer13527.Add(self.m_staticText11027, 0, wx.ALL, 5)

        self.m_staticText11127 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11127.Wrap(-1)

        bSizer13527.Add(self.m_staticText11127, 0, wx.ALL, 5)

        bSizer1327.Add(bSizer13527, 1, wx.EXPAND, 5)

        bSizer13537 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10937 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10937.Wrap(-1)

        bSizer13537.Add(self.m_staticText10937, 0, wx.ALL, 5)

        self.m_staticText11037 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11037.Wrap(-1)

        bSizer13537.Add(self.m_staticText11037, 0, wx.ALL, 5)

        self.m_staticText11137 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11137.Wrap(-1)

        bSizer13537.Add(self.m_staticText11137, 0, wx.ALL, 5)

        bSizer1327.Add(bSizer13537, 1, wx.EXPAND, 5)

        bSizer13547 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10947 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10947.Wrap(-1)

        bSizer13547.Add(self.m_staticText10947, 0, wx.ALL, 5)

        self.m_staticText11047 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11047.Wrap(-1)

        bSizer13547.Add(self.m_staticText11047, 0, wx.ALL, 5)

        self.m_staticText11147 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11147.Wrap(-1)

        bSizer13547.Add(self.m_staticText11147, 0, wx.ALL, 5)

        bSizer1327.Add(bSizer13547, 1, wx.EXPAND, 5)

        bSizer13557 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10957 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10957.Wrap(-1)

        bSizer13557.Add(self.m_staticText10957, 0, wx.ALL, 5)

        self.m_staticText11057 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11057.Wrap(-1)

        bSizer13557.Add(self.m_staticText11057, 0, wx.ALL, 5)

        self.m_staticText11157 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11157.Wrap(-1)

        bSizer13557.Add(self.m_staticText11157, 0, wx.ALL, 5)

        bSizer1327.Add(bSizer13557, 1, wx.EXPAND, 5)

        bSizer13317 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10317 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10317.Wrap(-1)

        bSizer13317.Add(self.m_staticText10317, 0, wx.ALL, 5)

        self.m_staticText10417 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10417.Wrap(-1)

        bSizer13317.Add(self.m_staticText10417, 0, wx.ALL, 5)

        self.m_staticText10517 = wx.StaticText(sbSizer46.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10517.Wrap(-1)

        bSizer13317.Add(self.m_staticText10517, 0, wx.ALL, 5)

        bSizer1327.Add(bSizer13317, 1, wx.EXPAND, 5)

        bSizer1507.Add(bSizer1327, 1, wx.EXPAND, 5)

        sbSizer46.Add(bSizer1507, 1, wx.EXPAND, 5)

        sbSizer37.Add(sbSizer46, 1, wx.EXPAND, 5)

        sbSizer45 = wx.StaticBoxSizer(wx.StaticBox(sbSizer37.GetStaticBox(), wx.ID_ANY, u"編成9"), wx.VERTICAL)

        bSizer1508 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1368 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1368.Wrap(-1)

        bSizer1508.Add(self.m_staticText1368, 0, wx.ALL, 5)

        bSizer1328 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1339 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1039 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1039.Wrap(-1)

        bSizer1339.Add(self.m_staticText1039, 0, wx.ALL, 5)

        self.m_staticText1049 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1049.Wrap(-1)

        bSizer1339.Add(self.m_staticText1049, 0, wx.ALL, 5)

        self.m_staticText1059 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1059.Wrap(-1)

        bSizer1339.Add(self.m_staticText1059, 0, wx.ALL, 5)

        bSizer1328.Add(bSizer1339, 1, wx.EXPAND, 5)

        bSizer1348 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1068 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1068.Wrap(-1)

        bSizer1348.Add(self.m_staticText1068, 0, wx.ALL, 5)

        self.m_staticText1078 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1078.Wrap(-1)

        bSizer1348.Add(self.m_staticText1078, 0, wx.ALL, 5)

        self.m_staticText1088 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1088.Wrap(-1)

        bSizer1348.Add(self.m_staticText1088, 0, wx.ALL, 5)

        bSizer1328.Add(bSizer1348, 1, wx.EXPAND, 5)

        bSizer13512 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10912 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10912.Wrap(-1)

        bSizer13512.Add(self.m_staticText10912, 0, wx.ALL, 5)

        self.m_staticText11012 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11012.Wrap(-1)

        bSizer13512.Add(self.m_staticText11012, 0, wx.ALL, 5)

        self.m_staticText11112 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11112.Wrap(-1)

        bSizer13512.Add(self.m_staticText11112, 0, wx.ALL, 5)

        bSizer1328.Add(bSizer13512, 1, wx.EXPAND, 5)

        bSizer13528 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10928 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10928.Wrap(-1)

        bSizer13528.Add(self.m_staticText10928, 0, wx.ALL, 5)

        self.m_staticText11028 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11028.Wrap(-1)

        bSizer13528.Add(self.m_staticText11028, 0, wx.ALL, 5)

        self.m_staticText11128 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11128.Wrap(-1)

        bSizer13528.Add(self.m_staticText11128, 0, wx.ALL, 5)

        bSizer1328.Add(bSizer13528, 1, wx.EXPAND, 5)

        bSizer13538 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10938 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10938.Wrap(-1)

        bSizer13538.Add(self.m_staticText10938, 0, wx.ALL, 5)

        self.m_staticText11038 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11038.Wrap(-1)

        bSizer13538.Add(self.m_staticText11038, 0, wx.ALL, 5)

        self.m_staticText11138 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11138.Wrap(-1)

        bSizer13538.Add(self.m_staticText11138, 0, wx.ALL, 5)

        bSizer1328.Add(bSizer13538, 1, wx.EXPAND, 5)

        bSizer13548 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10948 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10948.Wrap(-1)

        bSizer13548.Add(self.m_staticText10948, 0, wx.ALL, 5)

        self.m_staticText11048 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11048.Wrap(-1)

        bSizer13548.Add(self.m_staticText11048, 0, wx.ALL, 5)

        self.m_staticText11148 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11148.Wrap(-1)

        bSizer13548.Add(self.m_staticText11148, 0, wx.ALL, 5)

        bSizer1328.Add(bSizer13548, 1, wx.EXPAND, 5)

        bSizer13558 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10958 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10958.Wrap(-1)

        bSizer13558.Add(self.m_staticText10958, 0, wx.ALL, 5)

        self.m_staticText11058 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11058.Wrap(-1)

        bSizer13558.Add(self.m_staticText11058, 0, wx.ALL, 5)

        self.m_staticText11158 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11158.Wrap(-1)

        bSizer13558.Add(self.m_staticText11158, 0, wx.ALL, 5)

        bSizer1328.Add(bSizer13558, 1, wx.EXPAND, 5)

        bSizer13318 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10318 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10318.Wrap(-1)

        bSizer13318.Add(self.m_staticText10318, 0, wx.ALL, 5)

        self.m_staticText10418 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10418.Wrap(-1)

        bSizer13318.Add(self.m_staticText10418, 0, wx.ALL, 5)

        self.m_staticText10518 = wx.StaticText(sbSizer45.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10518.Wrap(-1)

        bSizer13318.Add(self.m_staticText10518, 0, wx.ALL, 5)

        bSizer1328.Add(bSizer13318, 1, wx.EXPAND, 5)

        bSizer1508.Add(bSizer1328, 1, wx.EXPAND, 5)

        sbSizer45.Add(bSizer1508, 1, wx.EXPAND, 5)

        sbSizer37.Add(sbSizer45, 1, wx.EXPAND, 5)

        sbSizer39 = wx.StaticBoxSizer(wx.StaticBox(sbSizer37.GetStaticBox(), wx.ID_ANY, u"編成10"), wx.VERTICAL)

        bSizer1509 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1369 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1369.Wrap(-1)

        bSizer1509.Add(self.m_staticText1369, 0, wx.ALL, 5)

        bSizer1329 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer13310 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10310 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10310.Wrap(-1)

        bSizer13310.Add(self.m_staticText10310, 0, wx.ALL, 5)

        self.m_staticText10410 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10410.Wrap(-1)

        bSizer13310.Add(self.m_staticText10410, 0, wx.ALL, 5)

        self.m_staticText10510 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10510.Wrap(-1)

        bSizer13310.Add(self.m_staticText10510, 0, wx.ALL, 5)

        bSizer1329.Add(bSizer13310, 1, wx.EXPAND, 5)

        bSizer1349 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1069 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1069.Wrap(-1)

        bSizer1349.Add(self.m_staticText1069, 0, wx.ALL, 5)

        self.m_staticText1079 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1079.Wrap(-1)

        bSizer1349.Add(self.m_staticText1079, 0, wx.ALL, 5)

        self.m_staticText1089 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1089.Wrap(-1)

        bSizer1349.Add(self.m_staticText1089, 0, wx.ALL, 5)

        bSizer1329.Add(bSizer1349, 1, wx.EXPAND, 5)

        bSizer13513 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10913 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10913.Wrap(-1)

        bSizer13513.Add(self.m_staticText10913, 0, wx.ALL, 5)

        self.m_staticText11013 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11013.Wrap(-1)

        bSizer13513.Add(self.m_staticText11013, 0, wx.ALL, 5)

        self.m_staticText11113 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11113.Wrap(-1)

        bSizer13513.Add(self.m_staticText11113, 0, wx.ALL, 5)

        bSizer1329.Add(bSizer13513, 1, wx.EXPAND, 5)

        bSizer13529 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10929 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10929.Wrap(-1)

        bSizer13529.Add(self.m_staticText10929, 0, wx.ALL, 5)

        self.m_staticText11029 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11029.Wrap(-1)

        bSizer13529.Add(self.m_staticText11029, 0, wx.ALL, 5)

        self.m_staticText11129 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11129.Wrap(-1)

        bSizer13529.Add(self.m_staticText11129, 0, wx.ALL, 5)

        bSizer1329.Add(bSizer13529, 1, wx.EXPAND, 5)

        bSizer13539 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10939 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10939.Wrap(-1)

        bSizer13539.Add(self.m_staticText10939, 0, wx.ALL, 5)

        self.m_staticText11039 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11039.Wrap(-1)

        bSizer13539.Add(self.m_staticText11039, 0, wx.ALL, 5)

        self.m_staticText11139 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11139.Wrap(-1)

        bSizer13539.Add(self.m_staticText11139, 0, wx.ALL, 5)

        bSizer1329.Add(bSizer13539, 1, wx.EXPAND, 5)

        bSizer13549 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10949 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10949.Wrap(-1)

        bSizer13549.Add(self.m_staticText10949, 0, wx.ALL, 5)

        self.m_staticText11049 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11049.Wrap(-1)

        bSizer13549.Add(self.m_staticText11049, 0, wx.ALL, 5)

        self.m_staticText11149 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11149.Wrap(-1)

        bSizer13549.Add(self.m_staticText11149, 0, wx.ALL, 5)

        bSizer1329.Add(bSizer13549, 1, wx.EXPAND, 5)

        bSizer13559 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10959 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10959.Wrap(-1)

        bSizer13559.Add(self.m_staticText10959, 0, wx.ALL, 5)

        self.m_staticText11059 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11059.Wrap(-1)

        bSizer13559.Add(self.m_staticText11059, 0, wx.ALL, 5)

        self.m_staticText11159 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11159.Wrap(-1)

        bSizer13559.Add(self.m_staticText11159, 0, wx.ALL, 5)

        bSizer1329.Add(bSizer13559, 1, wx.EXPAND, 5)

        bSizer13319 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10319 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10319.Wrap(-1)

        bSizer13319.Add(self.m_staticText10319, 0, wx.ALL, 5)

        self.m_staticText10419 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10419.Wrap(-1)

        bSizer13319.Add(self.m_staticText10419, 0, wx.ALL, 5)

        self.m_staticText10519 = wx.StaticText(sbSizer39.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10519.Wrap(-1)

        bSizer13319.Add(self.m_staticText10519, 0, wx.ALL, 5)

        bSizer1329.Add(bSizer13319, 1, wx.EXPAND, 5)

        bSizer1509.Add(bSizer1329, 1, wx.EXPAND, 5)

        sbSizer39.Add(bSizer1509, 1, wx.EXPAND, 5)

        sbSizer37.Add(sbSizer39, 1, wx.EXPAND, 5)

        self.m_scrolledWindow1.SetSizer(sbSizer37)
        self.m_scrolledWindow1.Layout()
        sbSizer37.Fit(self.m_scrolledWindow1)
        base_box.Add(self.m_scrolledWindow1, 1, wx.EXPAND | wx.ALL, 5)

        bSizer130 = wx.BoxSizer(wx.VERTICAL)

        self.m_button40 = wx.Button(self, wx.ID_ANY, u"閉じる", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Bind(wx.EVT_BUTTON, self.close, self.m_button40)
        bSizer130.Add(self.m_button40, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        base_box.Add(bSizer130, 0, wx.EXPAND, 5)

        self.SetSizer(base_box)
        self.Layout()

        self.Centre(wx.BOTH)

    def close(self, event):
        self.Close(True)
        return

    def __del__(self):
        pass
