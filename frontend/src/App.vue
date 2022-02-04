<template>
	<div class="app">
		<Header text="REST TODOs"/>
		<Tasks />
	</div>
</template>

<script>
import Header from './components/Header.vue'
import Tasks from './components/Tasks.vue'

export default {
	
	name: 'App',
	components: {
		Header,
		Tasks
	}
}
</script>

<style>
</style>
