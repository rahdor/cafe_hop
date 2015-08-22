$(function (){
	$.ajax({
		type: 'GET',
		url: '/',
		success: function(data) {
			console.log(data)
		}
	});

});