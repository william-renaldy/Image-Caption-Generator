"use strict";
var fileName;

function dragNdrop(event) {
    fileName = URL.createObjectURL(event.target.files[0]);
    var preview = document.getElementById("preview");
    var previewImg = document.createElement("img");
    previewImg.setAttribute("src", fileName);
    preview.innerHTML = "";
    preview.appendChild(previewImg);

    document.getElementById("uploader").setAttribute("hidden",false);
    document.getElementById("changerdiv").removeAttribute("hidden");
    document.getElementById("generate").removeAttribute("hidden");
}
function drag() {
    document.getElementById('uploadFile').parentNode.className = 'draging dragBox';
}
function drop() {
    document.getElementById('uploadFile').parentNode.className = 'dragBox';
}

function change(){
    document.getElementById("changerdiv").setAttribute("hidden",false);
    document.getElementById("uploader").removeAttribute("hidden");
    document.getElementById("loading").setAttribute("hidden",false);
    document.getElementById("resultdiv").setAttribute("hidden",false);
    document.getElementById("changer").removeAttribute("hidden");
    document.getElementById("generate").setAttribute("hidden",false);
    $('#preview').children().last().remove();
}



$(document).ready(function(){
    $("form").on("submit",function(event){
        //alert();


        var form_data = new FormData();
        form_data.append('file', $('#uploadFile').prop('files')[0]);

        //var msg = $("#uploadFile").val();
        
        //alert(files);

        if(true){
            //fd.append('file',files[0]);
            document.getElementById("changer").setAttribute("hidden",false);
            document.getElementById("loading").removeAttribute("hidden");
            document.getElementById("resultdiv").setAttribute("hidden",false);

            $.ajax({
                data:form_data,
                contentType: false,
                cache: false,
                processData: false,
                type:"POST",
                url:"/predict",
            }).done(function(data){
                document.getElementById("loading").setAttribute("hidden",false);
                document.getElementById("resultdiv").removeAttribute("hidden");
                document.getElementById("result").innerHTML = data;
            });
        }
        else{
            document.getElementById("resultdiv").setAttribute("hidden",false);
            document.getElementById("changer").removeAttribute("hidden");
        }
        event.preventDefault();
    });
});
