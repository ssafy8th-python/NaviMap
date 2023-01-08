<template>
  <div>
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
  </div>
</template>

<script>
import TodayRecommended from '@/views/Home/TodayRecommended.vue'
import PersonalRecommended from '@/views/Home/PersonalRecommended.vue'
import RecentThema from '@/views/Home/RecentThema.vue'
import PopularThema from '@/views/Home/PopularThema.vue'
import SearchBar from '@/views/Home/SearchBar.vue'

export default {
  name: 'MainPage',
  components: {
    TodayRecommended,
    PersonalRecommended,
    RecentThema,
    PopularThema,
    SearchBar,
  },
  data () {
  },
  
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
