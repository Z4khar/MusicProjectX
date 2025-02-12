<template>
  <div id="app">
    <header>
      <h1>Музыкальная библиотека</h1> <!-- Заголовок приложения -->
      <nav> <!-- Начало блока навигации -->
        <router-link to="/">Главная</router-link> <!-- Ссылка на главную страницу -->
        <router-link to="/favorites">Избранные</router-link> <!-- Ссылка на страницу избранных треков -->
      </nav> <!-- Конец блока навигации -->
    </header>

    <Player :currentTrack="currentTrack" /> <!-- Плеер под заголовком -->
    <router-view @play="currentTrack = $event" /> <!-- Используем router-view для отображения компонентов на основе маршрута -->
    <Track />
    <footer>
      <p>© 2023 Музыкальная библиотека</p> <!-- Футер приложения -->
    </footer>
  </div>
</template>

<script>
import Player from './components/Player.vue'; // Импортируем компонент Player
import Track from './components/Track.vue';
export default {
  components: {
    Player,  
    Track
  },
  data() {
    return {
      currentTrack: '' // Переменная для хранения текущего трека
    };
  }
};
</script>

<style>
/* Здесь могут быть стили для приложения */
</style>
