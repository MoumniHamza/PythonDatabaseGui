import wx, Database
class Frame(wx.Frame):
             def __init__(self):
                    wx.Frame.__init__(self, None, title ='hey world', size = (800, 600))
                    panel = wx.Panel(self)
                    menuBar = wx.MenuBar()
                    fileMenu = wx.Menu()
                    fileExit= fileMenu.Append(wx.NewId(), 'Exit')
                    menuBar.Append(fileMenu , "File")
                    self.SetMenuBar(menuBar)
                    self.Bind(wx.EVT_MENU, self.Exit , fileExit)
                    self.CreateStatusBar()
                    wx.StaticBox(panel , label = 'Add a character' , pos = (20, 40) , size = (280,190))
                    wx.StaticText(panel, label = 'Name:' , pos = (30,70))
                    wx.StaticText(panel, label = 'Gender:' , pos = (30,110))
                    wx.StaticText(panel, label = 'Age:' , pos = (30,150))
                    wx.StaticText(panel, label = 'Occupation:' , pos = (30,190))
                    wx.TextCtrl(panel , size =(150 , -1) , pos =(130 ,70))
                    wx.TextCtrl(panel , size =(150 , -1) , pos =(130 ,110))
                    wx.TextCtrl(panel , size =(150 , -1) , pos =(130 ,150))
                    wx.TextCtrl(panel , size =(150 , -1) , pos =(130 ,190))
             def Exit(self , event):
                 self.Destroy()

app = wx.App()
frame = Frame()
frame.Show()
app.MainLoop()
