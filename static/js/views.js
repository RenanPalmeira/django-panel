var BoardView = Backbone.View.extend({
	el: $('.board'),
	initialize: function(action, method) {
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

var PanelView = Backbone.View.extend({
	el: $('.board #panel'),
	initialize: function(action, method) {
		var self = this;
		var url = language+"/app/"+action+"/"+method+"/";

		var ajax = Backbone.ajax({
			url: url
		});
		ajax.success(function(context) {
			self.$el.html("context");
		});
	}
});