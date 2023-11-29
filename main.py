import PySimpleGUI as sg
from zip import create_zip


label1 = sg.Text("Add files to compress: ")
input1 = sg.Input()
button1 = sg.FilesBrowse("Choose", key='files')

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
button2 = sg.FolderBrowse("Choose", key='folders')

button3 = sg.Button("Compress")

output = sg.Text(key="output")

window = sg.Window("File Compressor", layout=[[label1, input1, button1],
                                              [label2, input2, button2 ],
                                              [button3,  output]])

while True:
    events, values = window.read()
    print(events, values)
    if events == sg.WIN_CLOSED:
        break
    filepaths = values['files'].split(';')
    folders = values['folders']
    create_zip(filepaths, folders)
    window["output"].update(value="compressed successfully ")

window.close()
