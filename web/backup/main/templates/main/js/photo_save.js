function getImageData (){
     var imgUrl = "a.jpg";
     var canvas = document.createElement("canvas");
     var context = canvas.getContext("2d");
     var img = new Image();
     img.src = imgUrl;
     context.drawImage(img,0,0);
     alert(canvas.toDataURL().toString()); // 변환된 문자열 이 보임
     target.innerHTML = "<img src='"+canvas.toDataURL().toString()+"'>"; //타겟 엘리먼트에 innerHTML
}

function download(){
        var download = document.getElementById("download");
        var image = document.getElementById("canvas").toDataURL("image/png")
                    .replace("image/png", "image/octet-stream");
        download.setAttribute("href", image);

    }

      <script> //사진 저장
        function download(){
          var download = document.getElementById("download");
          var image = document.getElementById("canvas").toDataURL("image/png")
          .replace("image/png", "image/octet-stream");
          download.setAttribute("href", image);
        }
      </script>
      <a id="download" download="image.png"><button type="button" onClick="download()">Download</button></a>