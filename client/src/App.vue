<template>
  <div id="app">
    <header>
      <h1>Музыкальная библиотека</h1>
    </header>

 



    <Vinyl /> <!-- Анимация виниловой пластинки -->
    <AnimatedText /> <!-- Анимированный текст -->
    <Player :currentTrack="currentTrack" /> <!-- Плеер под заголовком -->
    <Track @play="currentTrack = $event" />
    

    
    <footer>
      <p>© 2023 Музыкальная библиотека</p>
    </footer>
  </div>
</template>

<script>

import AnimatedText from './components/AnimatedText.vue';
import Track from './components/Track.vue'; 
import Player from './components/Player.vue'; 
import Vinyl from './components/Vinyl.vue'; // Импортируем компонент виниловой пластинки


export default {
  components: {
    Track,
    Player,
    AnimatedText,
    Vinyl // Добавляем компонент Vinyl
  },
  data() {
    return {
      currentTrack: '' // Текущий трек для воспроизведения
    };
  }
};


</script>


