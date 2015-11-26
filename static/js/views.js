var BoardView = Backbone.View.extend({
	el: $('.board'),
	template: _.template($('#board_template').html()),
	initialize: function(options) {
		if(options.step)
			this.step = options.step;
		this.model = new ApplicationBoardModel();
		this.model.fetch(options);
		this.listenTo(this.model, "change", this.render);
	},
	render: function(){
		var data = this.model.get(0);
		data.step = null;
		if(this.step)
			data.step = this.step;
		
		this.$el.html(this.template(data));
		$('.board').css('visibility', 'visible');
		$('#loading').css('visibility', 'hidden');
		return this;
	}
});