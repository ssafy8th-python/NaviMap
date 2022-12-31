<template>
	<div class="detail-page">
		<div class="detail-container">
			<div class="detail-box-container">
				<div class="detail-header-container">
					<div class="header-para">별마당 도서관</div>
					<span>서울특별시 강남구 영동대로 513 스타필드 코엑스몰 B1</span>
				</div>
				<div class="detail-body-container">
						<!-- 가게명 -->
					<div class="detail-main-container">
						<div class="detail-item-container">
							<!-- 지도 -->
							<div class="detail-item">
								<TheMap/>
							</div>

							<!-- 살펴보기 -->
							<div class="detail-item">
								<DetailPhoto/>
							</div>

							<!-- 태그 -->
							<div class="detail-item">
								<TheTag/>
							</div>
						</div>

						<div class="detail-item-container">
							<!-- 테마 -->
							
							<div class="detail-item">
								<TheThemes/>
							</div>
							
							<div>
								<MemoryLogForm/>
							</div>
							<!-- 추억로그들 -->
							<!-- <div class="detail-item">
								<TheMemories/>
							</div> -->

							<!-- 추억로그 남기기 -->
							<!-- <div class="detail-item">
								<MemoryInput/>
							</div> -->
						</div>
					</div>
				</div>
			</div>

		</div>
	</div>
</template>

<script>
import TheMap from '@/components/place-detail/TheMap'
import DetailPhoto from '@/components/place-detail/DetailPhoto'
import TheTag from '@/components/place-detail/TheTag'
import TheThemes from '@/components/place-detail/TheThemes'
// import TheMemories from '@/components/place-detail/TheMemories'
// import MemoryInput from '@/components/place-detail/MemoryInput'
import MemoryLogForm from '@/components/place-detail/memory-log-form/MemoryLogForm'

export default {
	name: 'PlaceDetailView',
	components:{
		TheMap,
		DetailPhoto,
		TheTag,
		TheThemes,
		// TheMemories,
		// MemoryInput,
		MemoryLogForm
	},
}
</script>

<style scoped>
	.header-para{
		font-size:1.7em;
	}
	.detail-page{
		position: fixed;
		z-index: 10;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background-color: rgba(0, 0, 0, 0.3);
		transition: opacity 0.3s ease;
		color:black;
		font-size:13px
	}
	.detail-container{
		max-width:1000px;
		margin:auto;
		height: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.detail-box-container{
		display: flex;
		flex-direction: column;
		width: 80%;
		height: 85%;
		align-items: center;
		justify-content: center;
		background-color: #f8f9fa ;
		box-shadow: 0 2px 8px rgba(0, 0, 0, 0.23);
		border-radius: 10px;
		padding:30px;
	}
	.detail-header-container{
		margin: 0 auto;
		width:100%;
		justify-content: start;
	}
	.detail-body-container{
		width: 100%;
		height: 100%;
		padding-top: 10px;
		transition: all 0.3s ease;
		font-family: Helvetica, Arial, sans-serif;
		overflow:auto;
	}
	.detail-body-container::-webkit-scrollbar{
		display: none;
	}
	.detail-main-container{
		display: flex;
		justify-content: space-between;
		margin:0 auto;
	}

	.detail-item-container{
		display: flex;
		flex-direction: column;
		width: 47%;
	}

	.detail-item{
		min-width:100%;
	}

</style> 

<style>
	.empty{
		background-color: white;
		width:90%;
		padding:20px;
		border-radius: 5px;
		text-align: center;
	}
</style>