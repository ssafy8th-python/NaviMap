<template>
  <div id="add_theme">
    <!-- 버튼 -->
    <button id="button" @click="is_clicked">테마 생성</button>
    <!-- 모달 -->
    <div v-if="is_btn_click">
      <div class="modal-mask">
        <div class="modal-wrapper">
          <div class="modal-container ">
            <!-- 모달 내부 content  -->
            <AddThemeDetail
            @is-clicked = "is_clicked"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AddThemeDetail from '@/components/theme/AddThemeDetail'
export default {
    name:'AddTheme',
    components:{AddThemeDetail},
    data(){
      return{
        is_btn_click : false,
      }
    },
    methods:{
        button_click(){
        // 숨기기
            const modal_like = document.getElementById("modal_like")
             if (modal_like.style.visibility !== "visible") {
            modal_like.style.visibility = "visible";}
        // 보이기 (visibility: visible)
            else {
                modal_like.style.visibility = "hidden";
      }
        },
        is_clicked(){
          this.is_btn_click = !this.is_btn_click
        }
    }
}
</script>

<style scoped>
    #add_theme{
    position:fixed;
    top:80%;
    left:90%;
    }
    #button{
    height: 100px;
    width: 100px ;
    border-radius: 50%;
    border: 2px black solid;
    }
 
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
    width:620px;
    max-width:620px;
    height: 90%;
    padding: 20px;
    background-color: white;
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