import PySimpleGUI as sg
susunan=[[sg.Text("UNISKA MAB", font=("helvetica", 24))],
          [sg.Text("BANJARMASIN", font=("courier", 18))]]
window = sg.Window(title="New Icon", 
                    layout=susunan,
                    element_justification="center",
                    icon="Letter R.ico",
                    resizable=True,
                    size=(430,200))

window()
window.close()