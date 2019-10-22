var app = new Vue({
	el: '#app',
	data: {
		lesson: "Events and Methods",
		counter: 0,
	},
	methods: {
		incrementCounter() {
			this.counter += 1;
			console.log(this.counter);
			if(this.counter == 10) {
				alert("Counter equals 10!");
			}
		},
		overTheBox() {
			console.log("Over the green box!");
		},
	},
})