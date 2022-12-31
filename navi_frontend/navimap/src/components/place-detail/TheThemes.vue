<template>
	<div>
		<div class="head-para">테마</div>
		<div class="theme-item" v-for="(theme, idx) in themeArray" :key="idx">
			<span>
				{{theme}}
			</span>
		</div>
	</div>
</template>

<script>
export default {
	name:'TheThemes',
	data(){
		return{
			themeArray:[
				'서점 모음',
				'휴일에 가기 좋은 곳',
				'데이트 장소 리스트'
			]
		}
	}
}
</script>

<style scoped>
.theme-item{
	border-radius: 4px;
	box-shadow: 2px 2px 4px rgb(0 0 0 / 30%);
	border-radius: 3px;
	display: inline-block;
	padding:10px;
	margin:3px;
	cursor: pointer;
	background-color: #FFFFF0;
}
</style>