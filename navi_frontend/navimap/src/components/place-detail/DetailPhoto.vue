<template>
	<div>
		<h3>살펴보기</h3>
		<div class="photo-container">
			<div class="phto-box">
				<div class="photo-item ex1">				
				</div>

				<div class="photo-item ex2">				
				</div>

				<div class="photo-item ex3">				
				</div>
			</div>
		</div>

	</div>
</template>

<script>
export default {
	name: 'DetailPhoto'
}
</script>

<style scoped>
	.photo-container{
		background-color: white;
		height:150px;
		border-radius: 10px;
	}
	
	.phto-box{
		width:90%;
		height: 100%;
		display: flex;
		justify-content: space-evenly;
		align-items: center;
		margin:auto;
	}

	.photo-item{
		background-color: red;
		width:32%;
		height:80%;

	}

	.ex1{
		background-image: url('@/assets/star1.jpg')
	}

	.ex2{
		background-image: url('@/assets/star2.jpg')
	}
	.ex3{
		background-image: url('@/assets/star3.jpg')
	}
</style>