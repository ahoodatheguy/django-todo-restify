<template>
	<Button text="Create New TODO" btnType="btn-primary" style="align-content: center;" :onClick="createTask"/>
	<div v-for="event in events" :key="event.id" class="task-list">
		<div class="task-header">
			<h3 class="task-name" @click="deleteTask(event.id)">{{event.name}}</h3>
		</div>
		<p>{{event.description}}</p>
	</div>
</template>

<script>
import axios from 'axios'
import Button from './Button.vue'

export default {
	name: 'Tasks',
	components: { Button },
	data() {
		return {
		events: {},
		}
	},
	methods: {
		deleteTask(id) {
			if (confirm('Delete Task?')) {
			axios
			.delete(`http://127.0.0.1:8000/api/delete-task/${id}`)
			location.reload()
			}
		},
		createTask() {
			const taskData = {
				'name': prompt('Task Name'),
				'description': prompt('Task Description')
			}
			axios.post('http://localhost:8000/api/create-task/', taskData)
			location.reload()
		},
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

body {
	padding-left: 25px;
	padding-right: 25px;
}
</style>