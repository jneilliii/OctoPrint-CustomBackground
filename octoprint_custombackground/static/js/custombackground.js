$(function() {
    function custombackgroundViewModel(parameters) {
        var self = this;
		
		self.settings = parameters[0];
		
		self.background_url = ko.observable();
		
		self.onBeforeBinding = function() {
            self.background_url(self.settings.settings.plugins.custombackground.background_url());
        }
		
		self.onAfterBinding = function() {
			$("#temperature-graph").css("background","url(" + self.settings.settings.plugins.custombackground.background_url() + ")");
		}
		
		self.onEventSettingsUpdated = function (payload) {            
            self.background_url = self.settings.settings.plugins.custombackground.background_url();
        }
    }

    // This is how our plugin registers itself with the application, by adding some configuration
    // information to the global variable OCTOPRINT_VIEWMODELS
    ADDITIONAL_VIEWMODELS.push([
        // This is the constructor to call for instantiating the plugin
        custombackgroundViewModel,

        // This is a list of dependencies to inject into the plugin, the order which you request
        // here is the order in which the dependencies will be injected into your view model upon
        // instantiation via the parameters argument
        ["settingsViewModel"],

        // Finally, this is the list of selectors for all elements we want this view model to be bound to.
        []
    ]);
});