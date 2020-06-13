#! python3

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
