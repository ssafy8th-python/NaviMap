<template>
	<div>
		<TheMemories
		:memories="memories"
		/>
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
			console.log('get', this.memories)
		}
	}
}
</script>

<style>

</style>