import PySimpleGUI as sg

sg.theme("DarkGreen4")
window = sg.Window(title="Profile", 
                    layout=[[sg.Text("NPM    : 2210010236")],
                            [sg.Text("Nama   : Gusti Randa")],
                            [sg.Text("Kelas  : 5O Regluer Banjarmasin")],
                            [sg.Text("Matkul :Pemrograman Visual 3")]
                            ], size=(400,200))
window()
window.close()