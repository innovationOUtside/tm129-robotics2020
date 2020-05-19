# Run this cell to set up the robot simulator environment

#Load the nbtutor extension
#%load_ext nbtutor

#Reset the notebook style
from IPython.core.display import display, HTML

display(HTML("<style>#notebook-container { width:50%; float:left !important;}</style>"))


#Launch the simulator
from nbev3devsim import ev3devsim_nb as eds
#%load_ext nbev3devsim

roboSim = eds.Ev3DevWidget()

roboSim.set_element("response", '')
             
display(roboSim)
roboSim.element.dialog()


roboSim.js_init("""
element.dialog({ "title" : "Robot Simulator" }).dialogExtend({
        "maximizable" : true,
        "dblclick" : "maximize",
        "icons" : { "maximize" : "ui-icon-arrow-4-diag" }});
""")

