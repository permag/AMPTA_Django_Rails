// init
$(function(){
	$(".confirmDelete").click(function(){
		var doDelete = confirm("Are you sure you wanna delete this?");
		if (doDelete){
			return true;
		}
		return false;
	});
});