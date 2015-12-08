var BoardView = Backbone.View.extend({
	el: $('.board'),
	template: _.template($('#board_template').html()),
	initialize: function(action) {
		this.model = new BoardModel({base:action});
		this.model.fetch();
		this.listenTo(this.model, "change", this.render);
	},
	render: function(){
		var data = this.model.toJSON();
		this.$el.html(this.template(data));
		return this;
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