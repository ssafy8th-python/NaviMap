<template>
  <div class="modal-mask">
    <div class="modal-wrapper">
      <div class="modal-container ">
        <AddPlace1
          v-if="modalPage === 1"
          @netxPage="changePage1"
        />
        <AddPlace2
          v-if="modalPage === 2"
          @saveData="saveData"
        />
        
      </div>
    </div>
  </div>
</template>

<script>
import AddPlace1 from './AddPlace1.vue'
import AddPlace2 from './AddPlace2.vue'

export default {
    name:'TheModal',
    data(){
      return{
        modalPage: 1,
        savePlaceData: {
          category: '',
          selectedTagArr:[],
          memoryLog:{},
          photo:''
        }
      }
    },
    components:{
      AddPlace1,
      AddPlace2,
    },
    props:{
    },
    methods:{
      changePage1(payload){
        this.modalPage=payload.page
        this.savePlaceData.category = payload.category
        this.savePlaceData.selectedTagArr = payload.selectedTag
      },
      getReviewContentF(payload){
        this.savePlaceData.memoryLog = payload

        console.log(this.savePlaceData)
      },
      saveData(payload){
        this.savePlaceData.memoryLog = payload.memoryLog
        this.savePlaceData.photo = payload.memoryPhoto

        console.log(this.savePlaceData)
      }
    }
   
    
}
</script>

<style scoped>

.modal-mask{
  position: fixed;
  z-index: 10;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  transition: opacity 0.3s ease;
}

.modal-wrapper{
  width: 100%;
  height: 100%;
  align-items: center;
	display: flex;
	justify-content: center;
	align-items: center;
}

.modal-container{
  width:340px;
  max-width:320px;
  height: 90%;
  padding: 20px;
  background-color: #f8f9fa ;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  border-radius: 10px;
  transition: all 0.3s ease;
  overflow:auto;
}


::-webkit-scrollbar {
  display: none;
}
</style>

<style>
  .head-para{
    font-size:16px;
    margin:8px 5px;
    font-weight: bold;
  }
</style>
