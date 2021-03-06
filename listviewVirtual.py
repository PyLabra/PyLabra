import wx

class ListViewVirtual(wx.ListCtrl):
    def __init__(self, parent, pos, size,array):
        wx.ListCtrl.__init__(self, parent,-1,pos, size,style=wx.LC_REPORT|wx.LC_VIRTUAL|wx.LC_VRULES|wx.LC_HRULES|wx.LC_SINGLE_SEL)

        self.InsertColumn(0,"No")
        self.InsertColumn(1,"Palabra")
        self.InsertColumn(2,"Genero")
        self.InsertColumn(3,"Plural")
        self.InsertColumn(4,"Traduccion")
        self.InsertColumn(5,"Tipo")        
        self.InsertColumn(6,"Tema")
        self.InsertColumn(7,"Notas")
        self.SetColumnWidth(0,30)
        for i in range(1,8): self.SetColumnWidth(i,65)#wx.LIST_AUTOSIZE)        
        
        self.OnRellenar(array)
    
    def OnRellenar(self, array):
        self.array = array                  # Guardo el array para su posterior uso en otros metodos.
        self.SetItemCount(len(self.array))  # SetitemCount llamara a OnGetItemText las interaciones necesarias.
    
    def OnGetItemText(self, item, col):       # Sobreescritura del metodo virtual original (polimorfismo).
        return "%s" % (self.array[item][col]) # %s convierte a string como en el scanf de C.