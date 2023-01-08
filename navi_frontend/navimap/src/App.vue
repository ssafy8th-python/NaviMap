<template>
  <div id="app">

    <!-- navbar -->
    <!-- <nav class="navbar navbar-light bg-light">
    <div class="container">
      <a class="navbar-brand" href="#">
      <img src="@/assets/Navimap_logo.png" style="width:150px; text-align:left;">      </a>
    </div>
    </nav> -->
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#"><img src="@/assets/Navimap_logo.png" style="width:150px; text-align:left;"></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-end" id="navbarNavDropdown">
      <ul class="navbar-nav" >
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">🏠홈</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">🦋테마보기</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">🌼나의 테마</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">⚙️마이페이지</a>
        </li>
        <li class="nav-item">
          <span class="nav-link" @click="kakaoLogin">🔑로그인</span>
        </li>
        <!-- <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown link
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li> -->
      </ul>
    </div>
  </div>
</nav>


    <!-- 타이틀 -->
    <h1 style="text-align:center; font-size:100px;"> 나비지도 </h1>
    <h4 style="text-align:center;"> 나만의 비밀 지도 </h4>
    <!-- 검색창 -->
    <SearchBar/>

    <!-- <router-view></router-view> -->

    <!-- 추천카드들 -->
    <v-row>
      <TodayRecommended/>
      <PersonalRecommended/>
    </v-row>
    <br>
    <v-divider></v-divider>

    <!-- 최근 만든 테마 & 인기 있는 테마 카드 창 -->
    <RecentThema/>
    <PopularThema/>
    
    <!-- 전체 테마 보기 버튼 -->
    <v-btn 
      style="margin:auto; width: 96.5%; display: block;"
      >
      전체 테마 보기
    </v-btn>
    <br>
    
    <!-- 테마 추가 버튼 -->
    <div>
      <v-btn
        id="show-btn" @click="$bvModal.show('bv-modal-example')"
        v-b-modal.modal-center
        class="mx-2"
        fab
        dark
        style="position:fixed; left:92%; right:0px; bottom:5%;"
      >
        <v-icon>
            mdi-plus
        </v-icon>
      </v-btn>

      <!-- 테마 작성 모달 -->
      <ThemaCreateModal/>
      
      <!-- 맨 위로 버튼 -->
      
      
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import TodayRecommended from '@/views/Home/TodayRecommended.vue'
import PersonalRecommended from '@/views/Home/PersonalRecommended.vue'
import RecentThema from '@/views/Home/RecentThema.vue'
import PopularThema from '@/views/Home/PopularThema.vue'
import ThemaCreateModal from '@/views/Home/ThemaCreateModal.vue'
import SearchBar from '@/views/Home/SearchBar.vue'

export default {
  name: 'App',
  components: {
    TodayRecommended,
    PersonalRecommended,
    RecentThema,
    PopularThema,
    ThemaCreateModal,
    SearchBar,
  },
  data () {
  },
  methods:{
    kakaoLogin(){
      axios({
        method:'get',
        url:"http://127.0.0.1:8000/api/v1/accounts/kakao/login/getcode/",
      })
        .then((res)=>{
          window.location.href="http://127.0.0.1:8000/api/v1/accounts/kakao/login/getcode/"
        })
        .catch((err)=> {console.log(err)})
    }
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
