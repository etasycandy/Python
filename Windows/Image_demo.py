"""
Display images

"""
from breezypythongui import EasyFrame

from tkinter import PhotoImage
from tkinter.font import Font


class ImageDemo(EasyFrame):
    """ Display an image and a caption """

    def __init__(self):
        """Set up the window and the widgets"""

        EasyFrame.__init__(self, title="Image Demo", width=1000, height=65)
        self.setResizable(False)
        imageLabel = self.addLabel(text="", row=0, column=0, sticky="WNES")
        textLabel = self.addLabel(text="EtasyCandy", row=1, column=0, sticky="WNES")


        # load image
        self.image = PhotoImage(file = "1.2.png")
        imageLabel['image'] = self.image
        font = Font(family='VNI-Bodon-Poster', size=25, slant="italic")
        textLabel['font'] = font
        textLabel['foreground'] = "red"


if __name__ == '__main__':
    window = ImageDemo()
    window.mainloop()


