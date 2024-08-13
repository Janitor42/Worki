from threading import Thread
import view
import controller
import model
import gui

Thread(target=gui.create_tk).start()
import wrap_py

wrap_py.app.start()
