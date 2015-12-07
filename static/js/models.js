var language = navigator.language=='pt-BR' ? 'pt' : 'en';
var api_root = '/'+language+'/api/';

var ApplicationModel = Backbone.Model.extend({
	urlRoot: api_root+'application/',
	initialize: function() {
		this.url = this.url()+'/';
	}
});

var BoardModel = Backbone.Model.extend({
	urlRoot: function() {
		return api_root+this.get('base')+'/';
	},
	parse: function(resp, xhr) {
		this.count = resp.count;
		return resp.results;
	}
});