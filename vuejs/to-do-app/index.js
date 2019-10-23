// task-list component
Vue.component("to-do", {
	props: {
		tasks: {
			type: Array,
			required: true,
		},
		counter: {
			type: Number,
			required: true,
		},
	},
	data: function() {
		return {
			new_task: null,
			error: null,
		}
	},
	methods: {
		submitTask() {
			if(this.new_task) {
				this.$emit('add-task', this.new_task);
				this.new_task = null;
				if(this.error) {
					this.error = null;
				}
			} else {
				this.error = "You've left the field empty."
			}
		},
		removeTask(task) {
			this.$emit('remove-task', task);
		},
	},
	template: `
		<div class="container mt-2">
			<div class="container">
				<p><strong>Remaining Tasks: {{ counter }}</strong></p>

				<input type="text"
					class="form-control"
					placeholder="What do you need to do?"
					v-model="new_task"
					@keyup.enter="submitTask">

				<br/>

				<p v-if="error">{{ error }}</p>
				<p v-if="counter == 0">To add a new task, write something and press enter!</p>

				<div class="single-task"
					v-for="(task, index) in tasks"
					:task="task"
					:key="index">

					<div class="alert alert-success">
						{{ task }}
						<button type="button"
								class="close no-outline"
								@click="removeTask(task)">
							<span>&times;</span>
						</button>
					</div>

				</div>
			</div>
		</div>
	`,
})

// single-task component
Vue.component("single-task", {
	props: {
		task: {
			type: Object,
			required: true,
		},
	},
	template: `
		<div class="mb-2">
			<div class="alert alert-success alert-dismissible fade show" role="alert">
				{{ task.content }}
				<button type="button" class="close" data-dismiss="alert" aria-label="Close">
					<span aria-hidden="true">&times;</span>
				</button>
			</div>
		</div>
	`,
})

var app = new Vue({
	el: '#app',
	data: {
		comments: [
			{ username: "nicole", content: "Thank you!" },
		],
		tasks: [],
	},
	computed: {
		taskCount() {
			return this.tasks.length;
		},
	},
	methods: {
		addNewTask(new_task) {
			this.tasks.push(new_task);
		},
		removeTask(task){
			this.tasks.splice(this.tasks.indexOf(task), 1);
		},
	},
})