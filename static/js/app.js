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
	var _sync = Backbone.sync;
	Backbone.sync = function(method, model, options) {
		options.beforeSend = function(xhr) {
			var token = $('meta[name="csrf-token"]').attr('content');
			xhr.setRequestHeader('X-CSRFToken', token);
		};
		return _sync(method, model, options);
	};
	var api = Backbone.ajax({
		url: api_root
	});
	api.success(function(context){
		apps = _.keys(context);
	});	
})();