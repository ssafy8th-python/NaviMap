<!-- 일일 추천 컴포넌트 -->

<template>
  <v-card
    :loading="loading"
    class="my-12"
    style="margin:30px; margin-right: 30px;"
  >
    <template slot="progress">
      <v-progress-linear
        color="deep-purple"
        height="10"
        indeterminate
      ></v-progress-linear>
    </template>



    <v-card-title 
      style="padding-bottom: 0px; margin-left:30px; margin-right: 30px;">
      <div class="col-8 col-sm-10 col-md-11">인기 있는 테마</div>
      <div class="col-4 col-sm-2 col-md-1">
        <v-btn >전체 보기</v-btn>
      </div>
    </v-card-title>
    <v-divider class="mx-4" style="margin-top: 2px; margin-bottom: 13px;"></v-divider>

    <!-- <div id="app">
      <vue-glide>
        <vue-glide-slide></vue-glide-slide>
      </vue-glide>
    </div> -->

    <vue-glide
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      style="margin:auto;"
      :breakpoints="{3000: {perView: 6}, 1100: {perView: 3}, 600: {perView: 3}}"
    >
      <vue-glide-slide
        style="margin:20px;"
>       <PopularThemaCard/>
      </vue-glide-slide>
    </vue-glide>
    


  </v-card>
</template>

<script>
import PopularThemaCard from '@/views/Home/PopularThemaCard.vue'

export default {
  name : 'PopularThema',
  components : {
    PopularThemaCard,
  },
  data () {
    return {
      loading : false,
      selection : 1,
    }
  },
  methods : {
    reserve () {
      this.loading = true
      setTimeout(() => (this.loading = false), 2000)
    }
  }
}
</script>
