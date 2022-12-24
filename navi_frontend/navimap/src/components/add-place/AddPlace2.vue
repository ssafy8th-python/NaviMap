<template>
	<div class="add-place-page">
		<body class="body">
			<div class="add-place-info">
				<AddPhoto
				@getImage="getImageF"
				/>
				<AddMemoryLog
				@getReviewContent="getReviewContentF"
				/>
			</div>
		</body>
		<footer class="footer">
			<input type="button" class="submit-log" value="저장하기" @click="saveData">
			</footer>
	</div>
</template>

<script>
import AddPhoto from '../add-place/add-place2/AddPhoto.vue'
import AddMemoryLog from '../add-place/add-place2/AddMemoryLog.vue'

export default {
	name: 'AddPlace2',
	components:{
		AddPhoto,
		AddMemoryLog
	},
	data() {
		return {
		memoryPhoto:'',
		memoryLog:{},
		}
	},
	methods:{
		getReviewContentF(payload) {
			this.memoryLog = payload
		},
		getImageF(image){
			this.memoryPhoto = image
		},
		saveData(){
			const memoryLog = this.memoryLog
			const memoryPhoto = this.memoryPhoto

			const payload ={
				memoryLog,memoryPhoto
			}

			this.$emit('saveData', payload)
		}
	}
}
</script>

<style scoped>
.add-place-page{
	height: 100%;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	font-size:13px
}
.body{
	height: 90%;
	overflow: auto;
	background-color:#f8f9fa;

}
.add-place-info{
	display: flex;
	flex-direction: column;
	width: 100%;
	height: 100%;
}
.footer{
	text-align: center;	
}

.submit-log{
	border:none;
	width:80%;
	cursor: pointer;
	font-size:16px;
	border-radius: 5px;
	padding: 10px;
	background-color: #FFA0A0;
	color: white;
	font-weight: bold;

}

.submit-log:hover {
	background-color: #FFC6C6;
}

::-webkit-scrollbar {
  display: none;
}

</style>