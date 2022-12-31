<template>
	<div class="memory-log-emoticon">
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
</template>

<script>
export default {
	name:'MemoryLogEmoticon',
	data() {
		return{
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
		selectEmoticon(emoticon){
			const newImoticonList = this.emoticonList.map((emo) => {
				if (emo === emoticon){
					emo.selected = !emo.selected
				} else{
					emo.selected = false
				}

				return emo
			})

			this.emoticonList = newImoticonList

			this.$emit('changeEmoticonList', this.emoticonList)

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
	height:auto;	
	border-radius:10px;
	cursor: pointer;
	box-shadow: 2px 2px 8px rgb(0 0 0 / 30%);
 }

 .emoticon-item-box{
	width:100%;
	height:auto;
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

</style>