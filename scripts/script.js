$(function() {
    // Handler for .ready() called.
  
  
  
  function showNav() {
   $('#topnav').html(
       `
      <ul>
          <li class="resources-link"><a href="resources.html">resources</a></li>
          <li class="favorite-foods-link"><a href="favorite-foods.html">Favorite Foods</a></li>
          <li class="apple-link"><a href="#">Apple</a></li>
      </ul>
      `
      );
  
  }
  
  
  function addActiveClass() {
      if ( $('body.favorite-foods') ){
  
              $('.favorite-foods-link').addClass('active');
      } else if ( $('body.resources') ){
          $('.resources-link').addClass('active');
      }
  }
  
  
  
  function initialize() {
      showNav();
      addActiveClass();
  }
  
  $(initialize());
  
  
  });