<!-- 일일 추천 컴포넌트 -->

<template>
  <v-card
    :loading="loading"
    class="mx-auto my-12"
    max-width="374"
  >
    <template slot="progress">
      <v-progress-linear
        color="deep-purple"
        height="10"
        indeterminate
      ></v-progress-linear>
    </template>

    <v-card-title style="text-align: center; padding-bottom: 0px;">오늘의 추천</v-card-title>
    <v-card-text style="text-align: right; padding-bottom: 0px;">22-12-23</v-card-text>
    <v-divider class="mx-4" style="margin-top: 2px; margin-bottom: 13px;"></v-divider>

    <v-card
    class="mx-auto"
    max-width="344"
    >
    <v-img
      height="250"
      src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
    ></v-img>
    <v-card-text style="padding-bottom:0px;">
      <div style="padding: 3px; text-align: center;">🍔🍕🍟</div>
      <div style="padding: 3px; text-align: center;">카공하기 좋은 카페</div>
      <div style="padding: 3px; text-align: center;">😀여도현</div>

    </v-card-text>
    <div style="text-align:right; padding: 16px; padding-top: 0px; padding-bottom: 5px;">      
      <v-btn
        icon
        color="pink"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      숫자
    </div>

    
  </v-card>
    <div style="padding:5px;">← →</div>
  </v-card>
</template>

<script>
export default {
  name : 'TodayRecommended',
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
