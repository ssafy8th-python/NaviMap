<template>
  <div class="modal-mask">
    <div class="modal-wrapper">
      <div class="modal-container ">
        <header class="d-flex justify-content-end">
          <button type="button" class="btn btn-outline-danger" @click="$emit('close',reviewId)">X</button>
        </header>
        <body class="body">
         
        </body>
        <footer>
          
        </footer>
      </div>
    </div>
  </div>
</template>

<script>

export default {
    name:'ReviewComment',
    data(){
      return{

      }
    },
    components:{
    },
    props:{
    },
   
    
}
</script>

<style scoped>

.modal-mask{
  position: fixed;
  z-index: 10;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  transition: opacity 0.3s ease;
  color:black;
}

.modal-wrapper{
  width: 100%;
  height: 100%;
  align-items: center;
	display: flex;
	justify-content: center;
	align-items: center;
}

.modal-container{
  width: 70%;
  height: 70%;
  padding: 20px 30px;
  background-color: #263859;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  border-radius: 10px;
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
  overflow:auto;
  color:aliceblue
}

.body{
  min-height: 85%;
  background-color: #263859;

}
.footer{
  background-color: #263859;

}

ul{
  justify-content: center;
}

::-webkit-scrollbar {
  display: none;
}
</style>
