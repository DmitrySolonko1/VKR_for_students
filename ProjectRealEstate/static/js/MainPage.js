$(document).ready(function() {
	$('.selling__slider').slick({
		arrows: true,
		dots: false,
		adaptiveHeight: true,
		autoplay: false,
		responsive: [
			{
				breakpoint: 924,
				settings: {
					arrows: false,
					dots: true
				}
			}
		]
	});
	$('.arenda__slider').slick({
		arrows: true,
		dots: false,
		adaptiveHeight: true,
		autoplay: false,
		responsive: [
			{
				breakpoint: 924,
				settings: {
					arrows: false,
					dots: true
				}
			}
		]
	});


});


