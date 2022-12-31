<template>
	<div class="add-input-page">
		<div class="page2-header-para">이 장소에 대한 로그를 남겨주세요</div>
		<MemoryLogEmoticon
		@changeEmoticonList="changeEmoticonList"
		/>
		<textarea class="memory-log-input" maxlength="100" v-model="reviewContent" @change="getReviewContentF" autofocus></textarea>
	</div>
</template>

<script>
import MemoryLogEmoticon from '@/components/place-detail/memory-log-form/MemoryLogEmoticon'

export default {
	name:'AddMemoryLog',
	data(){
		return {
			emoticonList:'',
			reviewContent: ''
		}
	},
	components:{
		MemoryLogEmoticon
	},
	methods:{
		getReviewContentF() {
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

			const payload = { newInput, newEmoticon}
			console.log(payload)
			this.$emit('getReviewContent', payload)

		},
		changeEmoticonList(emoList){
			this.emoticonList = emoList
		},

	}
}
</script>

<style scoped>
h3{
	text-align: center;
}
.add-input-page{
	height:50%;
	margin-top:35px;
}
.memory-log-input{
	width:100%;
	background-color: white;
	resize: none;
	padding:10px;
	height:6.5em;
	font-size: 13px;
}
 textarea:focus {outline: none;}
</style>