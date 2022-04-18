import PySimpleGUI as sg

def create_window(theme):
    # menu
    menu_layout = [
        ['File', ['Change Color',  ['dark', 'darkred', 'darkblue', 'random'], 'Exit']]
    ]
        
    # variables
    button_size = (6, 3)
    # design
    sg.theme(theme)
    sg.set_options(font = 'Calibri 14', button_element_size = button_size)

    layout = [
        [sg.Menu(menu_layout)],
        [sg.Text('Calculator', font = "Franklin 26", justification = 'center', expand_x = True, pad = (10, 20), key = '-TEXT-')],
        [sg.Button('Clear', expand_x = True), sg.Button('Enter', expand_x = True)],
        [sg.Button(7, size = button_size), sg.Button(8, size = button_size), sg.Button(9, size = button_size), sg.Button('*', size = button_size)],
        [sg.Button(4, size = button_size), sg.Button(5, size = button_size), sg.Button(6, size = button_size), sg.Button('/', size = button_size)],
        [sg.Button(1, size = button_size), sg.Button(2, size = button_size), sg.Button(3, size = button_size), sg.Button('-', size = button_size)],
        [sg.Button(0, expand_x = True), sg.Button('.', size = button_size), sg.Button('+', size = button_size)]
    ]

    return sg.Window('Calculator', layout)

window = create_window('darkred')

current_num = []
operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['-TEXT-'].update(num_string)
        
    if event in ['+', '-', '*', '/']:
        operation.append(''.join(current_num))
        current_num = []
        operation.append(event)
        window['-TEXT-'].update('')
        
    if event in ['Enter']:
        operation.append(''.join(current_num))
        result = eval(' '.join(operation))
        window['-TEXT-'].update(result)
        operation = []
        
    if event in ['Clear']:
        current_num = []
        operation = []
        window['-TEXT-'].update('')
        
    if event == 'dark' or event == 'darkred' or event == 'darkblue' or event == 'random':
        window.close()
        window = create_window(event)
    
    if event == 'Exit':
        window.close()
        
window.close()