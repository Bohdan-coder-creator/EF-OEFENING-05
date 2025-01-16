import FreeSimpleGUI as sg
from app.app_layout import AppLayout
from entiteit.slotmachine import SlotMachine
from bin.imagetkhelper import ImageTKHelper

class App:
    def __init__(self):
        self.layout = AppLayout()
        self.slot_machine = SlotMachine()

    def run(self):
        window = sg.Window("Gokautomaat", self.layout.create_layout(), finalize=True)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                break
            elif event == "-BTN-SPIN-":
                self.slot_machine.spin()
                images = self.slot_machine.afbeeldingen()
                window["-IMG-0-"].update(data=ImageTKHelper.schaal(images[0], grootte=(200,200)))
                window["-IMG-1-"].update(data=ImageTKHelper.schaal(images[1], grootte=(200,200)))
                window["-IMG-2-"].update(data=ImageTKHelper.schaal(images[2], grootte=(200,200)))
                window["-INP-PUNTEN-"].update(value=self.slot_machine.punten())
                window["-INP-SCORE-"].update(value=self.slot_machine.score())
                window["-INP-BEURTEN-"].update(value=self.slot_machine.aantal())

        window.close()