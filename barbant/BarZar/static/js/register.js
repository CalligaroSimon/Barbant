$(function(){   
	var check = {};

	check['pseudo'] = function() {
		if (( /^[a-z0-9-_]+$/i ).test($('#id_pseudo').val())){
			changeTooltip('pseudo',true,'Nom d\'utilisateur correct');
			return true;
		}
		else {
		    changeTooltip('pseudo',false,'Nom d\'utilisateur non valide');
			return false;
		}
	};
	
	check['email'] = function() {
		if ((/^[a-z0-9]+([_|\.|-]{1}[a-z0-9]+)*@[a-z0-9]+([_|\.|-]{1}[a-z0-9]+)*[\.]{1}[a-z]{2,6}$/i).test(id_email.value)){
			changeTooltip('email',true,'Adresse email valide.');
			return true ;
		}
		else {
			changeTooltip('email',false,'Adresse email non valide.');
			return false;
		}
	};
	
	check['pass1'] = function() {
		var pass = $("#id_pass1").val();
		if(pass.length >= 8){
			changeTooltip('pass1',true,'Mot de passe valide');
			return true;
		}
		else  {
			changeTooltip('pass1',false ,'Le mot de passe doit avoir au minimun 8 caractères.');
			return false;
		}
	};

	check['pass2'] = function() {
		var pass = $("#id_pass1").val(), pass2 = $("#id_pass2").val();
		if (pass == pass2 && pass2 != '') {
			changeTooltip('pass2',true,'Les mots de passes sont identique.')
			return true;
		}
		else {
			changeTooltip('pass2',false,'Les mots de passes doivent être identique.')
			return false;
		}
	};

	for (var i in check)
		$('#id_'+i).keyup(check[i]).focus(check[i]);
	
	$('#formRegister').submit( function(e) {
		var result = true;
		
		for (var i in check)
			result = check[i]() && result;
		
		if (result == false) 
			e.preventDefault();
		
	});
	
	function changeTooltip(input, condition, message){
		var $input = $('#id_'+input),
			$tooltip = $('#tooltip-'+input)
		
		if (condition) {
			$tooltip.css({display : "none"});
			$input.removeClass("incorrect").addClass("correct");
		} 
		else {
			$tooltip.css({display : "block"}).removeClass("correct").addClass("incorrect").text(message);
			$input.removeClass("correct").addClass("incorrect");
		}
	}
});
