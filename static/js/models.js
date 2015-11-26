var language = navigator.language=='pt-BR' ? 'pt' : 'en';

var ApplicationBoardModel = Backbone.Model.extend({
	urlRoot: '/'+language+'/api/app/',
	initialize : function() {
		this.url = this.url()+"?loadtype=results";
	}
});