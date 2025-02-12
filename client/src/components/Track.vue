<template>
  <div>
    <h2>Треки</h2>
    <p>Треки: {{ tracks.length }}</p>
    <div class="track-container">
      <div class="track" v-for="track in tracks" :key="track.id">
        <img :src="track.cover_image" @click="playTrack(track.audio_file)" alt="Cover" />
        <p>{{ track.title }} - {{ track.artist }}</p>
        <button @click="addToFavorites(track.id)">Добавить в избранное</button>
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
      console.log('ttt');
      axios.get('http://127.0.0.1:8000/api/tracks/') // Запрос к API
        .then(response => {
          console.log('Треки', response.data);
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

<style>
 .track-container {
    display: flex; /* Используем flexbox для отображения треков */
    flex-wrap: wrap; /* Оборачиваем элементы на новой строке */
    justify-content: space-between; /* Распределяем треки равномерно */
    gap: 20px; /* Отступы между элементами */
  }
  
  .track {
    background-color: #fff; /* Белый цвет фона для обложки */
    border-radius: 15px; /* Скругленные углы */
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Тень */
    overflow: hidden; /* Скроем элементы, выходящие за границы */
    text-align: center; /* Центрирование текста внутри трека */
    cursor: pointer; /* Курсор в виде указателя */
    transition: transform 0.2s; /* Плавный переход для эффекта */
    flex: 1 1 calc(25% - 20px); /* 4 трека в ряд с учетом отступов */
  }
  
  .track:hover {
    transform: scale(1.05); /* Увеличение при наведении */
  }
  
  .track img {
    width: 100%; /* Ширина обложки 100% */
    border-radius: 15px 15px 0 0; /* Скругление только верхних углов */
  }
  
  .track p {
    margin: 10px 0; /* Отступы для текста */
    color: #333; /* Цвет текста */
  }

button {
  background-color: #007bff; /* Цвет фона кнопки */
  color: white; /* Цвет текста кнопки */
  border: none; /* Убираем рамку */
  border-radius: 5px; /* Скругленные углы кнопки */
  padding: 10px 15px; /* Отступы внутри кнопки */
  cursor: pointer; /* Курсор в виде указателя */
  transition: background-color 0.3s; /* Плавный переход цвета фона */
}

button:hover {
  background-color: #0056b3; /* Цвет фона кнопки при наведении */
}
</style>
