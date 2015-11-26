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