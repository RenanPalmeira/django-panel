var BoardView = Backbone.View.extend({
	el: $('.board'),
	initialize: function(action) {
		var self = this;
		var url = language+"/app/"+action+"/";
		var ajax = Backbone.ajax({
			url: url
		});
		ajax.success(function(context) {
			self.$el.html(context);
		});
	}
});

var AccountView = Backbone.View.extend({
	el: $('#board-container'),
	initialize: function(action) {
		this.model = new AccountModel();
		this.model.fetch();
		this.listenTo(this.model, "change", this.render);
	},
	render: function(){
		var data = this.model.get('name');
		return this;
	}
});