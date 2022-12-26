<template>
  <div id="modal_content">
    <!-- 제목 -->
    <h2 style="text-align:center;margin-bottom:30px;"> <b>테마 지도 만들기 </b> </h2>
    <!-- 내용-->
    <!-- 테마명 -->
    <p style="font-size:18px;margin-bottom:8px;"><b>테마명</b></p>
    <div class="form-item" style="margin-bottom:8px;">
    <input 
    class="input_themename"
    type="text"
    maxlength='32'
    placeholder="ex) 흐린 날 책 읽기 좋은 서울의 독서 공간"
    v-model="themename"
    >
    <span style="color:#aaa;font-size:12px;" id="counter"> (0 / 32)</span>
    </div>
    <!-- 안내사항 -->
    <!-- 아이콘 -->
    <p style="font-size:18px;margin-bottom:8px;"><b>아이콘</b></p>  
    <div class="form-item" style="margin-bottom:8px;">
    <input 
    class="input_icon"
    type="text"
    maxlength='6'
    placeholder="ex) 🎄 "
    v-model="themeicon"
    >    <span> <button class="Addemoji"  onclick="window.open('https://www.emojiengine.com/ko/keyboard/')" > + 
    아이콘</button></span>

    </div>

    <!-- 키워드 -->
    <p style="font-size:18px;"><b>키워드</b></p>

    <div style="margin-left:10px;">
      <!-- 인원 -->
      <p style="font-size:14px;"> <b>#인원</b> </p>

      <!-- 특징 -->
      <p style="font-size:14px;"> <b>#특징</b> </p>
    </div>
    <!-- 미리보기 -->
    <p style="font-size:18px;"><b>미리보기</b></p>
    <div class="theme_preview">
      <div class="iconbox">
        <p class="themeicon">{{themeicon}}</p>
      </div>
      <!-- 제목 박스 -->
      <div class="namebox">
        <p class="themename"><b>{{themename}}</b></p>
      </div>
      <!-- 하위 정보  -->
      <div class="bottombox">
        <p style="font-size:14px;text-align:center;margin-bottom:1px;"> ㅇㅇㅇ님</p>
        <div class="infobox" style="margin:auto;">
          <div style="text-align:center;">
            <!-- 큐레이터 명수 -->
            <span style="font-size:12px;text-align:center;color:grey;margin:a;"> 🧑🏻‍🤝‍🧑🏻 6명</span> 
            <!-- 장소 -->
            <span style="font-size:12px;text-align:center;color:grey;"> <b>｜</b>🏡 10개 </span>
          </div>
        </div>
      </div>
      <!-- 생성자이름 -->
    </div>
    <!-- 생성하기 -->
    <button class="Addbutton" @click="is_clicked"> 테마 만들기 </button>
  </div>
</template>

<script>

export default {
  name:'AddThemeDetail',
  data(){
    return{
      themename:'',
      themeicon:'',

    }
  },
  methods:{
    is_clicked(){
      this.$emit('is-clicked')
    },
    
  }
}
</script>

<style scoped>
#modal_content{
  font-family:"Pretendard-Regular";
  color:black;
}
/* 테마명 작성 */
.input_themename{
  width:350px;
  height:45px;
  border: 1px solid #969696;
  padding:10px;
  font-size:14px;
}
.form-item input:focus{
  border:none;
  outline:1px solid #f68335;
}

.input_icon{
  width:350px;
  height:45px;
  border: 1px solid #969696;
  padding:10px;
  font-size:14px;
}
input::placeholder {
  color: #969696;
  font-size:14px;
}

/* 아이콘 */
.Addemoji{
  text-align: center;
  width:70px;
  height: 30px;
  border: 2px solid lightgrey;
  color:gray;
  border-radius: 50px;
  font-size:12px;
}
.Addemoji:hover{
  text-align: center;
  width:70px;
  height: 30px;
  border:none;
  border: 2px solid rgb(49, 49, 49);
  color:rgb(31, 31, 31);
  border-radius: 50px;
  font-size:12px;
  font-weight: 700;
}
/* 미리보기 */
.theme_preview{
  width:300px;
  height: 165px;
  border: 2px solid lightgrey;
  border-radius: 50px;
  margin:auto;
  box-shadow: 1px 1px 10px #969696;
}
.themeicon{
  text-align: center;
  font-size:17px;
  padding:5px;
}
.iconbox{
  height: 25px;
  margin-top:10px;
}
.themename{
  font-size:15px;
}
.namebox{
  width:200px;
  height: 55px;
  margin:auto;
  margin-top:10px;
  text-align: center;
  padding:5px;
}
/* 생성 */
.Addbutton{
  width:120px;
  height:35px;
  color:white;
  background-color: #9a09d3;
  border-radius: 20px;
  margin-top:20px;
  margin-left: 40%;

}
@font-face {
    font-family: 'Pretendard-Regular';
    src: url('https://cdn.jsdelivr.net/gh/Project-Noonnu/noonfonts_2107@1.1/Pretendard-Regular.woff') format('woff');
    font-weight: 400;
    font-style: normal;
}


</style>