'''
This is the main file that runs the CRM application.
'''
from tkinter import Tk
from crm_app import CRMApp
from metrics import Metrics
if __name__ == "__main__":
    root = Tk()
    app = CRMApp(root)
    metrics = Metrics()
    metrics.display_metrics()
    root.mainloop()