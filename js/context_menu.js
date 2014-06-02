function ShowMenu(control, e) {
	var posx = e.clientX +window.pageXOffset +'px'; //Left Position of Mouse Pointer
	var posy = e.clientY + window.pageYOffset + 'px'; //Top Position of Mouse Pointer
	document.getElementById(control).style.position = 'absolute';
	document.getElementById(control).style.display = 'inline';
	document.getElementById(control).style.left = posx;
	document.getElementById(control).style.top = posy;           
}
function HideMenu(control) {
	document.getElementById(control).style.display = 'none'; // JavaScript Document
}