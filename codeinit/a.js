function showTime() {
	document.getElementById('currentTime').innerHTML = new Date().toUTCString();
	to
}
showTime();
setInterval(function () {
	showTime();
}, 1000);