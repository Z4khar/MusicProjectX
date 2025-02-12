<template>
  <div>
    <h2>Треки</h2>
    <div class="track-container">
      <div class="track" v-for="track in tracks" :key="track.id">
        <img :src="track.cover_image" @click="playTrack(track.audio_file)" alt="Cover" />
        <p>{{ track.title }} - {{ track.artist }}</p>
        <button @click="addToFavorites(track.id)">Добавить в избранное</button> <!-- Кнопка для добавления в избранное -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      tracks: [] // Массив для хранения треков
    };
  },
  created() {
    this.fetchTracks(); // Получение треков при создании компонента
  },
  methods: {
    fetchTracks() {
      axios.get('http://127.0.0.1:8000/api/tracks/') // Запрос к API
        .then(response => {
          this.tracks = response.data; // Сохраняем полученные треки
        })
        .catch(error => {
          console.error('Ошибка при получении треков:', error);
        });
    },
    playTrack(audioFile) {
      this.$emit('play', audioFile); // Передаем путь к аудиофайлу в родительский компонент
    },
    addToFavorites(trackId) {
      const userId = 1; // Здесь нужно получить ID текущего пользователя
      axios.post('http://127.0.0.1:8000/api/favorite-tracks/', {
        user: userId,
        track: trackId
      })
      .then(response => {
        console.log('Трек добавлен в избранное:', response.data);
      })
      .catch(error => {
        console.error('Ошибка при добавлении в избранное:', error);
      });
    }
  }
};
</script>
