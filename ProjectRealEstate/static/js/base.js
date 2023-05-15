$(document).ready(function() {
	$('.header__burger').click(function(event) {
		$('.header__burger,.header__menu').toggleClass('active');
		$('body').toggleClass('lock');
	});


});

$(function(){
  $('.header__list [href]').each(function() {
    if (this.href == window.location.href) {
      $(this).addClass('active');
    }
  });
});

