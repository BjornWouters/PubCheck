function my_Function(){
	window.open("http://www.w3schools.com","_blank","toolbar=yes, scrollbars=yes, resizable=yes, top=500, left=500, width=400, height=400");
}

function generateTable(query){
	document.getElementById("values").value = query;
	document.getElementById("form").submit();
}