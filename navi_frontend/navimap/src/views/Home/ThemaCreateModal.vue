<template>
  <div>
    <b-modal id="modal-center" centered size="lg" hide-footer>
      <template #modal-title>
        <h2>테마 지도 만들기</h2>
      </template>
      <div class="d-block text-center">
        <h4 style="text-align:left; padding-bottom: 10px;">테마명</h4>
        <v-col style="padding:0px;">
          <v-textarea
            label="ex) 광주 양림동 귀여운 카페"
            auto-grow
            outlined
            rows="1"
            row-height="15"
          ></v-textarea>
        </v-col>
        <h4 style="text-align:left;">테마명 작성과 관련된 안내 사항</h4>
        <div style="padding:10px;">
          <p style="text-align:left">ex) 구체적인 특징이나 상황이 들어간 테마명을 추천해요!</p>
          <li style="text-align:left">예 : 2~3명이 술 마시며 이야기하기 좋은 곳</li>
          <li style="text-align:left">예 : 하루종일 있어도 눈치 보이지 않는 카페</li>
        </div>
        <br>
        <h4 style="text-align:left; padding-bottom: 10px;">키워드</h4>
        <br>
        <h4 style="text-align:left; padding-bottom: 10px;">미리보기</h4>
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
      <b-button class="mt-3" block style="display:block; margin:auto;">저장하기</b-button>
    </b-modal>
  </div>
</template>

<script>
export default {
  name : 'ThemaCreateModal',
  data () {
    return {
    }
  },
  methods : {

  },
}
</script>
