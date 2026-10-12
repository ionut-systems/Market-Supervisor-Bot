import tkinter as tk
import threading
from gui import ApplicationInterface
from moteur import executer_pipeline

def declencher_scan(callback_log, callback_fin):
    """Lance le moteur dans un thread séparé pour garder l'interface fluide"""
    thread = threading.Thread(target=executer_pipeline, args=(callback_log, callback_fin), daemon=True)
    thread.start()

if __name__ == "__main__":
    racine = tk.Tk()
    app = ApplicationInterface(racine, declencher_scan)
    racine.mainloop() 