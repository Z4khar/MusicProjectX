<template>
     <div>
    <h2>Избранные Треки</h2>
    <div class="track-container">
      <div class="track" v-for="track in favoriteTracks" :key="track.id">
        <img :src="track.cover_image" @click="playTrack(track.audio_file)" alt="Cover" />
        <p>{{ track.title }} - {{ track.artist }}</p>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      favoriteTracks: [] // Массив для хранения избранных треков
    };
  },
  created() {
    this.fetchFavoriteTracks(); // Получение треков при создании компонента
  },
  methods: {
    fetchFavoriteTracks() {
      axios.get('http://127.0.0.1:8000/api/favorite-tracks/') // Запрос к API для получения избранных треков
        .then(response => {
          this.favoriteTracks = response.data; // Сохраняем полученные треки
        })
        .catch(error => {
          console.error('Ошибка при получении треков:', error);
        });
    },
    playTrack(audioFile) {
      this.$emit('play', audioFile); // Передаем путь к аудиофайлу в родительский компонент
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
</style>
