$(document).ready(function() {

	var all_data;
	var url = "http://localhost:8000/static/data/data.json";
	var response_url = "http://localhost:8000/static/data/response.json";
    
	$('ul.nav li.dropdown').hover(function() {
	  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn(500);
	}, function() {
	  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut(500);
	});    
	
	/*============================================
	Scroll To Top
	==============================================*/	

	//When distance from top = 250px fade button in/out
	$(window).scroll(function(){
		if ($(this).scrollTop() > 250) {
			$('#scrollup').fadeIn(300);
		} else {
			$('#scrollup').fadeOut(300);
		}
	});

	//On click scroll to top of page t = 1000ms
	$('#scrollup').click(function(){
		$("html, body").animate({ scrollTop: 0 }, 1000);
		return false;
	});


	$.getJSON( url, {
	    tags: "mount rainier",
	    tagmode: "any",
	    format: "json"
	})
	.done(function( data ) {
      console.log(data);
	  all_data = data;
	  getResponses();
	  loadDefaultData(all_data, "meh");
    });

    function removeObjects() {
		$("#deck_wrapper").remove();
	}

	function addDeckWrapper() {
		$("#row_body").append('<div id="deck_wrapper" class="card-deck-wrapper"></div>');
	}

	function cleanData() {
		removeObjects();
		addDeckWrapper();
	}

	function getFilteredData(type) {
		var min_mag;
		var max_mag;
		var min_score;
		var max_score;
		var updateData = [];

		if (type == "meh") {
			$.each(all_data, function(key, value) {
				if (value.results.labels[0] == "happy" || value.results.labels[0] == "meh") {
					updateData.push(value);
				}
			});
		} else if (type == "sad") {
			$.each(all_data, function(key, value) {
				if (value.results.labels[0] == "happy") {
					updateData.push(value);
				}
			});
		}

		loadDefaultData(updateData, type);
	}

	$("#icon_happy").click(function() {
		cleanData();
		loadDefaultData(all_data, "happy");
	});

	$("#icon_meh").click(function() {
		cleanData();
		loadDefaultData(all_data, "meh");
		
	});

	$("#icon_sad").click(function() {
		cleanData();
		var updateData = [];
		$.each(all_data, function(key, value) {
				if (value.results.labels[0] == "happy" || value.results.labels[0] == "meh") {
					updateData.push(value);
				}
			});
		loadDefaultData(updateData, "sad");
	});

	function getResponses() {
		$.get(response_url)
		  .done(function(response) {
		    $.each(response, function(key, value) {
		    	console.log(value);
		    	updateData(value.id, value.sentiment, value.magnitude);
		    });
		 });
	}


	function loadDefaultData(data, mood_type) {
		var items_len = data.length;

		var counter = 0;
		var deck_counter = 1;
		var deck_id = "deck_" + deck_counter;
		$("#deck_wrapper").append('<div class="card-deck" id='+ deck_id +'></div>');
	
		$.each(data, function(key, value) {
			var i = value.id;
			var blog_id = "blog_" + i;
			var blog_img_src = "static/img/blog/"+ i + ".png";
			if (value.image == "none") {
				blog_img_src = "static/img/blog/place.png";
			}
			
			var blog_img_id = "blog_img_" + i;
			var blog_title_id = "blog_title_" + i;
			var blog_title = value.title;
			var blog_description = value.description;
			var blog_category = value.category;
			var user_name = value.user_name;
			var user_img_src = "static/img/users/"+ user_name.toLowerCase() + ".png";
			var user_img_id = "user_img_" + i;
			var href_val = "#";
			if (value.type == "url") {
				href_val = value.content;
			}
			var description_id = "description_" + i;
			$("#" + deck_id).append('<div class="card" id='+ blog_id +'><a target="_blank" href='+ href_val +'><img class="card-img-top img-fluid" id='+ blog_img_id +' src='+ blog_img_src +' alt="..."></a><div class="card-block"><h4 class="card-title" id='+ blog_title_id +'><a target="_blank" href='+ href_val +'>'+ blog_title +'</a></h4><h6 class="card-text"><a href="#">'+ blog_category +'</a>,&nbsp; <small>5 minutes ago</small></h6><p class="med-text" id='+ description_id +'>'+ blog_description+'</p></div><div class="card-footer"><hr/><ul class="author-2"><li><a href="#"><img class="" id='+ user_img_id +' src='+ user_img_src +' alt="..."/> &nbsp; <span>'+ user_name +'</span></a></li></ul><ul class="bottom_data pull-right hidden-xs-down"><li><i class="fa fa-comment-o"></i>200</li><li><i class="fa fa-heart-o"></i>30</li><li><i class="fa fa-align-left"></i>7 Min Read</li></ul></div></div>');
			counter++;
			if (counter % 3 == 0) {
				deck_counter++;
				deck_id = "deck_" + deck_counter;
				$("#deck_wrapper").append('<div class="card-deck" id='+ deck_id +'></div>');
			}

			// $(".med-text").css("color", "red");

			if (mood_type == "happy" && value.results.labels[0] == "sad") {
				$('#' + description_id).css("color", "red");
			}
		});
	}

	function updateData(id, sentiment, magnitude) {
		$.each(all_data, function(key, value) {
			if (value.id == id) {
				value.results.score = sentiment;
				value.results.magnitude = magnitude;

				if (sentiment < 0) {
					value.results.labels[0] = "sad";
				} else if (sentiment >= 0 && magnitude < 7) {
					value.results.labels[0] = "meh";
				} else {
					value.results.labels[0] = "happy";
				}

				return false;
			}
		});
	}

});

