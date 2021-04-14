#https://github.com/jupyter-widgets/ipywidgets/issues/2487#issuecomment-510721436
import ipywidgets as widgets
from IPython.display import clear_output
import random

def create_multipleChoice_widget(description, options, correct_answer, msg=None):
    if correct_answer not in options:
        options.append(correct_answer)
    
    # Randomise order
    options = random.sample(options, len(options))
    
    correct_answer_index = options.index(correct_answer)

    radio_options = [(words, i) for i, words in enumerate(options)]
    alternativ = widgets.RadioButtons(
        options = radio_options,
        description = '',
        disabled = False
    )
    
    description_out = widgets.Output()
    with description_out:
        print(description)
        
    feedback_out = widgets.Output()

    def check_selection(b):
        a = int(alternativ.value)
        if a==correct_answer_index:
            s = '\x1b[6;30;42m' + "Correct." + '\x1b[0m' +"\n" #green color
            if msg and 'correct' in msg:
                s = f"{s}\n{msg['correct']}"
                
        else:
            s = '\x1b[5;30;41m' + "Incorrect. " + '\x1b[0m' +"\n" #red color
            if msg and 'incorrect' in msg:
                s = f"{s}\n{msg['incorrect']}"
        with feedback_out:
            clear_output()
            print(s)
        return
    
    check = widgets.Button(description="submit")
    check.on_click(check_selection)
    
    
    return widgets.VBox([description_out, alternativ, check, feedback_out])

Q1 = create_multipleChoice_widget('What happens to the robot when you turn the motors on at a specified speed',
                                  ['The robot instantaneously travels at that speed?',
                                   'Is it coffee time yet?'],
                                  'The robot accelerates up to that speed', {'incorrect':'If the robot has non-zero mass, it cannot accelerate at an infinite rate: it will take take to accelerate up to the desired speed.'})