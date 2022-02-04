<template>
	<header>
		<h1>{{text}}</h1>
	</header>
</template>

<script>
export default {
	name: 'Header',
	props: {
		text: String
	}
}
</script>

<style scoped>
header {
	margin-top: 20px;
	display: flex;
}
</style>