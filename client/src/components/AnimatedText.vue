<template>
    <div class="container">
      <svg viewBox="0 0 960 300">
        <symbol id="s-text">
          <text text-anchor="middle" x="50%" y="80%">{{ text }}</text>
        </symbol>
  
        <g class="g-ants">
          <use xlink:href="#s-text" class="text-copy"></use>
          <use xlink:href="#s-text" class="text-copy"></use>
          <use xlink:href="#s-text" class="text-copy"></use>
          <use xlink:href="#s-text" class="text-copy"></use>
          <use xlink:href="#s-text" class="text-copy"></use>
        </g>
      </svg>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AnimatedText',
    props: {
      text: {
        type: String,
        default: 'Музыка — это жизнь',
      },
    },
  };
  </script>
  
  <style>
  @import url('https://fonts.googleapis.com/css?family=Montserrat');
  
  html, body {
    height: 100%;
    font-weight: 1400;
    margin: 0;
    padding: 0;
  }
  
  body {
    background: #030321;
    font-family: Arial;
  }
  
  .container {
    display: flex;
    height: 100%;
    align-items: center;
    justify-content: center; /* Центрируем текст по горизонтали */
  }
  
  svg {
    display: block;
    font: 5.6em 'Montserrat'; /* Увеличиваем размер шрифта */
    width: 1500px; /* Ширина SVG */
    height: 300px; /* Высота SVG */
    margin: 0 auto;
  }
  
  .text-copy {
    fill: none;
    stroke: white;
    stroke-dasharray: 6% 29%;
    stroke-width: 5px;
    stroke-dashoffset: 0%;
    animation: stroke-offset 5.5s infinite linear; /* Анимация обводки */
  }
  
  .text-copy:nth-child(1) {
    stroke: #4D163D;
    animation-delay: -1s;
  }
  
  .text-copy:nth-child(2) {
    stroke: #840037;
    animation-delay: -2s;
  }
  
  .text-copy:nth-child(3) {
    stroke: #BD0034;
    animation-delay: -3s;
  }
  
  .text-copy:nth-child(4) {
    stroke: #BD0034;
    animation-delay: -4s;
  }
  
  .text-copy:nth-child(5) {
    stroke: #FDB731;
    animation-delay: -5s;
  }
  
  @keyframes stroke-offset {
    100% {
      stroke-dashoffset: -35%; /* Анимация обводки */
    }
  }
  </style>
  