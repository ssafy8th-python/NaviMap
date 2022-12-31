<template>
	<div class="add-place-page">
		<header class="header">
			<div class="page2-header-para"> 이 장소에 대한 태그를 선택해주세요 </div>
			<div class="category-box">
				<div 
					class="category-item" 
					@click="selectCategory('food', food)" 
					:class="selectedCategory.name === 'food'? 'selected' : '' "
				>
					<span>FOOD</span>
				</div>
				<div 
					class="category-item" 
					@click="selectCategory('drink', drink)" 
					:class="selectedCategory.name === 'drink'? 'selected' : '' "
				>
					<span>DRINK</span>
				</div>
				<div 
					class="category-item" 
					@click="selectCategory('play', play)" 
					:class="selectedCategory.name === 'play'? 'selected' : '' "
				>
					<span>PLAY</span>
				</div>
			</div>
		</header>
		<body class="body">
			<AddPlaceCategoryBody
				:category='selectedCategory'
				@selectTag ="getSelectTagF"
			/>
		</body>
		<footer class="footer">
			<input 
				type="button" 
				class="submit-category-tag" 
				value="다음으로"
				@click="nextPage"
			>
			</footer>
	</div>
</template>

<script>
import AddPlaceCategoryBody from '../add-place/AddPlaceCategoryBody.vue'

export default {
	name: 'AddPlace1',
	components:{
		AddPlaceCategoryBody
	},
	data() {
		return {
			selectedCategory:{
				name:'',
				categoryArr:[],
				selectTagArr:[],
			},
			food:[
				{
					tag :
					['양식','중식','한식','일식','세계음식','생선','분식','고기','초밥','튀김','디저트','빵','면','채식',],
					phrase:
					'무엇을 먹나요?'
				},
				{
					tag :
					['순한맛','보통맛','매운맛'],
					phrase:
					'맛이 어떤가요?'
				},
				{
					tag :
					['혼자서','연인과','동료와','친구와','아이와','	부모님과'],
					phrase:
					'누구와 함께하나요?'
				},
				{
					tag:
					['친절한','가성비좋은','비싼','뚜벅이','차끌고','조용한','데이트하기 좋은','예쁜 인테리어','아름다운 경치','양이 많은','양이 적은'],
					phrase:
					'분위기와 특징이 어떤가요?'
				},
			],
			drink:[
				{
					tag :
					['커피','차','맥주','위스키','하이볼','칵테일','소주','에이드','스무디','프라페'],
					phrase:
					'무엇을 마시나요?'
				},
				{
					tag :
					['혼자서','연인과','동료와','친구와','아이와','	부모님과'],
					phrase:
					'누구와 함께하나요?'
				},
				{
					tag:
					['친절한','가성비좋은','비싼','뚜벅이','차끌고','조용한','데이트하기 좋은','예쁜 인테리어','아름다운 경치','양이 많은','양이 적은'],
					phrase:
					'분위기와 특징이 어떤가요?'
				},
			],
			play:[
				{
					tag :
					['공부하기','책읽기','일하기','음악듣기','산책하기','	운동하기','사진찍기','대화하기'],
					phrase:
					'무엇을 하나요?'
				},
				{
					tag :
					['혼자서','연인과','동료와','친구와','아이와','	부모님과'],
					phrase:
					'누구와 함께하나요?'
				},
				{
					tag:
					['친절한','가성비좋은','비싼','뚜벅이','차끌고','조용한','데이트하기 좋은','예쁜 인테리어','아름다운 경치','양이 많은','양이 적은'],
					phrase:
					'분위기와 특징이 어떤가요?'
				},
			]
		}
	},
	methods:{
		selectCategory(categoryName, categoryArr) {
			this.selectedCategory.name = categoryName
			this.selectedCategory.categoryArr = categoryArr
		},
		nextPage(){
			const payload = {
				page : 2,
				category : this.selectedCategory.name,
				selectedTag : this.selectedCategory.selectTagArr
			}

			console.log(payload)
			this.$emit('netxPage', payload)
		},
		getSelectTagF(selectedTagArr){
			this.selectedCategory.selectTagArr = selectedTagArr
		}
	},
	created(){
		this.selectCategory('food', this.food)
	}
}
</script>

<style scoped>
.add-place-page{
	height: 100%;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	font-size:13px
}
.header{
	text-align: center;
}
.body{
	height: 80%;
	overflow: auto;
	background-color:#f8f9fa;
	font-size:13px;
}
.footer{
	text-align: center;	
}
.category-box{
	display: flex;
	align-items: center;
	justify-content: space-evenly;
}
.category-item{
	box-shadow: 1px 1px 4px rgb(0 0 0 / 20%);
	border-radius: 5px;
	width:25%;
	height: 40px;
	display: flex;
	cursor: pointer;
}
.category-item > span{
	margin:auto
}
.category-item:hover{
	background-color: skyblue;
	color:aliceblue
}

.submit-category-tag{
	border:none;
	width:80%;
	cursor: pointer;
	font-size:16px;
	border-radius: 5px;
	padding: 10px;
	background-color: #FFA0A0;
	color: white;
	font-weight: bold;
}

.submit-category-tag:hover{
	background-color: #FFC6C6;
}

.selected{
	background-color: skyblue;
	color:aliceblue
}

::-webkit-scrollbar {
  display: none;
}


</style>

<style>
.page2-header-para{
	font-size:17px;
	font-weight: bold;
	margin-bottom:10px;
	text-align: center;
}
</style>