<!-- 인기 있는 테마의 카드 -->
<template>
  <div>
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
</div>

</template>

<script>
export default {
name : 'PopularThema',
data () {
return {
}
},
methods : {

},
}
</script>