// init
$(function(){
	// Confirm before delete
	$(".confirmDelete").click(function(){
		var doDelete = confirm("Are you sure you wanna delete this?");
		if (doDelete){
			return true;
		}
		return false;
	});

	// Add datepicker classes to input fields
	$("#id_start_date, #id_end_date").addClass("datepicker");
	// Datepicker
	$(".datepicker").datepicker({dateFormat: "yy-mm-dd"});

	// Light up anchored comment
	if (location.hash != null){
		var getHash = location.hash;
		getHash = getHash.substring(1);
		var comment = $("#" + getHash);
		var li = comment.parent();
		var originalBackground = li.css('backgroundColor');
		li.css({'border-left': '4px solid orange'})
		li.css({'backgroundColor': '#bbb'});
		window.setTimeout(function(){
			//li.animate().css({'background': originalBackground});
			li.animate({
				backgroundColor: originalBackground
			}, 'slow');
		},2222);
	}
});