"""
Author: Tran Dinh Hoang
Date: 30/08/2021
Program: Exercise_01_page_176.py
Problem:

    1.  Draw a structure chart for one of the solutions to the programming projects of Chapters 4 and 5.
        The program should include at least two function definitions other than the main function.

* * * * * ============================================================================================= * * * * *

Solution:
    Result:

"""

from breezypythongui import EasyFrame

from tkinter import PhotoImage
from tkinter.font import Font


class ImageDemo(EasyFrame):
    def __init__(self):
        """Set up the window and the widgets"""

        EasyFrame.__init__(self, title="Image Demo", width=720, height=560)
        self.setResizable(False)
        imageLabel = self.addLabel(text="", row=0, column=0, sticky="WNES")
        textLabel = self.addLabel(text="Project_05_page132.py", row=1, column=0, sticky="WNES")


        # load image
        self.image = PhotoImage(file="../fileTest/Ex01_page176.png")
        imageLabel['image'] = self.image
        font = Font(family='VNI-Bodon-Poster', size=15, slant="italic")
        textLabel['font'] = font


if __name__ == '__main__':
    window = ImageDemo()
    window.mainloop()
