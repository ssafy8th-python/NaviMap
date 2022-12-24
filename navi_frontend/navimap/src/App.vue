<template>
  <div id="app">
    <v-row>
      <TodayRecommended/>
      <PersonalRecommended/>
    </v-row>
    <br>
    <v-divider></v-divider>
    <RecentThema/>
    <PopularThema/>
    
    <v-btn 
      block
      style="margin:30px;"
      >
      전체 테마 보기
    </v-btn>
    
    <!-- 테마 추가 버튼 -->
    <v-btn
      class="mx-2"
      fab
      dark
    >
      <v-icon>
        mdi-plus
      </v-icon>
    </v-btn>

  </div>
</template>
<script>
import TodayRecommended from '@/views/Home/TodayRecommended.vue'
import PersonalRecommended from '@/views/Home/PersonalRecommended.vue'
import RecentThema from '@/views/Home/RecentThema.vue'
import PopularThema from '@/views/Home/PopularThema.vue'

export default {
  name: 'App',
  components: {
    TodayRecommended,
    PersonalRecommended,
    RecentThema,
    PopularThema,
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
