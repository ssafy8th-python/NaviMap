<template>
	<div>
		<div class="head-para">지도</div>
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
	width: auto;
	border-radius: 10px;
	background-image: url('@/assets/map-example.jpg');
	cursor: pointer;
	background-size:cover;
	background-repeat: no-repeat;
}

</style>