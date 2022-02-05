<template>
	<div class="app">
		<Header text="REST TODOs"/>
		<Tasks />
	</div>
</template>

<script>
import Header from './components/Header.vue'
import Tasks from './components/Tasks.vue'
import axios from 'axios'

export default {
	
	name: 'App',
	components: {
		Header,
		Tasks,
	},
	methods: {
		createTask() {
			const taskData = {
				'name': prompt('Task Name'),
				'description': prompt('Task Description')
			}
			axios.post('http://localhost:8000/api/create-task/', taskData)
			location.reload()
		}
	}
}
</script>

<style>
</style>
