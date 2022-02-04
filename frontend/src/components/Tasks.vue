<template>
	<div v-for="event in events" :key="event.id" class="task-list">
		<h3 class="task-name" @click="deleteTask(event.id)">{{event.name}}</h3>
		<p>{{event.description}}</p>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'Tasks',
	data() {
		return {
		events: {},
		}
	},
	methods: {
		deleteTask(id) {
			axios
			.delete(`http://127.0.0.1:8000/api/delete-task/${id}`)
			.then(() => location.reload)
		}
	},
	created() {
		axios
		.get('http://127.0.0.1:8000/api/view-tasks/')
		.then(response => {
			this.events = response.data
		})
	}
}
</script>

<style>
.task-name:hover {
	color: red;
	cursor: pointer;
	text-decoration: line-through;
}

.task-list {
	padding-left: 25px;
}
</style>