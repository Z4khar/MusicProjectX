<template>
  <br><br><br><br><br>
  <div class="vinyl-wrapper">
    <div class="vinyl"></div>
    <div class="record-sleeve"></div> 
  </div>
</template>

<script>
export default {
  name: 'Vinyl',
};
</script>

<style>
*,
*:before,
*:after {
  box-sizing: border-box;
}

body {
  background: lightgrey;
}

.vinyl-wrapper {
  position: relative;
  display: block;
  margin: 0 auto; /* Центрируем по горизонтали */
  width: 270px; /* Увеличиваем ширину */
  height: 270px; /* Увеличиваем высоту */
  transform: rotateX(10deg) rotateZ(-20deg);
}

.record-sleeve {
  width: 300px; /* Увеличиваем ширину */
  height: 300px; /* Увеличиваем высоту */
  position: absolute;
  background: radial-gradient(circle at 49% 50%, transparent 27%, #960f0f 10%);
  border-radius: 2px;
  
  z-index: 10;
}

.vinyl {
  position: absolute;
  transform: translate(120px); /* Позиционируем винил */
  top: 100px; /* Позиционируем винил */
  background: #f7aac7;
  width: 90px; /* Увеличиваем ширину */
  height: 90px; /* Увеличиваем высоту */
  border-radius: 50%;
  border: solid #e7568d;
  border-width: 40px 0px;
  border-left: 0;
  animation: pull-out 1.3s 2s ease-out forwards, spin 1.3s 4s linear infinite;
  box-shadow: 0px 0px 3px #f7aac7, 0px 0px 0px 10px #ea6a9b, 0px 0px 15px #f7aac7, 0px 0px 0px 16px #000, 0px 0px 0px 17px #252424, 0px 0px 0px 18px #000, 0px 0px 0px 19px #313030, 0px 0px 0px 20px #000, 0px 0px 0px 21px #3a3838, 0px 0px 0px 22px #000, 0px 0px 0px 23px #2b2a2a, 0px 0px 0px 24px #000, 0px 0px 0px 25px #313030, 0px 0px 0px 26px #000, 0px 0px 0px 27px #313030, 0px 0px 0px 28px #000, 0px 0px 0px 29px #333333, 0px 0px 0px 30px #000, 0px 0px 0px 31px #333232, 0px 0px 0px 32px #000, 0px 0px 0px 33px #4c4a4a, 0px 0px 0px 34px #000, 0px 0px 0px 35px #2f2e2e, 0px 0px 0px 36px #000, 0px 0px 0px 37px #252424, 0px 0px 0px 38px #000, 0px 0px 0px 39px #2f2e2e, 0px 0px 0px 40px #000, 0px 0px 0px 41px #2f2e2e, 0px 0px 0px 42px #000, 0px 0px 0px 55px #2f2e2e, 0px 0px 0px 56px #000, 0px 0px 0px 57px #2f2e2e, 0px 0px 0px 58px #cecece, 0px 0px 0px 59px #2f2e2e;
}

.vinyl:before {
  content: "";
  position: absolute;
  width: 6px;
  height: 6px;
  background: white;
  top: calc(50% - 3px);
  left: calc(50% - 3px);
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
    left: 300px;
  }
  100% {
    transform: rotate(360deg);
    left: 300px;
  }
}

@keyframes pull-out {
  0% {
    transform: translateX(69px);
  }
  100% {
    transform: translateX(300px);
  }
}
</style>
