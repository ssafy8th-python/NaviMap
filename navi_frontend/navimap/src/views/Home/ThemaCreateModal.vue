<template>
  <div>
    <b-modal id="modal-center" centered size="lg" hide-footer>
      <!-- 타이틀 -->
      <template #modal-title>
        <h2 style="text-align:center; margin-bottom:30px;"> <b>테마 지도 만들기</b></h2>      </template>

      <!-- 테마 이름 인풋창 -->
      <div class="d-block text-center">
        <h4 style="text-align:left; padding-bottom: 10px;">테마명</h4>
        <v-col style="padding:0px;">
          <v-textarea
            label="ex) 광주 양림동 귀여운 카페"
            auto-grow
            outlined
            maxlength="32"
            rows="1"
            row-height="15"
            v-model="themename"
          ></v-textarea>
        </v-col>
  
              </div>
 
      <!-- 이모지 -->
      <p style="font-size:18px;margin-bottom:8px;"><b>이모지</b></p>  
      <div class="form-item" style="margin-bottom:8px;">
        <input 
        class="input_icon"
        type="text"
        maxlength='6'
        placeholder="ex) 🎄 "
        v-model="themeicon"
        >    
        <span> 
          <button 
          class="Addemoji"  
          onclick="window.open('https://www.emojiengine.com/ko/keyboard/')" > 
          + 이모지
        </button>
        </span>
      </div>
      <br>
      
      <!-- 안내사항 -->
      <h4 style="text-align:left;">테마명 작성과 관련된 안내 사항</h4>
      <div style="padding:10px;">
        <p style="text-align:left">ex) 구체적인 특징이나 상황이 들어간 테마명을 추천해요!</p>
        <li style="text-align:left">예 : 2~3명이 술 마시며 이야기하기 좋은 곳</li>
        <li style="text-align:left">예 : 하루종일 있어도 눈치 보이지 않는 카페</li>
      </div>
      <br>

      <!-- 키워드 -->
      <h4 style="text-align:left; padding-bottom: 10px;">키워드</h4>
      <v-card class="mx-auto">
        <!-- 인원 -->
        <v-card-subtitle style="padding-bottom:0px;">
          <p class="text-h3 text--primary" >
            <b># 인원</b>
          </p>
        </v-card-subtitle>
        <div style="margin-left:20px;">
          <v-btn
          style="margin-right:10px;"
          rounded
          >
          🧍 1인
          </v-btn>
          <v-btn
          style="margin-right:10px;"
          rounded
          >
          🧑‍🤝‍🧑 다수
          </v-btn>
        </div>
       <!-- 특징 -->

        <v-card-subtitle style="padding-bottom:0px;">
          <p class="text-h3 text--primary" >
            <b># 특징</b>
          </p>
        </v-card-subtitle>
        <div style="margin-left:20px;">

          <v-btn
          style="margin-right:10px; margin-bottom:10px;"
          rounded
          >
          🤫 조용한
          </v-btn>

          <v-btn
          style="margin-right:10px; margin-bottom:10px;"
          rounded
          >
          🌞 햇살좋은
          </v-btn>
          <v-btn
          style="margin-right:10px; margin-bottom:10px;"
          rounded
          >
          📢 붐비는
          </v-btn>
          <v-btn
          style="margin-right:10px; margin-bottom:10px;"
          rounded
          >
          🧹 깔끔한
          </v-btn>
          <v-btn
          style="margin-right:10px; margin-bottom:10px;"
          rounded
          >
          👖 빈티지
          </v-btn>
          <v-btn
          style="margin-right:10px; margin-bottom:10px;"
          rounded
          >
          💪 건강한
          </v-btn>
          <v-btn
          style="margin-right:10px; margin-bottom:10px;"
          rounded
          >
          📷 인스타감성
          </v-btn>
          <v-btn
          style="margin-right:10px; margin-bottom:10px;"
          rounded
          >
          🚗 주차편한
          </v-btn>
          <v-btn
          style="margin-right:10px; margin-bottom:10px;"
          rounded
          >
          🥅 넓은
          </v-btn>
          <v-btn
          style="margin-right:10px; margin-bottom:10px;"
          rounded
          >
          🙋 친절한
          </v-btn>
          <v-btn
          style="margin-right:10px; margin-bottom:10px;"
          rounded
          >
          💡 밝은
          </v-btn>
          <v-btn
          style="margin-right:10px; margin-bottom:10px;"
          rounded
          >
          🔦 어두운
          </v-btn>
          <v-btn
          style="margin-right:10px; margin-bottom:10px;"
          rounded
          >
          😋 맛있는
          </v-btn>
          <v-btn
          style="margin-right:10px; margin-bottom:10px;"
          rounded
          >
          💰 가성비 좋은
          </v-btn>
        </div>
        <br>
      </v-card>

      <br>
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
      </div>
      <br>
      <!-- 저장하기 버튼 -->
      <b-button class="mt-3" block style="display:block; margin:auto;">저장하기</b-button>
    </b-modal>
  </div>
</template>

<script>
export default {
  name : 'ThemaCreateModal',
  data () {
    return {
      themename:'',
      themeicon:'',
    }
  },
  methods : {

  },
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