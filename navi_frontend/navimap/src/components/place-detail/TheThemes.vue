<template>
	<div>
		<h3>테마</h3>
		<div>
			<span class="theme-item">
				경치 좋은 카페
			</span>
			<span class="theme-item">
				공부하기 좋은 카페
			</span>
			<span class="theme-item">
				나만 알고 싶은 명소
			</span>
		</div>
	</div>
</template>

<script>
export default {
	name:'TheThemes',
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