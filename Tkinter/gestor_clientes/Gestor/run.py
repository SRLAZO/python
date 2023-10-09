# -*- coding:utf-8 -*-
import res.ui as ui
import sys
import os
import res.menu


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        res.menu.iniciar()
    else:
        app = ui.MainWindow()
        app.mainloop()