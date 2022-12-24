<template>
	<div>
		<TheMemories
		:memories="memories"
		/>
		<h3>추억로그 남기기</h3>
		<MemoryInput
		@getReviewContent='getContentF'
		/>
	</div>
</template>

<script>
import MemoryInput from '../memory-log-form/MemoryInput.vue'
import TheMemories from '../memory-log-form/TheMemories.vue'

export default {
	name:'MemoryLogForm',
	components:{
		MemoryInput,
		TheMemories
	},
	data() {
		return{
			memories:[],
		}
	},
	methods:{
		getContentF(newInput){
			this.memories.push(newInput)
		}
	}
}
</script>

<style>

</style>