<template>
	<div>
		<TheMemories
		:memories="memories"
		/>
		<div class="head-para">추억로그 남기기</div>
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
			this.memories.unshift(newInput)
		}
	}
}
</script>

<style>

</style>