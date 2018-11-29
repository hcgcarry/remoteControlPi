$(document).ready(function () {
	$("button").click(function (e) {
		console.log('active');
		var mode = $("button").attr("class");
		var pin = 17;
			$.POST("/web-pins/pi-write.php", {
                'mode':mode
                'pin':pin
			},
			function (data, status) {
				$('div.lightStatus').html("<div> data:" + data + "</div> status:"+status);
			});


	});
});
