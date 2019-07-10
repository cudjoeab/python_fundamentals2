def wrap_text(text, symbols): 
    return symbols + text + symbols

text = 'new message'


step1 = wrap_text(text, '###')   # ###newmessage###
step2 = wrap_text(step1, '===') 
step3 = wrap_text(step2, "---")
print(step3) 

#approach this in steps and save the variable as you add parts