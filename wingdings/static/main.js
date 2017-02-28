function displayImg(file) {
    console.log(file.id);
    var image = file.id;
    document.getElementById("largeImg").innerHTML = '<img src="img/'+image+'.jpg"/>';
}
