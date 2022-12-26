<template>
	<div class="add-input-page">
		<h3>이 장소에 대한 로그를 남겨주세요</h3>
		<MemoryInput
		@getReviewContent="getReviewContentF"
		/>
	</div>
</template>

<script>
import MemoryInput from '@/components/place-detail/memory-log-form/MemoryInput'

export default {
	name:'AddMemoryLog',
	components:{
		MemoryInput
	},
	methods:{
		getReviewContentF(payload) {
			this.$emit('getReviewContent', payload)
		}
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
</style>