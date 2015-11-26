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
	$('#loading').css('visibility', 'visible');
	$('#loading').fadeIn();
	
	if(method=='create') {
		var board = new BoardFormView();
	}
	else {
		var board = new BoardView({
			traditional: true,
			data:{
				"q":action
			}
		});
	}
});
Backbone.history.start();