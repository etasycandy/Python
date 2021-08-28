"""

Script demo easy frame show "Hello Student"
"""
from breezypythongui import EasyFrame


class LabelDemo(EasyFrame):
    """ class label demo """
    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text="Hello Student", row=0, column=0)
        self.addLabel(text="Hello Student", row=1, column=1)
        self.addLabel(text="Hello Student", row=3, column=2)


if __name__ == '__main__':
    window = LabelDemo()
    window.mainloop()


