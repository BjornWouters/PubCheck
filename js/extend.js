function addSynonym(){
	//var newRow = jQuery('<input type="text" name="synonyms">');
	//jQuery('synonym_form').append(newRow);
	
	var synonym_form = '<input type="text" name="synonyms" id="synonyms">';
	document.getElementById('synonym_form').innerHTML += synonym_form;
}

function addOrganism(){
	var organism = document.getElementById("organism").value;
	var synonyms = document.getElementsByName("synonyms");
	var url = new String();
	
	for (var i = 0; i < synonyms.length; i++) {
  		url += "&synonyms"+i+"="+synonyms[i].value;
	}
	window.open("add_organism.psp?organism="+organism+url,'windowOpenTab','width=250,height=400,left=50, top=100');
}
function addCompound(){
	var compound = document.getElementById("compound").value;
	window.open("add_compound.psp?compound="+compound,'windowOpenTab','width=250,height=400,left=50, top=100');
}
function searchCompound(){
	window.open("search.psp",'windowOpenTab','width=500,height=800,left=50, top=100');
}
