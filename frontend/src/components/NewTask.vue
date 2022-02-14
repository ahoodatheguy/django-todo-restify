<template>
	<input v-model="taskName" />
	<input v-model="taskDesc" />
	<Button
		text="Create New TODO"
		btnType="btn-primary"
		style="align-content: center"
		:onClick="createTask"
	/>
</template>

<script>
import Button from "./Button.vue";
import axios from "axios";

export default {
	name: "NewTask",
	components: { Button },
	data() {
		return {
			taskName: "",
			takDesc: "",
		};
	},
	methods: {
		createTask() {
			const taskData = {
				name: this.taskName,
				description: this.taskDesc,
			};
			console.log(taskData);
			axios.post("http://localhost:8000/api/create-task/", taskData);
			// location.reload();
			this.taskName = "";
			this.taskDesc = "";
		},
	},
};
</script>

<style scoped>
input {
	margin: 5px;
}
</style>
