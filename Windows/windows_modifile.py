"""

Example Windows and Windows Components (title, width, height, background color, ..ect)

"""
from breezypythongui import EasyFrame


class LayoutDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Label Demo", width=200, height=200, background='green')
        self.addLabel(text="(0, 0)", row=0, column=0, sticky="NSEW")
        self.addLabel(text="(0, 1)", row=0, column=1, sticky="NSEW")
        self.addLabel(text="(1, 0)", row=1, column=0, sticky="NSEW")
        self.addLabel(text="(1, 1)", row=1, column=1, sticky="NSEW")


if __name__ == '__main__':
    windows = LayoutDemo()
    windows.mainloop()


