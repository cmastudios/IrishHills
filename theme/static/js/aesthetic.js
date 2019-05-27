let prevScrollpos = window.pageYOffset;
window.onscroll = function() {
	let currentScrollPos = window.pageYOffset;
	if (prevScrollpos > currentScrollPos) {
		document.getElementById("navbar").classList.remove("hidden");
	} else {
		document.getElementById("navbar").classList.add("hidden");
	}
	prevScrollpos = currentScrollPos;
} 
