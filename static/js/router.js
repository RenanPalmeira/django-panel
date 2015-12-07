var fadeOut = function() {
	$('#loading').css('visibility', 'visible');
	$('#loading').fadeOut();
	$('#loading').css('visibility', 'hidden');		
};

var Router = Backbone.Router.extend({
	routes: {
		':action': 'desk',
		':action/:method': 'desk',
		'*default': 'defaultRoute'
	}, 
	defaultRoute: function(){
		fadeOut();
		$('.board').empty();
		$('.board').css('visibility', 'hidden');
	}
});
var app_router = new Router;

app_router.on('route:desk', function(action, method) {
	if(method==null) {
		$('#loading').css('visibility', 'visible');
		$('#loading').fadeIn();
	}
	
	var view = new BoardView(action);
	$('#loading').css('visibility', 'hidden');
	$('#loading').fadeIn();
	$('.board').css('visibility', 'visible');
});
Backbone.history.start();