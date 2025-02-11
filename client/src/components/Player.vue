<template>
  <div class="player-container">
    <audio ref="audio" v-if="currentTrack" class="audio-player" @timeupdate="updateTime">
      <source :src="currentTrack" type="audio/mpeg" />
      Ваш браузер не поддерживает аудиоплеер.
    </audio>
    <!-- Прогресс-бар -->
    <div class="progress-container">
      <div class="custom-progress" @mousedown="startDragProgress">
        <div
          class="progress-bar"
          :style="{ width: `${progress}%` }"
          @click="seekAudio"
        ></div>
      </div>
    </div>
    <!-- Кнопки управления вынесены отдельно -->
    <div class="controls">
      <button class="control-btn prev" @click="prevTrack">Prev</button>
      <button class="control-btn play-pause" @click="togglePlayPause">
        <span v-if="isPlaying">&#10074;&#10074;</span> <!-- Two bars for pause -->
        <span v-else>&#9654;</span> <!-- Triangle for play -->
      </button>
      <button class="control-btn next" @click="nextTrack">Next</button>
    </div>
    <!-- Ползунок громкости справа -->
    <div class="volume-container">
      <div class="custom-volume" @mousedown="startDragVolume">
        <div
          class="volume-bar"
          :style="{ width: `${volume * 100}%` }"
          @click="changeVolume"
        ></div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.player-container {
  width: 100%; /* Ширина контейнера плеера 100% */
  margin-top: 20px; /* Отступ сверху */
  position: fixed; /* Фиксируем плеер внизу */
  bottom: 0; /* Прикрепляем плеер к низу */
  left: 0;
  z-index: 1000; /* Устанавливаем высокий z-index, чтобы плеер не был скрыт другими элементами */
  background-color: #333; /* Цвет фона плеера */
  padding: 10px 0; /* Отступы внутри плеера */
  display: flex;
  flex-direction: column;
  align-items: center;
}

.audio-player {
  width: 90%; /* Ширина плеера 90% */
  height: 40px; /* Высота плеера */
  margin-bottom: 10px; /* Отступ снизу */
}

.controls {
  display: flex;
  justify-content: center;
  gap: 15px; /* Отступы между кнопками */
  margin-top: 10px;
}

.control-btn {
  background-color: #444;
  color: white;
  border: none;
  padding: 10px;
  cursor: pointer;
  border-radius: 50%; /* Круглая форма кнопок */
  width: 50px;
  height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: background-color 0.3s ease;
}

.control-btn:hover {
  background-color: #555;
}

.progress-container {
  margin-top: 10px;
  width: 90%; /* Ширина прогресс-бара */
  display: flex;
  justify-content: center;
  align-items: center;
}

.custom-progress {
  width: 100%;
  background-color: #555;
  height: 10px;
  border-radius: 5px;
  position: relative;
}

.progress-bar {
  height: 100%;
  background-color: #00bcd4;
  border-radius: 5px;
}

.volume-container {
  margin-top: 10px;
  display: flex;
  justify-content: flex-end; /* Позиционируем громкость справа */
  width: 90%; /* Ограничиваем ширину */
}

.custom-volume {
  width: 150px; /* Уменьшаем ширину ползунка */
  background-color: #555;
  height: 10px;
  border-radius: 5px;
  position: relative;
}

.volume-bar {
  height: 100%;
  background-color: #f44336;
  border-radius: 5px;
}
</style>

<script>
export default {
  props: ['currentTrack'], // Получаем текущий трек из родительского компонента
  data() {
    return {
      isPlaying: false, // Состояние плеера (играет или нет)
      currentTime: 0, // Текущее время воспроизведения
      audioDuration: 0, // Общая длительность трека
      volume: 1, // Уровень громкости
      progress: 0, // Прогресс плеера
      isDraggingProgress: false, // Флаг для отслеживания перетаскивания прогресс-бара
      isDraggingVolume: false, // Флаг для отслеживания перетаскивания ползунка громкости
    };
  },
  watch: {
    currentTrack(newTrack) {
      if (newTrack) {
        this.$nextTick(() => {
          const audio = this.$refs.audio;
          if (audio) {
            audio.load(); // Загружаем новый трек
            audio.play(); // Воспроизводим трек
            this.isPlaying = true; // Трек играет
          }
        });
      }
    }
  },
  methods: {
    // Включение/выключение воспроизведения
    togglePlayPause() {
      const audio = this.$refs.audio;
      if (audio) {
        if (audio.paused) {
          audio.play();
          this.isPlaying = true;
        } else {
          audio.pause();
          this.isPlaying = false;
        }
      }
    },
    // Остановка плеера
    stopAudio() {
      const audio = this.$refs.audio;
      if (audio) {
        audio.pause();
        audio.currentTime = 0;
        this.isPlaying = false;
      }
    },
    // Обновление прогресса
    updateProgress(event) {
      const audio = this.$refs.audio;
      if (audio) {
        audio.currentTime = event.target.value;
        this.currentTime = audio.currentTime;
      }
    },
    // Обновление времени и длительности трека
    updateTime() {
      const audio = this.$refs.audio;
      if (audio) {
        this.currentTime = audio.currentTime;
        this.audioDuration = audio.duration;
        this.progress = (this.currentTime / this.audioDuration) * 100; // Обновление прогресса
      }
    },
    // Переключение на следующий трек
    nextTrack() {
      this.$emit('next-track');
    },
    // Переключение на предыдущий трек
    prevTrack() {
      this.$emit('prev-track');
    },
    // Перемотка трека на новую позицию
    seekAudio(event) {
      const audio = this.$refs.audio;
      if (audio) {
        const clickPosition = (event.offsetX / event.target.offsetWidth) * 100;
        audio.currentTime = (clickPosition / 100) * audio.duration;
        this.currentTime = audio.currentTime;
      }
    },
    // Обновление громкости
    changeVolume(event) {
      const audio = this.$refs.audio;
      if (audio) {
        const clickPosition = (event.offsetX / event.target.offsetWidth);
        audio.volume = clickPosition;
        this.volume = audio.volume;
      }
    },
    // Запуск перемотки прогресса
    startDragProgress(event) {
      this.isDraggingProgress = true;
      this.seekAudio(event);
      window.addEventListener('mousemove', this.onDragProgress);
      window.addEventListener('mouseup', this.stopDragProgress);
    },
    // Перемотка в процессе перетаскивания прогресс-бара
    onDragProgress(event) {
      if (this.isDraggingProgress) {
        this.seekAudio(event);
      }
    },
    // Завершение перетаскивания прогресс-бара
    stopDragProgress() {
      this.isDraggingProgress = false;
      window.removeEventListener('mousemove', this.onDragProgress);
      window.removeEventListener('mouseup', this.stopDragProgress);
    },
    // Запуск перемотки громкости
    startDragVolume(event) {
      this.isDraggingVolume = true;
      this.changeVolume(event);
      window.addEventListener('mousemove', this.onDragVolume);
      window.addEventListener('mouseup', this.stopDragVolume);
    },
    // Перемотка в процессе перетаскивания ползунка громкости
    onDragVolume(event) {
      if (this.isDraggingVolume) {
        this.changeVolume(event);
      }
    },
    // Завершение перетаскивания ползунка громкости
    stopDragVolume() {
      this.isDraggingVolume = false;
      window.removeEventListener('mousemove', this.onDragVolume);
      window.removeEventListener('mouseup', this.stopDragVolume);
    }
  },
  mounted() {
    // Обновление прогресса по мере воспроизведения
    const audio = this.$refs.audio;
    if (audio) {
      audio.addEventListener('timeupdate', this.updateTime);
    }
  }
};
</script>
