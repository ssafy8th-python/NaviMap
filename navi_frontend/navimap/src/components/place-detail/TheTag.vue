<template>
	<div>
		<div class="head-para">태그</div>
		<div class="empty" v-if="!tagArray.length">
			<span>
				태그를 추가해 주세요!
			</span>
		</div>
		<div class="tag-item-box" v-for="(tag, idx) in tagArray" :key="idx">
			<span>
				{{tag}}
			</span>
		</div>
	</div>
</template>

<script>
export default {
	name:'TheTag',
	data() {
		return{
			tagArray: [
				'큐레이팅이 잘돼있는',
				'데이트 장소',
				'예뻐요',
				'휴일에 가기 좋은 곳'
			]
		}
	}
}
</script>

<style scoped>
	.tag-item-box{
		border-radius: 4px;
		box-shadow: 1px 1px 4px rgb(0 0 0 / 20%);
		display: inline-block;
		padding:7px;
		margin:4px;
		cursor: pointer;
		background-color: #F0F0FF;
	}

</style>