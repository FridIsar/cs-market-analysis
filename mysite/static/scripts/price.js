$( document ).ready(function() {
	console.log("document ready")
	$( "#priceButton" ).click(function()	{
		console.log("button clicked")
		$.ajax({
			url: 'getprice',
			type: 'get', // This is the default though, you don't actually need to always mention it
			success: function(data) {
				console.log(data.price);
			},
			failure: function(data) {
				console.log('Got an error dude');
			}
		});
	})
});
