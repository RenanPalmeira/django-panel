var BoardView = Backbone.View.extend({
	el: $('.board'),
	template: _.template($('#board_template').html()),
	initialize: function(options) {
		this.model = new ApplicationBoardModel();
		this.model.fetch(options);
		this.listenTo(this.model, "change", this.render);
	},
	render: function(){
		this.$el.html(this.template(this.model.get(0)));
		$('.board').css('visibility', 'visible');
		$('#loading').css('visibility', 'hidden');
		return this;
	}
});