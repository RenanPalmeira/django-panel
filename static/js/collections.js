var ApplicationBoardCollection = Backbone.Collection.extend({
	model: ApplicationBoardModel,
	url: '/'+language+'/api/apps/',
	initialize : function() {
		this.url = this.url()+"?loadtype=results";
	}
});