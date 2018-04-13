$(function() {
    function custombackgroundViewModel(parameters) {
        var self = this;
		
		self.settings = parameters[0];
		
		self.background_url = ko.observable();
		self.icon_url = ko.observable();
		self.fillMethod = ko.observable();
		self.fillOptions = ko.observableArray([{
						name : 'auto',
						value : 'auto'
					}, {
						name : 'cover',
						value : 'cover'
					}, {
						name : 'contain',
						value : 'contain'
					}
				]);
		self.position = ko.observable();
		
		self.onBeforeBinding = function() {
            self.background_url(self.settings.settings.plugins.custombackground.background_url());
            self.icon_url(self.settings.settings.plugins.custombackground.icon_url());
			self.fillMethod(self.settings.settings.plugins.custombackground.fillMethod());
			self.position(self.settings.settings.plugins.custombackground.position());
        }
		
		self.onAfterBinding = function() {
			$("#temperature-graph").css({"background-image":"url('" + window.location.pathname.replace(/\/$/, '') + self.settings.settings.plugins.custombackground.background_url() + "')","background-size":self.settings.settings.plugins.custombackground.fillMethod(),"background-position":self.settings.settings.plugins.custombackground.position()});
			$("#navbar .navbar-inner .brand span").css({"background-image":"url('" + window.location.pathname.replace(/\/$/, '') + self.settings.settings.plugins.custombackground.icon_url() + "')"});
		}
		
		self.onEventSettingsUpdated = function (payload) {
            self.background_url(self.settings.settings.plugins.custombackground.background_url());
            self.icon_url(self.settings.settings.plugins.custombackground.icon_url());
			$("#temperature-graph").css({"background-image":"url('" + window.location.pathname.replace(/\/$/, '') + self.settings.settings.plugins.custombackground.background_url() + "')","background-size":self.settings.settings.plugins.custombackground.fillMethod(),"background-position":self.settings.settings.plugins.custombackground.position()});
			$("#navbar .navbar-inner .brand span").css({"background-image":"url('" + window.location.pathname.replace(/\/$/, '') + self.settings.settings.plugins.custombackground.icon_url() + "')"});
        }
		
		self.onDataUpdaterPluginMessage = function(plugin, data) {
            if (plugin != "custombackground") {
                return;
            }
			
			if(data.type == "reload") {
				window.location.reload(true);
			}
		}
		
		self.resetBackgrounds = function(){
			self.settings.settings.plugins.custombackground.background_url('/static/img/graph-background.png');
			self.settings.settings.plugins.custombackground.icon_url('/static/img/tentacle-20x20.png');
			self.settings.settings.plugins.custombackground.fillMethod('auto');
			self.settings.settings.plugins.custombackground.position('center center');
			self.settings.saveData();
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
        ["#settings_plugin_custombackground_form"]
    ]);
});
