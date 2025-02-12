import { createRouter, createWebHistory } from 'vue-router'; // Импортируем функции для создания роутера и истории
import Track from './components/Track.vue'; // Импортируем компонент Track
import Favorites from './components/Favorites.vue'; // Импортируем компонент Favorites

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Track // Главная страница с треками
  },
  {
    path: '/favorites',
    name: 'Favorites',
    component: Favorites // Страница избранных треков
  }
];

const router = createRouter({
  history: createWebHistory(), // Указываем, что будем использовать историю браузера
  routes // Передаем массив маршрутов
});

export default router;
