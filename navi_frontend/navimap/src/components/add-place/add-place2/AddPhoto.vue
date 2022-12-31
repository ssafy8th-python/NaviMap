<template>
	<div class="add-photo-page">
		<div class="page2-header-para">이 장소에 대한 사진을 등록해주세요</div>
		<div class="add-photo-container">
			<div class="add-photo-box">
				<div class="empty-photo-msg" v-if="!upLoadImage">
					등록된 사진이 없습니다!
				</div>
				<div class="img-box" v-else>
					<img :src="upLoadImage" >
					<div class="photo-delete" @click="deletePhoto">
						&#10005;
					</div>
				</div>
			</div>
			<label for="file" class="photo-submit-btn">
				<span>사진 등록하기</span>
				<input type="file" name="file" id="file" ref="IMG" @change="imageUpload">
			</label>
		</div>
	</div>
</template>

<script>

export default {
	name:'AddPhoto',
	data() {
		return {
			upLoadImage : '',
		}
	},
	methods:{
		deletePhoto(){
			this.upLoadImage = ''
			this.$emit('getImage', '')
		},
		imageUpload() {
			const image = this.$refs.IMG.files[0]
			this.upLoadImage = URL.createObjectURL(image)
			
			this.$emit('getImage', image)
		}
	}
}
</script>

<style scoped>
.add-photo-page{
	margin-top:30px;
}
.add-photo-container{
	display: flex;
	flex-direction: column;
	align-items: center;
}
.add-photo-box{
	width:100%;
	height:160px;
	border-radius: 8px;
	background-color: gainsboro;
	display: flex;
	position: relative;
}

.photo-submit-btn{
	border:none;
	width:90%;
	cursor: pointer;
	font-size:16px;
	border-radius: 5px;
	padding: 10px;
	background-color:#D3D3FF;
	color: white;
	font-weight: bold;
	margin-top: 20px;
	text-align: center;
}
h3{
	text-align: center;
}
.empty-photo-msg{
	margin:auto;
	font-size:14px;
	font-weight: bold;
	color:gray
}

#file {
  display: none;
}
.img-box{
	width: 100%;
	height: 100%;
}

img{
	width:100%;
	height: 100%;
}

.photo-delete{
	position: absolute;
	cursor: pointer;
	right: 10px;
	top: 5px;
}
</style>