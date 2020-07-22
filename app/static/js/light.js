var x = document.getElementsByClassName('mode')[0];
var body = document.getElementsByTagName('body')[0];
var body_all = document.getElementsByClassName('body-all')[0];
console.log(body_all)

function fade(element) {
  var op = 1;  // initial opacity
  var timer = setInterval(function () {
      if (op <= 0.1){
          clearInterval(timer);
          element.style.display = 'none';
      }
      element.style.opacity = op;
      element.style.filter = 'alpha(opacity=' + op * 100 + ")";
      op -= op * 0.1;
  }, 50);
}

function unfade(element) {
  var op = 0.1;  // initial opacity
  element.style.display = 'block';
  var timer = setInterval(function () {
      if (op >= 1){
          clearInterval(timer);
      }
      element.style.opacity = op;
      element.style.filter = 'alpha(opacity=' + op * 100 + ")";
      op += op * 0.1;
  }, 10);
}

function changeClass(){
  console.log(x);
  if (x.classList.contains('dark-mode')) {
    console.log('Dark mode!')
    x.classList.remove('dark-mode');
    x.classList.toggle('light-mode');
    body.classList.remove('dark-mode');
    body.classList.toggle('light-mode');
    // var dark = document.getElementsByClassName('dark-mode');
    // for(let i = 0; i < dark.length; i++){ 
    //   // console.log(dark[i]);
    //   dark[i].classList.toggle('light-mode');
    //   dark[i].classList.remove('dark-mode');
    // }
    //! would want to add a fade to light here
  } else {
    console.log('Not dark mode')
    x.classList.remove('light-mode');
    x.classList.toggle('dark-mode');
    body.classList.toggle('dark-mode');
    body.classList.remove('light-mode');
    //! would want to add a fade to dark here
  }
  console.log(x);
}

window.onload = function(){
  x.addEventListener( 'click', changeClass);
}
/* End */
