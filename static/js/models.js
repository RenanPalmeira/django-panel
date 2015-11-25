var language = navigator.language=='pt-BR' ? 'pt' : 'en';

var ApplicationBoardModel = Backbone.Model.extend({
	urlRoot: '/'+language+'/api/apps/',
	initialize : function() {
		this.url = this.url()+"?loadtype=results";
	}
});