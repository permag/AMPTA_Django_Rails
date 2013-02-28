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
});