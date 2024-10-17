import PySimpleGUI as sg

sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile", 
                    layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                                    font=("Arial", 25, "italic", "bold", "underline"))],
                            [sg.Text("NPM    : 2210010236")],
                            [sg.Text("Nama   : Gusti Randa")],
                            [sg.Text("Kelas  : 5O Regluer Banjarmasin")],
                            ], 
                        size=(510,200), 
                        font=("Times", 18))
window()
window.close()