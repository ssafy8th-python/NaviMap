<template>
	<div>
		<h3>지도</h3>
		<div>
			<div class="map-item">

			</div>
		</div>
	</div>
</template>

<script>
export default {
	name:'TheMap'
}
</script>

<style scoped>
.map-item{
	height:160px;
	border-radius: 10px;
	background-image: url('@/assets/map-example.jpg');
	cursor: pointer;
}

</style>