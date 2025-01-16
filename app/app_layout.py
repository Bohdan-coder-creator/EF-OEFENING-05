import FreeSimpleGUI as sg

class AppLayout:
    def create_layout(self):
        image_size = (200, 200)
        padding = (30, 30)

        logo_and_title = sg.Column(
            [
                [
                    sg.Image(source='logo/logo.png', pad=(0, 0)), 
                    sg.Text(
                        text='SLOTMACHINE',
                        font=('Calibri', 24, 'bold')
                    )
                ]
            ],
            justification='center',
            element_justification='center',
            expand_x=True
        )

        separator = [
            sg.HorizontalSeparator()
        ]

        image_row = [
            sg.Image(key="-IMG-0-", size=image_size, pad=padding),
            sg.Image(key="-IMG-1-", size=image_size, pad=padding),
            sg.Image(key="-IMG-2-", size=image_size, pad=padding),
        ]

        stats_and_button_row = [
            sg.Text("Punten:"),
            sg.InputText(key="-INP-PUNTEN-", size=(5, 1), readonly=True),
            sg.Text("Score:"),
            sg.InputText(key="-INP-SCORE-", size=(5, 1), readonly=True),
            sg.Text("Beurten:"),
            sg.InputText(key="-INP-BEURTEN-", size=(5, 1), readonly=True),
            sg.Push(),
            sg.Button("Spin", key="-BTN-SPIN-", size=(12, 2), button_color=("white", "green"))
        ]

        layout = [
            [logo_and_title],
            image_row,
            separator,
            stats_and_button_row
        ]
        return layout
