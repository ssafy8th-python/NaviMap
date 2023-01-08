<!-- 검색창 컴포넌트 -->
<template>
  <!-- 여백용 -->
  <v-row>
    <v-col
      cols="4"
      sm="4"
    >
    </v-col>

    <!-- 검색창 -->
    <v-col 
    style="width:40%;"
    cols="3"
    sm="3"
    >
      <v-text-field
      v-model="search"
      label="검색어를 입력해 주세요."
      clearable
      >
      </v-text-field>
    </v-col>

    <!-- 돋보기 버튼 -->
    <v-col
    cols="3"
    sm="3"
    style="display:flex; padding-left: 0px;"
    >
      <button><v-icon>mdi-magnify</v-icon></button>
    </v-col>

    <!-- 여백용 -->
    <v-col
      cols="4"
      sm="4"
    >
    </v-col>
  </v-row>
</template>


<script>
  export default {
    name : 'SearchBar',
    components : {
    },
  }
</script>