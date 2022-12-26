<template>
  <div id="app">
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
import TodayRecommended from '@/views/Home/TodayRecommended.vue'
import PersonalRecommended from '@/views/Home/PersonalRecommended.vue'
import RecentThema from '@/views/Home/RecentThema.vue'
import PopularThema from '@/views/Home/PopularThema.vue'
import ThemaCreateModal from '@/views/Home/ThemaCreateModal.vue'

export default {
  name: 'App',
  components: {
    TodayRecommended,
    PersonalRecommended,
    RecentThema,
    PopularThema,
    ThemaCreateModal
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
