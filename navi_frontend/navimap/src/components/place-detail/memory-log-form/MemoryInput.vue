<template>
	<div>
		<h3>추억로그 남기기</h3>
		<div class="memory-log-emoticon" 			
		>
			<div 
				class="emoticon-item-container"
				v-for="(emoticon) in emoticonList"
				:key="emoticon.idx"	
				@click="selectEmoticon(emoticon)"
				:class="{ 'selected' : emoticon.selected}"
			>
				<div class="emoticon-item-box">
					<span v-html="emoticon.emoticon"></span>
				</div>
			</div>
		</div>
		<form class="memory-log-form" @submit.prevent="getReviewContent" v-if="isOpen">
				<textarea class="memory-log-input" type="text" maxlength="100" v-model="reviewContent" @keyup.enter="getReviewContent" autofocus ></textarea>
				<input type="submit" value="저장" class="memory-log-submit-btn" >
		</form>
	</div>
</template>

<script>
export default {
	name:'MemoryInput',
	data() {
		return {
			reviewContent : '', 
			isOpen: false,
			selectedEmoticon:'',
			emoticonList : [
				{
					idx: 0,
					emoticon:'&#128555;',
					selected: false,
				},
				{
					idx: 1,
					emoticon:'&#128528;',
					selected: false,
				},
				{
					idx: 2,
					emoticon:'&#128578;',
					selected: false,
				},
				{
					idx: 3,
					emoticon:'&#128523;',
					selected: false,
				},
				{
					idx: 4,
					emoticon:'&#128522;',
					selected: false,
				},
			],
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

			this.selectedEmoticon = newEmoticon
			const newImoticonList = this.emoticonList.map((emo) => {
				{
					emo.selected = false
				}

				return emo
			})

			const payload = { newInput, newEmoticon}

			console.log(this.selectedEmoticon)

			this.$emit('getReviewContent', payload)
		
			this.emoticonList = newImoticonList
			this.reviewContent = ''
			this.selectedEmoticon = ''
			this.isOpen = false
				

		
		},
		selectEmoticon(emoticon){
			this.isOpen = true

			const newImoticonList = this.emoticonList.map((emo) => {
				if (emo === emoticon){
					emo.selected = !emo.selected
				} else{
					emo.selected = false
				}

				return emo
			})

			this.newImoticonList = newImoticonList

		}
	}
}
</script>

<style scoped>
 .memory-log-emoticon{
	width:100%;
	height: 5.5em;
	margin-bottom:10px;
	display:flex;
	justify-content: space-around;
	align-items: center;
	border-radius:10px;

 }

 .emoticon-item-container{
	background-color:white;
	width:15%;
	min-width:40px;
	height:75%;	
	border-radius:10px;
	cursor: pointer;
	box-shadow: 2px 2px 8px rgb(0 0 0 / 30%);
 }

 .emoticon-item-box{
	width:100%;
	height:100%;
	display: flex;
	justify-content: center;
	align-items: center;
 }

 .emoticon-item-box > span{
	font-size:30px;
	text-align: center;
 }

 .selected{
	background-color: skyblue;
 }
 .memory-log-form{
	width:100%;
	background-color: white;
	display: flex;
	border-radius:10px;

 }
 .memory-log-input{
	width:90%;
	resize: none;
	height: 4.5em;
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
 }

 .memory-log-submit-btn:hover{
	background-color: #FFECEC;
	color:#FFC7B2;

 }
</style>