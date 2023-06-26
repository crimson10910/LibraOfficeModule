import uno
from com.sun.star.awt import XActionListener, XMenuListener

class MenuListener(uno.Any, XMenuListener):
    def init(self, ctx):
        self.ctx = ctx

    def itemSelected(self, action_event):
        pass

    def itemHighlighted(self, action_event):
        pass

    def itemActivated(self, action_event):
        pass

    def itemDeactivated(self, action_event):
        pass

class AddMenuExtension:
    def init(self, ctx):
        self.ctx = ctx
        self.menu_listener = None

    def createMenu(self):
        desktop = self.ctx.getDesktop()
        current_frame = desktop.getCurrentFrame()
        if current_frame:
            window = current_frame.getContainerWindow()
            toolkit = window.getToolkit()
            menu_bar = window.getMenuBar()
            if menu_bar:
                menu = menu_bar.getMenu(3)  # Индекс меню "Tools"
                if menu:
                    submenu = toolkit.createPopupMenu(window, None)
                    submenu.addMenuListener(self.menu_listener)
                    submenu.insertItem(0, "Check...", "", 0, 0)
                    menu.insertItem(0, "Libra", submenu, ())
                    menu.enableItem(0, True)

    def initialize(self, context):
        self.ctx = context
        self.menu_listener = MenuListener(self.ctx)

        # Добавление пункта меню
        self.createMenu()

g_exportedScripts = AddMenuExtension,