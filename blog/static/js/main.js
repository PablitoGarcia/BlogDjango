
window.onload = function onLoad() {
    var circle = new ProgressBar.Circle('#progress', {
        
    });

    
};
var element = document.getElementById('example-clock-container');

var seconds = new ProgressBar.Circle(element, {
    duration: 5400,
    color: "black",
    trailColor: "red",
     strokeWidth: 5.1,
    
    
});

setInterval(function() {
    var second = new Date().getSeconds();
    seconds.animate(second / 8, function() {
        seconds.setText(second);
    });
}, 1000);