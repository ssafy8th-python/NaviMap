<template>
	<div>
		<MemoryLogEmoticon
		@changeEmoticonList="changeEmoticonList"
		/>
		<form class="memory-log-form" @submit.prevent="getReviewContent">
				<textarea class="memory-log-input" type="text" maxlength="100" v-model="reviewContent" @keyup.enter="getReviewContent" autofocus ></textarea>
				<input type="submit" value="저장" class="memory-log-submit-btn">
		</form>
	</div>
</template>

<script>
import MemoryLogEmoticon from '../memory-log-form/MemoryLogEmoticon.vue'

export default {
	name:'MemoryInput',
	components:{
		MemoryLogEmoticon
	},
	data() {
		return {
			reviewContent : '', 
			selectedEmoticon:'',
			emoticonList:''
		}
	},
	methods:{
		getReviewContent(){
			const newInput = this.reviewContent
			const findEmoticon = this.emoticonList.filter((emo)=> {
				if (emo.selected){
					return emo
				}
			})
		
			if (findEmoticon.length === 0){
				alert('이모이콘을 선택해주세요!')
				return 
			} else if(!newInput){
				alert('메모리로그를 입력해주세요!')
				return 
			}

			const newEmoticon = findEmoticon[0].emoticon

			const newImoticonList = this.emoticonList.map((emo) => {
				{
					emo.selected = false
				}

				return emo
			})

			const payload = { newInput, newEmoticon}

			this.$emit('getReviewContent', payload)
		
			this.emoticonList = newImoticonList
			this.reviewContent = ''
		},
		changeEmoticonList(emoList){
			this.emoticonList = emoList
		}
	}
}
</script>

<style scoped>
 .memory-log-form{
	width:100%;
	background-color: white;
	display: flex;
	border-radius:10px;

 }
 .memory-log-input{
	width:90%;
	resize: none;
	height: 6.5em;
	padding: 10px;
	overflow:auto;
	border: none;
	border-radius:10px;

 }

	.memory-log-input::-webkit-scrollbar{
		display: none;
	}
 textarea:focus {outline: none;}
 label{
	background-color: white;
 }

 .memory-log-submit-btn{
	padding:10px;
	margin-top: auto;
	border:none;
	background-color: white;
	cursor: pointer;
	border-radius:10px;
	font-weight: bold;
 }

 .memory-log-submit-btn:hover{
	background-color: #FFECEC;
	color:#FFA0A0;
	font-weight: bold;

 }
</style>