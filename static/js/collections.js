var ApplicationBoardCollection = Backbone.Collection.extend({
	model: ApplicationBoardModel,
	url: '/'+language+'/api/app/',
	initialize : function() {
		this.url = this.url()+"?loadtype=results";
	}
});