<template>
	<div>
		<div class="head-para">살펴보기</div>
		<div class="photo-container">
			<div class="phto-box">
				<carousel
				:responsive="{0:{items:3,nav:false,dots:false,margin:10}}"
				>
					<img v-for="(img, index) in images" :src="img" :key="index" onclick="window.open(this.src,'asdfo8or','scrollbars=yes,width=417,height=385,top=10,left=20');">
				</carousel>
			
			</div>
		</div>

	</div>
</template>

<script>
import carousel from 'vue-owl-carousel'

export default {
	name: 'DetailPhoto',
	components:{
		carousel
	},
	data() {
		return {
			images: [
        "https://placeimg.com/200/200/any?1",
        "https://placeimg.com/200/200/any?2",
        "https://placeimg.com/200/200/any?3",
        "https://placeimg.com/200/200/any?4",
        "https://placeimg.com/200/200/any?5",
        "https://placeimg.com/200/200/any?6",
        "https://placeimg.com/200/200/any?7",
        "https://placeimg.com/200/200/any?8",
        "https://placeimg.com/200/200/any?9",
        "https://placeimg.com/200/200/any?10",
				
      ]
		}
	}
}
</script>

<style scoped>
	.photo-container{
		height:150px;
		border-radius: 10px;
		display: flex;
		justify-content: center;
		align-items: center;
	}
	
	.phto-box{
		width:100%;
		height: 95%;
		margin:auto;
	}

	img{
		cursor: pointer;
		height:140px;
	}

</style>