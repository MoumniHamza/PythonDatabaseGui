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
                    self.pName = wx.TextCtrl(panel , size =(150 , -1) , pos =(130 ,70))
                    self.pGen = wx.TextCtrl(panel , size =(150 , -1) , pos =(130 ,110))
                    self.pAge = wx.SpinCtrl(panel , value = '0', size =(70 , 25) , pos =(130 ,150))
                    self.pOcc = wx.TextCtrl(panel , size =(150 , -1) , pos =(130 ,190))
                    save = wx.Button(panel, label = ' Add character ' , pos = (100,300))
                    save.Bind(wx.EVT_BUTTON, self.addPerson)
                    self.listCtrl = wx.ListCtrl(panel, size = (400,400) , pos =(350,40), style = wx.LC_REPORT | wx.BORDER_SUNKEN)
                    self.listCtrl.InsertColumn(0,"ID")
                    self.listCtrl.InsertColumn(1,"NAME")
                    self.listCtrl.InsertColumn(2,"GENDER")
                    self.listCtrl.InsertColumn(3,"AGE")
                    self.listCtrl.InsertColumn(4,"OCCUPATION")
                    self.fillListCtrl()
                    delete = wx.Button(panel , label = "Delete" , pos =( 640 ,450))
                    delete.Bind(wx.EVT_BUTTON,self.onDelete)
                    self.listCtrl.Bind(wx.EVT_LIST_ITEM_SELECTED , self.onSelect)

            
             
             def addPerson(self, event):
                 name = self.pName.GetValue()
                 gen = self.pGen.GetValue()
                 age = self.pAge.GetValue()
                 occ = self.pOcc.GetValue()
                 if (name == '') or (gen == '') or ( age == '') or ( occ == ''):
                     dialog = wx.MessageDialog( None, ' One or more fields are missing. Enter a value in each text box. ', 'Missing Details' , wx.OK|wx.CANCEL)
                     dialog.ShowModal()
                     dialog.Destroy()
                     return False
                 print name
                 print gen
                 print age
                 print occ
                 Database.newPerson(name,gen,age,occ)
                 print Database.checkPerson()
                 self.pName.Clear()
                 self.pAge.SetValue(0)
                 self.pGen.Clear()
                 self.pOcc.Clear()
                 self.fillListCtrl()

             def fillListCtrl(self):
                 data = Database.checkPerson()
                 self.listCtrl.DeleteAllItems()
                 for row in data:
                     self.listCtrl.Append(row)

             def Exit(self , event):
                 self.Destroy()

             def onDelete(self, event):
                  Database.deletePerson(self.selectedId)
                  self.fillListCtrl()

             def onSelect(self, event):
                 self.selectedId = event.GetText()
            
app = wx.App()
frame = Frame()
frame.Show()
app.MainLoop()
