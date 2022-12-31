<template>
	<div>
		<div class="category-tag-box" v-for="(category, idx) in category.categoryArr" :key="idx">
			<div class="category-tag-item">
				<div class="head-para"># {{ category.phrase }}</div>
				<div 
					class="tag" 
					:class="selectTag.indexOf(tag) !== -1 ? 'selected' : ''"
					v-for="(tag, idx) in category.tag" 
					:key="idx" 
					@click="selectTagF(tag)"
				>
					{{ tag }}
				</div>
			</div>	
		</div>
	</div>
</template>

<script>
export default {
	name: 'AddPlaceCategoryBody',
	props:{
		category:Object
	},
	data (){
		return {
			selectTag:[]
		}
	},
	methods:{
		selectTagF(tag){
			const addSelectTagArr = [...this.selectTag]
			const idxTag = addSelectTagArr.indexOf(tag)

			if (idxTag === -1 ){
				addSelectTagArr.push(tag)
				this.selectTag = addSelectTagArr
			} else{
				addSelectTagArr.splice(idxTag, 1)
				this.selectTag = addSelectTagArr
			}
			
			this.$emit('selectTag', this.selectTag)
		}
	},
	watch:{
        "category.categoryArr": function(){
            this.selectTag = []
        }
	}

}
</script>

<style scoped>

.tag{
	border:none;
	border-radius: 4px;
	box-shadow: 1px 1px 4px rgb(0 0 0 / 20%);
	display: inline-block;
	padding:4px;
	margin:4px;
	cursor: pointer;
}

.tag:hover,.selected{
	background-color: #B9B9FF;
	color:aliceblue
}

.head-para{
	font-size:13px;
}


</style>