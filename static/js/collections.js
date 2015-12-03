var ApplicationBoardCollection = Backbone.Collection.extend({
	model: ApplicationBoardModel,
	url: '/'+language+'/api/app/',
	initialize : function() {
		this.url = this.url()+"?loadtype=results";
	}
});

var SocialCollection = Backbone.Collection.extend({
	model: SocialModel,
	url: api_root+'social/',
	initialize : function() {
		this.url = this.url +"?loadtype=results";
	}
});