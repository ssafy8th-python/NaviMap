<template>
  <div>
    <h1>와 이게 된다고?</h1>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'LoginView',
  created(){
    const urlParams = new URL(location.href).searchParams;
    const code = urlParams.get('code')
    axios({
      method: 'get',
      url: 'http://localhost:8000/api/v1/accounts/kakao/login/gettoken/',
      params: {code},
      withCredentials: true
    })
      .then((res) => {
        this.$router.push({name: 'MainPage'})
        console.log(res.data.message)
      })
  }
}
</script>

<style>

</style>