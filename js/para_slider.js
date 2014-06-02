function myFunction() 
{
element = document.getElementById('window_slider');

if (element.src.match("slider_arrow_back"))
	{
		$('.parameters').animate({width: 400}, 1000);
		$('.parameters_text').animate({opacity: 100}, 1000);
		$('.compount_input').animate({width: 190}, 1000);
		$('.compount_input').animate({opacity: 100}, 500);
		$('.compount_text').animate({width: 111}, 1000);
		$('.window_slider').animate({right: 400}, 1000);
		element.src = "slider_arrow.png";
	}
else{
		$('.parameters').animate({width: 0}, 1000);
		$('.parameters_text').animate({opacity: 0}, 1000);
		$('.compount_input').animate({opacity: 0}, 500);
		$('.compount_input').animate({width: 0}, 1000);
		$('.compount_text').animate({width: 0}, 1000);
		$('.window_slider').animate({right: 0}, 1000);
		element.src = "slider_arrow_back.png";
	}
}
 