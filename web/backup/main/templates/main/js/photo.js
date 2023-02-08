(function(){
	var video = document.getElementById('video'),
		canvas = document.getElementById('canvas')
		photo = document.getElementById('photo')
		context = canvas.getContext('2d')
		vendorUrl = window.URL || wondow.webkitURL;

	navigator.getMedia = navigator.getUserMedia ||
	                     navigator.webkitGetUserMedia ||
	                     navigator.mozGetUserMedia ||
	                     navigator.msGetUserMedia;

	navigator.getMedia =  navigator.getUserMedia ||
    navigator.webkitGetUserMedia ||
    navigator.mozGetuserMedia ||
    navigator.msGetUserMedia;

    navigator.getMedia({
      video: true,
      audio: false
    }, function(stream) {
      video.src = vendorUrl.createObjectURL(stream);
      video.play();
    }, function(error) {
      // an error occurred
    } );
	document.getElementById('capture').addEventListener('click'), function(){
		context.drawImage(video,0,0,400,300)
		photo.setAttribute('src', canvas.toDataURl('image/png'));

	};
}) ();