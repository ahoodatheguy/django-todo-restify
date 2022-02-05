<template>
	<button class="btn" :class="btnType" @click="onClick">{{text}}</button>
</template>

<script>
export default {
	name: 'Button',
	props: {
		text: String,
		btnType: String,
		onClick: Function
	}
	
}
</script>

<style>
</style>