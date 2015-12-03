var language = navigator.language=='pt-BR' ? 'pt' : 'en';
var api_root = '/'+language+'/api/';

var ApplicationBoardModel = Backbone.Model.extend({
	urlRoot: function() {
		return api_root+this.get('base')+'/';
	},
	initialize : function(options) {
		if(options && typeof options.id === 'number')
			this.url = this.url()+"/?loadtype=results";
		else	
			this.url = this.url()+"?loadtype=results";
	}
});


var SocialModel = Backbone.Model.extend({
	urlRoot: api_root+'social/'
});