var fadeOut = function() {
	$('#loading').css('visibility', 'visible');
	$('#loading').fadeOut();
	$('#loading').css('visibility', 'hidden');		
};

var Router = Backbone.Router.extend({
	routes: {
		':action': 'desk',
		'*default': 'defaultRoute'
	}, 
	defaultRoute: function(){
		fadeOut();
		$('.board').empty();
		$('.board').css('visibility', 'hidden');
	}
});
var app_router = new Router;

app_router.on('route:desk', function(action) {
	
	$('#loading').css('visibility', 'visible');
	$('#loading').fadeIn();

	var board = new BoardView({
		traditional: true,
		data:{
			"q":action
		}
	});

	
});
Backbone.history.start();