<template>
	<div class="loading-page">
		<div class="content">
			<div class="herbe">
				<div></div>
				<div></div>
				<div></div>
				<div></div>
			</div>
			</div>
		</div>
</template>

<script>
export default {
	name:"LoadingPage"
}
</script>

<style scoped>
.loading-page{
	position: fixed;
	display: flex;
	justify-content: center;
	align-content: center;
	align-items: center;
	width: 100%;
	height: 100%;
	text-align: center;
	background-color: rgba(1,1,1,0.9);
	
	z-index: 10;
}

.content{
	display: inline-block;
}
.herbe {
  position: relative;
}

.herbe > div {
  position: absolute;
  width: 1.5rem;
  height: 1.5rem;
  background: yellow;
  border-radius: 100% 100% 100% 5%;
  animation: fade .8s infinite;
}

.herbe > div:nth-child(2) {
  border-radius: 100% 100% 5% 100%;
  left: -25px;
  animation-delay: .2s;
}

.herbe > div:nth-child(3) {
  border-radius: 100% 5% 100% 100%;
  left: -25px;
  top: 25px;
  animation-delay: .4s;
}

.herbe > div:nth-child(4) {
  border-radius: 5% 100% 100% 100%;
  top: 25px;
  animation-delay: .6s;
}


@keyframes scale {
  from{transform: rotate(-20deg) scale(1)}
  to{transform: rotate(-20deg) scale(0)}
}

@keyframes butterfly {
  form{transform: skewY(0deg);}
  to{transform: skewY(15deg);}
}

@keyframes _butterfly {
  form{transform: skewY(0deg);}
  to{transform: skewY(-15deg);}
}

@keyframes bouncing {
  from{transform: translateY(0);opacity: 1;}
  to{transform: translateY(-1rem);opacity: .1;}
}

@keyframes spin {
  from{transform: rotate(0deg)}
  to{transform: rotate(360deg)}
}

@keyframes fade {
  from{opacity: 1;}
  to{opacity: .1;}
}

</style>