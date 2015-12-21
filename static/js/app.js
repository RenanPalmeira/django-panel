var apps = null; 

function ajax(url, callback) {
	var data = { url: url, success: callback};
	Backbone.ajax(data);
}

$('.navbar-text .fa-cog').click(function(){
	var gear = $('.navbar-text .gear');
	if(gear.css('display')=='none')
		gear.css('display', 'block');
	else
		gear.css('display', 'none');
});

$(window).keydown(function(e) {
	if (e.which == 27) {
		if(Backbone.history.fragment!='') {
			window.location='#';
		}
		$('.navbar-text .gear').css('display', 'none');	
	}
});

(function() {
	$(document).bind("ajaxSend", function(){
		NProgress.start();
	}).bind("ajaxComplete", function(){
		NProgress.done();
	});
	var _sync = Backbone.sync;
	Backbone.sync = function(method, model, options) {
		options.beforeSend = function(xhr) {
			var token = $('meta[name="csrf-token"]').attr('content');
			xhr.setRequestHeader('X-CSRFToken', token);
		};
		return _sync(method, model, options);
	};
})();

var board = {
	items: [],
	item: function(app) {
		var menu = $('ul.menu');
		var html = '';
		html += '<li id="'+app+'"><a href=\"javascript: void(0);\"><i class="fa fa-angle-right"></i><span>';
		html += app;
		html += '</span></a></li>';
		menu.append(html);
	},
	init: function() {
		if(this.items) {
			var self = this;
			_.each(this.items, function(item) {
				self.item(item);
			})
		}

		if(Backbone.history.fragment.split('/').length==2) {
			var method = Backbone.history.fragment.split('/');
			method = $('ul.menu #'+method[1]);
			if(_.isObject(method)) {
				var li = $('ul.menu li').each(function(obj) {
					$(this).removeClass('active');
				})
				method.addClass('active');
			}
		}
	}
}