import FreeSimpleGUI as sg
from convert_function import convert

sg.theme("Black")
label1 = sg.Text("Enter feet: ")
input1 = sg.Input(key='feet')

label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key='inches')

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")
output_label = sg.Text(key='output', text_color='white')

window = sg.Window("Converter",
                   layout=[[label1, input1],
                           [label2, input2],
                           [convert_button, exit_button, output_label]])
while True:
    event, values = window.read()
    # ✅ Exit if window is closed
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Convert":
        try:
            metres= convert(float(values['feet']), float(values['inches']))
            window['output'].update(value=f"{metres} m")
        except ValueError:
            window['output'].update(value="Please enter the valid number")
    if event == "Exit":
        break

window.close()
