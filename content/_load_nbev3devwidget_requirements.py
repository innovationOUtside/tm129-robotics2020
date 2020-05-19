from nbev3devsim import ev3devsim_nb as eds
from IPython.display import display

#https://github.com/AaronWatters/jp_doodle/blob/master/notebooks/misc/JQueryUI%20dialogextend%20plugin%20demo.ipynb
#Load and initialise the jquery.dialogextend package
import jp_proxy_widget
cdn_url = "https://cdn.jsdelivr.net/npm/binary-com-jquery-dialogextended@1.0.0/jquery.dialogextend.js"
cdn_url = eds.get_file_path('js/jquery.dialogextend.js')
module_id = "dialogExtend"


# Load the module using a widget (any widget -- the module loads to the global jQuery object).
loader = jp_proxy_widget.JSProxyWidget()

# Configure the module to be loaded.
loader.require_js(module_id, cdn_url)

# Load the module
loader.js_init("""
    element.requirejs([module_identifier], function(module_value) {
        //element.html("loaded " + module_identifier + " : " + module_value);
    });
""", module_identifier=module_id)

display(loader)

# I think we need to wait for this to load
# else we may get an error in next cell from dialogExtend not being available?