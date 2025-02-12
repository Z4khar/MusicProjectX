import { createApp } from 'vue'; // Импортируем функцию для создания приложения Vue
import App from './App.vue'; // Импортируем корневой компонент приложения
import router from './router'; // Импортируем роутер, который мы создали ранее
import './assets/styles.css'; // Импортируем глобальные стили


createApp(App)
  .use(router) 
  .mount('#app'); 
