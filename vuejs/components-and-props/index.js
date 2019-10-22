Vue.component("comment", {
	props: {
		comment: {
			type: Object,
			required: true,
		},
	},
	template: `
		<div>
			<div class="card-body">
				<p>{{ comment.username }}</p>
				<p>{{ comment.content }}</p>
			</div>
			<hr/>
		</div>
	`,
})

var app = new Vue({
	el: '#app',
	data: {
		comments: [
			{ username: "nicole", content: "Thank you!" },
			{ username: "jinnell", content: "Xie xie!" },
			{ username: "brandon", content: "Gracias!" },
			{ username: "bryan", content: "Arigato!" },
		]
	},
	computed: {
	},
	methods: {
	},
})