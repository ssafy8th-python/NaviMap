<template>
	<div>
		<div class="head-para">추억 로그들</div>
		<div 
			class="memory-log-box"
		>
			<div v-if="!memories.length" class="empty">
				<span>
					추억 로그를 작성해주세요!
				</span>
			</div>
			<div 
				class="memory-log-card"
				v-for="(memory, idx) in memories"
				:key="idx"	
				>
				<div v-html="memory.newEmoticon" class="emoticon-box">
				</div>
				<span>
					{{memory.newInput}}
				</span>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name:'TheMemories',
	data() {
		return{

		}
	},
	props:{
		memories:Array
}, 
	compouted:{

	}
}
</script>

<style scoped>
	.memory-log-box{
		padding-top:15px;
		display: flex;
		flex-direction: column;
		max-height: 210px;
		overflow: auto;
	}

	.memory-log-box::-webkit-scrollbar{
		display: none;
	}

	.memory-log-card{
		width:90%;
		margin:auto;
		padding:15px;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
		border-radius: 6px;
		margin-bottom:20px;
		background-color: white;
		position:relative;

	}

	.emoticon-box{
		font-size: 30px;
    display: inline-block;
    position: absolute;
    top: -22px;
	}
</style>