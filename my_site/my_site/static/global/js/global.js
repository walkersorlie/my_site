
//Get the button
var mybutton = document.getElementById("topBtn");

// When the user scrolls down 75px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 75 || document.documentElement.scrollTop > 75) {
    mybutton.style.display = "inline-block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  // document.body.scrollTop = 0;
  // document.documentElement.scrollTop = 0;
  // $('html, body').animate({ scrollTop: 0 }, 1000, "slow");
  $('html, body').animate({ scrollTop: 0 }, 1000, "easeInOutExpo");
  // $('html,body').animate({ scrollTop: 0 }, { duration: 'slow', easing: 'ease-in-out'});
  // document.body.scrollIntoView(alignToTop);
}
