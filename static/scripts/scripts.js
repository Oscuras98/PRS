function randombg(){
  var random= Math.floor(Math.random() * 14) + 0;
  var bigSize = ["url('../static/img/gifs/1.gif')",
                 "url('../static/img/gifs/2.gif')",
                 "url('../static/img/gifs/3.gif')",
                 "url('../static/img/gifs/4.gif')",
                 "url('../static/img/gifs/5.gif')",
                 "url('../static/img/gifs/6.gif')",
                 "url('../static/img/gifs/7.gif')",
		 "url('../static/img/gifs/8.GIF')",
		 "url('../static/img/gifs/9.GIF')",
		 "url('../static/img/gifs/10.GIF')",
		 "url('../static/img/gifs/11.GIF')",
		 "url('../static/img/gifs/12.GIF')",
		 "url('../static/img/gifs/13.GIF')",
		 "url('../static/img/gifs/14.GIF')",];
  document.getElementById("boxes").style.backgroundImage=bigSize[random];
}