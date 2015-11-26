var language = navigator.language=='pt-BR' ? 'pt' : 'en';

var ApplicationBoardModel = Backbone.Model.extend({
	urlRoot: '/'+language+'/api/app/',
	initialize : function(options) {

		if(options && typeof options.id === 'number')
			this.url = this.url()+"/?loadtype=results";
		else	
			this.url = this.url()+"?loadtype=results";
	}
});