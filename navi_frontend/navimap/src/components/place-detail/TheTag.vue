<template>
	<div>
		<h3>태그</h3>
		<!-- <div class="empty">
			<span>
				태그를 추가해 주세요!
			</span>
		</div> -->
		<div class="tag-item-box">
			<span>
				가성비 좋은
			</span>
		</div>
		<div class="tag-item-box">
			<span>
				술집
			</span>
		</div>
	</div>
</template>

<script>
export default {
	name:'TheTag',
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