<template>
	<div v-for="event in events" :key="event.id">
		<h3>{{event.name}}</h3>
		<p>{{event.description}}</p>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'Tasks',
	data() {
		return {
		events: {}
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

</style>