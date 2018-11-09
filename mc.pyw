#! python3
 
# Usage :
#   python3 mc.pyw ls : lists all the keys 
#   python3 mc.pyw save <keyword> : saves the current thing in clipboard with the following key
#   python3 mc.pyw del <keyword> : deletes the key from the shelve 
#   python3 mc.pyw key <keyword> : copies the keyword in the clipboardS

import shelve, sys, pyperclip, pprint 

mc = shelve.open('multiclipboard_data')

if len(sys.argv) == 3 :
    if sys.argv[1].lower() == 'save' :
        mc[str(sys.argv[2])] = pyperclip.paste() 
    elif sys.argv[1].lower() == 'del' :
        del mc[str(sys.argv[2])]
    elif sys.argv[1].lower() == 'key':
        pyperclip.copy(mc[str(sys.argv[2])])

elif len(sys.argv) == 2  and sys.argv[1].lower() == 'ls' :
        print(list(mc.keys()))
        
else :
    print("command not found" )
